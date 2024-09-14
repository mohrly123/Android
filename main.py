# main.py
import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QErrorMessage,
    QMessageBox

)

from PySide6.QtCore import Qt

############################################
#auswahlfenster.py

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

#######################################################################
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bahnsteigberechnung.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QWidget)

class Ui_MainWindow_bahnsteig(object):
    def setupUi(self, MainWindow_bahnsteig):
        if not MainWindow_bahnsteig.objectName():
            MainWindow_bahnsteig.setObjectName(u"MainWindow_bahnsteig")
        MainWindow_bahnsteig.resize(500, 480)
        self.centralwidget = QWidget(MainWindow_bahnsteig)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_abstand = QPushButton(self.centralwidget)
        self.button_abstand.setObjectName(u"button_abstand")

        self.gridLayout.addWidget(self.button_abstand, 6, 1, 1, 1)

        self.label_abstandberechnung = QLabel(self.centralwidget)
        self.label_abstandberechnung.setObjectName(u"label_abstandberechnung")
        font = QFont()
        font.setFamilies([u"Segoe UI Variable Small Light"])
        font.setItalic(True)
        self.label_abstandberechnung.setFont(font)
        self.label_abstandberechnung.setFrameShape(QFrame.Shape.Panel)
        self.label_abstandberechnung.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_abstandberechnung.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_abstandberechnung.setMargin(2)

        self.gridLayout.addWidget(self.label_abstandberechnung, 3, 0, 1, 2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 2)

        self.label_ergebnis_abstand = QLabel(self.centralwidget)
        self.label_ergebnis_abstand.setObjectName(u"label_ergebnis_abstand")
        self.label_ergebnis_abstand.setMargin(0)

        self.gridLayout.addWidget(self.label_ergebnis_abstand, 4, 0, 1, 1)

        self.input_abstand = QLineEdit(self.centralwidget)
        self.input_abstand.setObjectName(u"input_abstand")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_abstand.sizePolicy().hasHeightForWidth())
        self.input_abstand.setSizePolicy(sizePolicy)
        self.input_abstand.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.input_abstand, 5, 1, 1, 1)

        self.button_hoehe = QPushButton(self.centralwidget)
        self.button_hoehe.setObjectName(u"button_hoehe")

        self.gridLayout.addWidget(self.button_hoehe, 12, 1, 1, 1)

        self.label_ist_hoehe = QLabel(self.centralwidget)
        self.label_ist_hoehe.setObjectName(u"label_ist_hoehe")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_ist_hoehe.sizePolicy().hasHeightForWidth())
        self.label_ist_hoehe.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setUnderline(True)
        self.label_ist_hoehe.setFont(font1)
        self.label_ist_hoehe.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_ist_hoehe, 11, 0, 1, 1)

        self.labelhoehenberechnung = QLabel(self.centralwidget)
        self.labelhoehenberechnung.setObjectName(u"labelhoehenberechnung")
        self.labelhoehenberechnung.setFont(font)
        self.labelhoehenberechnung.setFrameShape(QFrame.Shape.Panel)
        self.labelhoehenberechnung.setFrameShadow(QFrame.Shadow.Sunken)
        self.labelhoehenberechnung.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelhoehenberechnung.setMargin(0)

        self.gridLayout.addWidget(self.labelhoehenberechnung, 9, 0, 1, 2)

        self.label_ueberschrift = QLabel(self.centralwidget)
        self.label_ueberschrift.setObjectName(u"label_ueberschrift")
        sizePolicy.setHeightForWidth(self.label_ueberschrift.sizePolicy().hasHeightForWidth())
        self.label_ueberschrift.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.label_ueberschrift.setFont(font2)
        self.label_ueberschrift.setTextFormat(Qt.TextFormat.AutoText)
        self.label_ueberschrift.setScaledContents(False)
        self.label_ueberschrift.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_ueberschrift.setMargin(0)

        self.gridLayout.addWidget(self.label_ueberschrift, 0, 0, 1, 2)

        self.label_ergebnis_hoehe = QLabel(self.centralwidget)
        self.label_ergebnis_hoehe.setObjectName(u"label_ergebnis_hoehe")

        self.gridLayout.addWidget(self.label_ergebnis_hoehe, 10, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 13, 0, 1, 2)

        self.input_hoehe = QLineEdit(self.centralwidget)
        self.input_hoehe.setObjectName(u"input_hoehe")
        self.input_hoehe.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.input_hoehe, 11, 1, 1, 1)

        self.label_sollhoehe = QLabel(self.centralwidget)
        self.label_sollhoehe.setObjectName(u"label_sollhoehe")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setUnderline(True)
        self.label_sollhoehe.setFont(font3)
        self.label_sollhoehe.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)
        self.label_sollhoehe.setMargin(18)

        self.gridLayout.addWidget(self.label_sollhoehe, 10, 1, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 8, 0, 1, 2)

        self.label_ist_abstand = QLabel(self.centralwidget)
        self.label_ist_abstand.setObjectName(u"label_ist_abstand")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_ist_abstand.sizePolicy().hasHeightForWidth())
        self.label_ist_abstand.setSizePolicy(sizePolicy2)
        self.label_ist_abstand.setFont(font1)
        self.label_ist_abstand.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_ist_abstand, 5, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 7, 0, 1, 2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)
        self.label.setMargin(18)

        self.gridLayout.addWidget(self.label, 4, 1, 1, 1)

        MainWindow_bahnsteig.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow_bahnsteig)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 33))
        MainWindow_bahnsteig.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow_bahnsteig)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow_bahnsteig.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_bahnsteig)

        QMetaObject.connectSlotsByName(MainWindow_bahnsteig)
    # setupUi

    def retranslateUi(self, MainWindow_bahnsteig):
        MainWindow_bahnsteig.setWindowTitle(QCoreApplication.translate("MainWindow_bahnsteig", u"MainWindow", None))
        self.button_abstand.setText(QCoreApplication.translate("MainWindow_bahnsteig", u"Berechnen", None))
        self.label_abstandberechnung.setText(QCoreApplication.translate("MainWindow_bahnsteig", u"Abstandsberechnung", None))
        self.label_ergebnis_abstand.setText(QCoreApplication.translate("MainWindow_bahnsteig", u"Ergebnis", None))
        self.input_abstand.setText("")
        self.button_hoehe.setText(QCoreApplication.translate("MainWindow_bahnsteig", u"Berechnen", None))
        self.label_ist_hoehe.setText(QCoreApplication.translate("MainWindow_bahnsteig", u"IST H\u00f6he:", None))
        self.labelhoehenberechnung.setText(QCoreApplication.translate("MainWindow_bahnsteig", u"H\u00f6henberechnung", None))
        self.label_ueberschrift.setText(QCoreApplication.translate("MainWindow_bahnsteig", u"Bahnsteigberechnung", None))
        self.label_ergebnis_hoehe.setText(QCoreApplication.translate("MainWindow_bahnsteig", u"Ergebnis", None))
        self.label_sollhoehe.setText(QCoreApplication.translate("MainWindow_bahnsteig", u"Sollh\u00f6he : 550 mm", None))
        self.label_ist_abstand.setText(QCoreApplication.translate("MainWindow_bahnsteig", u"IST Abstand:", None))
        self.label.setText(QCoreApplication.translate("MainWindow_bahnsteig", u"Sollabstand : 1665 mm", None))
    # retranslateUi


#######################################################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(502, 481)
        self.action550_mm = QAction(MainWindow)
        self.action550_mm.setObjectName(u"action550_mm")
        self.action380mm = QAction(MainWindow)
        self.action380mm.setObjectName(u"action380mm")
        self.actionMindestverrechnung = QAction(MainWindow)
        self.actionMindestverrechnung.setObjectName(u"actionMindestverrechnung")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, -1, 30, -1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton.setFont(font)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 502, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pushButton, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action550_mm.setText(QCoreApplication.translate("MainWindow", u"550 mm", None))
        self.action380mm.setText(QCoreApplication.translate("MainWindow", u"380 mm", None))
        self.actionMindestverrechnung.setText(QCoreApplication.translate("MainWindow", u"Mindestverrechnung", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Bahnsteigberechnung 550 mm", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Bahnsteigberechnung 380 mm", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Mindestverrechnung", None))
    # retranslateUi


##########################################


# Klasse für das Bahnsteigberechnungsfenster (550 mm)
class MainWindow_bahnsteig(QMainWindow):
    def __init__(
            self,
            abstand,
            min_abstand,
            max_abstand,
            hoehe,
            min_hoehe,
            max_hoehe,
            parent=None,
    ):
        super(MainWindow_bahnsteig, self).__init__(parent)
        self.ui = Ui_MainWindow_bahnsteig()  # Erzeuge ein UI-Objekt
        self.ui.setupUi(self)  # Initialisiere das UI
        self.ui.gridLayout.setSpacing(20)
        self.abstand = abstand
        self.min_abstand = min_abstand
        self.max_abstand = max_abstand
        self.hoehe = hoehe
        self.min_hoehe = min_hoehe
        self.max_hoehe = max_hoehe

        self.setWindowTitle(f"Bahnsteig mit {hoehe} mm")

        # Stylesheets
        self.backgroundcolor = "#AAABBC"
        self.text_color = "#373F47"
        self.button_color = "#8B8982"
        # Hintergrundfarbe festlegen
        self.setStyleSheet(f"background-color:{self.backgroundcolor};")
        self.ui.input_abstand.setStyleSheet(
            f"background-color:{self.text_color};" "color:white;"
        )
        self.ui.input_hoehe.setStyleSheet(
            f"background-color:{self.text_color};" "color:white;"
        )
        self.ui.button_abstand.setStyleSheet(f"background-color:{self.button_color};")
        self.ui.button_hoehe.setStyleSheet(f"background-color:{self.button_color};")

        # Label Sollabstand und Sollhöhe beschriften
        self.ui.label.setText(f"Sollabstand = {abstand} mm")
        self.ui.label_sollhoehe.setText(f"Sollhöhe = {hoehe} mm")
        # ErgebnisText auf Leer setzen
        self.ui.label_ergebnis_abstand.setText("")
        self.ui.label_ergebnis_hoehe.setText("")

        # Widgets reinholen
        self.ui.button_abstand.clicked.connect(self.berechnen_abstand)
        self.ui.button_hoehe.clicked.connect(self.berechnen_hoehe)
        # Methoden

        # Enter Taste

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter) and self.ui.input_abstand.hasFocus():
            self.berechnen_abstand()
        elif (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter) and self.ui.input_abstand.hasFocus():
            self.berechnen_hoehe()

        # Abstand berechnen

    def berechnen_abstand(self):
        try:
            current_value = int(self.ui.input_abstand.text())
            sollabstand = self.abstand
            min_abstand = self.min_abstand
            max_abstand = self.max_abstand
            ergebnis = current_value - sollabstand
            if current_value > min_abstand and current_value < max_abstand:
                if current_value < sollabstand:
                    self.ui.label_ergebnis_abstand.setText(
                        f"Gleis um {abs(ergebnis)} mm weg vom Bahnsteig")
                    self.ui.input_abstand.clear()
                    self.ui.input_abstand.setFocus()
                elif current_value > sollabstand:
                    self.ui.label_ergebnis_abstand.setText(
                        f"Gleis um {abs(ergebnis)} mm zum Bahnsteig")
                    self.ui.input_abstand.clear()
                    self.ui.input_abstand.setFocus()
                else:
                    self.ui.label_ergebnis_abstand.setText(f"Gleis liegt auf < 0 > ")
                    self.ui.input_abstand.clear()
                    self.ui.input_abstand.setFocus()
            elif current_value < min_abstand or current_value > max_abstand:
                msg = QMessageBox.warning(
                    self,
                    "Achtung",
                    f"Der eingegebene Wert {current_value} ist nicht\ninnerhalb des IHP Regelwerkes!\nMindesabstand: {min_abstand} mm Maximalabstand: {max_abstand} mm",
                )
                self.ui.input_abstand.clear()
                self.ui.input_abstand.setFocus()

        except ValueError:
            print("Error")

    def berechnen_hoehe(self):
        try:
            current_value = int(self.ui.input_hoehe.text())
            sollhoehe = self.hoehe
            min_hoehe = self.min_hoehe
            max_hoehe = self.max_hoehe
            ergebnis = current_value - sollhoehe
            if current_value > min_hoehe and current_value < max_hoehe:
                if current_value < sollhoehe:
                    self.ui.label_ergebnis_hoehe.setText(
                        f"Gleis ist um {abs(ergebnis)} mm zu hoch! ")
                    self.ui.input_hoehe.clear()
                    self.ui.input_hoehe.setFocus()
                elif current_value > sollhoehe:
                    self.ui.label_ergebnis_hoehe.setText(
                        f"Gleis hat {abs(ergebnis)} mm Hebung")
                    self.ui.input_hoehe.clear()
                    self.ui.input_hoehe.setFocus()
                else:
                    self.ui.label_ergebnis_hoehe.setText(f"Gleis liegt auf < 0 > ")
                    self.ui.input_hoehe.clear()
                    self.ui.input_hoehe.setFocus()
            elif current_value < min_hoehe or current_value > max_hoehe:
                msg = QMessageBox.warning(
                    self,
                    "Achtung",
                    f"Der eingegebene Wert {current_value} ist nicht\ninnerhalb des IHP Regelwerkes!\nMindesthöhe: {min_hoehe} mm Maximalhöhe: {max_hoehe} mm",
                )
                self.ui.input_hoehe.clear()
                self.ui.input_hoehe.setFocus()

        except ValueError:
            print("Error")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Initialisiere die UI

        # Hier können Slots mit den Buttons verbunden werden, z. B.:
        self.ui.pushButton.clicked.connect(self.open_window_550)
        self.ui.pushButton_3.clicked.connect(self.open_window_380)
        # self.ui.pushButton_2.clicked.connect(self.mindestverrechnung)

    def open_window_550(self):
        self.window550 = MainWindow_bahnsteig(1665, 1600, 1700, 550, 500, 600, self)
        self.window550.show()

    def open_window_380(self):
        self.window_380 = MainWindow_bahnsteig(1600, 1550, 1650, 380, 350, 400, self)
        self.window_380.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
