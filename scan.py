from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import argparse
import codecs
import distutils.spawn
import os.path
import platform
import re
import sys
import subprocess
import shutil
import webbrowser as wb
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
import sys
from tkinter import *
from os.path import expanduser

from functools import partial
from collections import defaultdict
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QPushButton,QFileDialog
from PyQt5.QtGui import QIcon, QImageReader

try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

except ImportError:
    # needed for py3+qt4
    # Ref:
    # http://pyqt.sourceforge.net/Docs/PyQt4/incompatible_apis.html
    # http://stackoverflow.com/questions/21217399/pyqt4-qtcore-qvariant-object-instead-of-a-string
    if sys.version_info.major >= 3:
        import sip
        sip.setapi('QVariant', 2)
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *


from libs.combobox import ComboBox
from libs.resources import *
from libs.constants import *
from libs.utils import *
from libs.settings import Settings
from libs.shape import Shape, DEFAULT_LINE_COLOR, DEFAULT_FILL_COLOR
from libs.stringBundle import StringBundle
from libs.canvas import Canvas
from libs.zoomWidget import ZoomWidget
from libs.labelDialog import LabelDialog
from libs.colorDialog import ColorDialog
from libs.labelFile import LabelFile, LabelFileError, LabelFileFormat
from libs.toolBar import ToolBar
from libs.pascal_voc_io import PascalVocReader
from libs.pascal_voc_io import XML_EXT
from libs.yolo_io import YoloReader
from libs.yolo_io import TXT_EXT
from libs.create_ml_io import CreateMLReader
from libs.create_ml_io import JSON_EXT
from libs.ustr import ustr
from libs.hashableQListWidgetItem import HashableQListWidgetItem
from Run_Screen import Ui_Run_Screen
from labelImg import MainWindow

__appname__ = "Scandat Studio"


class WindowMixin(object):

    def menu(self, title, actions=None):
        menu = self.menuBar().addMenu(title)
        if actions:
            add_actions(menu, actions)
        return menu

    def toolbar(self, title, actions=None):
        toolbar = ToolBar(title)
        toolbar.setObjectName(u'%sToolBar' % title)
        # toolbar.setOrientation(Qt.Vertical)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        if actions:
            add_actions(toolbar, actions)
        self.addToolBar(Qt.LeftToolBarArea, toolbar)
        return toolbar


class Ui_MainWindow(QMainWindow,WindowMixin,QWidget):
    FIT_WINDOW, FIT_WIDTH, MANUAL_ZOOM = list(range(3))
    def Windows(self):
        self.window = QtWidgets.QMainWindow()
        self.Ui = Ui_Run_Screen()
        self.Ui.setupUis(self.window)
        self.window.show()

    def setupUi(self, MainWindow, default_filename=None, default_prefdef_class_file=None, default_save_dir=None):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1457, 769)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("G:\Scandat\sacndat_studio\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BoxAndFileLists = QtWidgets.QTabWidget(self.centralwidget)
        self.BoxAndFileLists.setGeometry(QtCore.QRect(1150, 0, 211, 741))
        self.BoxAndFileLists.setObjectName("BoxAndFileLists")
        self.BoxLists = QtWidgets.QWidget()
        self.BoxLists.setObjectName("BoxLists")
        self.listView_2 = QtWidgets.QListWidget(self.BoxLists)
        self.listView_2.setGeometry(QtCore.QRect(0, -10, 211, 731))
        self.listView_2.setObjectName("listView_2")
        self.BoxAndFileLists.addTab(self.BoxLists, "")
        self.FileLabels = QtWidgets.QWidget()
        self.FileLabels.setObjectName("FileLabels")
        self.listView_3 = QtWidgets.QListWidget(self.FileLabels)
        self.listView_3.setGeometry(QtCore.QRect(0, -10, 211, 731))
        self.listView_3.setObjectName("listView_3")
        self.BoxAndFileLists.addTab(self.FileLabels, "")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(0, 10, 1151, 731))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpenDir = QtWidgets.QAction(MainWindow)
        self.actionOpenDir.setIcon(icon1)
        self.actionOpenDir.setObjectName("actionOpenDir")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon3)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionCreate_RectBox = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/objects.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_RectBox.setIcon(icon4)
        self.actionCreate_RectBox.setObjectName("actionCreate_RectBox")
        self.actionEdit_Label = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Label.setIcon(icon5)
        self.actionEdit_Label.setObjectName("actionEdit_Label")
        self.actionDuplicate_RectBox = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDuplicate_RectBox.setIcon(icon6)
        self.actionDuplicate_RectBox.setObjectName("actionDuplicate_RectBox")
        self.actionDelete_RectBox = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_RectBox.setIcon(icon7)
        self.actionDelete_RectBox.setObjectName("actionDelete_RectBox")
        self.actionHide_RectBox = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHide_RectBox.setIcon(icon8)
        self.actionHide_RectBox.setObjectName("actionHide_RectBox")
        self.actionShow_RectBox = QtWidgets.QAction(MainWindow)
        self.actionShow_RectBox.setIcon(icon8)
        self.actionShow_RectBox.setObjectName("actionShow_RectBox")
        self.actionZoom_In = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_In.setIcon(icon9)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_Out.setIcon(icon10)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionOriginal_Size = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/zoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOriginal_Size.setIcon(icon11)
        self.actionOriginal_Size.setObjectName("actionOriginal_Size")
        self.actionFit_Window = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/fit-window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFit_Window.setIcon(icon12)
        self.actionFit_Window.setObjectName("actionFit_Window")
        self.actionFit_Width = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/fit-width.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFit_Width.setIcon(icon13)
        self.actionFit_Width.setObjectName("actionFit_Width")
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon14)
        self.actionClose.setObjectName("actionClose")
        self.actionReset_All = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/resetall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset_All.setIcon(icon15)
        self.actionReset_All.setObjectName("actionReset_All")
        self.actionDelete_Current_Image = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_Current_Image.setIcon(icon16)
        self.actionDelete_Current_Image.setObjectName("actionDelete_Current_Image")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon17)
        self.actionQuit.setObjectName("actionQuit")
        self.actionrun = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("G:/Scandat/sacndat_studio/resources/icons/done.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionrun.setIcon(icon18)
        self.actionrun.setObjectName("actionrun")
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionOpenDir)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSaveAs)
        self.toolBar.addAction(self.actionCreate_RectBox)
        self.toolBar.addAction(self.actionEdit_Label)
        self.toolBar.addAction(self.actionDuplicate_RectBox)
        self.toolBar.addAction(self.actionDelete_RectBox)
        self.toolBar.addAction(self.actionHide_RectBox)
        self.toolBar.addAction(self.actionShow_RectBox)
        self.toolBar.addAction(self.actionrun)
        self.toolBar.addAction(self.actionZoom_In)
        self.toolBar.addAction(self.actionZoom_Out)
        self.toolBar.addAction(self.actionOriginal_Size)
        self.toolBar.addAction(self.actionFit_Window)
        self.toolBar.addAction(self.actionFit_Width)
        self.toolBar.addAction(self.actionClose)
        self.toolBar.addAction(self.actionReset_All)
        self.toolBar.addAction(self.actionDelete_Current_Image)
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)
        self.BoxAndFileLists.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Load string bundle for i18n
        self.string_bundle = StringBundle.get_bundle()
        get_str = lambda str_id: self.string_bundle.get_string(str_id)

        self.actionOpen.triggered.connect(self.open_file)
        self.actionOpenDir.triggered.connect(self.open_dir_dialog)
        self.actionZoom_In.triggered.connect(self.add_zoom, 10)
        self.actionZoom_Out.triggered.connect(self.add_zoom, -10)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSaveAs.triggered.connect(self.save_file_as)
        self.actionOriginal_Size.triggered.connect(self.set_zoom, 100)
        self.actionFit_Window.triggered.connect(self.set_fit_window)
        self.actionFit_Width.triggered.connect(self.set_fit_width)
        # self.actionCreate_RectBox.triggered.connect(self.set_create_mode)
        self.actionCreate_RectBox.triggered.connect(self.create_shape)
        self.actionEdit_Label.triggered.connect(self.set_edit_mode)
        self.actionClose.triggered.connect(self.close)
        self.actionQuit.triggered.connect(self.close)
        self.actionrun.triggered.connect(self.Windows)

        self.retranslateUi(MainWindow)
        self.BoxAndFileLists.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Load setting in the main thread
        self.settings = Settings()
        self.settings.load()
        settings = self.settings

        self.os_name = platform.system()

        # Load string bundle for i18n
        self.string_bundle = StringBundle.get_bundle()
        get_str = lambda str_id: self.string_bundle.get_string(str_id)

        # Save as Pascal voc xml
        self.default_save_dir = default_save_dir
        self.label_file_format = settings.get(SETTING_LABEL_FILE_FORMAT, LabelFileFormat.PASCAL_VOC)

        # For loading all image under a directory
        self.m_img_list = []
        self.dir_name = None
        self.label_hist = []
        self.last_open_dir = None
        self.cur_img_idx = 0
        self.img_count = 1

        # Whether we need to save or not.
        self.dirty = False

        self._no_selection_slot = False
        self._beginner = True
        self.screencast = "https://youtu.be/p0nR2YsCY_U"

        # self.load_predefined_classes(default_prefdef_class_file)
        self.label_dialog = LabelDialog(parent=self, list_item=self.label_hist)

        self.items_to_shapes = {}
        self.shapes_to_items = {}
        self.prev_label_text = ''

        list_layout = QVBoxLayout()
        list_layout.setContentsMargins(0, 0, 0, 0)

        self.zoom_widget = ZoomWidget()
        self.color_dialog = ColorDialog(parent=self)

        self.canvas = Canvas(parent=self)
        self.canvas.zoomRequest.connect(self.zoom_request)
        self.canvas.set_drawing_shape_to_square(settings.get(SETTING_DRAW_SQUARE, False))

        scroll = QScrollArea()
        scroll.setWidget(self.canvas)
        scroll.setWidgetResizable(True)
        self.scroll_bars = {
            Qt.Vertical: scroll.verticalScrollBar(),
            Qt.Horizontal: scroll.horizontalScrollBar()
        }
        self.scroll_area = scroll
        self.canvas.scrollRequest.connect(self.scroll_request)

        self.canvas.newShape.connect(self.new_shape)
        self.canvas.shapeMoved.connect(self.set_dirty)
        self.canvas.selectionChanged.connect(self.shape_selection_changed)
        self.canvas.drawingPolygon.connect(self.toggle_drawing_sensitive)


        self.scalers = {
            self.FIT_WINDOW: self.scale_fit_window,
            self.FIT_WIDTH: self.scale_fit_width,
            # Set to one to scale to 100% when loading files.
            self.MANUAL_ZOOM: lambda: 1,
        }

        # self.setCentralWidget(scroll)
        # self.addDockWidget(Qt.RightDockWidgetArea, self.dock)
        # self.addDockWidget(Qt.RightDockWidgetArea, self.file_dock)
        # self.file_dock.setFeatures(QDockWidget.DockWidgetFloatable)

        zoom = QWidgetAction(self)
        zoom.setDefaultWidget(self.zoom_widget)
        self.zoom_widget.setWhatsThis(
            u"Zoom in or out of the image. Also accessible with"
            " %s and %s from the canvas." % (format_shortcut("Ctrl+[-+]"),
                                             format_shortcut("Ctrl+Wheel")))
        self.zoom_widget.setEnabled(False)
        self.Zoom_Widget = ZoomWidget()
        self.image = QImage()
        self.file_path = ustr(default_filename)
        self.last_open_dir = None
        self.recent_files = []
        self.max_recent = 7
        self.line_color = None
        self.fill_color = None
        self.zoom_level = 100
        self.fit_window = False
        # Add Chris
        self.difficult = False


        # self.restoreState(settings.get(SETTING_WIN_STATE, QByteArray()))
        Shape.line_color = self.line_color = QColor(settings.get(SETTING_LINE_COLOR, DEFAULT_LINE_COLOR))
        Shape.fill_color = self.fill_color = QColor(settings.get(SETTING_FILL_COLOR, DEFAULT_FILL_COLOR))
        self.canvas.set_drawing_color(self.line_color)
        # Add chris
        Shape.difficult = self.difficult

        self.default_save_dir = default_save_dir

        # Actions
        action = partial(new_action, self)
        open = action(get_str('openFile'), self.open_file,
                      'Ctrl+O', 'open', get_str('openFileDetail'))
        open_dir = action(get_str('openDir'), self.open_dir_dialog,
                          'Ctrl+u', 'open', get_str('openDir'))
        change_save_dir = action(get_str('changeSaveDir'), self.change_save_dir_dialog,
                                 'Ctrl+r', 'open', get_str('changeSavedAnnotationDir'))
        open_annotation = action(get_str('openAnnotation'), self.open_annotation_dialog,
                                 'Ctrl+Shift+O', 'open', get_str('openAnnotationDetail'))
        copy_prev_bounding = action(get_str('copyPrevBounding'), self.copy_previous_bounding_boxes, 'Ctrl+v', 'copy',
                                    get_str('copyPrevBounding'))

        open_next_image = action(get_str('nextImg'), self.open_next_image,
                                 'd', 'next', get_str('nextImgDetail'))
        open_prev_image = action(get_str('prevImg'), self.open_prev_image,
                                 'a', 'prev', get_str('prevImgDetail'))

        verify = action(get_str('verifyImg'), self.verify_image,
                        'space', 'verify', get_str('verifyImgDetail'))

        save = action(get_str('save'), self.save_file,
                      'Ctrl+S', 'save', get_str('saveDetail'), enabled=False)
        def get_format_meta(format):
            """
            returns a tuple containing (title, icon_name) of the selected format
            """
            if format == LabelFileFormat.PASCAL_VOC:
                return '&PascalVOC', 'format_voc'
            elif format == LabelFileFormat.YOLO:
                return '&YOLO', 'format_yolo'
            elif format == LabelFileFormat.CREATE_ML:
                return '&CreateML', 'format_createml'

        save_format = action(get_format_meta(self.label_file_format)[0],
                             self.change_format, 'Ctrl+',
                             get_format_meta(self.label_file_format)[1],
                             get_str('changeSaveFormat'), enabled=True)
        close = action(get_str('closeCur'), self.close_file, 'Ctrl+W', 'close', get_str('closeCurDetail'))
        delete_image = action(get_str('deleteImg'), self.delete_image, 'Ctrl+Shift+D', 'close',
                              get_str('deleteImgDetail'))
        delete_image = action(get_str('deleteImg'), self.delete_image, 'Ctrl+Shift+D', 'close',
                              get_str('deleteImgDetail'))

        reset_all = action(get_str('resetAll'), self.reset_all, None, 'resetall', get_str('resetAllDetail'))

        color1 = action(get_str('boxLineColor'), self.choose_color1,
                        'Ctrl+L', 'color_line', get_str('boxLineColorDetail'))
        create_mode = action(get_str('crtBox'), self.set_create_mode,
                             'w', 'new', get_str('crtBoxDetail'), enabled=False)
        edit_mode = action(get_str('editBox'), self.set_edit_mode,
                           'Ctrl+J', 'edit', get_str('editBoxDetail'), enabled=False)
        edit = action(get_str('editLabel'), self.edit_label,
                      'Ctrl+E', 'edit', get_str('editLabelDetail'),
                      enabled=False)
        create = action(get_str('crtBox'), self.create_shape,
                        'w', 'new', get_str('crtBoxDetail'), enabled=False)
        copy = action(get_str('dupBox'), self.copy_selected_shape,
                      'Ctrl+D', 'copy', get_str('dupBoxDetail'),
                      enabled=False)
        advanced_mode = action(get_str('advancedMode'), self.toggle_advanced_mode,
                               'Ctrl+Shift+A', 'expert', get_str('advancedModeDetail'),
                               checkable=True)
        delete = action(get_str('delBox'), self.delete_selected_shape,
                        'Delete', 'delete', get_str('delBoxDetail'), enabled=False)

        shape_line_color = action(get_str('shapeLineColor'), self.choose_shape_line_color,
                                  icon='color_line', tip=get_str('shapeLineColorDetail'),
                                  enabled=False)
        shape_fill_color = action(get_str('shapeFillColor'), self.choose_shape_fill_color,
                                  icon='color', tip=get_str('shapeFillColorDetail'),
                                  enabled=False)
        zoom_in = action(get_str('zoomin'), partial(self.add_zoom, 10),
                         'Ctrl++', 'zoom-in', get_str('zoominDetail'), enabled=False)
        zoom_out = action(get_str('zoomout'), partial(self.add_zoom, -10),
                          'Ctrl+-', 'zoom-out', get_str('zoomoutDetail'), enabled=False)
        zoom_org = action(get_str('originalsize'), partial(self.set_zoom, 100),
                          'Ctrl+=', 'zoom', get_str('originalsizeDetail'), enabled=False)
        fit_window = action(get_str('fitWin'), self.set_fit_window,
                            'Ctrl+F', 'fit-window', get_str('fitWinDetail'),
                            checkable=True, enabled=False)
        fit_width = action(get_str('fitWidth'), self.set_fit_width,
                           'Ctrl+Shift+F', 'fit-width', get_str('fitWidthDetail'),
                           checkable=True, enabled=False)
        # Group zoom controls into a list for easier toggling.
        zoom_actions = (self.zoom_widget, zoom_in, zoom_out,
                        zoom_org, fit_window, fit_width)
        self.zoom_mode = self.MANUAL_ZOOM
        self.scalers = {
            self.FIT_WINDOW: self.scale_fit_window,
            self.FIT_WIDTH: self.scale_fit_width,
            # Set to one to scale to 100% when loading files.
            self.MANUAL_ZOOM: lambda: 1,
        }

        # Draw squares/rectangles
        self.draw_squares_option = QAction(get_str('drawSquares'), self)
        self.draw_squares_option.setShortcut('Ctrl+Shift+R')
        self.draw_squares_option.setCheckable(True)
        self.draw_squares_option.setChecked(settings.get(SETTING_DRAW_SQUARE, False))
        self.draw_squares_option.triggered.connect(self.toggle_draw_square)

        self.actions = Struct(save=save, save_format=save_format, open=open, close=close, resetAll=reset_all, deleteImg=delete_image,
                              lineColor=color1, create=create, delete=delete, edit=edit, copy=copy,
                              createMode=create_mode, editMode=edit_mode, advancedMode=advanced_mode,
                              shapeLineColor=shape_line_color, shapeFillColor=shape_fill_color,
                              zoom=zoom, zoomIn=zoom_in, zoomOut=zoom_out, zoomOrg=zoom_org,
                              fitWindow=fit_window, fitWidth=fit_width,
                              zoomActions=zoom_actions,
                              fileMenuActions=(
                                  open, open_dir, save, close, reset_all, quit),
                              beginner=(), advanced=(),
                              editMenu=(edit, copy, delete,
                                        None, color1, self.draw_squares_option),
                              beginnerContext=(create, edit, copy, delete),
                              advancedContext=(create_mode, edit_mode, edit, copy,
                                               delete, shape_line_color, shape_fill_color),
                              onLoadActive=(
                                  close, create, create_mode, edit_mode))
                              # onShapesPresent=(save_as, hide_all, show_all))






        # Label list context menu.
        label_menu = QMenu()
        add_actions(label_menu, (create,edit, copy, delete))
        self.image_label.setContextMenuPolicy(Qt.CustomContextMenu)
        self.image_label.customContextMenuRequested.connect(
            self.pop_label_list_menu)

        add_actions(self.canvas.menus[0], self.actions.beginnerContext)
        add_actions(self.canvas.menus[1], (
            action('&Copy here', self.copy_shape),
            action('&Move here', self.move_shape)))



        self.toolBars = Struct(
            file=self.menu(get_str('menu_file')),
            edit=self.menu(get_str('menu_edit')),
            view=self.menu(get_str('menu_view')),
            Run=self.menu(get_str('menu_run')),
            help=self.menu(get_str('menu_help')),
            recentFiles=QMenu(get_str('menu_openRecent')),
            labelList=label_menu)

        # Auto saving : Enable auto saving if pressing next
        self.auto_saving = QAction(get_str('autoSaveMode'), self)
        self.auto_saving.setCheckable(True)
        self.auto_saving.setChecked(settings.get(SETTING_AUTO_SAVE, False))
        # Sync single class mode from PR#106
        self.single_class_mode = QAction(get_str('singleClsMode'), self)
        self.single_class_mode.setShortcut("Ctrl+Shift+S")
        self.single_class_mode.setCheckable(True)
        self.single_class_mode.setChecked(settings.get(SETTING_SINGLE_CLASS, False))
        self.lastLabel = None
        # Add option to enable/disable labels being displayed at the top of bounding boxes
        self.display_label_option = QAction(get_str('displayLabel'), self)
        self.display_label_option.setShortcut("Ctrl+Shift+P")
        self.display_label_option.setCheckable(True)
        self.display_label_option.setChecked(settings.get(SETTING_PAINT_LABEL, False))

        # add_actions(self.toolbars,
        #             (open, open_dir, change_save_dir, open_annotation, copy_prev_bounding, save,
        #              close, reset_all, delete_image, quit))
        # add_actions(self.toolBars, (
        #     self.auto_saving,
        #     self.single_class_mode,
        #     self.display_label_option,
        #     advanced_mode, None, None,
        #     zoom_in, zoom_out, zoom_org, None,
        #     fit_window, fit_width))
        # add_actions(self.canvas.menus[0], self.actions.beginnerContext)
        # add_actions(self.canvas.menus[1], (
        #     action('&Copy here', self.copy_shape),
        #     action('&Move here', self.move_shape)))
        # self.tools = self.toolbar('Tools')

        self.actions.advanced = (
            open, open_dir, change_save_dir, open_next_image, open_prev_image, save, save_format, None,
            create_mode, edit_mode, None)

        self.statusBar().showMessage('%s started.' % __appname__)
        self.statusBar().show()

        # Application state.
        self.image = QImage()
        self.file_path = ustr(default_filename)
        self.last_open_dir = None
        self.recent_files = []
        self.max_recent = 7
        self.line_color = None
        self.fill_color = None
        self.zoom_level = 100
        self.fit_window = False

        # self.display_label_option.triggered.connect(self.toggle_paint_labels_option)

        # Fix the compatible issue for qt4 and qt5. Convert the QStringList to python list
        if settings.get(SETTING_RECENT_FILES):
            if have_qstring():
                recent_file_qstring_list = settings.get(SETTING_RECENT_FILES)
                self.recent_files = [ustr(i) for i in recent_file_qstring_list]
            else:
                self.recent_files = recent_file_qstring_list = settings.get(SETTING_RECENT_FILES)

        size = settings.get(SETTING_WIN_SIZE, QSize(600, 500))
        position = QPoint(0, 0)
        saved_position = settings.get(SETTING_WIN_POSE, position)
        # Fix the multiple monitors issue
        for i in range(QApplication.desktop().screenCount()):
            if QApplication.desktop().availableGeometry(i).contains(saved_position):
                position = saved_position
                break
        self.resize(size)
        self.move(position)
        save_dir = ustr(settings.get(SETTING_SAVE_DIR, None))
        self.last_open_dir = ustr(settings.get(SETTING_LAST_OPEN_DIR, None))
        if self.default_save_dir is None and save_dir is not None and os.path.exists(save_dir):
            self.default_save_dir = save_dir
            self.statusBar().showMessage('%s started. Annotation will be saved to %s' %
                                         (__appname__, self.default_save_dir))
            self.statusBar().show()

        self.restoreState(settings.get(SETTING_WIN_STATE, QByteArray()))
        Shape.line_color = self.line_color = QColor(settings.get(SETTING_LINE_COLOR, DEFAULT_LINE_COLOR))
        Shape.fill_color = self.fill_color = QColor(settings.get(SETTING_FILL_COLOR, DEFAULT_FILL_COLOR))
        self.canvas.set_drawing_color(self.line_color)
        # Add chris
        Shape.difficult = self.difficult

        # self.statusBar().showMessage('%s started.' % __appname__)
        # self.statusBar().show()

        def xbool(x):
            if isinstance(x, QVariant):
                return x.toBool()
            return bool(x)

        if xbool(settings.get(SETTING_ADVANCE_MODE, False)):
            self.actions.advancedMode.setChecked(True)
            self.toggle_advanced_mode()

        # Populate the File menu dynamically.
        self.update_file_menu()

        # Since loading the file may take some time, make sure it runs in the background.
        if self.file_path and os.path.isdir(self.file_path):
            self.queue_event(partial(self.import_dir_images, self.file_path or ""))
        elif self.file_path:
            self.queue_event(partial(self.load_file, self.file_path or ""))

        # Callbacks:
        self.zoom_widget.valueChanged.connect(self.paint_canvas)

        # self.populate_mode_actions()

        # Display cursor coordinates at the right of status bar
        self.label_coordinates = QLabel('')
        # self.statusBar().addPermanentWidget(self.label_coordinates)

        # Open Dir if default file
        if self.file_path and os.path.isdir(self.file_path):
            self.open_dir_dialog(dir_path=self.file_path, silent=True)

    def queue_event(self, function):
        QTimer.singleShot(0, function)

    def pop_label_list_menu(self, point):
        self.menus.labelList.exec_(self.image_label.mapToGlobal(point))

    def toggle_draw_square(self):
        self.canvas.set_drawing_shape_to_square(self.draw_squares_option.isChecked())

    def change_format(self):
        if self.label_file_format == LabelFileFormat.PASCAL_VOC:
            self.set_format(FORMAT_YOLO)
        elif self.label_file_format == LabelFileFormat.YOLO:
            self.set_format(FORMAT_CREATEML)
        elif self.label_file_format == LabelFileFormat.CREATE_ML:
            self.set_format(FORMAT_PASCALVOC)
        else:
            raise ValueError('Unknown label file format.')
        self.set_dirty()

    def edit_label(self):
        if not self.canvas.editing():
            return
        item = self.current_item()
        if not item:
            return
        text = self.label_dialog.pop_up(item.text())
        if text is not None:
            item.setText(text)
            item.setBackground(generate_color_by_text(text))
            self.set_dirty()
            self.update_combo_box()

    def delete_selected_shape(self):
        self.remove_label(self.canvas.delete_selected())
        self.set_dirty()
        if self.no_shapes():
            for action in self.actions.onShapesPresent:
                action.setEnabled(False)

    def choose_shape_line_color(self):
        color = self.color_dialog.getColor(self.line_color, u'Choose Line Color',
                                           default=DEFAULT_LINE_COLOR)
        if color:
            self.canvas.selected_shape.line_color = color
            self.canvas.update()
            self.set_dirty()

    def choose_shape_fill_color(self):
        color = self.color_dialog.getColor(self.fill_color, u'Choose Fill Color',
                                           default=DEFAULT_FILL_COLOR)
        if color:
            self.canvas.selected_shape.fill_color = color
            self.canvas.update()
            self.set_dirty()

    def copy_selected_shape(self):
        self.add_label(self.canvas.copy_selected_shape())
        # fix copy and delete
        self.shape_selection_changed(True)

    def copy_shape(self):
        self.canvas.end_move(copy=True)
        self.add_label(self.canvas.selected_shape)
        self.set_dirty()

    def move_shape(self):
        self.canvas.end_move(copy=False)
        self.set_dirty()

    def no_shapes(self):
        return not self.items_to_shapes

    def choose_color1(self):
        color = self.color_dialog.getColor(self.line_color, u'Choose line color',
                                           default=DEFAULT_LINE_COLOR)
        if color:
            self.line_color = color
            Shape.line_color = color
            self.canvas.set_drawing_color(color)
            self.canvas.update()
            self.set_dirty()

    def reset_all(self):
        self.settings.reset()
        self.close()
        process = QProcess()
        process.startDetached(os.path.abspath(__file__))

    # Tzutalin 20160906 : Add file list and dock to move faster
    def file_item_double_clicked(self, item=None):
        self.cur_img_idx = self.m_img_list.index(ustr(item.text()))
        filename = self.m_img_list[self.cur_img_idx]
        if filename:
            self.load_file(filename)

    def toggle_advanced_mode(self, value=True):
        print("it is inside toggle advance")
        self._beginner = not value
        self.canvas.set_editing(True)
        self.populate_mode_actions()
        self.edit_button.setVisible(not value)
        if value:
            self.actions.createMode.setEnabled(True)
            self.actions.editMode.setEnabled(False)
            self.dock.setFeatures(self.dock.features() | self.dock_features)
        else:
            self.dock.setFeatures(self.dock.features() ^ self.dock_features)

    def scale_fit_window(self):
        """Figure out the size of the pixmap in order to fit the main widget."""
        e = 2.0  # So that no scrollbars are generated.
        w1 = self.centralWidget().width() - e
        h1 = self.centralWidget().height() - e
        a1 = w1 / h1
        # Calculate a new scale value based on the pixmap's aspect ratio.
        w2 = self.canvas.pixmap.width() - 0.0
        h2 = self.canvas.pixmap.height() - 0.0
        a2 = w2 / h2
        return w1 / w2 if a2 >= a1 else h1 / h2

    def scale_fit_width(self):
        # The epsilon does not seem to work too well here.
        w = self.centralWidget().width() - 2.0
        return w / self.canvas.pixmap.width()

    def update_file_menu(self):
        curr_file_path = self.file_path

        def exists(filename):
            return os.path.exists(filename)
        files = [f for f in self.recent_files if f !=
                 curr_file_path and exists(f)]
        for i, f in enumerate(files):
            icon = new_icon('labels')
            action = QAction(
                icon, '&%d %s' % (i + 1, QFileInfo(f).fileName()), self)
            action.triggered.connect(partial(self.load_recent, f))
            # menu.addAction(action)

    def load_recent(self, filename):
        if self.may_continue():
            self.load_file(filename)

    def new_shape(self):
        """Pop-up and give focus to the label editor.

        position MUST be in global coordinates.
        """
        if not self.use_default_label_checkbox.isChecked() or not self.default_label_text_line.text():
            if len(self.label_hist) > 0:
                self.label_dialog = LabelDialog(
                    parent=self, list_item=self.label_hist)

            # Sync single class mode from PR#106
            if self.single_class_mode.isChecked() and self.lastLabel:
                text = self.lastLabel
            else:
                text = self.label_dialog.pop_up(text=self.prev_label_text)
                self.lastLabel = text
        else:
            text = self.default_label_text_line.text()

        # Add Chris
        self.diffc_button.setChecked(False)
        if text is not None:
            self.prev_label_text = text
            generate_color = generate_color_by_text(text)
            shape = self.canvas.set_last_label(text, generate_color, generate_color)
            self.add_label(shape)
            if self.beginner():  # Switch to edit mode.
                self.canvas.set_editing(True)
                self.actions.create.setEnabled(True)
            else:
                self.actions.editMode.setEnabled(True)
            self.set_dirty()

            if text not in self.label_hist:
                self.label_hist.append(text)
        else:
            # self.canvas.undoLastLine()
            self.canvas.reset_all_lines()

    def shape_selection_changed(self, selected=False):
        if self._no_selection_slot:
            self._no_selection_slot = False
        else:
            shape = self.canvas.selected_shape
            if shape:
                self.shapes_to_items[shape].setSelected(True)
            else:
                self.label_list.clearSelection()
        self.actions.delete.setEnabled(selected)
        self.actions.copy.setEnabled(selected)
        self.actions.edit.setEnabled(selected)
        self.actions.shapeLineColor.setEnabled(selected)
        self.actions.shapeFillColor.setEnabled(selected)

    def verify_image(self, _value=False):
        # Proceeding next image without dialog if having any label
        if self.file_path is not None:
            try:
                self.label_file.toggle_verify()
            except AttributeError:
                # If the labelling file does not exist yet, create if and
                # re-save it with the verified attribute.
                self.save_file()
                if self.label_file is not None:
                    self.label_file.toggle_verify()
                else:
                    return

            self.canvas.verified = self.label_file.verified
            self.paint_canvas()
            self.save_file()

    def toggle_drawing_sensitive(self, drawing=True):
        """In the middle of drawing, toggling between modes should be disabled."""
        self.actions.editMode.setEnabled(not drawing)
        if not drawing and self.beginner():
            # Cancel creation.
            print('Cancel creation.')
            self.canvas.set_editing(True)
            self.canvas.restore_cursor()
            self.actions.create.setEnabled(True)

    def set_fit_window(self, value=True):
        if value:
            self.actions.fitWidth.setChecked(False)
        self.zoom_mode = self.FIT_WINDOW if value else self.MANUAL_ZOOM
        self.adjust_scale()

    def set_fit_width(self, value=True):
        if value:
            self.actions.fitWindow.setChecked(False)
        self.zoom_mode = self.FIT_WIDTH if value else self.MANUAL_ZOOM
        self.adjust_scale()

    def set_dirty(self):
        self.dirty = True
        self.actions.save.setEnabled(True)

    def scroll_request(self, delta, orientation):
        units = - delta / (8 * 15)
        bar = self.scroll_bars[orientation]
        bar.setValue(bar.value() + bar.singleStep() * units)


    def set_zoom(self, value = 50):
        self.Zoom_Mode = self.MANUAL_ZOOM
        self.Zoom_Widget.setValue(value)

    def add_zoom(self, increment=10):
        self.set_zoom(self.Zoom_Widget.value() + increment)

    def zoom_request(self, delta):
        # get the current scrollbar positions
        # calculate the percentages ~ coordinates
        h_bar = self.scroll_bars[Qt.Horizontal]
        v_bar = self.scroll_bars[Qt.Vertical]

        # get the current maximum, to know the difference after zooming
        h_bar_max = h_bar.maximum()
        v_bar_max = v_bar.maximum()

        # get the cursor position and canvas size
        # calculate the desired movement from 0 to 1
        # where 0 = move left
        #       1 = move right
        # up and down analogous
        cursor = QCursor()
        pos = cursor.pos()
        relative_pos = QWidget.mapFromGlobal(self, pos)

        cursor_x = relative_pos.x()
        cursor_y = relative_pos.y()

        w = self.scroll_area.width()
        h = self.scroll_area.height()

        # the scaling from 0 to 1 has some padding
        # you don't have to hit the very leftmost pixel for a maximum-left movement
        margin = 0.1
        move_x = (cursor_x - margin * w) / (w - 2 * margin * w)
        move_y = (cursor_y - margin * h) / (h - 2 * margin * h)

        # clamp the values from 0 to 1
        move_x = min(max(move_x, 0), 1)
        move_y = min(max(move_y, 0), 1)

        # zoom in
        units = delta / (8 * 15)
        scale = 8
        self.add_zoom(scale * units)

        # get the difference in scrollbar values
        # this is how far we can move
        d_h_bar_max = h_bar.maximum() - h_bar_max
        d_v_bar_max = v_bar.maximum() - v_bar_max

        # get the new scrollbar values
        new_h_bar_value = h_bar.value() + move_x * d_h_bar_max
        new_v_bar_value = v_bar.value() + move_y * d_v_bar_max

        h_bar.setValue(new_h_bar_value)
        v_bar.setValue(new_v_bar_value)

    def open_file(self):
        print('it is coming inside')
        # file_name, _ = QFileDialog.getOpenFileName(self, "open the Image file", r"<Default dir>",
        #                                            "Image files(*.jpg *.png *.jpeg *.gif)")
        # self.image_label.setPixmap(QPixmap(file_name))
        if not self.may_continue():
            return
        path = os.path.dirname(ustr(self.file_path)) if self.file_path else '.'
        formats = ['*.%s' % fmt.data().decode("ascii").lower() for fmt in QImageReader.supportedImageFormats()]
        filters = "Image & Label files (%s)" % ' '.join(formats + ['*%s' % LabelFile.suffix])
        filename = QFileDialog.getOpenFileName(self, '%s - Choose Image or Label file' % __appname__, path, filters)
        if filename:
            if isinstance(filename, (tuple, list)):
                filename = filename[0]
            self.cur_img_idx = 0
            self.img_count = 1
            self.load_file(filename)


    def load_predefined_classes(self, predef_classes_file):
        if os.path.exists(predef_classes_file) is True:
            with codecs.open(predef_classes_file, 'r', 'utf8') as f:
                for line in f:
                    line = line.strip()
                    if self.label_hist is None:
                        self.label_hist = [line]
                    else:
                        self.label_hist.append(line)

    def close_file(self, _value=False):
        if not self.may_continue():
            return
        self.reset_state()
        self.set_clean()
        self.toggle_actions(False)
        self.canvas.setEnabled(False)
        self.actions.saveAs.setEnabled(False)

    def open_dir_dialog(self, _value=False, dir_path=None, silent=False):
        if not self.may_continue():
            return
        print("it is outside if")
        default_open_dir_path = dir_path if dir_path else '.'
        if self.last_open_dir and os.path.exists(self.last_open_dir):
            print("it is inside if")
            default_open_dir_path = self.last_open_dir
        else:
            print("it is in else")
            default_open_dir_path = os.path.dirname(self.file_path) if self.file_path else '.'
        if silent != True:
            print("it is in if silent")
            target_dir_path = ustr(QFileDialog.getExistingDirectory(self,
                                                                    '%s - Open Directory' % __appname__,
                                                                    default_open_dir_path,
                                                                    QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks))
        else:
            print("it is in else silent")
            target_dir_path = ustr(default_open_dir_path)
        print("it is outside if and else ")
        self.last_open_dir = target_dir_path
        print("it is next to last")
        self.import_dir_images(target_dir_path)
        print("it is next to target")

    def open_annotation_dialog(self, _value=False):
        if self.file_path is None:
            self.statusBar().showMessage('Please select image first')
            self.statusBar().show()
            return

        path = os.path.dirname(ustr(self.file_path))\
            if self.file_path else '.'
        if self.label_file_format == LabelFileFormat.PASCAL_VOC:
            filters = "Open Annotation XML file (%s)" % ' '.join(['*.xml'])
            filename = ustr(QFileDialog.getOpenFileName(self, '%s - Choose a xml file' % __appname__, path, filters))
            if filename:
                if isinstance(filename, (tuple, list)):
                    filename = filename[0]
            self.load_pascal_xml_by_filename(filename)

    def copy_previous_bounding_boxes(self):
        current_index = self.m_img_list.index(self.file_path)
        if current_index - 1 >= 0:
            prev_file_path = self.m_img_list[current_index - 1]
            self.show_bounding_box_from_annotation_file(prev_file_path)
            self.save_file()

    def import_dir_images(self, dir_path):
        if not self.may_continue() or not dir_path:
            return
        self.last_open_dir = dir_path
        self.dir_name = dir_path
        self.file_path = None
        self.image_label.clear()
        self.m_img_list = self.scan_all_images(dir_path)
        self.img_count = len(self.m_img_list)
        self.open_next_image()
        print("it is after open_next_image")
        for imgPath in self.m_img_list:
            print("it is after for loop")
            item = QListWidgetItem(imgPath)
            print("it is after item")
            self.listView_3.addItem(item)
            print("it is after listadd")

    def change_save_dir_dialog(self, _value=False):
        if self.default_save_dir is not None:
            path = ustr(self.default_save_dir)
        else:
            path = '.'

        dir_path = ustr(QFileDialog.getExistingDirectory(self,
                                                         '%s - Save annotations to the directory' % __appname__,
                                                         path,
                                                         QFileDialog.ShowDirsOnly
                                                         | QFileDialog.DontResolveSymlinks))

        if dir_path is not None and len(dir_path) > 1:
            self.default_save_dir = dir_path

        self.statusBar().showMessage('%s . Annotation will be saved to %s' %
                                     ('Change saved folder', self.default_save_dir))
        self.statusBar().show()

    def open_prev_image(self, _value=False):
        # Proceeding prev image without dialog if having any label
        if self.auto_saving.isChecked():
            if self.default_save_dir is not None:
                if self.dirty is True:
                    self.save_file()
            else:
                self.change_save_dir_dialog()
                return

        if not self.may_continue():
            return

        if self.img_count <= 0:
            return

        if self.file_path is None:
            return

        if self.cur_img_idx - 1 >= 0:
            self.cur_img_idx -= 1
            filename = self.m_img_list[self.cur_img_idx]
            if filename:
                self.load_file(filename)

    def open_next_image(self, _value=False, default_save_dir=None):
        # Proceeding prev image without dialog if having any label
        if self.auto_saving.isChecked():
            print("it is inside if auto saving")
            if self.default_save_dir is not None:
                print("it is inside if default_save_dir")
                if self.dirty is True:
                    print("it is inside if dirty")
                    self.save_file()
            else:
                print("it is inside else")
                self.change_save_dir_dialog()
                return
        if not self.may_continue():
            print("it is inside if may_continue")
            return

        if self.img_count <= 0:
            print("it is inside if img_count")
            return
        filename = None
        if self.file_path is None:
            print("it is inside if filepath")
            filename = self.m_img_list[0]
            print("it is inside if after filename")
            self.cur_img_idx = 0
        else:
            if self.cur_img_idx + 1 < self.img_count:
                print("it is inside else if cur_img")
                self.cur_img_idx += 1
                filename = self.m_img_list[self.cur_img_idx]
        if filename:
            self.load_file(filename)
            print("it is inside if after load_file")

    def reset_state(self):
        self.items_to_shapes.clear()
        self.shapes_to_items.clear()
        self.image_label.clear()
        self.file_path = None
        self.image_data = None
        self.label_file = None
        self.canvas.reset_state()
        self.label_coordinates.clear()

    def error_message(self, title, message):
        return QMessageBox.critical(self, title,'<p><b>%s</b></p>%s' % (title, message))

    def status(self, message, delay=5000):
        self.statusBar().showMessage(message, delay)

    def create_shape(self):
        print("it is inside create_shape")
        assert self.beginner()
        print("it is after assert in create shape")
        self.canvas.set_editing(False)
        print("it is after canvas")
        # self.actions.create.setEnabled(False)
        print("it is after actions create")

    def load_labels(self, shapes):
        s = []
        for label, points, line_color, fill_color, difficult in shapes:
            shape = Shape(label=label)
            for x, y in points:

                # Ensure the labels are within the bounds of the image. If not, fix them.
                x, y, snapped = self.canvas.snap_point_to_canvas(x, y)
                if snapped:
                    self.set_dirty()

                shape.add_point(QPointF(x, y))
            shape.difficult = difficult
            shape.close()
            s.append(shape)

            if line_color:
                shape.line_color = QColor(*line_color)
            else:
                shape.line_color = generate_color_by_text(label)

            if fill_color:
                shape.fill_color = QColor(*fill_color)
            else:
                shape.fill_color = generate_color_by_text(label)

            self.add_label(shape)
        self.update_combo_box()
        self.canvas.load_shapes(s)

    def save_labels(self, annotation_file_path):
        annotation_file_path = ustr(annotation_file_path)
        if self.label_file is None:
            self.label_file = LabelFile()
            self.label_file.verified = self.canvas.verified

        def format_shape(s):
            return dict(label=s.label,
                        line_color=s.line_color.getRgb(),
                        fill_color=s.fill_color.getRgb(),
                        points=[(p.x(), p.y()) for p in s.points],
                        # add chris
                        difficult=s.difficult)

        shapes = [format_shape(shape) for shape in self.canvas.shapes]
        # Can add different annotation formats here
        try:
            if self.label_file_format == LabelFileFormat.PASCAL_VOC:
                if annotation_file_path[-4:].lower() != ".xml":
                    annotation_file_path += XML_EXT
                self.label_file.save_pascal_voc_format(annotation_file_path, shapes, self.file_path, self.image_data,
                                                       self.line_color.getRgb(), self.fill_color.getRgb())
            elif self.label_file_format == LabelFileFormat.YOLO:
                if annotation_file_path[-4:].lower() != ".txt":
                    annotation_file_path += TXT_EXT
                self.label_file.save_yolo_format(annotation_file_path, shapes, self.file_path, self.image_data, self.label_hist,
                                                 self.line_color.getRgb(), self.fill_color.getRgb())
            elif self.label_file_format == LabelFileFormat.CREATE_ML:
                if annotation_file_path[-5:].lower() != ".json":
                    annotation_file_path += JSON_EXT
                self.label_file.save_create_ml_format(annotation_file_path, shapes, self.file_path, self.image_data,
                                                      self.label_hist, self.line_color.getRgb(), self.fill_color.getRgb())
            else:
                self.label_file.save(annotation_file_path, shapes, self.file_path, self.image_data,
                                     self.line_color.getRgb(), self.fill_color.getRgb())
            print('Image:{0} -> Annotation:{1}'.format(self.file_path, annotation_file_path))
            return True
        except LabelFileError as e:
            self.error_message(u'Error saving label data', u'<b>%s</b>' % e)
            return False

    def set_clean(self):
        self.dirty = False

    def adjust_scale(self, initial=False):
        value = self.scalers[self.FIT_WINDOW if initial else self.zoom_mode]()
        self.zoom_widget.setValue(int(100 * value))

    def paint_canvas(self):
        assert not self.image.isNull(), "cannot paint null image"
        self.canvas.scale = 0.01 * self.zoom_widget.value()
        self.canvas.label_font_size = int(0.02 * max(self.image.width(), self.image.height()))
        self.canvas.adjustSize()
        self.canvas.update()

    def add_recent_file(self, file_path):
        if file_path in self.recent_files:
            self.recent_files.remove(file_path)
        elif len(self.recent_files) >= self.max_recent:
            self.recent_files.pop()
        self.recent_files.insert(0, file_path)

    def toggle_actions(self, value=True):
        """Enable/Disable widgets which depend on an opened image."""
        for z in self.actions.zoomActions:
            z.setEnabled(value)
        for action in self.actions.onLoadActive:
            action.setEnabled(value)

    def show_bounding_box_from_annotation_file(self, file_path):
        if self.default_save_dir is not None:
            basename = os.path.basename(os.path.splitext(file_path)[0])
            xml_path = os.path.join(self.default_save_dir, basename + XML_EXT)
            txt_path = os.path.join(self.default_save_dir, basename + TXT_EXT)
            json_path = os.path.join(self.default_save_dir, basename + JSON_EXT)

            """Annotation file priority:
            PascalXML > YOLO
            """
            if os.path.isfile(xml_path):
                self.load_pascal_xml_by_filename(xml_path)
            elif os.path.isfile(txt_path):
                self.load_yolo_txt_by_filename(txt_path)
            elif os.path.isfile(json_path):
                self.load_create_ml_json_by_filename(json_path, file_path)

        else:
            xml_path = os.path.splitext(file_path)[0] + XML_EXT
            txt_path = os.path.splitext(file_path)[0] + TXT_EXT
            if os.path.isfile(xml_path):
                self.load_pascal_xml_by_filename(xml_path)
            elif os.path.isfile(txt_path):
                self.load_yolo_txt_by_filename(txt_path)

    def counter_str(self):
        """
        Converts image counter to string representation.
        """
        return '[{} / {}]'.format(self.cur_img_idx + 1, self.img_count)


    def add_label(self, shape):
        shape.paint_label = self.display_label_option.isChecked()
        item = HashableQListWidgetItem(shape.label)
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Checked)
        item.setBackground(generate_color_by_text(shape.label))
        self.items_to_shapes[item] = shape
        self.shapes_to_items[shape] = item
        self.label_list.addItem(item)
        for action in self.actions.onShapesPresent:
            action.setEnabled(True)
        self.update_combo_box()

    def remove_label(self, shape):
        if shape is None:
            # print('rm empty label')
            return
        item = self.shapes_to_items[shape]
        self.label_list.takeItem(self.label_list.row(item))
        del self.shapes_to_items[shape]
        del self.items_to_shapes[item]
        self.update_combo_box()


    def load_file(self, file_path=None):
        """Load the specified file, or the last opened file if None."""
        self.reset_state()
        self.canvas.setEnabled(False)
        if file_path is None:
            file_path = self.settings.get(SETTING_FILENAME)

        # Make sure that filePath is a regular python string, rather than QString
        file_path = ustr(file_path)

        # Fix bug: An  index error after select a directory when open a new file.
        unicode_file_path = ustr(file_path)
        unicode_file_path = os.path.abspath(unicode_file_path)
        # Tzutalin 20160906 : Add file list and dock to move faster
        # Highlight the file item
        print("it is before unicode_file_path")
        if unicode_file_path and self.listView_3.count() > 0:
            print("it is after unicode_file_path")
            if unicode_file_path in self.m_img_list:
                index = self.m_img_list.index(unicode_file_path)
                file_widget_item = self.listView_3.item(index)
                file_widget_item.setSelected(True)
            else:
                self.listView_3.clear()
                self.m_img_list.clear()
        print("it is before unicode_file_path and os.path")
        if unicode_file_path and os.path.exists(unicode_file_path):
            print("it is inside unicode_file_path and os.path")
            if LabelFile.is_label_file(unicode_file_path):
                print("it is inside after unicode_file_path and os.path")
                try:
                    self.label_file = LabelFile(unicode_file_path)
                except LabelFileError as e:
                    self.error_message(u'Error opening file',
                                       (u"<p><b>%s</b></p>"
                                        u"<p>Make sure <i>%s</i> is a valid label file.")
                                       % (e, unicode_file_path))
                    self.status("Error reading %s" % unicode_file_path)
                    return False
                self.image_data = self.label_file.image_data
                self.line_color = QColor(*self.label_file.lineColor)
                self.fill_color = QColor(*self.label_file.fillColor)
                self.canvas.verified = self.label_file.verified
            else:
                print("it is else part unicode_file_path and os.path")
                # Load image:
                # read data first and store for saving into label file.
                self.image_data = read(unicode_file_path, None)
                print("after image_data", unicode_file_path)
                self.label_file = None
                print("after label_file")
                self.canvas.verified = False
                print("after canvas")

            if isinstance(self.image_data, QImage):
                print("it is after if")
                image = self.image_data
            else:
                image = QImage.fromData(self.image_data)
                print("it is inside else")


            if image.isNull():
                print("it is before if")
                self.error_message(u'Error opening file',
                                   u"<p>Make sure <i>%s</i> is a valid image file." % unicode_file_path)
                self.status("Error reading %s" % unicode_file_path)
                return False
            self.status("Loaded %s" % os.path.basename(unicode_file_path))
            print("it is after status")
            self.image = image
            print("it is after image")
            self.file_path = unicode_file_path
            print("it is after filepath")
            self.canvas.load_pixmap(QPixmap.fromImage(image))
            print("it is after canvas")
            if self.label_file:
                print("it is inside if")
                self.load_labels(self.label_file.shapes)
                print("it is after load albels")
            print("it is before set_clean")
            self.set_clean()
            print("it is after set_clean")
            self.canvas.setEnabled(True)
            print("after canvas")
            # self.adjust_scale(initial=True)
            # print("after adjust")
            # self.paint_canvas()
            # print("after paint_canvas")
            self.add_recent_file(self.file_path)
            print("add recent")
            # self.toggle_actions(True)
            print("toggle")
            self.show_bounding_box_from_annotation_file(file_path)
            print("it is after show bounding box")

            counter = self.counter_str()
            print("it is after counter")
            self.setWindowTitle(__appname__ + ' ' + file_path + ' ' + counter)
            print("it is after setwindow title")

            # Default : select last item if there is at least one item
            if self.listView_3.count():
                self.listView_3.setCurrentItem(self.listView_3.item(self.listView_3.count() - 1))
                self.listView_3.item(self.listView_3.count() - 1).setSelected(True)
            print("it is outside if")
            self.canvas.setFocus(True)
            print("it is after canvas focus")
            return True
        return False

    def delete_image(self):
        delete_path = self.file_path
        if delete_path is not None:
            self.open_next_image()
            self.cur_img_idx -= 1
            self.img_count -= 1
            if os.path.exists(delete_path):
                os.remove(delete_path)
            self.import_dir_images(self.last_open_dir)

    def save_file(self, _value=False):
        if self.default_save_dir is not None and len(ustr(self.default_save_dir)):
            if self.file_path:
                image_file_name = os.path.basename(self.file_path)
                saved_file_name = os.path.splitext(image_file_name)[0]
                saved_path = os.path.join(ustr(self.default_save_dir), saved_file_name)
                self._save_file(saved_path)
        else:
            image_file_dir = os.path.dirname(self.file_path)
            image_file_name = os.path.basename(self.file_path)
            saved_file_name = os.path.splitext(image_file_name)[0]
            saved_path = os.path.join(image_file_dir, saved_file_name)
            self._save_file(saved_path if self.label_file
                            else self.save_file_dialog(remove_ext=False))

    def save_file_as(self, _value=False):
        assert not self.image.isNull(), "cannot save empty image"
        self._save_file(self.save_file_dialog())

    def save_file_dialog(self, remove_ext=True):
        caption = '%s - Choose File' % __appname__
        filters = 'File (*%s)' % LabelFile.suffix
        open_dialog_path = self.current_path()
        dlg = QFileDialog(self, caption, open_dialog_path, filters)
        dlg.setDefaultSuffix(LabelFile.suffix[1:])
        dlg.setAcceptMode(QFileDialog.AcceptSave)
        filename_without_extension = os.path.splitext(self.file_path)[0]
        dlg.selectFile(filename_without_extension)
        dlg.setOption(QFileDialog.DontUseNativeDialog, False)
        if dlg.exec_():
            full_file_path = ustr(dlg.selectedFiles()[0])
            if remove_ext:
                return os.path.splitext(full_file_path)[0]  # Return file path without the extension.
            else:
                return full_file_path
        return ''

    def _save_file(self, annotation_file_path):
        if annotation_file_path and self.save_labels(annotation_file_path):
            self.set_clean()
            self.statusBar().showMessage('Saved to  %s' % annotation_file_path)
            self.statusBar().show()

    def scan_all_images(self, folder_path):
        extensions = ['.%s' % fmt.data().decode("ascii").lower() for fmt in QImageReader.supportedImageFormats()]
        images = []

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(tuple(extensions)):
                    relative_path = os.path.join(root, file)
                    path = ustr(os.path.abspath(relative_path))
                    images.append(path)
        natural_sort(images, key=lambda x: x.lower())
        return images

    def toggle_draw_mode(self, edit=True):
        self.canvas.set_editing(edit)
        self.actions.createMode.setEnabled(edit)
        self.actions.editMode.setEnabled(not edit)

    def set_create_mode(self):
        print("it is inside set_create_mode")
        assert self.advanced()
        print("it is after assert")
        self.toggle_draw_mode(False)
        print("it is after toggle")

    def set_edit_mode(self):
        print("it is inside set_edit_mode")
        assert self.advanced()
        print("it is after assert in edit")
        self.toggle_draw_mode(True)
        print("it is after toggle draw mode true")
        self.label_selection_changed()
        print("it is after label_selection_changed")

    def label_selection_changed(self):
        item = self.current_item()
        if item and self.canvas.editing():
            self._no_selection_slot = True
            self.canvas.select_shape(self.items_to_shapes[item])
            shape = self.items_to_shapes[item]
            # Add Chris
            self.diffc_button.setChecked(shape.difficult)

    def current_item(self):
        items = self.tabWidget.selectedItems()
        if items:
            return items[0]
        return None

    def beginner(self):
        return self._beginner

    def advanced(self):
        return not self.beginner()

    def may_continue(self):
        if not self.dirty:
            return True
        else:
            discard_changes = self.discard_changes_dialog()
            if discard_changes == QMessageBox.No:
                return True
            elif discard_changes == QMessageBox.Yes:
                self.save_file()
                return True
            else:
                return False

    def discard_changes_dialog(self):
        yes, no, cancel = QMessageBox.Yes, QMessageBox.No, QMessageBox.Cancel
        msg = u'You have unsaved changes, would you like to save them and proceed?\nClick "No" to undo all changes.'
        return QMessageBox.warning(self, u'Attention', msg, yes | no | cancel)

    def show_info_dialog(self):
        from libs.__init__ import __version__
        msg = u'Name:{0} \nApp Version:{1} \n{2} '.format(__appname__, __version__, sys.version_info)
        QMessageBox.information(self, u'Information', msg)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScandatStudio"))
        self.BoxAndFileLists.setTabText(self.BoxAndFileLists.indexOf(self.BoxLists), _translate("MainWindow", "Box Lists"))
        self.BoxAndFileLists.setTabText(self.BoxAndFileLists.indexOf(self.FileLabels), _translate("MainWindow", "File Labels"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpenDir.setText(_translate("MainWindow", "OpenDir"))
        self.actionOpenDir.setToolTip(_translate("MainWindow", "open the directory"))
        self.actionOpenDir.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSaveAs.setText(_translate("MainWindow", "SaveAs"))
        self.actionSaveAs.setToolTip(_translate("MainWindow", "save as"))
        self.actionSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionCreate_RectBox.setText(_translate("MainWindow", "Create RectBox"))
        self.actionCreate_RectBox.setToolTip(_translate("MainWindow", "create the rect"))
        self.actionCreate_RectBox.setShortcut(_translate("MainWindow", "W"))
        self.actionEdit_Label.setText(_translate("MainWindow", "Edit Label"))
        self.actionEdit_Label.setToolTip(_translate("MainWindow", "edit the label"))
        self.actionEdit_Label.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionDuplicate_RectBox.setText(_translate("MainWindow", "Duplicate RectBox"))
        self.actionDuplicate_RectBox.setToolTip(_translate("MainWindow", "duplicate the rectbox"))
        self.actionDuplicate_RectBox.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionDelete_RectBox.setText(_translate("MainWindow", "Delete RectBox"))
        self.actionDelete_RectBox.setToolTip(_translate("MainWindow", "delete the rectbox"))
        self.actionDelete_RectBox.setShortcut(_translate("MainWindow", "Del"))
        self.actionHide_RectBox.setText(_translate("MainWindow", "Hide RectBox"))
        self.actionHide_RectBox.setToolTip(_translate("MainWindow", "hide the rectbox"))
        self.actionHide_RectBox.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionShow_RectBox.setText(_translate("MainWindow", "Show RectBox"))
        self.actionShow_RectBox.setToolTip(_translate("MainWindow", "showing the rectbox"))
        self.actionShow_RectBox.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_In.setToolTip(_translate("MainWindow", "zoom in"))
        self.actionZoom_In.setShortcut(_translate("MainWindow", "Ctrl++"))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionZoom_Out.setToolTip(_translate("MainWindow", "zoom out"))
        self.actionZoom_Out.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.actionOriginal_Size.setText(_translate("MainWindow", "Original Size"))
        self.actionOriginal_Size.setToolTip(_translate("MainWindow", "original size"))
        self.actionOriginal_Size.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.actionFit_Window.setText(_translate("MainWindow", "Fit Window"))
        self.actionFit_Window.setToolTip(_translate("MainWindow", "fit window"))
        self.actionFit_Window.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionFit_Width.setText(_translate("MainWindow", "Fit Width"))
        self.actionFit_Width.setToolTip(_translate("MainWindow", "fit width"))
        self.actionFit_Width.setShortcut(_translate("MainWindow", "Ctrl+Shift+F"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setToolTip(_translate("MainWindow", "close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionReset_All.setText(_translate("MainWindow", "Reset All"))
        self.actionReset_All.setToolTip(_translate("MainWindow", "reset all"))
        self.actionDelete_Current_Image.setText(_translate("MainWindow", "Delete Current Image"))
        self.actionDelete_Current_Image.setToolTip(_translate("MainWindow", "delete the current image"))
        self.actionDelete_Current_Image.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setToolTip(_translate("MainWindow", "quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        newAct = contextMenu.addAction("New")
        openAct = contextMenu.addAction("Open")
        quitAct = contextMenu.addAction("Quit")
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            self.close()
        self.show()

def read(filename, default=None):
    try:
        reader = QImageReader(filename)
        reader.setAutoTransform(True)
        return reader.read()
    except:
        return default


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
