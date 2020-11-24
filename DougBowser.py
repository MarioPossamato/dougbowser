#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# DougBowser
# An Experimental Super Mario Maker 2 Course Editor 
# Version 0.1
# Created by MarioPossamato

# This file is part of DougBowser.


#==== Module and library imports ====#
import sys             # Built-in module
import zlib            # Built-in module
from PyQt5 import QtCore, QtGui, QtWidgets
import Encryption
#====================================#
CoursePath = ""
HeaderSize = 0x10
FooterSize = 0x30

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__(None)
        self.setObjectName("Form")
        self.setWindowTitle("Doug Bowser; Super Mario Maker 2 Binary Course Data Editor")
        self.resize(771, 790)
        self.setMinimumSize(QtCore.QSize(771, 790))
        self.setMaximumSize(QtCore.QSize(771, 790))

        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.setFont(font)

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 751, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.openCourseButton = QtWidgets.QPushButton(self.groupBox)
        self.openCourseButton.setGeometry(QtCore.QRect(9, 10, 364, 41))
        self.openCourseButton.setObjectName("openCourseButton")
        self.openCourseButton.clicked.connect(self.HandleOpenFromFile)
        self.openCourseButton.setText("Open SMM2 Binary Course Data")

        self.saveCourseButton = QtWidgets.QPushButton(self.groupBox)
        self.saveCourseButton.setGeometry(QtCore.QRect(377, 10, 364, 41))
        self.saveCourseButton.setObjectName("saveCourseButton")
        self.saveCourseButton.clicked.connect(self.HandleSave)
        self.saveCourseButton.setText("Save SMM2 Binary Course Data")

        self.coursePath = QtWidgets.QLineEdit(self.groupBox)
        self.coursePath.setGeometry(QtCore.QRect(10, 60, 731, 31))
        self.coursePath.setReadOnly(True)
        self.coursePath.setObjectName("coursePath")
        self.coursePath.setPlaceholderText("No Course Selected...")

        self.GroupBox2 = QtWidgets.QGroupBox(self)
        self.GroupBox2.setGeometry(QtCore.QRect(10, 120, 751, 660))
        self.GroupBox2.setObjectName("GroupBox2")
        self.GroupBox2.setTitle("Raw Data Editor")

        self.GroupBox3 = QtWidgets.QGroupBox(self.GroupBox2)
        self.GroupBox3.setGeometry(QtCore.QRect(10, 20, 271, 61))
        self.GroupBox3.setObjectName("GroupBox3")
        self.GroupBox3.setTitle("Time Limit")

        self.TimeLimit = QtWidgets.QLineEdit(self.GroupBox3)
        self.TimeLimit.setGeometry(QtCore.QRect(10, 20, 251, 31))
        self.TimeLimit.setMaxLength(5)
        self.TimeLimit.setReadOnly(False)
        self.TimeLimit.setObjectName("TimeLimit")
        self.TimeLimit.setPlaceholderText("500")

        self.GroupBox4 = QtWidgets.QGroupBox(self.GroupBox2)
        self.GroupBox4.setGeometry(QtCore.QRect(10, 90, 271, 371))
        self.GroupBox4.setObjectName("GroupBox4")
        self.GroupBox4.setTitle("Date")

        self.GroupBox5 = QtWidgets.QGroupBox(self.GroupBox4)
        self.GroupBox5.setGeometry(QtCore.QRect(10, 20, 251, 61))
        self.GroupBox5.setObjectName("GroupBox5")
        self.GroupBox5.setTitle("Last Saved Year")

        self.CreationYear = QtWidgets.QLineEdit(self.GroupBox5)
        self.CreationYear.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.CreationYear.setText("")
        self.CreationYear.setMaxLength(5)
        self.CreationYear.setReadOnly(False)
        self.CreationYear.setObjectName("CreationYear")
        self.CreationYear.raise_()
        self.CreationYear.setPlaceholderText("2020")

        self.GroupBox6 = QtWidgets.QGroupBox(self.GroupBox4)
        self.GroupBox6.setGeometry(QtCore.QRect(10, 90, 251, 61))
        self.GroupBox6.setObjectName("GroupBox6")
        self.GroupBox6.setTitle("Last Saved Month")

        self.CreationMonth = QtWidgets.QLineEdit(self.GroupBox6)
        self.CreationMonth.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.CreationMonth.setMaxLength(3)
        self.CreationMonth.setReadOnly(False)
        self.CreationMonth.setObjectName("CreationMonth")
        self.CreationMonth.raise_()
        self.CreationMonth.setPlaceholderText("1")

        self.GroupBox8 = QtWidgets.QGroupBox(self.GroupBox4)
        self.GroupBox8.setGeometry(QtCore.QRect(10, 230, 251, 61))
        self.GroupBox8.setObjectName("GroupBox8")
        self.GroupBox8.setTitle("Last Saved Hour")

        self.CreationHour = QtWidgets.QLineEdit(self.GroupBox8)
        self.CreationHour.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.CreationHour.setMaxLength(3)
        self.CreationHour.setReadOnly(False)
        self.CreationHour.setObjectName("CreationHour")
        self.CreationHour.raise_()
        self.CreationHour.setPlaceholderText("1")

        self.GroupBox7 = QtWidgets.QGroupBox(self.GroupBox4)
        self.GroupBox7.setGeometry(QtCore.QRect(10, 160, 251, 61))
        self.GroupBox7.setObjectName("GroupBox7")
        self.GroupBox7.setTitle("Last Saved Day")

        self.CreationDay = QtWidgets.QLineEdit(self.GroupBox7)
        self.CreationDay.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.CreationDay.setMaxLength(3)
        self.CreationDay.setReadOnly(False)
        self.CreationDay.setObjectName("CreationDay")
        self.CreationDay.raise_()
        self.CreationDay.setPlaceholderText("1")

        self.GroupBox9 = QtWidgets.QGroupBox(self.GroupBox4)
        self.GroupBox9.setGeometry(QtCore.QRect(10, 300, 251, 61))
        self.GroupBox9.setObjectName("GroupBox9")
        self.GroupBox9.setTitle("Last Saved Minute")

        self.CreationMinute = QtWidgets.QLineEdit(self.GroupBox9)
        self.CreationMinute.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.CreationMinute.setMaxLength(3)
        self.CreationMinute.setReadOnly(False)
        self.CreationMinute.setObjectName("CreationMinute")
        self.CreationMinute.raise_()
        self.CreationMinute.setPlaceholderText("1")

        self.GroupBox10 = QtWidgets.QGroupBox(self.GroupBox2)
        self.GroupBox10.setGeometry(QtCore.QRect(290, 20, 451, 61))
        self.GroupBox10.setObjectName("GroupBox10")
        self.GroupBox10.setTitle("Autoscroll")

        self.Autoscroll = QtWidgets.QLineEdit(self.GroupBox10)
        self.Autoscroll.setGeometry(QtCore.QRect(10, 20, 431, 31))
        self.Autoscroll.setReadOnly(False)
        self.Autoscroll.setObjectName("Autoscroll")
        self.Autoscroll.setMaxLength(3)
        self.Autoscroll.raise_()
        self.Autoscroll.setPlaceholderText("0")

        self.GroupBox11 = QtWidgets.QGroupBox(self.GroupBox2)
        self.GroupBox11.setGeometry(QtCore.QRect(290, 90, 451, 482))
        self.GroupBox11.setObjectName("GroupBox11")
        self.GroupBox11.setTitle("Sprites")

        self.GroupBox12 = QtWidgets.QGroupBox(self.GroupBox11)
        self.GroupBox12.setGeometry(QtCore.QRect(10, 20, 431, 61))
        self.GroupBox12.setObjectName("GroupBox12")
        self.GroupBox12.setTitle("Sprite Count")

        self.SpriteCount = QtWidgets.QLineEdit(self.GroupBox12)
        self.SpriteCount.setGeometry(QtCore.QRect(10, 20, 411, 31))
        self.SpriteCount.setReadOnly(True)
        self.SpriteCount.setObjectName("SpriteCount")
        self.SpriteCount.raise_()
        self.SpriteCount.setPlaceholderText("1")

        self.GroupBox13 = QtWidgets.QGroupBox(self.GroupBox11)
        self.GroupBox13.setGeometry(QtCore.QRect(10, 90, 431, 382))
        self.GroupBox13.setObjectName("GroupBox13")
        self.GroupBox13.setTitle("All Sprites In Course")

        self.SpritesList = QtWidgets.QListWidget(self.GroupBox13)
        self.SpritesList.setGeometry(QtCore.QRect(10, 20, 411, 350))
        self.SpritesList.setObjectName("SpritesList")
        self.SpritesList.setFont(font)

        self.GroupBox14 = QtWidgets.QGroupBox(self)
        self.GroupBox14.setGeometry(QtCore.QRect(20, 589, 272, 103))
        self.GroupBox14.setObjectName("GroupBox14")
        self.GroupBox14.setTitle("Sprite Data Viewer")

        self.SpriteCountBox = QtWidgets.QComboBox(self.GroupBox14)
        self.SpriteCountBox.setGeometry(QtCore.QRect(10, 20, 252, 30))
        self.SpriteCountBox.setObjectName("SpriteCountBox")
        self.SpriteCountBox.currentIndexChanged.connect(self.SpriteCountBoxIndexChanged, self.SpriteCountBox.currentIndex())

        self.SpriteFlags = QtWidgets.QLineEdit(self.GroupBox14)
        self.SpriteFlags.setGeometry(QtCore.QRect(10, 60, 135, 30))
        self.SpriteFlags.setMaxLength(16)
        self.SpriteFlags.setPlaceholderText("0600004006000040")

        self.SpriteID = QtWidgets.QLineEdit(self.GroupBox14)
        self.SpriteID.setGeometry(QtCore.QRect(153, 60, 109, 30))
        self.SpriteID.setMaxLength(3)
        self.SpriteID.setPlaceholderText("0")

        self.CourseName = QtWidgets.QLineEdit(self)
        self.CourseName.setGeometry(QtCore.QRect(20, 700, 270, 30))
        self.CourseName.setMaxLength(32)
        self.CourseName.setReadOnly(True)
        self.CourseName.setPlaceholderText("Course Name...")

        self.CourseDescription = QtWidgets.QLineEdit(self)
        self.CourseDescription.setGeometry(QtCore.QRect(20, 739, 733, 30))
        self.CourseDescription.setMaxLength(100)
        self.CourseDescription.setReadOnly(True)
        self.CourseDescription.setPlaceholderText("Course Description...")

    def __init2__(self):
        return

    def SpriteCountBoxIndexChanged(self):
        global data
        ParentSpriteFlags = data[0x254+HeaderSize+0x20*(int(self.SpriteCountBox.currentText())-1):0x254+HeaderSize+0x20*(int(self.SpriteCountBox.currentText())-1)+4]
        ParentSpriteFlags = bytearray(ParentSpriteFlags)
        ParentSpriteFlags.reverse()
        ParentSpriteFlags = bytes(ParentSpriteFlags)
        ParentSpriteFlags = bytes.hex(ParentSpriteFlags)
        ChildSpriteFlags = data[0x258+HeaderSize+0x20*(int(self.SpriteCountBox.currentText())-1):0x258+HeaderSize+0x20*(int(self.SpriteCountBox.currentText())-1)+4]
        ChildSpriteFlags = bytearray(ChildSpriteFlags)
        ChildSpriteFlags.reverse()
        ChildSpriteFlags = bytes(ChildSpriteFlags)
        ChildSpriteFlags = bytes.hex(ChildSpriteFlags)
        SpriteFlags = ParentSpriteFlags + ChildSpriteFlags
        self.SpriteFlags.setText(SpriteFlags)
        SpriteID = data[0x260+HeaderSize+0x20*(int(self.SpriteCountBox.currentText())-1):0x260+HeaderSize+0x20*(int(self.SpriteCountBox.currentText())-1)+1]
        self.SpriteID.setText(str(int.from_bytes(SpriteID, "big")))

    def HandleOpenFromFile(self):
        global CoursePath, data
        CoursePath = QtWidgets.QFileDialog.getOpenFileName(self, "Open Course", "", "Binary Course Data File (*.bcd)")[0]
        if not CoursePath:
            return
        self.coursePath.setText(CoursePath)
        with open(CoursePath,"rb") as Course:
            data = Course.read()
            if data[4:6] == bytes([0x10,0x00]) and data[12:16].decode("utf-8") == "SCDL":
                pass
            else:
                QtWidgets.QMessageBox.warning(None, "Error", "Not a valid Super Mario Maker 2 course file!")
                return
            data = Encryption.DecryptData(data, Encryption.CourseKeyTable, 0x10)
            CourseName = data[0xF4+HeaderSize:0xF4+HeaderSize+0x42].decode("utf-16")
            self.CourseName.setText(CourseName)
            CourseDescription = data[0x136+HeaderSize:0x136+HeaderSize+0xCA].decode("utf-16")
            self.CourseDescription.setText(CourseDescription)
            TimeLimit = data[0x4+HeaderSize:0x4+HeaderSize+0x4]
            TimeLimit = bytearray(TimeLimit)
            TimeLimit.reverse()
            TimeLimit = bytes(TimeLimit)
            TimeLimit = bytes.hex(TimeLimit)
            TimeLimit = int(TimeLimit, 16)
            self.TimeLimit.setText(str(TimeLimit))
            CreationYear = data[0x8+HeaderSize:0x8+HeaderSize+0x2]
            CreationYear = bytearray(CreationYear)
            CreationYear.reverse()
            CreationYear = bytes(CreationYear)
            CreationYear = bytes.hex(CreationYear)
            CreationYear = int(CreationYear, 16)
            self.CreationYear.setText(str(CreationYear))
            CreationMonth = data[0xA+HeaderSize:0xA+HeaderSize+0x1]
            CreationMonth = bytes.hex(CreationMonth)
            CreationMonth = int(CreationMonth, 16)
            self.CreationMonth.setText(str(CreationMonth))
            CreationDay = data[0xB+HeaderSize:0xB+HeaderSize+0x1]
            CreationDay = bytes.hex(CreationDay)
            CreationDay = int(CreationDay, 16)
            self.CreationDay.setText(str(CreationDay))
            CreationHour = data[0xC+HeaderSize:0xC+HeaderSize+0x1]
            CreationHour = bytes.hex(CreationHour)
            CreationHour = int(CreationHour, 16)
            self.CreationHour.setText(str(CreationHour))
            CreationMinute = data[0xD+HeaderSize:0xD+HeaderSize+0x1]
            CreationMinute = bytes.hex(CreationMinute)
            CreationMinute = int(CreationMinute, 16)
            self.CreationMinute.setText(str(CreationMinute))
            Autoscroll = data[0x6+HeaderSize:0x6+HeaderSize+0x1]
            Autoscroll = bytes.hex(Autoscroll)
            Autoscroll = int(Autoscroll, 16)
            self.Autoscroll.setText(str(Autoscroll))
            SpriteCount = data[0x21C+HeaderSize:0x21C+HeaderSize+0x4]
            SpriteCount = bytearray(SpriteCount)
            SpriteCount.reverse()
            SpriteCount = bytes(SpriteCount)
            SpriteCount = bytes.hex(SpriteCount)
            SpriteCount = int(SpriteCount, 16)
            self.SpriteCount.setText(str(SpriteCount))
            for i in range(2600):
                SpriteID = data[0x260+HeaderSize+0x20*i:0x260+HeaderSize+0x20*i+1]
                SpriteName = f"Unknown({SpriteID})"
                if int.from_bytes(SpriteID, "big") in range(0x00,0x77):
                    self.SpritesList.addItem("Sprite " + str(i) + ":"+(" "*(5-len(str(i))))+ hex(int.from_bytes(SpriteID, "big")) + " located at " + str(hex(608 + 32 * i)))
                    self.SpriteCountBox.addItem(str(i + 1))
            

    def HandleSave(self):
        global CoursePath, data
        if not CoursePath:
            print("No course has been opened!  Please open one before you try to save it! ;)")
            return
        else:
            data = bytearray(data)
            TimeLimit = "%04X" % int(self.TimeLimit.text())
            TimeLimit = bytes.fromhex(TimeLimit)
            TimeLimit = bytearray(TimeLimit)
            TimeLimit.reverse()
            TimeLimit = bytes(TimeLimit)
            Autoscroll = "%02X" % int(self.Autoscroll.text())
            Autoscroll = bytes.fromhex(Autoscroll)
            CreationYear = "%04X" % int(self.CreationYear.text())
            CreationYear = bytes.fromhex(CreationYear)
            CreationYear = bytearray(CreationYear)
            CreationYear.reverse()
            CreationYear = bytes(CreationYear)
            CreationMonth = "%02X" % int(self.CreationMonth.text())
            CreationMonth = bytes.fromhex(CreationMonth)
            CreationMonth = bytearray(CreationMonth)
            CreationMonth.reverse()
            CreationMonth = bytes(CreationMonth)
            CreationDay = "%02X" % int(self.CreationDay.text())
            CreationDay = bytes.fromhex(CreationDay)
            CreationDay = bytearray(CreationDay)
            CreationDay.reverse()
            CreationDay = bytes(CreationDay)
            CreationHour = "%02X" % int(self.CreationHour.text())
            CreationHour = bytes.fromhex(CreationHour)
            CreationHour = bytearray(CreationHour)
            CreationHour.reverse()
            CreationHour = bytes(CreationHour)
            CreationMinute = "%02X" % int(self.CreationMinute.text())
            CreationMinute = bytes.fromhex(CreationMinute)
            CreationMinute = bytearray(CreationMinute)
            CreationMinute.reverse()
            CreationMinute = bytes(CreationMinute)
            SpriteFlags = self.SpriteFlags.text()
            ParentSpriteFlags, ChildSpriteFlags = SpriteFlags[:len(SpriteFlags)//2], SpriteFlags[len(SpriteFlags)//2:]
            ParentSpriteFlags, ChildSpriteFlags = SpriteFlags[:len(SpriteFlags)//2], SpriteFlags[len(SpriteFlags)//2:]
            ParentSpriteFlags = bytes.fromhex(ParentSpriteFlags)
            ParentSpriteFlags = bytearray(ParentSpriteFlags)
            ParentSpriteFlags.reverse()
            ParentSpriteFlags = bytes(ParentSpriteFlags)
            ChildSpriteFlags = bytes.fromhex(ChildSpriteFlags)
            ChildSpriteFlags = bytearray(ChildSpriteFlags)
            ChildSpriteFlags.reverse()
            Flags = bytes(ChildSpriteFlags)
            SpriteFlags = bytes.hex(ParentSpriteFlags)+bytearray.hex(ChildSpriteFlags)
            SpriteFlags = bytearray.fromhex(SpriteFlags)
            SpriteID = self.SpriteID.text()
            CourseName = self.CourseName.text()
            CourseDescription = self.CourseDescription.text()
            data[0x4+HeaderSize:0x6+HeaderSize] = TimeLimit
            data[0x6+HeaderSize:0x7+HeaderSize] = Autoscroll
            data[0x8+HeaderSize:0xA+HeaderSize] = CreationYear
            data[0xA+HeaderSize:0xB+HeaderSize] = CreationMonth
            data[0xB+HeaderSize:0xC+HeaderSize] = CreationDay
            data[0xC+HeaderSize:0xD+HeaderSize] = CreationHour
            data[0xD+HeaderSize:0xE+HeaderSize] = CreationMinute
            with open(CoursePath,"wb") as Course:
                data = bytearray(data)
                data[0x8:0xC] = int.to_bytes(zlib.crc32(data[0x10:]), 0x4, "little")
                data = Encryption.EncryptData(data, Encryption.CourseKeyTable, 0x10)
                Course.write(data)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationDisplayName("")

    mainWindow = MainWindow()
    mainWindow.__init2__()
    mainWindow.show()
    app.exec_()
    sys.exit()


if __name__ == "__main__": main()
