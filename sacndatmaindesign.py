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
from os import read

from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
import sys
from tkinter import *
from os.path import expanduser

from functools import partial
from collections import defaultdict
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QPushButton,QFileDialog, QStatusBar
from PyQt5.QtGui import QIcon, QImageReader
import pyqt5_tools

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

from labelImg import MainWindow
from labelImg import WindowMixin




from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialog import dialogapp
from functools import partial
from libs.zoomWidget import ZoomWidget

__appname__ = "Scandat Studio"

class open_dir(QWidget):


    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.labelimage = QLabel()
        #layout.addWidget(self.labelimage)
        self.setLayout(layout)

        self.get_image_file()

    def get_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "open the Image file", r"<Default dir>",
                                                   "Image files(*.jpg *.png *.jpeg *.gif)")
        self.labelimage.setPixmap(QPixmap(file_name))







class Ui_ScandatStudio(QWidget):
    FIT_WINDOW, FIT_WIDTH, MANUAL_ZOOM = list(range(3))

    def setupUi(self, ScandatStudio, default_filename=None, default_prefdef_class_file=None, default_save_dir=None):
        ScandatStudio.setObjectName("ScandatStudio")
        ScandatStudio.resize(1400, 767)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ScandatStudio.setWindowIcon(icon)
        ScandatStudio.setAutoFillBackground(False)
        ScandatStudio.setStyleSheet("background-color: rgb(247, 255, 197);")
        self.centralwidget = QtWidgets.QWidget(ScandatStudio)
        self.centralwidget.setObjectName("centralwidget")
        self.logolabel = QtWidgets.QLabel(self.centralwidget)
        self.logolabel.setGeometry(QtCore.QRect(0, 0, 81, 51))
        self.logolabel.setText("")
        self.logolabel.setPixmap(QtGui.QPixmap("logo.png"))
        self.logolabel.setObjectName("logolabel")
        self.label2 = QtWidgets.QLabel("centralwidget")
        self.label2.setGeometry(QtCore.QRect(30,30,100, 60))
        self.label2.setText("")
        self.label3 = QtWidgets.QLabel("centralwidget")
        self.label3.setGeometry(QtCore.QRect(50, 50, 150, 100))
        self.label3.setText("")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(1060, 0, 301, 691))
        self.tabWidget.setObjectName("tabWidget")
        self.FileList = QtWidgets.QWidget()
        self.FileList.setObjectName("FileList")
        self.tabWidget.addTab(self.FileList, "")
        self.BoxLabel = QtWidgets.QWidget()
        self.BoxLabel.setObjectName("BoxLabel")
        self.tabWidget.addTab(self.BoxLabel, "")
        ScandatStudio.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ScandatStudio)
        self.statusbar.setObjectName("statusbar")
        ScandatStudio.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(ScandatStudio)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolBar.setMouseTracking(False)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet("background-color: rgb(179, 0, 0);")
        self.toolBar.setObjectName("toolBar")
        ScandatStudio.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionopen = QtWidgets.QAction(ScandatStudio)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pyqt5 icons/icons/icons/open-source.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionopen.setIcon(icon1)
        self.actionopen.setObjectName("actionopen")
        self.actionnew = QtWidgets.QAction(ScandatStudio)
        #self.actionnew.actiontriggered[QAction].connect(self.toolbtnpressed)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pyqt5 icons/icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionnew.setIcon(icon2)
        self.actionnew.setObjectName("actionnew")
        self.actionsave = QtWidgets.QAction(ScandatStudio)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pyqt5 icons/icons/icons/safe--plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionsave.setIcon(icon3)
        self.actionsave.setObjectName("actionsave")
        self.actionsaveAs = QtWidgets.QAction(ScandatStudio)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("pyqt5 icons/icons/icons/safe--pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionsaveAs.setIcon(icon4)
        self.actionsaveAs.setObjectName("actionsaveAs")
        self.actioncreateRECT = QtWidgets.QAction(ScandatStudio)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("pyqt5 icons/icons/icons/receipt-medium.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncreateRECT.setIcon(icon5)
        self.actioncreateRECT.setObjectName("actioncreateRECT")
        self.actionEditLabel = QtWidgets.QAction(ScandatStudio)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("pyqt5 icons/icons/icons/edit-list-rtl.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionEditLabel.setIcon(icon6)
        self.actionEditLabel.setObjectName("actionEditLabel")
        self.actionDeleteRECT = QtWidgets.QAction(ScandatStudio)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("pyqt5 icons/icons/icons/document-attribute-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteRECT.setIcon(icon7)
        self.actionDeleteRECT.setObjectName("actionDeleteRECT")
        self.actionZoomIn = QtWidgets.QAction(ScandatStudio)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("pyqt5 icons/icons/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomIn.setIcon(icon8)
        self.actionZoomIn.setObjectName("actionZoomIn")
        self.actionZoomOut = QtWidgets.QAction(ScandatStudio)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("pyqt5 icons/icons/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomOut.setIcon(icon9)
        self.actionZoomOut.setObjectName("actionZoomOut")
        self.actionRun = QtWidgets.QAction(ScandatStudio)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("pyqt5 icons/icons/done.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon10)
        self.actionRun.setObjectName("actionRun")
        self.actionQuit = QtWidgets.QAction(ScandatStudio)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("pyqt5 icons/icons/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon11)
        self.actionQuit.setObjectName("actionQuit")
        self.actionInformation = QtWidgets.QAction(ScandatStudio)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("pyqt5 icons/icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInformation.setIcon(icon12)
        self.actionInformation.setObjectName("actionInformation")
        self.toolBar.addAction(self.actionopen)
        self.toolBar.addAction(self.actionnew)
        self.toolBar.addAction(self.actionsave)
        self.toolBar.addAction(self.actionsaveAs)
        self.toolBar.addAction(self.actioncreateRECT)
        self.toolBar.addAction(self.actionEditLabel)
        self.toolBar.addAction(self.actionDeleteRECT)
        self.toolBar.addAction(self.actionZoomIn)
        self.toolBar.addAction(self.actionZoomOut)
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addAction(self.actionInformation)

        self.actionRun.triggered.connect(self.window)
        self.actionopen.triggered.connect(self.open_file)
        self.actionZoomIn.triggered.connect(self.add_zoom,10)
        self.actionZoomOut.triggered.connect(self.add_zoom,-10)
        self.actionnew.triggered.connect(self.open_dir_dialog)
        self.actionsave.triggered.connect(self.save_file)
        self.actioncreateRECT.triggered.connect(self.set_create_mode)
        self.actionsaveAs.triggered.connect(self.save_file_as)
        self.actionEditLabel.triggered.connect(self.set_edit_mode)
        self.actionQuit.triggered.connect(self.close)
        self.actionInformation.triggered.connect(self.show_info_dialog)

        self.retranslateUi(ScandatStudio)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ScandatStudio)

        self.string_bundle = StringBundle.get_bundle()
        get_str = lambda str_id: self.string_bundle.get_string(str_id)

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

        self.settings = Settings()
        self.settings.load()
        settings = self.settings

        self.auto_saving = QAction(get_str('autoSaveMode'), self)
        self.auto_saving.setCheckable(True)
        self.auto_saving.setChecked(settings.get(SETTING_AUTO_SAVE, False))

        self.default_save_dir = default_save_dir

        self.canvas = Canvas(parent=self)
        self.canvas.zoomRequest.connect(self.zoom_request)
        self.canvas.set_drawing_shape_to_square(settings.get(SETTING_DRAW_SQUARE, False))

        self.dirty = False

        self.actions = Struct(createMode= self.actioncreateRECT, editMode= self.actionEditLabel, beginner=(), advanced=())

        self._beginner = True

        self.items_to_shapes = {}
        self.shapes_to_items = {}
        self.prev_label_text = ''



    def retranslateUi(self, ScandatStudio):
        _translate = QtCore.QCoreApplication.translate
        ScandatStudio.setWindowTitle(_translate("ScandatStudio", "Scandat Studio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FileList), _translate("ScandatStudio", "File_List"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BoxLabel), _translate("ScandatStudio", "Box_Label"))
        self.toolBar.setWindowTitle(_translate("ScandatStudio", "toolBar"))
        self.actionopen.setText(_translate("ScandatStudio", "open"))
        self.actionopen.setShortcut(_translate("ScandatStudio", "Ctrl+O"))
        self.actionnew.setText(_translate("ScandatStudio", "opendir"))
        self.actionnew.setShortcut(_translate("ScandatStudio", "Ctrl+N"))
        self.actionsave.setText(_translate("ScandatStudio", "save"))
        self.actionsave.setShortcut(_translate("ScandatStudio", "Ctrl+S"))
        self.actionsaveAs.setText(_translate("ScandatStudio", "saveAs"))
        self.actioncreateRECT.setText(_translate("ScandatStudio", "createRECT"))
        self.actioncreateRECT.setShortcut(_translate("ScandatStudio", "W"))
        self.actionEditLabel.setText(_translate("ScandatStudio", "EditLabel"))
        self.actionEditLabel.setShortcut(_translate("ScandatStudio", "Ctrl+E"))
        self.actionDeleteRECT.setText(_translate("ScandatStudio", "DeleteRECT"))
        self.actionDeleteRECT.setShortcut(_translate("ScandatStudio", "Del"))
        self.actionZoomIn.setText(_translate("ScandatStudio", "ZoomIn"))
        self.actionZoomIn.setShortcut(_translate("ScandatStudio", "Ctrl+=, Ctrl+="))
        self.actionZoomOut.setText(_translate("ScandatStudio", "ZoomOut"))
        self.actionZoomOut.setShortcut(_translate("ScandatStudio", "Ctrl+-"))
        self.actionRun.setText(_translate("ScandatStudio", "Run"))
        self.actionQuit.setText(_translate("ScandatStudio", "Quit"))
        self.actionQuit.setShortcut(_translate("ScandatStudio", "Ctrl+Q"))
        self.actionInformation.setText(_translate("ScandatStudio", "Information"))


    def window(self):
        self.w = dialogapp()
        self.w.show()

    def win(self):
        self.w2 = open_dir()
        self.w2.show()

    def set_zoom(self, value):
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
        scale = 10
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

    def open_file(self, _value=False):
        print('it is coming inside')
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

    def open_dir_dialog(self, _value=False, dir_path=None, silent=False):
        if not self.may_continue():
            return

        default_open_dir_path = dir_path if dir_path else '.'
        if self.last_open_dir and os.path.exists(self.last_open_dir):
            default_open_dir_path = self.last_open_dir
        else:
            default_open_dir_path = os.path.dirname(self.file_path) if self.file_path else '.'
        if silent != True:
            target_dir_path = ustr(QFileDialog.getExistingDirectory(self,
                                                                    '%s - Open Directory' % __appname__, default_open_dir_path,
                                                                    QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks))
        else:
            target_dir_path = ustr(default_open_dir_path)
        self.last_open_dir = target_dir_path
        self.import_dir_images(target_dir_path)

    def import_dir_images(self, dir_path):
        if not self.may_continue() or not dir_path:
            return

        self.last_open_dir = dir_path
        self.dir_name = dir_path
        self.file_path = None
        self.tabWidget.clear()
        self.m_img_list = self.scan_all_images(dir_path)
        self.img_count = len(self.m_img_list)
        self.open_next_image()
        for imgPath in self.m_img_list:
            item = QListWidgetItem(imgPath)
            self.tabWidget.addItem(item)

    def change_save_dir_dialog(self, _value=False):
        if self.default_save_dir is not None:
            path = ustr(self.default_save_dir)
        else:
            path = '.'

        dir_path = ustr(QFileDialog.getExistingDirectory(self,
                                                         '%s - Save annotations to the directory' % __appname__, path,
                                                         QFileDialog.ShowDirsOnly
                                                         | QFileDialog.DontResolveSymlinks))

        if dir_path is not None and len(dir_path) > 1:
            self.default_save_dir = dir_path

        self.statusBar().showMessage('%s . Annotation will be saved to %s' %
                                     ('Change saved folder', self.default_save_dir))
        self.statusBar().show()

    def open_next_image(self, _value=False, default_save_dir=None):
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

        filename = None
        if self.file_path is None:
            filename = self.m_img_list[0]
            self.cur_img_idx = 0
        else:
            if self.cur_img_idx + 1 < self.img_count:
                self.cur_img_idx += 1
                filename = self.m_img_list[self.cur_img_idx]

        if filename:
            self.load_file(filename)

    def reset_state(self):
        self.items_to_shapes.clear()
        self.shapes_to_items.clear()
        self.label_list.clear()
        self.file_path = None
        self.image_data = None
        self.label_file = None
        self.canvas.reset_state()
        self.label_coordinates.clear()
        self.combo_box.cb.clear()

    def error_message(self, title, message):
        return QMessageBox.critical(self, title,
                                    '<p><b>%s</b></p>%s' % (title, message))

    def status(self, message, delay=5000):
        self.statusBar().showMessage(message, delay)

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

    def set_clean(self):
        self.dirty = False
        self.actions.save.setEnabled(False)
        self.actions.create.setEnabled(True)

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
        if unicode_file_path and self.tabWidget.count() > 0:
            if unicode_file_path in self.m_img_list:
                index = self.m_img_list.index(unicode_file_path)
                file_widget_item = self.tabWidget.item(index)
                file_widget_item.setSelected(True)
            else:
                self.tabWidget.clear()
                self.m_img_list.clear()

        if unicode_file_path and os.path.exists(unicode_file_path):
            if LabelFile.is_label_file(unicode_file_path):
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
                # Load image:
                # read data first and store for saving into label file.
                self.image_data = read(unicode_file_path, None)
                self.label_file = None
                self.canvas.verified = False

            if isinstance(self.image_data, QImage):
                image = self.image_data
            else:
                image = QImage.fromData(self.image_data)
            if image.isNull():
                self.error_message(u'Error opening file',
                                   u"<p>Make sure <i>%s</i> is a valid image file." % unicode_file_path)
                self.status("Error reading %s" % unicode_file_path)
                return False
            self.status("Loaded %s" % os.path.basename(unicode_file_path))
            self.image = image
            self.file_path = unicode_file_path
            self.canvas.load_pixmap(QPixmap.fromImage(image))
            if self.label_file:
                self.load_labels(self.label_file.shapes)
            self.set_clean()
            self.canvas.setEnabled(True)
            self.adjust_scale(initial=True)
            self.paint_canvas()
            self.add_recent_file(self.file_path)
            self.toggle_actions(True)
            self.show_bounding_box_from_annotation_file(file_path)

            counter = self.counter_str()
            self.setWindowTitle(__appname__ + ' ' + file_path + ' ' + counter)

            # Default : select last item if there is at least one item
            if self.label_list.count():
                self.label_list.setCurrentItem(self.label_list.item(self.label_list.count() - 1))
                self.label_list.item(self.label_list.count() - 1).setSelected(True)

            self.canvas.setFocus(True)
            return True
        return False

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
        assert self.advanced()
        self.toggle_draw_mode(False)

    def set_edit_mode(self):
        assert self.advanced()
        self.toggle_draw_mode(True)
        self.label_selection_changed()

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

    def show_info_dialog(self):
        from libs.__init__ import __version__
        msg = u'Name:{0} \nApp Version:{1} \n{2} '.format(__appname__, __version__, sys.version_info)
        QMessageBox.information(self, u'Information', msg)


    def file_item_double_clicked(self, item=None):
        self.cur_img_idx = self.m_img_list.index(ustr(item.text()))
        filename = self.m_img_list[self.cur_img_idx]
        if filename:
            self.load_file(filename)

    def Window2(self):
        self.w = MainWindow()
        self.w.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScandatStudio = QtWidgets.QMainWindow()
    ui = Ui_ScandatStudio()
    ui.setupUi(ScandatStudio)
    ScandatStudio.show()
    sys.exit(app.exec_())
