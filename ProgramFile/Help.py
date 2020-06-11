# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ProgramFile\Help.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(331, 211)
        Dialog.setStyleSheet("background-color:#3C3F41;color:green")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 160, 311, 21))
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setStyleSheet("background-color:white")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.LabelRememmber = QtWidgets.QLabel(Dialog)
        self.LabelRememmber.setGeometry(QtCore.QRect(10, 10, 301, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelRememmber.sizePolicy().hasHeightForWidth())
        self.LabelRememmber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.LabelRememmber.setFont(font)
        self.LabelRememmber.setStyleSheet("overflow : auto;color:yellow")
        self.LabelRememmber.setScaledContents(True)
        self.LabelRememmber.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.LabelRememmber.setWordWrap(True)
        self.LabelRememmber.setObjectName("LabelRememmber")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Help"))
        self.LabelRememmber.setStatusTip(_translate("Dialog", "NOTE!!!"))
        self.LabelRememmber.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Rememmber</span></p><p>If your series have season , season should be in these 4 formats (no matter Captal letter or not): S01 , Season01 , ف01 , فصل01</p><p>And episodes should be in these 4 formats (no matter Captal letter or not): E01, Episode01 , ق01 , قسمت01</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

