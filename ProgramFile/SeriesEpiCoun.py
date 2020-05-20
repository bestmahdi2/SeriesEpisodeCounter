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
        MainWindow.resize(529, 468)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1, 1))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setWindowOpacity(0.978)
        MainWindow.setStyleSheet("background-color:#3C3F41;")
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowserEpi = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserEpi.setGeometry(QtCore.QRect(10, 150, 511, 131))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.textBrowserEpi.setFont(font)
        self.textBrowserEpi.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowserEpi.setStyleSheet("color:white ; align:\"center\";font-size:12px;")
        self.textBrowserEpi.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowserEpi.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.textBrowserEpi.setObjectName("textBrowserEpi")
        self.label_Error = QtWidgets.QLabel(self.centralwidget)
        self.label_Error.setGeometry(QtCore.QRect(10, 410, 351, 16))
        self.label_Error.setStyleSheet("color:red;")
        self.label_Error.setText("")
        self.label_Error.setObjectName("label_Error")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 150, 20))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_No = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_No.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_No.setStyleSheet("color:#FF7F50")
        self.radioButton_No.setChecked(True)
        self.radioButton_No.setObjectName("radioButton_No")
        self.horizontalLayout.addWidget(self.radioButton_No)
        self.radioButton_yes = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_yes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_yes.setStyleSheet("color:#FF7F50")
        self.radioButton_yes.setObjectName("radioButton_yes")
        self.horizontalLayout.addWidget(self.radioButton_yes)
        self.textBrowserSeri = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserSeri.setGeometry(QtCore.QRect(10, 290, 511, 121))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.textBrowserSeri.setFont(font)
        self.textBrowserSeri.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowserSeri.setStyleSheet("color:white ; align:\"center\";font-size:12px;")
        self.textBrowserSeri.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowserSeri.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.textBrowserSeri.setObjectName("textBrowserSeri")
        self.LabelRememmber = QtWidgets.QLabel(self.centralwidget)
        self.LabelRememmber.setGeometry(QtCore.QRect(10, 10, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.LabelRememmber.setFont(font)
        self.LabelRememmber.setStyleSheet("overflow : auto;color:yellow")
        self.LabelRememmber.setScaledContents(True)
        self.LabelRememmber.setWordWrap(True)
        self.LabelRememmber.setObjectName("LabelRememmber")
        self.LabelSelect = QtWidgets.QLabel(self.centralwidget)
        self.LabelSelect.setGeometry(QtCore.QRect(10, 100, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LabelSelect.setFont(font)
        self.LabelSelect.setStyleSheet("color:white")
        self.LabelSelect.setObjectName("LabelSelect")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 90, 511, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Series Episode Counter"))
        self.textBrowserEpi.setStatusTip(_translate("MainWindow", "Reasults"))
        self.textBrowserEpi.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20px;\"><br /></p></body></html>"))
        self.radioButton_No.setToolTip(_translate("MainWindow", "Shortcut : CTRL + E"))
        self.radioButton_No.setStatusTip(_translate("MainWindow", "Change language"))
        self.radioButton_No.setText(_translate("MainWindow", "No Seasons"))
        self.radioButton_yes.setToolTip(_translate("MainWindow", "Shortcut : CTRL + P"))
        self.radioButton_yes.setStatusTip(_translate("MainWindow", "Change language"))
        self.radioButton_yes.setText(_translate("MainWindow", "Have Seasons"))
        self.textBrowserSeri.setStatusTip(_translate("MainWindow", "Reasults"))
        self.textBrowserSeri.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20px;\"><br /></p></body></html>"))
        self.LabelRememmber.setText(_translate("MainWindow", "<html><head/><body><p>Rememmber : Copy program into series folder</p><p>If your series have season , season should be in these 4 formats (no matter Captal letter or not): S01 , Season01 , ف01 , فصل01</p><p>And episodes should be in these 4 formats (no matter Captal letter or not): E01, Episode01 , ق01 , قسمت01</p></body></html>"))
        self.LabelSelect.setText(_translate("MainWindow", "Select one below:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
