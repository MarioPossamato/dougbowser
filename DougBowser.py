#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# DougBowser
# An Experimental Super Mario Maker 2 Course Editor 
# Version 0.1
# Created by MarioPossamato

# This file is part of DougBowser.


#==== Module and library imports ====#
import sys             # Built-in module
from PyQt5 import QtCore, QtGui, QtWidgets
import Encryption
#====================================#
CoursePath = ''
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

        self.SaveYear = QtWidgets.QLineEdit(self.GroupBox5)
        self.SaveYear.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.SaveYear.setText("")
        self.SaveYear.setMaxLength(5)
        self.SaveYear.setReadOnly(False)
        self.SaveYear.setObjectName("SaveYear")
        self.SaveYear.raise_()
        self.SaveYear.setPlaceholderText("2020")

        self.GroupBox6 = QtWidgets.QGroupBox(self.GroupBox4)
        self.GroupBox6.setGeometry(QtCore.QRect(10, 90, 251, 61))
        self.GroupBox6.setObjectName("GroupBox6")
        self.GroupBox6.setTitle("Last Saved Month")

        self.SaveMonth = QtWidgets.QLineEdit(self.GroupBox6)
        self.SaveMonth.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.SaveMonth.setMaxLength(3)
        self.SaveMonth.setReadOnly(False)
        self.SaveMonth.setObjectName("SaveMonth")
        self.SaveMonth.raise_()
        self.SaveMonth.setPlaceholderText("1")

        self.GroupBox8 = QtWidgets.QGroupBox(self.GroupBox4)
        self.GroupBox8.setGeometry(QtCore.QRect(10, 230, 251, 61))
        self.GroupBox8.setObjectName("GroupBox8")
        self.GroupBox8.setTitle("Last Saved Hour")

        self.SaveHour = QtWidgets.QLineEdit(self.GroupBox8)
        self.SaveHour.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.SaveHour.setMaxLength(3)
        self.SaveHour.setReadOnly(False)
        self.SaveHour.setObjectName("SaveHour")
        self.SaveHour.raise_()
        self.SaveHour.setPlaceholderText("1")

        self.GroupBox7 = QtWidgets.QGroupBox(self.GroupBox4)
        self.GroupBox7.setGeometry(QtCore.QRect(10, 160, 251, 61))
        self.GroupBox7.setObjectName("GroupBox7")
        self.GroupBox7.setTitle("Last Saved Day")

        self.SaveDay = QtWidgets.QLineEdit(self.GroupBox7)
        self.SaveDay.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.SaveDay.setMaxLength(3)
        self.SaveDay.setReadOnly(False)
        self.SaveDay.setObjectName("SaveDay")
        self.SaveDay.raise_()
        self.SaveDay.setPlaceholderText("1")

        self.GroupBox9 = QtWidgets.QGroupBox(self.GroupBox4)
        self.GroupBox9.setGeometry(QtCore.QRect(10, 300, 251, 61))
        self.GroupBox9.setObjectName("GroupBox9")
        self.GroupBox9.setTitle("Last Saved Minute")

        self.SaveMinute = QtWidgets.QLineEdit(self.GroupBox9)
        self.SaveMinute.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.SaveMinute.setMaxLength(3)
        self.SaveMinute.setReadOnly(False)
        self.SaveMinute.setObjectName("SaveMinute")
        self.SaveMinute.raise_()
        self.SaveMinute.setPlaceholderText("1")

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
        self.GroupBox11.setTitle("Entities")

        self.GroupBox12 = QtWidgets.QGroupBox(self.GroupBox11)
        self.GroupBox12.setGeometry(QtCore.QRect(10, 20, 431, 61))
        self.GroupBox12.setObjectName("GroupBox12")
        self.GroupBox12.setTitle("Object Count")

        self.ObjectCount = QtWidgets.QLineEdit(self.GroupBox12)
        self.ObjectCount.setGeometry(QtCore.QRect(10, 20, 411, 31))
        self.ObjectCount.setReadOnly(True)
        self.ObjectCount.setObjectName("ObjectCount")
        self.ObjectCount.raise_()
        self.ObjectCount.setPlaceholderText("1")

        self.GroupBox13 = QtWidgets.QGroupBox(self.GroupBox11)
        self.GroupBox13.setGeometry(QtCore.QRect(10, 90, 431, 382))
        self.GroupBox13.setObjectName("GroupBox13")
        self.GroupBox13.setTitle("All Entities In Course")

        self.EntitiesList = QtWidgets.QListWidget(self.GroupBox13)
        self.EntitiesList.setGeometry(QtCore.QRect(10, 20, 411, 350))
        self.EntitiesList.setObjectName("EntitiesList")
        self.EntitiesList.setFont(font)

        self.GroupBox14 = QtWidgets.QGroupBox(self)
        self.GroupBox14.setGeometry(QtCore.QRect(20, 589, 272, 103))
        self.GroupBox14.setObjectName("GroupBox14")
        self.GroupBox14.setTitle("Entity Data Viewer")

        self.EntityNumberBox = QtWidgets.QComboBox(self.GroupBox14)
        self.EntityNumberBox.setGeometry(QtCore.QRect(10, 20, 252, 30))
        self.EntityNumberBox.setObjectName("EntityNumberBox")
        self.EntityNumberBox.currentIndexChanged.connect(self.EntityNumberBoxIndexChanged, self.EntityNumberBox.currentIndex())

        self.EntityFlags = QtWidgets.QLineEdit(self.GroupBox14)
        self.EntityFlags.setGeometry(QtCore.QRect(10, 60, 135, 30))
        self.EntityFlags.setMaxLength(16)
        self.EntityFlags.setPlaceholderText("0600004006000040")

        self.EntityID = QtWidgets.QLineEdit(self.GroupBox14)
        self.EntityID.setGeometry(QtCore.QRect(153, 60, 109, 30))
        self.EntityID.setMaxLength(3)
        self.EntityID.setPlaceholderText("0")

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

    def EntityNumberBoxIndexChanged(self):
        global Buf
        ParentFlags = Buf[0x254+HeaderSize+0x20*(int(self.EntityNumberBox.currentText())-1):0x254+HeaderSize+0x20*(int(self.EntityNumberBox.currentText())-1)+4]
        ParentFlags = bytearray(ParentFlags)
        ParentFlags.reverse()
        ParentFlags = bytes(ParentFlags)
        ParentFlags = bytes.hex(ParentFlags)
        ChildFlags = Buf[0x258+HeaderSize+0x20*(int(self.EntityNumberBox.currentText())-1):0x258+HeaderSize+0x20*(int(self.EntityNumberBox.currentText())-1)+4]
        ChildFlags = bytearray(ChildFlags)
        ChildFlags.reverse()
        ChildFlags = bytes(ChildFlags)
        ChildFlags = bytes.hex(ChildFlags)
        EntityFlags = ParentFlags + ChildFlags
        self.EntityFlags.setText(EntityFlags)
        EntityID = Buf[0x260+HeaderSize+0x20*(int(self.EntityNumberBox.currentText())-1):0x260+HeaderSize+0x20*(int(self.EntityNumberBox.currentText())-1)+1]
        self.EntityID.setText(str(int.from_bytes(EntityID, 'big')))

    def HandleOpenFromFile(self):
        global CoursePath, Buf
        CoursePath = QtWidgets.QFileDialog.getOpenFileName(self, "Open Course", '', 'Binary Course Data File (*.bcd)')[0]
        if not CoursePath:
            return
        self.coursePath.setText(CoursePath)
        with open(CoursePath,'rb') as Course:
            Buf = Course.read()
            if Buf[4:6] == bytes([0x10,0x00]) and Buf[12:16].decode('utf-8') == 'SCDL':
                pass
            else:
                QtWidgets.QMessageBox.warning(None, 'Error', 'Not a valid Super Mario Maker 2 course file!')
                return
            Buf = Encryption.DecryptData(Buf, Encryption.CourseKeyTable, 0x10)
            CourseName = Buf[0xF4+HeaderSize:0xF4+HeaderSize+0x42].decode('utf-16')
            self.CourseName.setText(CourseName)
            CourseDescription = Buf[0x136+HeaderSize:0x136+HeaderSize+0xCA].decode('utf-16')
            self.CourseDescription.setText(CourseDescription)
            TimeLimit = Buf[0x4+HeaderSize:0x4+HeaderSize+0x4]
            TimeLimit = bytearray(TimeLimit)
            TimeLimit.reverse()
            TimeLimit = bytes(TimeLimit)
            TimeLimit = bytes.hex(TimeLimit)
            TimeLimit = int(TimeLimit, 16)
            self.TimeLimit.setText(str(TimeLimit))
            SaveYear = Buf[0x8+HeaderSize:0x8+HeaderSize+0x2]
            SaveYear = bytearray(SaveYear)
            SaveYear.reverse()
            SaveYear = bytes(SaveYear)
            SaveYear = bytes.hex(SaveYear)
            SaveYear = int(SaveYear, 16)
            self.SaveYear.setText(str(SaveYear))
            SaveMonth = Buf[0xA+HeaderSize:0xA+HeaderSize+0x1]
            SaveMonth = bytes.hex(SaveMonth)
            SaveMonth = int(SaveMonth, 16)
            self.SaveMonth.setText(str(SaveMonth))
            SaveDay = Buf[0xB+HeaderSize:0xB+HeaderSize+0x1]
            SaveDay = bytes.hex(SaveDay)
            SaveDay = int(SaveDay, 16)
            self.SaveDay.setText(str(SaveDay))
            SaveHour = Buf[0xC+HeaderSize:0xC+HeaderSize+0x1]
            SaveHour = bytes.hex(SaveHour)
            SaveHour = int(SaveHour, 16)
            self.SaveHour.setText(str(SaveHour))
            SaveMinute = Buf[0xD+HeaderSize:0xD+HeaderSize+0x1]
            SaveMinute = bytes.hex(SaveMinute)
            SaveMinute = int(SaveMinute, 16)
            self.SaveMinute.setText(str(SaveMinute))
            Autoscroll = Buf[0x6+HeaderSize:0x6+HeaderSize+0x1]
            Autoscroll = bytes.hex(Autoscroll)
            Autoscroll = int(Autoscroll, 16)
            self.Autoscroll.setText(str(Autoscroll))
            ObjectCount = Buf[0x21C+HeaderSize:0x21C+HeaderSize+0x4]
            ObjectCount = bytearray(ObjectCount)
            ObjectCount.reverse()
            ObjectCount = bytes(ObjectCount)
            ObjectCount = bytes.hex(ObjectCount)
            ObjectCount = int(ObjectCount, 16)
            self.ObjectCount.setText(str(ObjectCount))
            for i in range(2600):
                EntityID = Buf[0x260+HeaderSize+0x20*i:0x260+HeaderSize+0x20*i+1]
                EntityName = f'Unknown({EntityID})'
                if int.from_bytes(EntityID, 'big') in range(0x00,0x77):
                    self.EntitiesList.addItem(str(i) + ':'+(' '*(5-len(str(i))))+ hex(int.from_bytes(EntityID, 'big')) + ' located at ' + str(hex(608 + 32 * i)))
                    self.EntityNumberBox.addItem(str(i + 1))
            

    def HandleSave(self):
        global CoursePath, Buf
        if not CoursePath:
            print('No course has been opened!  Please open one before you try to save it! ;)')
            return
        else:
            Buf = bytearray(Buf)
            TimeLimit = "%04X" % int(self.TimeLimit.text())
            TimeLimit = bytes.fromhex(TimeLimit)
            TimeLimit = bytearray(TimeLimit)
            TimeLimit.reverse()
            TimeLimit = bytes(TimeLimit)
            Autoscroll = "%02X" % int(self.Autoscroll.text())
            Autoscroll = bytes.fromhex(Autoscroll)
            SaveYear = "%04X" % int(self.SaveYear.text())
            SaveYear = bytes.fromhex(SaveYear)
            SaveYear = bytearray(SaveYear)
            SaveYear.reverse()
            SaveYear = bytes(SaveYear)
            SaveMonth = "%02X" % int(self.SaveMonth.text())
            SaveMonth = bytes.fromhex(SaveMonth)
            SaveMonth = bytearray(SaveMonth)
            SaveMonth.reverse()
            SaveMonth = bytes(SaveMonth)
            SaveDay = "%02X" % int(self.SaveDay.text())
            SaveDay = bytes.fromhex(SaveDay)
            SaveDay = bytearray(SaveDay)
            SaveDay.reverse()
            SaveDay = bytes(SaveDay)
            SaveHour = "%02X" % int(self.SaveHour.text())
            SaveHour = bytes.fromhex(SaveHour)
            SaveHour = bytearray(SaveHour)
            SaveHour.reverse()
            SaveHour = bytes(SaveHour)
            SaveMinute = "%02X" % int(self.SaveMinute.text())
            SaveMinute = bytes.fromhex(SaveMinute)
            SaveMinute = bytearray(SaveMinute)
            SaveMinute.reverse()
            SaveMinute = bytes(SaveMinute)
            EntityFlags = self.EntityFlags.text()
            ParentFlags, ChildFlags = EntityFlags[:len(EntityFlags)//2], EntityFlags[len(EntityFlags)//2:]
            ParentFlags, ChildFlags = EntityFlags[:len(EntityFlags)//2], EntityFlags[len(EntityFlags)//2:]
            ParentFlags = bytes.fromhex(ParentFlags)
            ParentFlags = bytearray(ParentFlags)
            ParentFlags.reverse()
            ParentFlags = bytes(ParentFlags)
            ChildFlags = bytes.fromhex(ChildFlags)
            ChildFlags = bytearray(ChildFlags)
            ChildFlags.reverse()
            ChildFlags = bytes(ChildFlags)
            EntityFlags = bytes.hex(ParentFlags)+bytes.hex(ChildFlags)
            EntityFlags = bytes.fromhex(EntityFlags)
            EntityID = self.EntityID.text()
            CourseName = self.CourseName.text()
            CourseDescription = self.CourseDescription.text()
            Buf[0x4+HeaderSize:0x6+HeaderSize] = TimeLimit
            Buf[0x6+HeaderSize:0x7+HeaderSize] = Autoscroll
            Buf[0x8+HeaderSize:0xA+HeaderSize] = SaveYear
            Buf[0xA+HeaderSize:0xB+HeaderSize] = SaveMonth
            Buf[0xB+HeaderSize:0xC+HeaderSize] = SaveDay
            Buf[0xC+HeaderSize:0xD+HeaderSize] = SaveHour
            Buf[0xD+HeaderSize:0xE+HeaderSize] = SaveMinute
            with open(CoursePath,'wb') as Course:
                Course.write(Encryption.EncryptData(Buf, Encryption.CourseKeyTable, 0x10))


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationDisplayName('')

    mainWindow = MainWindow()
    mainWindow.__init2__()
    mainWindow.show()
    app.exec_()
    sys.exit()


if __name__ == '__main__': main()
