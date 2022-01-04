from  PyQt5.QtCore import QDate, QDateTime, QTime, Qt

now = QDate.currentDate()
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleShortDate))
print()

datetime = QDateTime.currentDateTime()
print(datetime.toUTC().toString(Qt.ISODate))
print(datetime.toString())
print()

time = QTime.currentTime()
print(time.toString(Qt.DefaultLocaleShortDate))


