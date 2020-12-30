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
import codecs          # Built-in module
import struct          # Built-in module
from PyQt5 import QtCore, QtGui, QtWidgets
from SMM2 import encryption
#====================================#

class MainWindow(QtWidgets.QMainWindow):
    def CreateAction(self, shortname, function, icon, text, statustext, shortcut, toggle=False):
        if icon is not None:
            act = QtWidgets.QAction(icon, text, self)

        else:
            act = QtWidgets.QAction(text, self)

        if shortcut is not None:
            act.setShortcut(shortcut)

        if statustext is not None:
            act.setStatusTip(statustext)

        if toggle:
            act.setCheckable(True)

        if function is not None:
            act.triggered.connect(function)

        self.actions[shortname] = act

    def __init__(self):
        super().__init__(None)
        self.setObjectName("MainWindow")
        self.setWindowTitle("Doug Bowser; Super Mario Maker 2 Binary Course Data Editor")
        self.resize(771, 355)
        self.setMinimumSize(QtCore.QSize(771, 315))
        self.setMaximumSize(QtCore.QSize(771, 315))

        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.setFont(font)

        self.actions = {}
        self.CreateAction("openfromfile", self.handleOpenFromFile, None, "Open Course by File...", "Open a course based on its filename", QtGui.QKeySequence("Ctrl+O"))
        self.CreateAction("save", self.handleSave, None, "Save Course", "Save the course back to the archive file", QtGui.QKeySequence.Save)

        menubar = QtWidgets.QMenuBar()
        self.setMenuBar(menubar)
        fmenu = menubar.addMenu("&File")
        fmenu.setFont(font)
        fmenu.addAction(self.actions["openfromfile"])
        fmenu.addSeparator()
        fmenu.addAction(self.actions["save"])

        self.timer = QtWidgets.QLineEdit(self)
        self.timer.setGeometry(QtCore.QRect(10, 35, 231, 31))
        self.timer.setMaxLength(5)
        self.timer.setReadOnly(False)
        self.timer.setObjectName("timer")
        self.timer.setPlaceholderText("Timer...")

        self.saveyear = QtWidgets.QLineEdit(self)
        self.saveyear.setGeometry(QtCore.QRect(10, 75, 231, 31))
        self.saveyear.setText("")
        self.saveyear.setMaxLength(5)
        self.saveyear.setReadOnly(False)
        self.saveyear.setObjectName("saveyear")
        self.saveyear.setPlaceholderText("Save year...")

        self.savemonth = QtWidgets.QLineEdit(self)
        self.savemonth.setGeometry(QtCore.QRect(10, 115, 231, 31))
        self.savemonth.setMaxLength(3)
        self.savemonth.setReadOnly(False)
        self.savemonth.setObjectName("savemonth")
        self.savemonth.setPlaceholderText("Save month...")

        self.saveday = QtWidgets.QLineEdit(self)
        self.saveday.setGeometry(QtCore.QRect(10, 155, 231, 31))
        self.saveday.setMaxLength(3)
        self.saveday.setReadOnly(False)
        self.saveday.setObjectName("saveday")
        self.saveday.setPlaceholderText("Save day...")

        self.savehour = QtWidgets.QLineEdit(self)
        self.savehour.setGeometry(QtCore.QRect(10, 195, 231, 31))
        self.savehour.setMaxLength(3)
        self.savehour.setReadOnly(False)
        self.savehour.setObjectName("savehour")
        self.savehour.setPlaceholderText("Save hour...")

        self.saveminute = QtWidgets.QLineEdit(self)
        self.saveminute.setGeometry(QtCore.QRect(10, 235, 231, 31))
        self.saveminute.setMaxLength(3)
        self.saveminute.setReadOnly(False)
        self.saveminute.setObjectName("saveminute")
        self.saveminute.setPlaceholderText("Save minute...")

        self.autoscroll = QtWidgets.QLineEdit(self)
        self.autoscroll.setGeometry(QtCore.QRect(10, 275, 231, 31))
        self.autoscroll.setReadOnly(False)
        self.autoscroll.setObjectName("autoscroll")
        self.autoscroll.setMaxLength(3)
        self.autoscroll.setPlaceholderText("Autoscroll...")

    def __init2__(self):
        self.handleOpenFromFile()

    def handleOpenFromFile(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open Course", "", "Binary Course Data File (*.bcd)")[0]
        if not self.filename:
            return None
        else:
            data = open(self.filename, "rb").read()
            course = encryption.Course(data)
            course.decrypt()
            data = course.data
            self.load(data)

    def load(self, data=None):
        if not data:
            return None
        else:
            self.data = data
            self.timer.setText("%s" % struct.unpack("<H", self.data[0x4:0x6]))
            self.saveyear.setText("%s" % struct.unpack("<H", self.data[0x8:0xA]))
            self.savemonth.setText("%s" % struct.unpack("<B", self.data[0xA:0xB]))
            self.saveday.setText("%s" % struct.unpack("<B", self.data[0xB:0xC]))
            self.savehour.setText("%s" % struct.unpack("<B", self.data[0xC:0xD]))
            self.saveminute.setText("%s" % struct.unpack("<B", self.data[0xD:0xE]))
            self.autoscroll.setText("%s" % struct.unpack("<B", self.data[0xE:0xF]))

    def handleSave(self):
        if not self.filename:
            QtWidgets.QMessageBox.warning(None, "Success", "No Course Selected!")
        else:
            with open(self.filename, "rb") as inf:
                self.data = bytearray(inf.read())
                self.data[0x4:0x6] = struct.pack("<H", int(self.timer.text()))
                self.data[0x8:0xA] = struct.pack("<H", int(self.saveyear.text()))
                self.data[0xA:0xB] = struct.pack("<B", int(self.savemonth.text()))
                self.data[0xB:0xC] = struct.pack("<B", int(self.saveday.text()))
                self.data[0xC:0xD] = struct.pack("<B", int(self.savehour.text()))
                self.data[0xD:0xE] = struct.pack("<B", int(self.saveminute.text()))
                self.data[0xE:0xF] = struct.pack("<B", int(self.autoscroll.text()))
                with open(self.filename, "wb") as outf:
                    course = encryption.Course(self.data)
                    course.encrypt()
                    outf.write(course.data)
                    QtWidgets.QMessageBox.information(None, "Success", "Saved to {}!".format(self.filename))

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationDisplayName("")
    mainWindow = MainWindow()
    mainWindow.__init2__()
    mainWindow.show()
    app.exec_()
    sys.exit()

if __name__ == "__main__":
    main()
