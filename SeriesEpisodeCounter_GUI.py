from os import sep
from PyQt5 import QtWidgets, QtCore, QtGui
from ProgramFile.SeriesEpiCoun import Ui_MainWindow
from ProgramFile.SeriesEpisodeCounterQT import noseason,seasonable

# Handle high resolution displays:
# if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
# if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class MainClass(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        
                        # region icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("."+sep+"film.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        
        
    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        # _translate = QtCore.QCoreApplication.translate

    def calculator(self):
        self.label_Error.setText("")
        if self.radioButton_No.isChecked() == True:
            try:
                M = noseason()
                Epi = M.missEpisode
                toPrint = ""
                if len(Epi) == 0:
                    toPrint = "No missing Episode found"
                if len(Epi) == 1:
                    toPrint = "The missing Episode is :  " + str(Epi).replace("\'", "").replace("[", "").replace("]","")
                if len(Epi) > 1:
                    toPrint = "All missing Episodes are : " + str(Epi).replace("\'", "").replace("[", "").replace("]","")

                self.textBrowserEpi.setText("========Episodes========\n" + "\n" + toPrint)
                self.textBrowserSeri.setText("")

            except :
                self.label_Error.setText("Error accrued !!! , be sure about season choice.")

        if self.radioButton_yes.isChecked() == True:
            try:
                toPrintE = []
                toPrintS = ""
                M = seasonable()
                M.Ecounter()
                M.Scounter()
                Sea = M.missSeason
                Epi = M.missEpisode

                if len(Sea) > 1:
                    toPrintS = "Missing Seasons are :    " +str(Sea).replace("[", "").replace("]", "").replace("\'","")
                elif len(Sea) == 1:
                    toPrintS = "Missing Season is :    "+ str(Sea).replace("[", "").replace("]", "").replace("\'","")
                else:
                    toPrintS = "No missing Season found"

                self.textBrowserSeri.setText("========Seasons========\n\n"+ toPrintS)

                for E in Epi:
                    season = E[-1]
                    E.remove(E[-1])

                    if len(E) > 1 :
                        toPrintE.append(str(len(E)) + " Episodes are missing "+ "in " + season.replace("s","Season *") + "* :    "+str(E).replace("[","").replace("]","").replace("\'",""))
                    elif len(E) == 1:
                        toPrintE.append("1 Episode is missing " + "in " + season.replace("s", "Season *") + "* :    "+str(E).replace("[", "").replace("]", "").replace("\'",""))
                    else:
                        toPrintE.append("No missing Episode found in "+season.replace("s","Season *") + "*")
                    toPrintE.append("\n\n")

                self.textBrowserEpi.setText("========Episodes========\n\n" +"".join(toPrintE))
            except :
                self.label_Error.setText("Error accrued !!! , be sure about season choice.")

if __name__ == "__main__":
    from sys import argv , exit
    app = QtWidgets.QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainClass()
    ui.setupUi(MainWindow)
    ###
    ui.calculator()
    ui.radioButton_yes.setChecked(False)
    ui.radioButton_No.setChecked(False)

    ui.radioButton_yes.clicked.connect(ui.calculator)
    ui.radioButton_No.clicked.connect(ui.calculator)
    ###

    MainWindow.show()
    exit(app.exec_())