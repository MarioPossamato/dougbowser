from PyQt5 import QtCore, QtGui, QtWidgets

CoursePath = ''

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(771, 713)
        Form.setMinimumSize(QtCore.QSize(771, 713))
        Form.setMaximumSize(QtCore.QSize(771, 713))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        Form.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 751, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.openCourseButton = QtWidgets.QPushButton(self.groupBox)
        self.openCourseButton.setGeometry(QtCore.QRect(9, 10, 364, 41))
        self.openCourseButton.setObjectName("openCourseButton")
        self.openCourseButton.clicked.connect(self.HandleOpenFromFile)
        self.saveCourseButton = QtWidgets.QPushButton(self.groupBox)
        self.saveCourseButton.setGeometry(QtCore.QRect(377, 10, 364, 41))
        self.saveCourseButton.setObjectName("saveCourseButton")
        self.saveCourseButton.clicked.connect(self.HandleSaveAs)
        self.coursePath = QtWidgets.QLineEdit(self.groupBox)
        self.coursePath.setGeometry(QtCore.QRect(10, 60, 731, 31))
        self.coursePath.setReadOnly(True)
        self.coursePath.setObjectName("coursePath")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 751, 583))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 271, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.TimeLimit = QtWidgets.QLineEdit(self.groupBox_3)
        self.TimeLimit.setGeometry(QtCore.QRect(10, 20, 251, 31))
        self.TimeLimit.setMaxLength(5)
        self.TimeLimit.setReadOnly(False)
        self.TimeLimit.setObjectName("TimeLimit")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 90, 271, 371))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 20, 251, 61))
        self.groupBox_5.setObjectName("groupBox_5")
        self.LastSavedYear = QtWidgets.QLineEdit(self.groupBox_5)
        self.LastSavedYear.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.LastSavedYear.setText("")
        self.LastSavedYear.setMaxLength(5)
        self.LastSavedYear.setReadOnly(False)
        self.LastSavedYear.setObjectName("LastSavedYear")
        self.LastSavedYear.raise_()
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 90, 251, 61))
        self.groupBox_6.setObjectName("groupBox_6")
        self.LastSavedMonth = QtWidgets.QLineEdit(self.groupBox_6)
        self.LastSavedMonth.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.LastSavedMonth.setMaxLength(3)
        self.LastSavedMonth.setReadOnly(False)
        self.LastSavedMonth.setObjectName("LastSavedMonth")
        self.LastSavedMonth.raise_()
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 230, 251, 61))
        self.groupBox_8.setObjectName("groupBox_8")
        self.LastSavedHour = QtWidgets.QLineEdit(self.groupBox_8)
        self.LastSavedHour.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.LastSavedHour.setMaxLength(3)
        self.LastSavedHour.setReadOnly(False)
        self.LastSavedHour.setObjectName("LastSavedHour")
        self.LastSavedHour.raise_()
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 160, 251, 61))
        self.groupBox_7.setObjectName("groupBox_7")
        self.LastSavedDay = QtWidgets.QLineEdit(self.groupBox_7)
        self.LastSavedDay.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.LastSavedDay.setMaxLength(3)
        self.LastSavedDay.setReadOnly(False)
        self.LastSavedDay.setObjectName("LastSavedDay")
        self.LastSavedDay.raise_()
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 300, 251, 61))
        self.groupBox_9.setObjectName("groupBox_9")
        self.LastSavedMinute = QtWidgets.QLineEdit(self.groupBox_9)
        self.LastSavedMinute.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.LastSavedMinute.setMaxLength(3)
        self.LastSavedMinute.setReadOnly(False)
        self.LastSavedMinute.setObjectName("LastSavedMinute")
        self.LastSavedMinute.raise_()
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_10.setGeometry(QtCore.QRect(290, 20, 451, 61))
        self.groupBox_10.setObjectName("groupBox_10")
        self.Autoscroll = QtWidgets.QLineEdit(self.groupBox_10)
        self.Autoscroll.setGeometry(QtCore.QRect(10, 20, 431, 31))
        self.Autoscroll.setReadOnly(False)
        self.Autoscroll.setObjectName("Autoscroll")
        self.Autoscroll.setMaxLength(3)
        self.Autoscroll.raise_()
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_11.setGeometry(QtCore.QRect(290, 90, 451, 482))
        self.groupBox_11.setObjectName("groupBox_11")
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 20, 431, 61))
        self.groupBox_12.setObjectName("groupBox_12")
        self.ObjectCount = QtWidgets.QLineEdit(self.groupBox_12)
        self.ObjectCount.setGeometry(QtCore.QRect(10, 20, 411, 31))
        self.ObjectCount.setReadOnly(True)
        self.ObjectCount.setObjectName("ObjectCount")
        self.ObjectCount.raise_()
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 90, 431, 382))
        self.groupBox_13.setObjectName("groupBox_13")
        self.EntitiesList = QtWidgets.QListWidget(self.groupBox_13)
        self.EntitiesList.setGeometry(QtCore.QRect(10, 20, 411, 350))
        self.EntitiesList.setObjectName("EntitiesList")
        self.EntitiesList.setFont(font)
        self.groupBox_14 = QtWidgets.QGroupBox(Form)
        self.groupBox_14.setGeometry(QtCore.QRect(20, 589, 272, 103))
        self.groupBox_14.setObjectName("groupBox_14")
        self.EntityNumberBox = QtWidgets.QComboBox(self.groupBox_14)
        self.EntityNumberBox.setGeometry(QtCore.QRect(10, 20, 252, 30))
        self.EntityNumberBox.setObjectName("EntityNumberBox")
        self.EntityNumberBox.currentIndexChanged.connect(self.EntityNumberBox_Index_Changed, self.EntityNumberBox.currentIndex())
        self.EntityFlags = QtWidgets.QLineEdit(self.groupBox_14)
        self.EntityFlags.setGeometry(QtCore.QRect(10, 60, 135, 30))
        self.EntityFlags.setMaxLength(16)
        self.EntityID = QtWidgets.QLineEdit(self.groupBox_14)
        self.EntityID.setGeometry(QtCore.QRect(153, 60, 109, 30))
        self.EntityID.setMaxLength(3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Doug Bowser; Super Mario Maker 2 Binary Course Data Editor"))
        self.openCourseButton.setText(_translate("Form", "Open Decrypted SMM2 Binary Course Data"))
        self.saveCourseButton.setText(_translate("Form", "Save Decrypted SMM2 Binary Course Data"))
        self.coursePath.setPlaceholderText(_translate("Form", "No Course Selected..."))
        self.groupBox_2.setTitle(_translate("Form", "Raw Data Editor"))
        self.groupBox_3.setTitle(_translate("Form", "Time Limit"))
        self.TimeLimit.setPlaceholderText(_translate("Form", "500"))
        self.groupBox_4.setTitle(_translate("Form", "Date"))
        self.groupBox_5.setTitle(_translate("Form", "Last Saved Year"))
        self.LastSavedYear.setPlaceholderText(_translate("Form", "2020"))
        self.groupBox_6.setTitle(_translate("Form", "Last Saved Month"))
        self.LastSavedMonth.setPlaceholderText(_translate("Form", "1"))
        self.groupBox_8.setTitle(_translate("Form", "Last Saved Hour"))
        self.LastSavedHour.setPlaceholderText(_translate("Form", "1"))
        self.groupBox_7.setTitle(_translate("Form", "Last Saved Day"))
        self.LastSavedDay.setPlaceholderText(_translate("Form", "1"))
        self.groupBox_9.setTitle(_translate("Form", "Last Saved Minute"))
        self.LastSavedMinute.setPlaceholderText(_translate("Form", "1"))
        self.groupBox_10.setTitle(_translate("Form", "Autoscroll"))
        self.Autoscroll.setPlaceholderText(_translate("Form", "0"))
        self.groupBox_11.setTitle(_translate("Form", "Entities"))
        self.groupBox_12.setTitle(_translate("Form", "Object Count"))
        self.ObjectCount.setPlaceholderText(_translate("Form", "1"))
        self.groupBox_13.setTitle(_translate("Form", "All Entities In Course"))
        self.groupBox_14.setTitle(_translate("Form", "Entity Data Editor"))
        self.EntityFlags.setPlaceholderText(_translate("Form", "0600004006000040"))
        self.EntityID.setPlaceholderText(_translate("Form", "0"))

    def HandleOpenFromFile(self):
        global CoursePath
        CoursePath = QtWidgets.QFileDialog.getOpenFileName(Form, "Open Course", '', 'Binary Course Data File (*.bcd)')[0]
        if not CoursePath:
            return
        self.coursePath.setText(CoursePath)
        with open(CoursePath,'rb') as Course:
            Course.seek(0x4)
            TimeLimit = Course.read(2)
            TimeLimit = bytearray(TimeLimit)
            TimeLimit.reverse()
            TimeLimit = bytes(TimeLimit)
            TimeLimit = bytes.hex(TimeLimit)
            TimeLimit = int(TimeLimit, 16)
            self.TimeLimit.setText(str(TimeLimit))
            Course.seek(0x8)
            SaveYear = Course.read(2)
            SaveYear = bytearray(SaveYear)
            SaveYear.reverse()
            SaveYear = bytes(SaveYear)
            SaveYear = bytes.hex(SaveYear)
            SaveYear = int(SaveYear, 16)
            self.LastSavedYear.setText(str(SaveYear))
            Course.seek(0xA)
            SaveMonth = Course.read(1)
            SaveMonth = bytes.hex(SaveMonth)
            SaveMonth = int(SaveMonth, 16)
            self.LastSavedMonth.setText(str(SaveMonth))
            Course.seek(0xB)
            SaveDay = Course.read(1)
            SaveDay = bytes.hex(SaveDay)
            SaveDay = int(SaveDay, 16)
            self.LastSavedDay.setText(str(SaveDay))
            Course.seek(0xC)
            SaveHour = Course.read(1)
            SaveHour = bytes.hex(SaveHour)
            SaveHour = int(SaveHour, 16)
            self.LastSavedHour.setText(str(SaveHour))
            Course.seek(0xD)
            SaveMinute = Course.read(1)
            SaveMinute = bytes.hex(SaveMinute)
            SaveMinute = int(SaveMinute, 16)
            self.LastSavedMinute.setText(str(SaveMinute))
            Course.seek(0x6)
            Autoscroll = Course.read(1)
            Autoscroll = bytes.hex(Autoscroll)
            Autoscroll = int(Autoscroll, 16)
            self.Autoscroll.setText(str(Autoscroll))
            Course.seek(0x21C)
            ObjectCount = Course.read(4)
            ObjectCount = bytearray(ObjectCount)
            ObjectCount.reverse()
            ObjectCount = bytes(ObjectCount)
            ObjectCount = bytes.hex(ObjectCount)
            ObjectCount = int(ObjectCount, 16)
            self.ObjectCount.setText(str(ObjectCount))
            for i in range(2600):
                Course.seek(608 + 32 * i)
                entity_id = Course.read(3)
                entity_name = f'Unknown({entity_id})'
                if entity_id == bytes([0x00, 0x00, 0xFF]) or entity_id == bytes([0x00, 0x12, 0xFF]):
                    entity_name = 'Goomba/Galoomba'
                if entity_id == bytes([0x01, 0x00, 0xFF]) or entity_id == bytes([0x01, 0x12, 0xFF]):
                    entity_name = 'Koopa Troopa'
                if entity_id == bytes([0x02, 0x00, 0xFF]) or entity_id == bytes([0x02, 0x12, 0xFF]):
                    entity_name = 'Piranha Plant/Jumping Piranha Plant'
                if entity_id == bytes([0x03, 0x00, 0xFF]) or entity_id == bytes([0x03, 0x12, 0xFF]):
                    entity_name = 'Hammer Bro'
                if entity_id == bytes([0x04, 0x00, 0xFF]) or entity_id == bytes([0x04, 0x12, 0xFF]):
                    entity_name = 'Block'
                if entity_id == bytes([0x05, 0x00, 0xFF]) or entity_id == bytes([0x05, 0x12, 0xFF]):
                    entity_name = '? Block'
                if entity_id == bytes([0x06, 0x00, 0xFF]) or entity_id == bytes([0x06, 0x12, 0xFF]):
                    entity_name = 'Hard Block'
                if entity_id == bytes([0x07, 0x00, 0xFF]) or entity_id == bytes([0x07, 0x12, 0xFF]):
                    entity_name = 'Ground'
                if entity_id == bytes([0x08, 0x00, 0xFF]) or entity_id == bytes([0x08, 0x12, 0xFF]):
                    entity_name = 'Coin/Frozen Coin'
                if entity_id == bytes([0x09, 0x00, 0xFF]) or entity_id == bytes([0x09, 0x12, 0xFF]):
                    entity_name = 'Pipe'
                if entity_id == bytes([0x0A, 0x00, 0xFF]) or entity_id == bytes([0x0A, 0x12, 0xFF]):
                    entity_name = 'Trampoline'
                if entity_id == bytes([0x0B, 0x00, 0xFF]) or entity_id == bytes([0x0B, 0x12, 0xFF]):
                    entity_name = 'Lift/Cloud Lift'
                if entity_id == bytes([0x0C, 0x00, 0xFF]) or entity_id == bytes([0x0C, 0x12, 0xFF]):
                    entity_name = 'Thwomp'
                if entity_id == bytes([0x0D, 0x00, 0xFF]) or entity_id == bytes([0x0D, 0x12, 0xFF]):
                    entity_name = 'Bill Blaster'
                if entity_id == bytes([0x0E, 0x00, 0xFF]) or entity_id == bytes([0x0E, 0x12, 0xFF]):
                    entity_name = 'Mushroom Platform'
                if entity_id == bytes([0x0F, 0x00, 0xFF]) or entity_id == bytes([0x0F, 0x12, 0xFF]):
                    entity_name = 'Bob-omb'
                if entity_id == bytes([0x10, 0x00, 0xFF]) or entity_id == bytes([0x70, 0x12, 0xFF]):
                    entity_name = 'Semisolid Platform'
                if entity_id == bytes([0x11, 0x00, 0xFF]) or entity_id == bytes([0x11, 0x12, 0xFF]):
                    entity_name = 'Bridge'
                if entity_id == bytes([0x12, 0x00, 0xFF]) or entity_id == bytes([0x12, 0x12, 0xFF]):
                    entity_name = 'P-Switch'
                if entity_id == bytes([0x13, 0x00, 0xFF]) or entity_id == bytes([0x13, 0x12, 0xFF]):
                    entity_name = 'Pow Block'
                if entity_id == bytes([0x14, 0x00, 0xFF]) or entity_id == bytes([0x14, 0x12, 0xFF]):
                    entity_name = 'Super Mushroom/Master Sword'
                if entity_id == bytes([0x15, 0x00, 0xFF]) or entity_id == bytes([0x15, 0x12, 0xFF]):
                    entity_name = 'Donut Block'
                if entity_id == bytes([0x16, 0x00, 0xFF]) or entity_id == bytes([0x16, 0x12, 0xFF]):
                    entity_name = 'Cloud Block'
                if entity_id == bytes([0x17, 0x00, 0xFF]) or entity_id == bytes([0x17, 0x12, 0xFF]):
                    entity_name = 'Note Block'
                if entity_id == bytes([0x18, 0x00, 0xFF]) or entity_id == bytes([0x18, 0x12, 0xFF]):
                    entity_name = 'Firebar'
                if entity_id == bytes([0x19, 0x00, 0xFF]) or entity_id == bytes([0x19, 0x12, 0xFF]):
                    entity_name = 'Spiny'
                if entity_id == bytes([0x1A, 0x00, 0xFF]) or entity_id == bytes([0x1A, 0x12, 0xFF]):
                    entity_name = 'Goal Ground'
                if entity_id == bytes([0x1B, 0x00, 0xFF]) or entity_id == bytes([0x1B, 0x12, 0xFF]):
                    entity_name = 'Goal Pole'
                if entity_id == bytes([0x1C, 0x00, 0xFF]) or entity_id == bytes([0x1C, 0x12, 0xFF]):
                    entity_name = 'Buzzy Beatle'
                if entity_id == bytes([0x1D, 0x00, 0xFF]) or entity_id == bytes([0x1D, 0x12, 0xFF]):
                    entity_name = 'Hidden Block'
                if entity_id == bytes([0x1E, 0x00, 0xFF]) or entity_id == bytes([0x1E, 0x12, 0xFF]):
                    entity_name = 'Lakitu'
                if entity_id == bytes([0x1F, 0x00, 0xFF]) or entity_id == bytes([0x1F, 0x12, 0xFF]):
                    entity_name = 'Cloud'
                if entity_id == bytes([0x20, 0x00, 0xFF]) or entity_id == bytes([0x70, 0x12, 0xFF]):
                    entity_name = 'Banzai Bill'
                if entity_id == bytes([0x21, 0x00, 0xFF]) or entity_id == bytes([0x21, 0x12, 0xFF]):
                    entity_name = '1-Up Mushroom'
                if entity_id == bytes([0x22, 0x00, 0xFF]) or entity_id == bytes([0x22, 0x12, 0xFF]):
                    entity_name = 'Fire Flower'
                if entity_id == bytes([0x23, 0x00, 0xFF]) or entity_id == bytes([0x23, 0x12, 0xFF]):
                    entity_name = 'Super Star'
                if entity_id == bytes([0x24, 0x00, 0xFF]) or entity_id == bytes([0x24, 0x12, 0xFF]):
                    entity_name = 'Lava Lift'
                if entity_id == bytes([0x25, 0x00, 0xFF]) or entity_id == bytes([0x25, 0x12, 0xFF]):
                    entity_name = 'Ground Start'
                if entity_id == bytes([0x26, 0x00, 0xFF]) or entity_id == bytes([0x26, 0x12, 0xFF]):
                    entity_name = 'Start Arrow'
                if entity_id == bytes([0x27, 0x00, 0xFF]) or entity_id == bytes([0x27, 0x12, 0xFF]):
                    entity_name = 'Kameck'
                if entity_id == bytes([0x28, 0x00, 0xFF]) or entity_id == bytes([0x28, 0x12, 0xFF]):
                    entity_name = 'Spike Top'
                if entity_id == bytes([0x29, 0x00, 0xFF]) or entity_id == bytes([0x29, 0x12, 0xFF]):
                    entity_name = 'Boo'
                if entity_id == bytes([0x2A, 0x00, 0xFF]) or entity_id == bytes([0x2A, 0x12, 0xFF]):
                    entity_name = 'Koopa Clown Car'
                if entity_id == bytes([0x2B, 0x00, 0xFF]) or entity_id == bytes([0x2B, 0x12, 0xFF]):
                    entity_name = 'Spike Trap'
                if entity_id == bytes([0x2C, 0x00, 0xFF]) or entity_id == bytes([0x2C, 0x12, 0xFF]):
                    entity_name = '3rd Tier Powerup'
                if entity_id == bytes([0x2D, 0x00, 0xFF]) or entity_id == bytes([0x2D, 0x12, 0xFF]):
                    entity_name = 'Shoe Goomba/Yoshi'
                if entity_id == bytes([0x2E, 0x00, 0xFF]) or entity_id == bytes([0x2E, 0x12, 0xFF]):
                    entity_name = 'Dry Bones'
                if entity_id == bytes([0x2F, 0x00, 0xFF]) or entity_id == bytes([0x2F, 0x12, 0xFF]):
                    entity_name = 'Cannon'
                if entity_id == bytes([0x30, 0x00, 0xFF]) or entity_id == bytes([0x70, 0x12, 0xFF]):
                    entity_name = 'Blooper'
                if entity_id == bytes([0x31, 0x00, 0xFF]) or entity_id == bytes([0x31, 0x12, 0xFF]):
                    entity_name = 'Castle Bridge'
                if entity_id == bytes([0x32, 0x00, 0xFF]) or entity_id == bytes([0x32, 0x12, 0xFF]):
                    entity_name = 'Hop-Chops'
                if entity_id == bytes([0x33, 0x00, 0xFF]) or entity_id == bytes([0x33, 0x12, 0xFF]):
                    entity_name = 'Skipsqueak'
                if entity_id == bytes([0x34, 0x00, 0xFF]) or entity_id == bytes([0x34, 0x12, 0xFF]):
                    entity_name = 'Wiggler'
                if entity_id == bytes([0x35, 0x00, 0xFF]) or entity_id == bytes([0x35, 0x12, 0xFF]):
                    entity_name = 'Conveyer Belt'
                if entity_id == bytes([0x36, 0x00, 0xFF]) or entity_id == bytes([0x36, 0x12, 0xFF]):
                    entity_name = 'Burner'
                if entity_id == bytes([0x37, 0x00, 0xFF]) or entity_id == bytes([0x37, 0x12, 0xFF]):
                    entity_name = 'Warp Door'
                if entity_id == bytes([0x38, 0x00, 0xFF]) or entity_id == bytes([0x38, 0x12, 0xFF]):
                    entity_name = 'Cheep Cheep'
                if entity_id == bytes([0x39, 0x00, 0xFF]) or entity_id == bytes([0x39, 0x12, 0xFF]):
                    entity_name = 'Muncher'
                if entity_id == bytes([0x3A, 0x00, 0xFF]) or entity_id == bytes([0x3A, 0x12, 0xFF]):
                    entity_name = 'Rocky Wrench'
                if entity_id == bytes([0x3B, 0x00, 0xFF]) or entity_id == bytes([0x3B, 0x12, 0xFF]):
                    entity_name = 'Rail'
                if entity_id == bytes([0x3C, 0x00, 0xFF]) or entity_id == bytes([0x3C, 0x12, 0xFF]):
                    entity_name = 'Lava Bubble'
                if entity_id == bytes([0x3D, 0x00, 0xFF]) or entity_id == bytes([0x3D, 0x12, 0xFF]):
                    entity_name = 'Chain Chomp'
                if entity_id == bytes([0x3E, 0x00, 0xFF]) or entity_id == bytes([0x3E, 0x12, 0xFF]):
                    entity_name = 'Bowser/Meowser'
                if entity_id == bytes([0x3F, 0x00, 0xFF]) or entity_id == bytes([0x3F, 0x12, 0xFF]):
                    entity_name = 'Ice Block'
                if entity_id == bytes([0x40, 0x00, 0xFF]) or entity_id == bytes([0x70, 0x12, 0xFF]):
                    entity_name = 'Vine'
                if entity_id == bytes([0x41, 0x00, 0xFF]) or entity_id == bytes([0x41, 0x12, 0xFF]):
                    entity_name = 'Stingby'
                if entity_id == bytes([0x42, 0x00, 0xFF]) or entity_id == bytes([0x42, 0x12, 0xFF]):
                    entity_name = 'Arrow Sign'
                if entity_id == bytes([0x43, 0x00, 0xFF]) or entity_id == bytes([0x43, 0x12, 0xFF]):
                    entity_name = 'One-Way Wall'
                if entity_id == bytes([0x44, 0x00, 0xFF]) or entity_id == bytes([0x44, 0x12, 0xFF]):
                    entity_name = 'Grinder'
                if entity_id == bytes([0x45, 0x00, 0xFF]) or entity_id == bytes([0x45, 0x12, 0xFF]):
                    entity_name = 'Player'
                if entity_id == bytes([0x46, 0x00, 0xFF]) or entity_id == bytes([0x46, 0x12, 0xFF]):
                    entity_name = '10-Coin'
                if entity_id == bytes([0x47, 0x00, 0xFF]) or entity_id == bytes([0x47, 0x12, 0xFF]):
                    entity_name = 'Semisolid Platform (3D World)'
                if entity_id == bytes([0x48, 0x00, 0xFF]) or entity_id == bytes([0x48, 0x12, 0xFF]):
                    entity_name = 'Koopa Troopa Car'
                if entity_id == bytes([0x49, 0x00, 0xFF]) or entity_id == bytes([0x49, 0x12, 0xFF]):
                    entity_name = 'Toad'
                if entity_id == bytes([0x4A, 0x00, 0xFF]) or entity_id == bytes([0x4A, 0x12, 0xFF]):
                    entity_name = 'Spike/Spike Ball'
                if entity_id == bytes([0x4B, 0x00, 0xFF]) or entity_id == bytes([0x4B, 0x12, 0xFF]):
                    entity_name = 'Stone'
                if entity_id == bytes([0x4C, 0x00, 0xFF]) or entity_id == bytes([0x4C, 0x12, 0xFF]):
                    entity_name = 'Twister'
                if entity_id == bytes([0x4D, 0x00, 0xFF]) or entity_id == bytes([0x4D, 0x12, 0xFF]):
                    entity_name = 'Boom Boom'
                if entity_id == bytes([0x4E, 0x00, 0xFF]) or entity_id == bytes([0x4E, 0x12, 0xFF]):
                    entity_name = 'Pokey'
                if entity_id == bytes([0x4F, 0x00, 0xFF]) or entity_id == bytes([0x4F, 0x12, 0xFF]):
                    entity_name = 'P-Block'
                if entity_id == bytes([0x50, 0x00, 0xFF]) or entity_id == bytes([0x70, 0x12, 0xFF]):
                    entity_name = 'Dash Block'
                if entity_id == bytes([0x51, 0x00, 0xFF]) or entity_id == bytes([0x51, 0x12, 0xFF]):
                    entity_name = 'None'
                if entity_id == bytes([0x52, 0x00, 0xFF]) or entity_id == bytes([0x52, 0x12, 0xFF]):
                    entity_name = 'Bumper'
                if entity_id == bytes([0x53, 0x00, 0xFF]) or entity_id == bytes([0x53, 0x12, 0xFF]):
                    entity_name = 'Spike Pillar'
                if entity_id == bytes([0x54, 0x00, 0xFF]) or entity_id == bytes([0x54, 0x12, 0xFF]):
                    entity_name = 'Snake Block'
                if entity_id == bytes([0x55, 0x00, 0xFF]) or entity_id == bytes([0x55, 0x12, 0xFF]):
                    entity_name = 'Track Block'
                if entity_id == bytes([0x56, 0x00, 0xFF]) or entity_id == bytes([0x56, 0x12, 0xFF]):
                    entity_name = 'Charvaargh'
                if entity_id == bytes([0x57, 0x00, 0xFF]) or entity_id == bytes([0x57, 0x12, 0xFF]):
                    entity_name = 'Gentle Slope'
                if entity_id == bytes([0x58, 0x00, 0xFF]) or entity_id == bytes([0x58, 0x12, 0xFF]):
                    entity_name = 'Steep Slope'
                if entity_id == bytes([0x59, 0x00, 0xFF]) or entity_id == bytes([0x59, 0x12, 0xFF]):
                    entity_name = 'Custom Scroll Waypoint'
                if entity_id == bytes([0x5A, 0x00, 0xFF]) or entity_id == bytes([0x5A, 0x12, 0xFF]):
                    entity_name = 'Checkpoint Flag'
                if entity_id == bytes([0x5B, 0x00, 0xFF]) or entity_id == bytes([0x5B, 0x12, 0xFF]):
                    entity_name = 'Seesaw'
                if entity_id == bytes([0x5C, 0x00, 0xFF]) or entity_id == bytes([0x5C, 0x12, 0xFF]):
                    entity_name = 'Pink Coin'
                if entity_id == bytes([0x5D, 0x00, 0xFF]) or entity_id == bytes([0x5D, 0x12, 0xFF]):
                    entity_name = 'Clear Pipe'
                if entity_id == bytes([0x5E, 0x00, 0xFF]) or entity_id == bytes([0x5E, 0x12, 0xFF]):
                    entity_name = 'Sloped Conveyer Belt'
                if entity_id == bytes([0x5F, 0x00, 0xFF]) or entity_id == bytes([0x5F, 0x12, 0xFF]):
                    entity_name = 'Key'
                if entity_id == bytes([0x60, 0x00, 0xFF]) or entity_id == bytes([0x60, 0x12, 0xFF]):
                    entity_name = 'Ant Trooper'
                if entity_id == bytes([0x61, 0x00, 0xFF]) or entity_id == bytes([0x61, 0x12, 0xFF]):
                    entity_name = 'Warp Box'
                if entity_id == bytes([0x62, 0x00, 0xFF]) or entity_id == bytes([0x62, 0x12, 0xFF]):
                    entity_name = 'Bowser Jr.'
                if entity_id == bytes([0x63, 0x00, 0xFF]) or entity_id == bytes([0x63, 0x12, 0xFF]):
                    entity_name = 'On/Off Switch'
                if entity_id == bytes([0x64, 0x00, 0xFF]) or entity_id == bytes([0x64, 0x12, 0xFF]):
                    entity_name = 'Dotted-Line Block'
                if entity_id == bytes([0x65, 0x00, 0xFF]) or entity_id == bytes([0x65, 0x12, 0xFF]):
                    entity_name = 'Lava Editor'
                if entity_id == bytes([0x66, 0x00, 0xFF]) or entity_id == bytes([0x66, 0x12, 0xFF]):
                    entity_name = 'Monty Mole'
                if entity_id == bytes([0x67, 0x00, 0xFF]) or entity_id == bytes([0x67, 0x12, 0xFF]):
                    entity_name = 'Fish Bones'
                if entity_id == bytes([0x68, 0x00, 0xFF]) or entity_id == bytes([0x68, 0x12, 0xFF]):
                    entity_name = 'Angry Sun'
                if entity_id == bytes([0x69, 0x00, 0xFF]) or entity_id == bytes([0x69, 0x12, 0xFF]):
                    entity_name = 'Swinging Claw'
                if entity_id == bytes([0x6A, 0x00, 0xFF]) or entity_id == bytes([0x6A, 0x12, 0xFF]):
                    entity_name = 'Tree'
                if entity_id == bytes([0x6B, 0x00, 0xFF]) or entity_id == bytes([0x6B, 0x12, 0xFF]):
                    entity_name = 'Piranha Creeper'
                if entity_id == bytes([0x6C, 0x00, 0xFF]) or entity_id == bytes([0x6C, 0x12, 0xFF]):
                    entity_name = 'Blinking Block'
                if entity_id == bytes([0x6D, 0x00, 0xFF]) or entity_id == bytes([0x6D, 0x12, 0xFF]):
                    entity_name = 'Sound Effect Icon'
                if entity_id == bytes([0x6E, 0x00, 0xFF]) or entity_id == bytes([0x6E, 0x12, 0xFF]):
                    entity_name = 'Spike Block'
                if entity_id == bytes([0x6F, 0x00, 0xFF]) or entity_id == bytes([0x6F, 0x12, 0xFF]):
                    entity_name = 'None'
                if entity_id == bytes([0x70, 0x00, 0xFF]) or entity_id == bytes([0x70, 0x12, 0xFF]):
                    entity_name = 'Crate'
                if entity_id == bytes([0x71, 0x00, 0xFF]) or entity_id == bytes([0x71, 0x12, 0xFF]):
                    entity_name = 'Mushroom Trampoline'
                if entity_id == bytes([0x72, 0x00, 0xFF]) or entity_id == bytes([0x72, 0x12, 0xFF]):
                    entity_name = 'Porcupuffer'
                if entity_id == bytes([0x73, 0x00, 0xFF]) or entity_id == bytes([0x73, 0x12, 0xFF]):
                    entity_name = 'Goal Toadette'
                if entity_id == bytes([0x74, 0x00, 0xFF]) or entity_id == bytes([0x74, 0x12, 0xFF]):
                    entity_name = 'Super Hammer'
                if entity_id == bytes([0x75, 0x00, 0xFF]) or entity_id == bytes([0x75, 0x12, 0xFF]):
                    entity_name = 'Bully'
                if entity_id == bytes([0x76, 0x00, 0xFF]) or entity_id == bytes([0x76, 0x12, 0xFF]):
                    entity_name = 'Icicle'
                if entity_id == bytes([0x77, 0x00, 0xFF]) or entity_id == bytes([0x77, 0x12, 0xFF]):
                    entity_name = '! Block'
                self.EntitiesList.addItem(str(i) + ': ' + str(entity_name) + ' @' + str(hex(608 + 32 * i)))
                if not entity_id == bytes([0x00, 0x00, 0x00]):
                    self.EntityNumberBox.addItem(str(i + 1))
            

    def HandleSaveAs(self):
        global CoursePath
        if not CoursePath:
            return
        else:
            with open(CoursePath,'rb') as Course:
                data = Course.read()
                data = bytearray(data)
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
                data[0x4:0x6] = TimeLimit
                data[0x6:0x7] = Autoscroll
                data[0x8:0xA] = SaveYear
                data[0xA:0xB] = SaveMonth
                data[0xB:0xC] = SaveDay
                data[0xC:0xD] = SaveHour
                data[0xD:0xE] = SaveMinute
                data[596 + 32 * (int(self.EntityNumberBox.currentText())-1):604 + 32 * (int(self.EntityNumberBox.currentText())-1)] = EntityFlags
                data[608 + 32 * (int(self.EntityNumberBox.currentText())-1):609 + 32 * (int(self.EntityNumberBox.currentText())-1)] = (int(EntityID)).to_bytes(1, byteorder='big')
                with open(CoursePath,'wb') as Course:
                    Course.write(data)

    def EntityNumberBox_Index_Changed(self):
        with open(CoursePath,'rb') as Course:
            Course.seek(596 + 32 * (int(self.EntityNumberBox.currentText())-1))
            ParentFlags = Course.read(4)
            ParentFlags = bytearray(ParentFlags)
            ParentFlags.reverse()
            ParentFlags = bytes(ParentFlags)
            ParentFlags = bytes.hex(ParentFlags)
            Course.seek(600 + 32 * (int(self.EntityNumberBox.currentText())-1))
            ChildFlags = Course.read(4)
            ChildFlags = bytearray(ChildFlags)
            ChildFlags.reverse()
            ChildFlags = bytes(ChildFlags)
            ChildFlags = bytes.hex(ChildFlags)
            EntityFlags = ParentFlags + ChildFlags
            self.EntityFlags.setText(EntityFlags)
            Course.seek(608 + 32 * (int(self.EntityNumberBox.currentText())-1))
            EntityID = Course.read(1)
            self.EntityID.setText(str(int.from_bytes(EntityID, 'big')))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

