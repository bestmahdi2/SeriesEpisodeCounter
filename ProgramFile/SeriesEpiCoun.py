# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SeriesEpiCoun.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(822, 608)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(822, 608))
        MainWindow.setMaximumSize(QtCore.QSize(822, 608))
        MainWindow.setWindowOpacity(0.978)
        MainWindow.setStyleSheet("background-color:#3C3F41;color:green")
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 160, 298, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_No = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_No.sizePolicy().hasHeightForWidth())
        self.radioButton_No.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_No.setFont(font)
        self.radioButton_No.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_No.setStyleSheet("color:#FF7F50")
        self.radioButton_No.setChecked(True)
        self.radioButton_No.setObjectName("radioButton_No")
        self.horizontalLayout.addWidget(self.radioButton_No)
        self.radioButton_yes = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_yes.sizePolicy().hasHeightForWidth())
        self.radioButton_yes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_yes.setFont(font)
        self.radioButton_yes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_yes.setStyleSheet("color:#FF7F50")
        self.radioButton_yes.setObjectName("radioButton_yes")
        self.horizontalLayout.addWidget(self.radioButton_yes)
        self.label_Error = QtWidgets.QLabel(self.centralwidget)
        self.label_Error.setGeometry(QtCore.QRect(11, 540, 793, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Error.sizePolicy().hasHeightForWidth())
        self.label_Error.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Error.setFont(font)
        self.label_Error.setStyleSheet("color:red;")
        self.label_Error.setText("")
        self.label_Error.setObjectName("label_Error")
        self.LabelRememmber = QtWidgets.QLabel(self.centralwidget)
        self.LabelRememmber.setGeometry(QtCore.QRect(11, 11, 793, 91))
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
        self.LabelSelect = QtWidgets.QLabel(self.centralwidget)
        self.LabelSelect.setGeometry(QtCore.QRect(10, 120, 381, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelSelect.sizePolicy().hasHeightForWidth())
        self.LabelSelect.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LabelSelect.setFont(font)
        self.LabelSelect.setStyleSheet("color:white")
        self.LabelSelect.setObjectName("LabelSelect")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(11, 100, 793, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setLineWidth(0)
        self.line_2.setMidLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.textBrowserEpi = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserEpi.setGeometry(QtCore.QRect(10, 190, 801, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowserEpi.sizePolicy().hasHeightForWidth())
        self.textBrowserEpi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.textBrowserEpi.setFont(font)
        self.textBrowserEpi.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowserEpi.setStyleSheet("color:white ; align:\"center\";font-size:17px;")
        self.textBrowserEpi.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowserEpi.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.textBrowserEpi.setObjectName("textBrowserEpi")
        self.textBrowserSeri = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserSeri.setGeometry(QtCore.QRect(10, 370, 801, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowserSeri.sizePolicy().hasHeightForWidth())
        self.textBrowserSeri.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.textBrowserSeri.setFont(font)
        self.textBrowserSeri.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowserSeri.setStyleSheet("color:white ; align:\"center\";font-size:17px;")
        self.textBrowserSeri.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowserSeri.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.textBrowserSeri.setObjectName("textBrowserSeri")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color:#383B3D;")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Series Episode Counter"))
        self.radioButton_No.setToolTip(_translate("MainWindow", "Shortcut : CTRL + E"))
        self.radioButton_No.setStatusTip(_translate("MainWindow", "Change format to : not having seasons"))
        self.radioButton_No.setText(_translate("MainWindow", "Has No Seasons"))
        self.radioButton_yes.setToolTip(_translate("MainWindow", "Shortcut : CTRL + P"))
        self.radioButton_yes.setStatusTip(_translate("MainWindow", "Change format to : having seasons"))
        self.radioButton_yes.setText(_translate("MainWindow", "Has Seasons"))
        self.LabelRememmber.setStatusTip(_translate("MainWindow", "NOTE!!!"))
        self.LabelRememmber.setText(_translate("MainWindow", "<html><head/><body><p>Rememmber : Copy program into series folder</p><p>If your series have season , season should be in these 4 formats (no matter Captal letter or not): S01 , Season01 , ف01 , فصل01</p><p>And episodes should be in these 4 formats (no matter Captal letter or not): E01, Episode01 , ق01 , قسمت01</p></body></html>"))
        self.LabelSelect.setStatusTip(_translate("MainWindow", "Does your series has seasons or not?"))
        self.LabelSelect.setText(_translate("MainWindow", "Select one below: (My series ...)"))
        self.textBrowserEpi.setStatusTip(_translate("MainWindow", "Reasults For Episodes"))
        self.textBrowserEpi.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:17px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20px;\"><br /></p></body></html>"))
        self.textBrowserSeri.setStatusTip(_translate("MainWindow", "Reasults For Seasons"))
        self.textBrowserSeri.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:17px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
