#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# DougBowser
# Version 0.1
# Created by MarioPossamato

# This file is part of DougBowser.


import encryption
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


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

        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 751, 660))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setTitle("Raw Data Editor")

        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 271, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setTitle("Time Limit")

        self.TimeLimit = QtWidgets.QLineEdit(self.groupBox_3)
        self.TimeLimit.setGeometry(QtCore.QRect(10, 20, 251, 31))
        self.TimeLimit.setMaxLength(5)
        self.TimeLimit.setReadOnly(False)
        self.TimeLimit.setObjectName("TimeLimit")
        self.TimeLimit.setPlaceholderText("500")

        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 90, 271, 371))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.setTitle("Date")

        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 20, 251, 61))
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_5.setTitle("Last Saved Year")

        self.LastSavedYear = QtWidgets.QLineEdit(self.groupBox_5)
        self.LastSavedYear.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.LastSavedYear.setText("")
        self.LastSavedYear.setMaxLength(5)
        self.LastSavedYear.setReadOnly(False)
        self.LastSavedYear.setObjectName("LastSavedYear")
        self.LastSavedYear.raise_()
        self.LastSavedYear.setPlaceholderText("2020")

        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 90, 251, 61))
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_6.setTitle("Last Saved Month")

        self.LastSavedMonth = QtWidgets.QLineEdit(self.groupBox_6)
        self.LastSavedMonth.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.LastSavedMonth.setMaxLength(3)
        self.LastSavedMonth.setReadOnly(False)
        self.LastSavedMonth.setObjectName("LastSavedMonth")
        self.LastSavedMonth.raise_()
        self.LastSavedMonth.setPlaceholderText("1")

        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 230, 251, 61))
        self.groupBox_8.setObjectName("groupBox_8")
        self.groupBox_8.setTitle("Last Saved Hour")

        self.LastSavedHour = QtWidgets.QLineEdit(self.groupBox_8)
        self.LastSavedHour.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.LastSavedHour.setMaxLength(3)
        self.LastSavedHour.setReadOnly(False)
        self.LastSavedHour.setObjectName("LastSavedHour")
        self.LastSavedHour.raise_()
        self.LastSavedHour.setPlaceholderText("1")

        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 160, 251, 61))
        self.groupBox_7.setObjectName("groupBox_7")
        self.groupBox_7.setTitle("Last Saved Day")

        self.LastSavedDay = QtWidgets.QLineEdit(self.groupBox_7)
        self.LastSavedDay.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.LastSavedDay.setMaxLength(3)
        self.LastSavedDay.setReadOnly(False)
        self.LastSavedDay.setObjectName("LastSavedDay")
        self.LastSavedDay.raise_()
        self.LastSavedDay.setPlaceholderText("1")

        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 300, 251, 61))
        self.groupBox_9.setObjectName("groupBox_9")
        self.groupBox_9.setTitle("Last Saved Minute")

        self.LastSavedMinute = QtWidgets.QLineEdit(self.groupBox_9)
        self.LastSavedMinute.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.LastSavedMinute.setMaxLength(3)
        self.LastSavedMinute.setReadOnly(False)
        self.LastSavedMinute.setObjectName("LastSavedMinute")
        self.LastSavedMinute.raise_()
        self.LastSavedMinute.setPlaceholderText("1")

        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_10.setGeometry(QtCore.QRect(290, 20, 451, 61))
        self.groupBox_10.setObjectName("groupBox_10")
        self.groupBox_10.setTitle("Autoscroll")

        self.Autoscroll = QtWidgets.QLineEdit(self.groupBox_10)
        self.Autoscroll.setGeometry(QtCore.QRect(10, 20, 431, 31))
        self.Autoscroll.setReadOnly(False)
        self.Autoscroll.setObjectName("Autoscroll")
        self.Autoscroll.setMaxLength(3)
        self.Autoscroll.raise_()
        self.Autoscroll.setPlaceholderText("0")

        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_11.setGeometry(QtCore.QRect(290, 90, 451, 482))
        self.groupBox_11.setObjectName("groupBox_11")
        self.groupBox_11.setTitle("Entities")

        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 20, 431, 61))
        self.groupBox_12.setObjectName("groupBox_12")
        self.groupBox_12.setTitle("Object Count")

        self.ObjectCount = QtWidgets.QLineEdit(self.groupBox_12)
        self.ObjectCount.setGeometry(QtCore.QRect(10, 20, 411, 31))
        self.ObjectCount.setReadOnly(True)
        self.ObjectCount.setObjectName("ObjectCount")
        self.ObjectCount.raise_()
        self.ObjectCount.setPlaceholderText("1")

        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 90, 431, 382))
        self.groupBox_13.setObjectName("groupBox_13")
        self.groupBox_13.setTitle("All Entities In Course")

        self.EntitiesList = QtWidgets.QListWidget(self.groupBox_13)
        self.EntitiesList.setGeometry(QtCore.QRect(10, 20, 411, 350))
        self.EntitiesList.setObjectName("EntitiesList")

        self.groupBox_14 = QtWidgets.QGroupBox(self)
        self.groupBox_14.setGeometry(QtCore.QRect(20, 589, 272, 103))
        self.groupBox_14.setObjectName("groupBox_14")
        self.groupBox_14.setTitle("Entity Data Viewer")

        self.EntityNumberBox = QtWidgets.QComboBox(self.groupBox_14)
        self.EntityNumberBox.setGeometry(QtCore.QRect(10, 20, 252, 30))
        self.EntityNumberBox.setObjectName("EntityNumberBox")
        self.EntityNumberBox.currentIndexChanged.connect(self.EntityNumberBoxIndexChanged, self.EntityNumberBox.currentIndex())

        self.EntityFlags = QtWidgets.QLineEdit(self.groupBox_14)
        self.EntityFlags.setGeometry(QtCore.QRect(10, 60, 135, 30))
        self.EntityFlags.setMaxLength(16)
        self.EntityFlags.setPlaceholderText("0600004006000040")

        self.EntityID = QtWidgets.QLineEdit(self.groupBox_14)
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

    def HandleOpenFromFile(self):
        global CoursePath, buffer
        CoursePath = QtWidgets.QFileDialog.getOpenFileName(self, "Open Course", '', 'Binary Course Data File (*.bcd)')[0]
        if not CoursePath:
            return
        self.coursePath.setText(CoursePath)
        with open(CoursePath,'rb') as Course:
            buffer = Course.read()
            if buffer[4:6] == bytes([0x10,0x00]):
                pass
            else:
                QtWidgets.QMessageBox.warning(None, 'Error', 'Not a valid Super Mario Maker 2 course file!')
                return
            buffer = encryption.DecryptCourse(buffer)
            CourseName = buffer[0xF4+HeaderSize:0xF4+HeaderSize+0x42].decode('utf-16')
            self.CourseName.setText(CourseName)
            CourseDescription = buffer[0x136+HeaderSize:0x136+HeaderSize+0xCA].decode('utf-16')
            self.CourseDescription.setText(CourseDescription)
            TimeLimit = buffer[0x4+HeaderSize:0x4+HeaderSize+0x4]
            TimeLimit = bytearray(TimeLimit)
            TimeLimit.reverse()
            TimeLimit = bytes(TimeLimit)
            TimeLimit = bytes.hex(TimeLimit)
            TimeLimit = int(TimeLimit, 16)
            self.TimeLimit.setText(str(TimeLimit))
            SaveYear = buffer[0x8+HeaderSize:0x8+HeaderSize+0x2]
            SaveYear = bytearray(SaveYear)
            SaveYear.reverse()
            SaveYear = bytes(SaveYear)
            SaveYear = bytes.hex(SaveYear)
            SaveYear = int(SaveYear, 16)
            self.LastSavedYear.setText(str(SaveYear))
            SaveMonth = buffer[0xA+HeaderSize:0xA+HeaderSize+0x1]
            SaveMonth = bytes.hex(SaveMonth)
            SaveMonth = int(SaveMonth, 16)
            self.LastSavedMonth.setText(str(SaveMonth))
            SaveDay = buffer[0xB+HeaderSize:0xB+HeaderSize+0x1]
            SaveDay = bytes.hex(SaveDay)
            SaveDay = int(SaveDay, 16)
            self.LastSavedDay.setText(str(SaveDay))
            SaveHour = buffer[0xC+HeaderSize:0xC+HeaderSize+0x1]
            SaveHour = bytes.hex(SaveHour)
            SaveHour = int(SaveHour, 16)
            self.LastSavedHour.setText(str(SaveHour))
            SaveMinute = buffer[0xD+HeaderSize:0xD+HeaderSize+0x1]
            SaveMinute = bytes.hex(SaveMinute)
            SaveMinute = int(SaveMinute, 16)
            self.LastSavedMinute.setText(str(SaveMinute))
            Autoscroll = buffer[0x6+HeaderSize:0x6+HeaderSize+0x1]
            Autoscroll = bytes.hex(Autoscroll)
            Autoscroll = int(Autoscroll, 16)
            self.Autoscroll.setText(str(Autoscroll))
            ObjectCount = buffer[0x21C+HeaderSize:0x21C+HeaderSize+0x4]
            ObjectCount = bytearray(ObjectCount)
            ObjectCount.reverse()
            ObjectCount = bytes(ObjectCount)
            ObjectCount = bytes.hex(ObjectCount)
            ObjectCount = int(ObjectCount, 16)
            self.ObjectCount.setText(str(ObjectCount))
            for i in range(2600):
                EntityID = buffer[0x260+HeaderSize+0x20*i:0x260+HeaderSize+0x3+0x20*i]
                EntityName = f'Unknown({EntityID})'
                if EntityID == bytes([0x00, 0x00, 0xFF]) or EntityID == bytes([0x00, 0x12, 0xFF]):
                    EntityName = 'Goomba/Galoomba'
                if EntityID == bytes([0x01, 0x00, 0xFF]) or EntityID == bytes([0x01, 0x12, 0xFF]):
                    EntityName = 'Koopa Troopa'
                if EntityID == bytes([0x02, 0x00, 0xFF]) or EntityID == bytes([0x02, 0x12, 0xFF]):
                    EntityName = 'Piranha Plant/Jumping Piranha Plant'
                if EntityID == bytes([0x03, 0x00, 0xFF]) or EntityID == bytes([0x03, 0x12, 0xFF]):
                    EntityName = 'Hammer Bro'
                if EntityID == bytes([0x04, 0x00, 0xFF]) or EntityID == bytes([0x04, 0x12, 0xFF]):
                    EntityName = 'Block'
                if EntityID == bytes([0x05, 0x00, 0xFF]) or EntityID == bytes([0x05, 0x12, 0xFF]):
                    EntityName = '? Block'
                if EntityID == bytes([0x06, 0x00, 0xFF]) or EntityID == bytes([0x06, 0x12, 0xFF]):
                    EntityName = 'Hard Block'
                if EntityID == bytes([0x07, 0x00, 0xFF]) or EntityID == bytes([0x07, 0x12, 0xFF]):
                    EntityName = 'Ground'
                if EntityID == bytes([0x08, 0x00, 0xFF]) or EntityID == bytes([0x08, 0x12, 0xFF]):
                    EntityName = 'Coin/Frozen Coin'
                if EntityID == bytes([0x09, 0x00, 0xFF]) or EntityID == bytes([0x09, 0x12, 0xFF]):
                    EntityName = 'Pipe'
                if EntityID == bytes([0x0A, 0x00, 0xFF]) or EntityID == bytes([0x0A, 0x12, 0xFF]):
                    EntityName = 'Trampoline'
                if EntityID == bytes([0x0B, 0x00, 0xFF]) or EntityID == bytes([0x0B, 0x12, 0xFF]):
                    EntityName = 'Lift/Cloud Lift'
                if EntityID == bytes([0x0C, 0x00, 0xFF]) or EntityID == bytes([0x0C, 0x12, 0xFF]):
                    EntityName = 'Thwomp'
                if EntityID == bytes([0x0D, 0x00, 0xFF]) or EntityID == bytes([0x0D, 0x12, 0xFF]):
                    EntityName = 'Bill Blaster'
                if EntityID == bytes([0x0E, 0x00, 0xFF]) or EntityID == bytes([0x0E, 0x12, 0xFF]):
                    EntityName = 'Mushroom Platform'
                if EntityID == bytes([0x0F, 0x00, 0xFF]) or EntityID == bytes([0x0F, 0x12, 0xFF]):
                    EntityName = 'Bob-omb'
                if EntityID == bytes([0x10, 0x00, 0xFF]) or EntityID == bytes([0x70, 0x12, 0xFF]):
                    EntityName = 'Semisolid Platform'
                if EntityID == bytes([0x11, 0x00, 0xFF]) or EntityID == bytes([0x11, 0x12, 0xFF]):
                    EntityName = 'Bridge'
                if EntityID == bytes([0x12, 0x00, 0xFF]) or EntityID == bytes([0x12, 0x12, 0xFF]):
                    EntityName = 'P-Switch'
                if EntityID == bytes([0x13, 0x00, 0xFF]) or EntityID == bytes([0x13, 0x12, 0xFF]):
                    EntityName = 'Pow Block'
                if EntityID == bytes([0x14, 0x00, 0xFF]) or EntityID == bytes([0x14, 0x12, 0xFF]):
                    EntityName = 'Super Mushroom/Master Sword'
                if EntityID == bytes([0x15, 0x00, 0xFF]) or EntityID == bytes([0x15, 0x12, 0xFF]):
                    EntityName = 'Donut Block'
                if EntityID == bytes([0x16, 0x00, 0xFF]) or EntityID == bytes([0x16, 0x12, 0xFF]):
                    EntityName = 'Cloud Block'
                if EntityID == bytes([0x17, 0x00, 0xFF]) or EntityID == bytes([0x17, 0x12, 0xFF]):
                    EntityName = 'Note Block'
                if EntityID == bytes([0x18, 0x00, 0xFF]) or EntityID == bytes([0x18, 0x12, 0xFF]):
                    EntityName = 'Firebar'
                if EntityID == bytes([0x19, 0x00, 0xFF]) or EntityID == bytes([0x19, 0x12, 0xFF]):
                    EntityName = 'Spiny'
                if EntityID == bytes([0x1A, 0x00, 0xFF]) or EntityID == bytes([0x1A, 0x12, 0xFF]):
                    EntityName = 'Goal Ground'
                if EntityID == bytes([0x1B, 0x00, 0xFF]) or EntityID == bytes([0x1B, 0x12, 0xFF]):
                    EntityName = 'Goal Pole'
                if EntityID == bytes([0x1C, 0x00, 0xFF]) or EntityID == bytes([0x1C, 0x12, 0xFF]):
                    EntityName = 'Buzzy Beatle'
                if EntityID == bytes([0x1D, 0x00, 0xFF]) or EntityID == bytes([0x1D, 0x12, 0xFF]):
                    EntityName = 'Hidden Block'
                if EntityID == bytes([0x1E, 0x00, 0xFF]) or EntityID == bytes([0x1E, 0x12, 0xFF]):
                    EntityName = 'Lakitu'
                if EntityID == bytes([0x1F, 0x00, 0xFF]) or EntityID == bytes([0x1F, 0x12, 0xFF]):
                    EntityName = 'Cloud'
                if EntityID == bytes([0x20, 0x00, 0xFF]) or EntityID == bytes([0x70, 0x12, 0xFF]):
                    EntityName = 'Banzai Bill'
                if EntityID == bytes([0x21, 0x00, 0xFF]) or EntityID == bytes([0x21, 0x12, 0xFF]):
                    EntityName = '1-Up Mushroom'
                if EntityID == bytes([0x22, 0x00, 0xFF]) or EntityID == bytes([0x22, 0x12, 0xFF]):
                    EntityName = 'Fire Flower'
                if EntityID == bytes([0x23, 0x00, 0xFF]) or EntityID == bytes([0x23, 0x12, 0xFF]):
                    EntityName = 'Super Star'
                if EntityID == bytes([0x24, 0x00, 0xFF]) or EntityID == bytes([0x24, 0x12, 0xFF]):
                    EntityName = 'Lava Lift'
                if EntityID == bytes([0x25, 0x00, 0xFF]) or EntityID == bytes([0x25, 0x12, 0xFF]):
                    EntityName = 'Ground Start'
                if EntityID == bytes([0x26, 0x00, 0xFF]) or EntityID == bytes([0x26, 0x12, 0xFF]):
                    EntityName = 'Start Arrow'
                if EntityID == bytes([0x27, 0x00, 0xFF]) or EntityID == bytes([0x27, 0x12, 0xFF]):
                    EntityName = 'Kameck'
                if EntityID == bytes([0x28, 0x00, 0xFF]) or EntityID == bytes([0x28, 0x12, 0xFF]):
                    EntityName = 'Spike Top'
                if EntityID == bytes([0x29, 0x00, 0xFF]) or EntityID == bytes([0x29, 0x12, 0xFF]):
                    EntityName = 'Boo'
                if EntityID == bytes([0x2A, 0x00, 0xFF]) or EntityID == bytes([0x2A, 0x12, 0xFF]):
                    EntityName = 'Koopa Clown Car'
                if EntityID == bytes([0x2B, 0x00, 0xFF]) or EntityID == bytes([0x2B, 0x12, 0xFF]):
                    EntityName = 'Spike Trap'
                if EntityID == bytes([0x2C, 0x00, 0xFF]) or EntityID == bytes([0x2C, 0x12, 0xFF]):
                    EntityName = '3rd Tier Powerup'
                if EntityID == bytes([0x2D, 0x00, 0xFF]) or EntityID == bytes([0x2D, 0x12, 0xFF]):
                    EntityName = 'Shoe Goomba/Yoshi'
                if EntityID == bytes([0x2E, 0x00, 0xFF]) or EntityID == bytes([0x2E, 0x12, 0xFF]):
                    EntityName = 'Dry Bones'
                if EntityID == bytes([0x2F, 0x00, 0xFF]) or EntityID == bytes([0x2F, 0x12, 0xFF]):
                    EntityName = 'Cannon'
                if EntityID == bytes([0x30, 0x00, 0xFF]) or EntityID == bytes([0x70, 0x12, 0xFF]):
                    EntityName = 'Blooper'
                if EntityID == bytes([0x31, 0x00, 0xFF]) or EntityID == bytes([0x31, 0x12, 0xFF]):
                    EntityName = 'Castle Bridge'
                if EntityID == bytes([0x32, 0x00, 0xFF]) or EntityID == bytes([0x32, 0x12, 0xFF]):
                    EntityName = 'Hop-Chops'
                if EntityID == bytes([0x33, 0x00, 0xFF]) or EntityID == bytes([0x33, 0x12, 0xFF]):
                    EntityName = 'Skipsqueak'
                if EntityID == bytes([0x34, 0x00, 0xFF]) or EntityID == bytes([0x34, 0x12, 0xFF]):
                    EntityName = 'Wiggler'
                if EntityID == bytes([0x35, 0x00, 0xFF]) or EntityID == bytes([0x35, 0x12, 0xFF]):
                    EntityName = 'Conveyer Belt'
                if EntityID == bytes([0x36, 0x00, 0xFF]) or EntityID == bytes([0x36, 0x12, 0xFF]):
                    EntityName = 'Burner'
                if EntityID == bytes([0x37, 0x00, 0xFF]) or EntityID == bytes([0x37, 0x12, 0xFF]):
                    EntityName = 'Warp Door'
                if EntityID == bytes([0x38, 0x00, 0xFF]) or EntityID == bytes([0x38, 0x12, 0xFF]):
                    EntityName = 'Cheep Cheep'
                if EntityID == bytes([0x39, 0x00, 0xFF]) or EntityID == bytes([0x39, 0x12, 0xFF]):
                    EntityName = 'Muncher'
                if EntityID == bytes([0x3A, 0x00, 0xFF]) or EntityID == bytes([0x3A, 0x12, 0xFF]):
                    EntityName = 'Rocky Wrench'
                if EntityID == bytes([0x3B, 0x00, 0xFF]) or EntityID == bytes([0x3B, 0x12, 0xFF]):
                    EntityName = 'Rail'
                if EntityID == bytes([0x3C, 0x00, 0xFF]) or EntityID == bytes([0x3C, 0x12, 0xFF]):
                    EntityName = 'Lava Bubble'
                if EntityID == bytes([0x3D, 0x00, 0xFF]) or EntityID == bytes([0x3D, 0x12, 0xFF]):
                    EntityName = 'Chain Chomp'
                if EntityID == bytes([0x3E, 0x00, 0xFF]) or EntityID == bytes([0x3E, 0x12, 0xFF]):
                    EntityName = 'Bowser/Meowser'
                if EntityID == bytes([0x3F, 0x00, 0xFF]) or EntityID == bytes([0x3F, 0x12, 0xFF]):
                    EntityName = 'Ice Block'
                if EntityID == bytes([0x40, 0x00, 0xFF]) or EntityID == bytes([0x70, 0x12, 0xFF]):
                    EntityName = 'Vine'
                if EntityID == bytes([0x41, 0x00, 0xFF]) or EntityID == bytes([0x41, 0x12, 0xFF]):
                    EntityName = 'Stingby'
                if EntityID == bytes([0x42, 0x00, 0xFF]) or EntityID == bytes([0x42, 0x12, 0xFF]):
                    EntityName = 'Arrow Sign'
                if EntityID == bytes([0x43, 0x00, 0xFF]) or EntityID == bytes([0x43, 0x12, 0xFF]):
                    EntityName = 'One-Way Wall'
                if EntityID == bytes([0x44, 0x00, 0xFF]) or EntityID == bytes([0x44, 0x12, 0xFF]):
                    EntityName = 'Grinder'
                if EntityID == bytes([0x45, 0x00, 0xFF]) or EntityID == bytes([0x45, 0x12, 0xFF]):
                    EntityName = 'Player'
                if EntityID == bytes([0x46, 0x00, 0xFF]) or EntityID == bytes([0x46, 0x12, 0xFF]):
                    EntityName = '10-Coin'
                if EntityID == bytes([0x47, 0x00, 0xFF]) or EntityID == bytes([0x47, 0x12, 0xFF]):
                    EntityName = 'Semisolid Platform (3D World)'
                if EntityID == bytes([0x48, 0x00, 0xFF]) or EntityID == bytes([0x48, 0x12, 0xFF]):
                    EntityName = 'Koopa Troopa Car'
                if EntityID == bytes([0x49, 0x00, 0xFF]) or EntityID == bytes([0x49, 0x12, 0xFF]):
                    EntityName = 'Toad'
                if EntityID == bytes([0x4A, 0x00, 0xFF]) or EntityID == bytes([0x4A, 0x12, 0xFF]):
                    EntityName = 'Spike/Spike Ball'
                if EntityID == bytes([0x4B, 0x00, 0xFF]) or EntityID == bytes([0x4B, 0x12, 0xFF]):
                    EntityName = 'Stone'
                if EntityID == bytes([0x4C, 0x00, 0xFF]) or EntityID == bytes([0x4C, 0x12, 0xFF]):
                    EntityName = 'Twister'
                if EntityID == bytes([0x4D, 0x00, 0xFF]) or EntityID == bytes([0x4D, 0x12, 0xFF]):
                    EntityName = 'Boom Boom'
                if EntityID == bytes([0x4E, 0x00, 0xFF]) or EntityID == bytes([0x4E, 0x12, 0xFF]):
                    EntityName = 'Pokey'
                if EntityID == bytes([0x4F, 0x00, 0xFF]) or EntityID == bytes([0x4F, 0x12, 0xFF]):
                    EntityName = 'P-Block'
                if EntityID == bytes([0x50, 0x00, 0xFF]) or EntityID == bytes([0x70, 0x12, 0xFF]):
                    EntityName = 'Dash Block'
                if EntityID == bytes([0x51, 0x00, 0xFF]) or EntityID == bytes([0x51, 0x12, 0xFF]):
                    EntityName = 'None'
                if EntityID == bytes([0x52, 0x00, 0xFF]) or EntityID == bytes([0x52, 0x12, 0xFF]):
                    EntityName = 'Bumper'
                if EntityID == bytes([0x53, 0x00, 0xFF]) or EntityID == bytes([0x53, 0x12, 0xFF]):
                    EntityName = 'Spike Pillar'
                if EntityID == bytes([0x54, 0x00, 0xFF]) or EntityID == bytes([0x54, 0x12, 0xFF]):
                    EntityName = 'Snake Block'
                if EntityID == bytes([0x55, 0x00, 0xFF]) or EntityID == bytes([0x55, 0x12, 0xFF]):
                    EntityName = 'Track Block'
                if EntityID == bytes([0x56, 0x00, 0xFF]) or EntityID == bytes([0x56, 0x12, 0xFF]):
                    EntityName = 'Charvaargh'
                if EntityID == bytes([0x57, 0x00, 0xFF]) or EntityID == bytes([0x57, 0x12, 0xFF]):
                    EntityName = 'Gentle Slope'
                if EntityID == bytes([0x58, 0x00, 0xFF]) or EntityID == bytes([0x58, 0x12, 0xFF]):
                    EntityName = 'Steep Slope'
                if EntityID == bytes([0x59, 0x00, 0xFF]) or EntityID == bytes([0x59, 0x12, 0xFF]):
                    EntityName = 'Custom Scroll Waypoint'
                if EntityID == bytes([0x5A, 0x00, 0xFF]) or EntityID == bytes([0x5A, 0x12, 0xFF]):
                    EntityName = 'Checkpoint Flag'
                if EntityID == bytes([0x5B, 0x00, 0xFF]) or EntityID == bytes([0x5B, 0x12, 0xFF]):
                    EntityName = 'Seesaw'
                if EntityID == bytes([0x5C, 0x00, 0xFF]) or EntityID == bytes([0x5C, 0x12, 0xFF]):
                    EntityName = 'Pink Coin'
                if EntityID == bytes([0x5D, 0x00, 0xFF]) or EntityID == bytes([0x5D, 0x12, 0xFF]):
                    EntityName = 'Clear Pipe'
                if EntityID == bytes([0x5E, 0x00, 0xFF]) or EntityID == bytes([0x5E, 0x12, 0xFF]):
                    EntityName = 'Sloped Conveyer Belt'
                if EntityID == bytes([0x5F, 0x00, 0xFF]) or EntityID == bytes([0x5F, 0x12, 0xFF]):
                    EntityName = 'Key'
                if EntityID == bytes([0x60, 0x00, 0xFF]) or EntityID == bytes([0x60, 0x12, 0xFF]):
                    EntityName = 'Ant Trooper'
                if EntityID == bytes([0x61, 0x00, 0xFF]) or EntityID == bytes([0x61, 0x12, 0xFF]):
                    EntityName = 'Warp Box'
                if EntityID == bytes([0x62, 0x00, 0xFF]) or EntityID == bytes([0x62, 0x12, 0xFF]):
                    EntityName = 'Bowser Jr.'
                if EntityID == bytes([0x63, 0x00, 0xFF]) or EntityID == bytes([0x63, 0x12, 0xFF]):
                    EntityName = 'On/Off Switch'
                if EntityID == bytes([0x64, 0x00, 0xFF]) or EntityID == bytes([0x64, 0x12, 0xFF]):
                    EntityName = 'Dotted-Line Block'
                if EntityID == bytes([0x65, 0x00, 0xFF]) or EntityID == bytes([0x65, 0x12, 0xFF]):
                    EntityName = 'Lava Editor'
                if EntityID == bytes([0x66, 0x00, 0xFF]) or EntityID == bytes([0x66, 0x12, 0xFF]):
                    EntityName = 'Monty Mole'
                if EntityID == bytes([0x67, 0x00, 0xFF]) or EntityID == bytes([0x67, 0x12, 0xFF]):
                    EntityName = 'Fish Bones'
                if EntityID == bytes([0x68, 0x00, 0xFF]) or EntityID == bytes([0x68, 0x12, 0xFF]):
                    EntityName = 'Angry Sun'
                if EntityID == bytes([0x69, 0x00, 0xFF]) or EntityID == bytes([0x69, 0x12, 0xFF]):
                    EntityName = 'Swinging Claw'
                if EntityID == bytes([0x6A, 0x00, 0xFF]) or EntityID == bytes([0x6A, 0x12, 0xFF]):
                    EntityName = 'Tree'
                if EntityID == bytes([0x6B, 0x00, 0xFF]) or EntityID == bytes([0x6B, 0x12, 0xFF]):
                    EntityName = 'Piranha Creeper'
                if EntityID == bytes([0x6C, 0x00, 0xFF]) or EntityID == bytes([0x6C, 0x12, 0xFF]):
                    EntityName = 'Blinking Block'
                if EntityID == bytes([0x6D, 0x00, 0xFF]) or EntityID == bytes([0x6D, 0x12, 0xFF]):
                    EntityName = 'Sound Effect Icon'
                if EntityID == bytes([0x6E, 0x00, 0xFF]) or EntityID == bytes([0x6E, 0x12, 0xFF]):
                    EntityName = 'Spike Block'
                if EntityID == bytes([0x6F, 0x00, 0xFF]) or EntityID == bytes([0x6F, 0x12, 0xFF]):
                    EntityName = 'None'
                if EntityID == bytes([0x70, 0x00, 0xFF]) or EntityID == bytes([0x70, 0x12, 0xFF]):
                    EntityName = 'Crate'
                if EntityID == bytes([0x71, 0x00, 0xFF]) or EntityID == bytes([0x71, 0x12, 0xFF]):
                    EntityName = 'Mushroom Trampoline'
                if EntityID == bytes([0x72, 0x00, 0xFF]) or EntityID == bytes([0x72, 0x12, 0xFF]):
                    EntityName = 'Porcupuffer'
                if EntityID == bytes([0x73, 0x00, 0xFF]) or EntityID == bytes([0x73, 0x12, 0xFF]):
                    EntityName = 'Goal Toadette'
                if EntityID == bytes([0x74, 0x00, 0xFF]) or EntityID == bytes([0x74, 0x12, 0xFF]):
                    EntityName = 'Super Hammer'
                if EntityID == bytes([0x75, 0x00, 0xFF]) or EntityID == bytes([0x75, 0x12, 0xFF]):
                    EntityName = 'Bully'
                if EntityID == bytes([0x76, 0x00, 0xFF]) or EntityID == bytes([0x76, 0x12, 0xFF]):
                    EntityName = 'Icicle'
                if EntityID == bytes([0x77, 0x00, 0xFF]) or EntityID == bytes([0x77, 0x12, 0xFF]):
                    EntityName = '! Block'
                self.EntitiesList.addItem(str(i) + ': ' + str(EntityName) + ' @' + str(hex(608 + 32 * i)))
                if not EntityID == bytes([0x00, 0x00, 0x00]):
                    self.EntityNumberBox.addItem(str(i + 1))
            

    def HandleSave(self):
        global CoursePath, buffer
        if not CoursePath:
            print('No course has been opened!  Please open one before you try to save it! ;)')
            return
        else:
            buffer = bytearray(buffer)
            TimeLimit = "%04X" % int(self.TimeLimit.text())
            TimeLimit = bytes.fromhex(TimeLimit)
            TimeLimit = bytearray(TimeLimit)
            TimeLimit.reverse()
            TimeLimit = bytes(TimeLimit)
            Autoscroll = "%02X" % int(self.Autoscroll.text())
            Autoscroll = bytes.fromhex(Autoscroll)
            SaveYear = "%04X" % int(self.LastSavedYear.text())
            SaveYear = bytes.fromhex(SaveYear)
            SaveYear = bytearray(SaveYear)
            SaveYear.reverse()
            SaveYear = bytes(SaveYear)
            SaveMonth = "%02X" % int(self.LastSavedMonth.text())
            SaveMonth = bytes.fromhex(SaveMonth)
            SaveMonth = bytearray(SaveMonth)
            SaveMonth.reverse()
            SaveMonth = bytes(SaveMonth)
            SaveDay = "%02X" % int(self.LastSavedDay.text())
            SaveDay = bytes.fromhex(SaveDay)
            SaveDay = bytearray(SaveDay)
            SaveDay.reverse()
            SaveDay = bytes(SaveDay)
            SaveHour = "%02X" % int(self.LastSavedHour.text())
            SaveHour = bytes.fromhex(SaveHour)
            SaveHour = bytearray(SaveHour)
            SaveHour.reverse()
            SaveHour = bytes(SaveHour)
            SaveMinute = "%02X" % int(self.LastSavedMinute.text())
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
            buffer[0x4+HeaderSize:0x6+HeaderSize] = TimeLimit
            buffer[0x6+HeaderSize:0x7+HeaderSize] = Autoscroll
            buffer[0x8+HeaderSize:0xA+HeaderSize] = SaveYear
            buffer[0xA+HeaderSize:0xB+HeaderSize] = SaveMonth
            buffer[0xB+HeaderSize:0xC+HeaderSize] = SaveDay
            buffer[0xC+HeaderSize:0xD+HeaderSize] = SaveHour
            buffer[0xD+HeaderSize:0xE+HeaderSize] = SaveMinute
            with open(CoursePath,'rb') as Course:
                buffer = Course.read()
                decrypted = buffer[0x10:]
                encrypted = encryption.EncryptCourse(decrypted)
                with open(CoursePath,'wb') as Course:
                    Course.write(encrypted)

    def EntityNumberBoxIndexChanged(self):
        global buffer
        ParentFlags = buffer[0x254+HeaderSize+0x20*(int(self.EntityNumberBox.currentText())-1):0x254+HeaderSize+0x20*(int(self.EntityNumberBox.currentText())-1)+4]
        ParentFlags = bytearray(ParentFlags)
        ParentFlags.reverse()
        ParentFlags = bytes(ParentFlags)
        ParentFlags = bytes.hex(ParentFlags)
        ChildFlags = buffer[0x258+HeaderSize+0x20*(int(self.EntityNumberBox.currentText())-1):0x258+HeaderSize+0x20*(int(self.EntityNumberBox.currentText())-1)+4]
        ChildFlags = bytearray(ChildFlags)
        ChildFlags.reverse()
        ChildFlags = bytes(ChildFlags)
        ChildFlags = bytes.hex(ChildFlags)
        EntityFlags = ParentFlags + ChildFlags
        self.EntityFlags.setText(EntityFlags)
        EntityID = buffer[0x260+HeaderSize+0x20*(int(self.EntityNumberBox.currentText())-1):0x260+HeaderSize+0x20*(int(self.EntityNumberBox.currentText())-1)+1]
        self.EntityID.setText(str(int.from_bytes(EntityID, 'big')))


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationDisplayName('')

    mainWindow = MainWindow()
    mainWindow.__init2__()
    mainWindow.show()
    app.exec_()
    sys.exit()


if __name__ == '__main__': main()
