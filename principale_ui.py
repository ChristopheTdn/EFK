# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principale.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QCommandLinkButton, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QTabWidget, QTextEdit,
    QWidget)
import ressources_rc

class Ui_Fenetre_Principale(object):
    def setupUi(self, Fenetre_Principale):
        if not Fenetre_Principale.objectName():
            Fenetre_Principale.setObjectName(u"Fenetre_Principale")
        Fenetre_Principale.resize(605, 710)
        Fenetre_Principale.setMinimumSize(QSize(605, 710))
        Fenetre_Principale.setMaximumSize(QSize(605, 710))
        Fenetre_Principale.setBaseSize(QSize(605, 760))
        font = QFont()
        font.setPointSize(10)
        Fenetre_Principale.setFont(font)
        icon = QIcon()
        icon.addFile(u":/gfx/gfx/tt.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        Fenetre_Principale.setWindowIcon(icon)
        self.centralWidget = QWidget(Fenetre_Principale)
        self.centralWidget.setObjectName(u"centralWidget")
        self.tabWidget_FenetrePrincipale = QTabWidget(self.centralWidget)
        self.tabWidget_FenetrePrincipale.setObjectName(u"tabWidget_FenetrePrincipale")
        self.tabWidget_FenetrePrincipale.setGeometry(QRect(5, 375, 576, 256))
        self.tabWidget_FenetrePrincipale.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox_ModList = QGroupBox(self.tab)
        self.groupBox_ModList.setObjectName(u"groupBox_ModList")
        self.groupBox_ModList.setGeometry(QRect(15, 10, 551, 81))
        self.label_IconStatus_MODManager = QLabel(self.groupBox_ModList)
        self.label_IconStatus_MODManager.setObjectName(u"label_IconStatus_MODManager")
        self.label_IconStatus_MODManager.setGeometry(QRect(95, 25, 31, 31))
        self.label_IconStatus_MODManager.setText(u"")
        self.label_IconStatus_MODManager.setPixmap(QPixmap(u":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_MODManager.setScaledContents(True)
        self.label = QLabel(self.groupBox_ModList)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 25, 371, 26))
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(15, 95, 551, 91))
        self.label_difficultEASY = QLabel(self.groupBox_2)
        self.label_difficultEASY.setObjectName(u"label_difficultEASY")
        self.label_difficultEASY.setGeometry(QRect(70, 25, 111, 16))
        self.label_difficultSTD = QLabel(self.groupBox_2)
        self.label_difficultSTD.setObjectName(u"label_difficultSTD")
        self.label_difficultSTD.setGeometry(QRect(225, 25, 126, 16))
        self.label_difficultHARD = QLabel(self.groupBox_2)
        self.label_difficultHARD.setObjectName(u"label_difficultHARD")
        self.label_difficultHARD.setGeometry(QRect(400, 25, 121, 16))
        self.label_IconStatus_difficultEASY = QLabel(self.groupBox_2)
        self.label_IconStatus_difficultEASY.setObjectName(u"label_IconStatus_difficultEASY")
        self.label_IconStatus_difficultEASY.setGeometry(QRect(90, 45, 31, 31))
        self.label_IconStatus_difficultEASY.setText(u"")
        self.label_IconStatus_difficultEASY.setPixmap(QPixmap(u":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_difficultEASY.setScaledContents(True)
        self.label_IconStatus_difficultSTD = QLabel(self.groupBox_2)
        self.label_IconStatus_difficultSTD.setObjectName(u"label_IconStatus_difficultSTD")
        self.label_IconStatus_difficultSTD.setGeometry(QRect(260, 45, 31, 31))
        self.label_IconStatus_difficultSTD.setText(u"")
        self.label_IconStatus_difficultSTD.setPixmap(QPixmap(u":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_difficultSTD.setScaledContents(True)
        self.label_IconStatus_difficultHARD = QLabel(self.groupBox_2)
        self.label_IconStatus_difficultHARD.setObjectName(u"label_IconStatus_difficultHARD")
        self.label_IconStatus_difficultHARD.setGeometry(QRect(435, 40, 31, 31))
        self.label_IconStatus_difficultHARD.setText(u"")
        self.label_IconStatus_difficultHARD.setPixmap(QPixmap(u":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_difficultHARD.setScaledContents(True)
        self.tabWidget_FenetrePrincipale.addTab(self.tab, "")
        self.tab_Log = QWidget()
        self.tab_Log.setObjectName(u"tab_Log")
        self.textEdit_Log = QTextEdit(self.tab_Log)
        self.textEdit_Log.setObjectName(u"textEdit_Log")
        self.textEdit_Log.setGeometry(QRect(10, 10, 556, 181))
        self.checkBox_LOGWarn = QCheckBox(self.tab_Log)
        self.checkBox_LOGWarn.setObjectName(u"checkBox_LOGWarn")
        self.checkBox_LOGWarn.setGeometry(QRect(115, 195, 61, 20))
        self.checkBox_LOGDebug = QCheckBox(self.tab_Log)
        self.checkBox_LOGDebug.setObjectName(u"checkBox_LOGDebug")
        self.checkBox_LOGDebug.setGeometry(QRect(255, 195, 61, 20))
        self.checkBox_LOG = QCheckBox(self.tab_Log)
        self.checkBox_LOG.setObjectName(u"checkBox_LOG")
        self.checkBox_LOG.setGeometry(QRect(395, 195, 61, 20))
        self.tabWidget_FenetrePrincipale.addTab(self.tab_Log, "")
        self.tab_Options = QWidget()
        self.tab_Options.setObjectName(u"tab_Options")
        self.groupBox_maj = QGroupBox(self.tab_Options)
        self.groupBox_maj.setObjectName(u"groupBox_maj")
        self.groupBox_maj.setGeometry(QRect(10, 5, 241, 216))
        self.pushButton_MajEFK = QPushButton(self.groupBox_maj)
        self.pushButton_MajEFK.setObjectName(u"pushButton_MajEFK")
        self.pushButton_MajEFK.setEnabled(True)
        self.pushButton_MajEFK.setGeometry(QRect(15, 140, 216, 51))
        font1 = QFont()
        font1.setPointSize(15)
        self.pushButton_MajEFK.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/gfx/gfx/update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_MajEFK.setIcon(icon1)
        self.pushButton_MajEFK.setIconSize(QSize(32, 32))
        self.label_MajEFKLauncherTexte = QLabel(self.groupBox_maj)
        self.label_MajEFKLauncherTexte.setObjectName(u"label_MajEFKLauncherTexte")
        self.label_MajEFKLauncherTexte.setGeometry(QRect(20, 35, 206, 81))
        self.label_noConnexion = QLabel(self.groupBox_maj)
        self.label_noConnexion.setObjectName(u"label_noConnexion")
        self.label_noConnexion.setGeometry(QRect(10, 190, 211, 21))
        self.label_noConnexion.setAlignment(Qt.AlignCenter)
        self.label_UpdateAvailable = QLabel(self.groupBox_maj)
        self.label_UpdateAvailable.setObjectName(u"label_UpdateAvailable")
        self.label_UpdateAvailable.setGeometry(QRect(20, 115, 206, 21))
        self.label_UpdateAvailable.setTextFormat(Qt.RichText)
        self.label_UpdateAvailable.setAlignment(Qt.AlignCenter)
        self.groupBox_UninstallEFK = QGroupBox(self.tab_Options)
        self.groupBox_UninstallEFK.setObjectName(u"groupBox_UninstallEFK")
        self.groupBox_UninstallEFK.setGeometry(QRect(265, 5, 296, 216))
        self.pushButton_UninstallEFK = QPushButton(self.groupBox_UninstallEFK)
        self.pushButton_UninstallEFK.setObjectName(u"pushButton_UninstallEFK")
        self.pushButton_UninstallEFK.setEnabled(True)
        self.pushButton_UninstallEFK.setGeometry(QRect(10, 145, 266, 51))
        font2 = QFont()
        font2.setPointSize(19)
        self.pushButton_UninstallEFK.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/gfx/gfx/skull.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_UninstallEFK.setIcon(icon2)
        self.pushButton_UninstallEFK.setIconSize(QSize(48, 48))
        self.label_UninstallEFK = QLabel(self.groupBox_UninstallEFK)
        self.label_UninstallEFK.setObjectName(u"label_UninstallEFK")
        self.label_UninstallEFK.setGeometry(QRect(15, 25, 266, 116))
        font3 = QFont()
        font3.setPointSize(9)
        self.label_UninstallEFK.setFont(font3)
        self.tabWidget_FenetrePrincipale.addTab(self.tab_Options, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(25, 25, 61, 61))
        self.label_7.setText(u"")
        self.label_7.setPixmap(QPixmap(u":/gfx/gfx/EFK.png"))
        self.label_7.setScaledContents(True)
        self.label_Titre_3 = QLabel(self.tab_2)
        self.label_Titre_3.setObjectName(u"label_Titre_3")
        self.label_Titre_3.setGeometry(QRect(95, 20, 411, 71))
        self.label_Titre_3.setText(u"<html><head/><body><p align=\"justify\"><span style=\" font-size:20pt; font-weight:700;\">ESCAPE FROM KNOX COUNTY<br/>Launcher</span></p></body></html>")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 100, 41, 16))
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 120, 41, 16))
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 140, 71, 16))
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(85, 100, 91, 16))
        self.label_10.setText(u"<html><head/><body><p><span style=\" font-weight:700;\">Tancred Terror</span></p></body></html>")
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(85, 120, 56, 16))
        self.label_11.setText(u"<html><head/><body><p><span style=\" font-weight:700;\">MrGToF</span></p></body></html>")
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(115, 140, 186, 16))
        self.label_12.setText(u"<html><head/><body><p><span style=\" font-weight:700;\">MrGToF </span>(fr,en)<span style=\" font-weight:700;\">, screamff </span>(cn)</p></body></html>")
        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 180, 91, 16))
        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(40, 160, 91, 16))
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(295, 75, 271, 146))
        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(5, 10, 46, 46))
        self.label_17.setText(u"")
        self.label_17.setPixmap(QPixmap(u":/gfx/gfx/point_interrogation.png"))
        self.label_17.setScaledContents(True)
        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 60, 51, 31))
        self.label_18.setText(u"")
        self.label_18.setPixmap(QPixmap(u":/gfx/gfx/pyside.png"))
        self.label_18.setScaledContents(True)
        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(60, 60, 201, 36))
        self.label_19.setText(u"<html><head/><body><p><span style=\" font-size:9pt;\">coded with</span><span style=\" font-size:9pt; font-weight:700;\"> Python 3.11 + Pyside6</span></p></body></html>")
        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(40, 10, 221, 51))
        self.label_20.setText(u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:700;\">EFK Launcher </span><span style=\" font-size:9pt;\">allow you to install<br/>or uninstall the </span><span style=\" font-size:9pt; font-weight:700;\">mod</span><span style=\" font-size:9pt;\"> for </span><span style=\" font-size:9pt; font-weight:700;\">Project<br/>Zomboid  : Escape from Knox County</span></p></body></html>")
        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 110, 46, 26))
        self.label_21.setText(u"")
        self.label_21.setPixmap(QPixmap(u":/gfx/gfx/agplv3.png"))
        self.label_21.setScaledContents(True)
        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(60, 105, 126, 36))
        self.label_22.setText(u"<html><head/><body><p>2023 EFK Launcher<br/><span style=\" font-size:9pt;\">Licence GNU AGPLv3</span></p></body></html>")
        self.label_AboutGithub = QLabel(self.tab_2)
        self.label_AboutGithub.setObjectName(u"label_AboutGithub")
        self.label_AboutGithub.setGeometry(QRect(130, 180, 46, 16))
        self.label_AboutGithub.setText(u"<html><head/><body><p><a href=\"https://github.com/ChristopheTdn/EFK-Launcher\"><span style=\" font-weight:700; text-decoration: underline; color:#0000ff;\">Github</span></a></p></body></html>")
        self.label_AboutGithub.setOpenExternalLinks(True)
        self.label_AboutDiscord = QLabel(self.tab_2)
        self.label_AboutDiscord.setObjectName(u"label_AboutDiscord")
        self.label_AboutDiscord.setGeometry(QRect(95, 155, 76, 26))
        self.label_AboutDiscord.setText(u"<html><head/><body><p><a href=\"https://discord.com/invite/rbd36ERXyu\"><span style=\" font-weight:700; text-decoration: underline; color:#0000ff; vertical-align:top;\">Discord</span></a></p></body></html>")
        self.label_AboutDiscord.setOpenExternalLinks(True)
        self.tabWidget_FenetrePrincipale.addTab(self.tab_2, "")
        self.groupBox_UserDir = QGroupBox(self.centralWidget)
        self.groupBox_UserDir.setObjectName(u"groupBox_UserDir")
        self.groupBox_UserDir.setGeometry(QRect(15, 160, 576, 116))
        self.lineEdit_ProfilPZ = QLineEdit(self.groupBox_UserDir)
        self.lineEdit_ProfilPZ.setObjectName(u"lineEdit_ProfilPZ")
        self.lineEdit_ProfilPZ.setGeometry(QRect(95, 55, 351, 21))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setKerning(True)
        self.lineEdit_ProfilPZ.setFont(font4)
        self.lineEdit_ProfilPZ.setReadOnly(True)
        self.label_IconStatus_RepertoireSaveGame = QLabel(self.groupBox_UserDir)
        self.label_IconStatus_RepertoireSaveGame.setObjectName(u"label_IconStatus_RepertoireSaveGame")
        self.label_IconStatus_RepertoireSaveGame.setGeometry(QRect(455, 75, 31, 31))
        self.label_IconStatus_RepertoireSaveGame.setText(u"")
        self.label_IconStatus_RepertoireSaveGame.setPixmap(QPixmap(u":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_RepertoireSaveGame.setScaledContents(True)
        self.lineEdit_RepertoireSaveGame = QLineEdit(self.groupBox_UserDir)
        self.lineEdit_RepertoireSaveGame.setObjectName(u"lineEdit_RepertoireSaveGame")
        self.lineEdit_RepertoireSaveGame.setGeometry(QRect(95, 80, 351, 21))
        self.lineEdit_RepertoireSaveGame.setFont(font4)
        self.lineEdit_RepertoireSaveGame.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_RepertoireSaveGame.setReadOnly(True)
        self.label_IconStatus_ProfilPZ = QLabel(self.groupBox_UserDir)
        self.label_IconStatus_ProfilPZ.setObjectName(u"label_IconStatus_ProfilPZ")
        self.label_IconStatus_ProfilPZ.setGeometry(QRect(455, 50, 31, 31))
        self.label_IconStatus_ProfilPZ.setText(u"")
        self.label_IconStatus_ProfilPZ.setPixmap(QPixmap(u":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_ProfilPZ.setScaledContents(True)
        self.label_4 = QLabel(self.groupBox_UserDir)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 55, 81, 20))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.groupBox_UserDir)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 80, 81, 20))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_SetRepertoireSaveGame = QPushButton(self.groupBox_UserDir)
        self.pushButton_SetRepertoireSaveGame.setObjectName(u"pushButton_SetRepertoireSaveGame")
        self.pushButton_SetRepertoireSaveGame.setGeometry(QRect(495, 80, 71, 24))
        self.lineEdit_ExePZ = QLineEdit(self.groupBox_UserDir)
        self.lineEdit_ExePZ.setObjectName(u"lineEdit_ExePZ")
        self.lineEdit_ExePZ.setGeometry(QRect(95, 30, 351, 21))
        self.lineEdit_ExePZ.setFont(font4)
        self.lineEdit_ExePZ.setReadOnly(True)
        self.label_IconStatus_ExePZ = QLabel(self.groupBox_UserDir)
        self.label_IconStatus_ExePZ.setObjectName(u"label_IconStatus_ExePZ")
        self.label_IconStatus_ExePZ.setGeometry(QRect(455, 25, 31, 31))
        self.label_IconStatus_ExePZ.setText(u"")
        self.label_IconStatus_ExePZ.setPixmap(QPixmap(u":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_ExePZ.setScaledContents(True)
        self.label_6 = QLabel(self.groupBox_UserDir)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 30, 81, 20))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_SetExePZ = QPushButton(self.groupBox_UserDir)
        self.pushButton_SetExePZ.setObjectName(u"pushButton_SetExePZ")
        self.pushButton_SetExePZ.setGeometry(QRect(495, 30, 71, 24))
        self.label_Titre = QLabel(self.centralWidget)
        self.label_Titre.setObjectName(u"label_Titre")
        self.label_Titre.setGeometry(QRect(105, 10, 241, 71))
        self.label_2 = QLabel(self.centralWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(5, 10, 91, 91))
        self.label_2.setText(u"")
        self.label_2.setPixmap(QPixmap(u":/gfx/gfx/EFK.png"))
        self.label_2.setScaledContents(True)
        self.label_Danger = QLabel(self.centralWidget)
        self.label_Danger.setObjectName(u"label_Danger")
        self.label_Danger.setGeometry(QRect(315, 635, 51, 46))
        self.label_Danger.setText(u"")
        self.label_Danger.setPixmap(QPixmap(u":/gfx/gfx/danger.png"))
        self.label_Danger.setScaledContents(True)
        self.pushButton_WIPE = QPushButton(self.centralWidget)
        self.pushButton_WIPE.setObjectName(u"pushButton_WIPE")
        self.pushButton_WIPE.setGeometry(QRect(85, 635, 166, 51))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.pushButton_WIPE.setFont(font5)
        self.label_Titre_2 = QLabel(self.centralWidget)
        self.label_Titre_2.setObjectName(u"label_Titre_2")
        self.label_Titre_2.setGeometry(QRect(375, 630, 196, 71))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(9)
        font6.setBold(False)
        self.label_Titre_2.setFont(font6)
        self.commandLinkButton_Twitch = QCommandLinkButton(self.centralWidget)
        self.commandLinkButton_Twitch.setObjectName(u"commandLinkButton_Twitch")
        self.commandLinkButton_Twitch.setGeometry(QRect(95, 70, 36, 36))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(9)
        self.commandLinkButton_Twitch.setFont(font7)
        self.commandLinkButton_Twitch.setText(u"")
        icon3 = QIcon()
        icon3.addFile(u":/gfx/gfx/Twitch-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_Twitch.setIcon(icon3)
        self.commandLinkButton_Youtube = QCommandLinkButton(self.centralWidget)
        self.commandLinkButton_Youtube.setObjectName(u"commandLinkButton_Youtube")
        self.commandLinkButton_Youtube.setGeometry(QRect(125, 70, 41, 41))
        self.commandLinkButton_Youtube.setFont(font7)
        self.commandLinkButton_Youtube.setText(u"")
        icon4 = QIcon()
        icon4.addFile(u":/gfx/gfx/youtube.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_Youtube.setIcon(icon4)
        self.commandLinkButton_Youtube.setIconSize(QSize(30, 30))
        self.commandLinkButton_Discord = QCommandLinkButton(self.centralWidget)
        self.commandLinkButton_Discord.setObjectName(u"commandLinkButton_Discord")
        self.commandLinkButton_Discord.setGeometry(QRect(165, 70, 41, 41))
        self.commandLinkButton_Discord.setFont(font7)
        self.commandLinkButton_Discord.setText(u"")
        icon5 = QIcon()
        icon5.addFile(u":/gfx/gfx/discord.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_Discord.setIcon(icon5)
        self.commandLinkButton_Discord.setIconSize(QSize(30, 30))
        self.label_IconStatus_WIPEMAP = QLabel(self.centralWidget)
        self.label_IconStatus_WIPEMAP.setObjectName(u"label_IconStatus_WIPEMAP")
        self.label_IconStatus_WIPEMAP.setGeometry(QRect(25, 635, 51, 46))
        self.label_IconStatus_WIPEMAP.setText(u"")
        self.label_IconStatus_WIPEMAP.setPixmap(QPixmap(u":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_WIPEMAP.setScaledContents(True)
        self.commandLinkButton_STEAM = QCommandLinkButton(self.centralWidget)
        self.commandLinkButton_STEAM.setObjectName(u"commandLinkButton_STEAM")
        self.commandLinkButton_STEAM.setGeometry(QRect(15, 105, 581, 51))
        font8 = QFont()
        font8.setFamilies([u"Ubuntu"])
        font8.setPointSize(13)
        font8.setBold(False)
        font8.setItalic(True)
        font8.setKerning(False)
        self.commandLinkButton_STEAM.setFont(font8)
        icon6 = QIcon()
        icon6.addFile(u":/gfx/gfx/Steam_Icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_STEAM.setIcon(icon6)
        self.commandLinkButton_STEAM.setIconSize(QSize(40, 40))
        self.commandLinkButton_STEAM.setCheckable(False)
        self.pushButton_RunPZ = QPushButton(self.centralWidget)
        self.pushButton_RunPZ.setObjectName(u"pushButton_RunPZ")
        self.pushButton_RunPZ.setGeometry(QRect(445, 20, 141, 46))
        self.pushButton_RunPZ.setFont(font5)
        icon7 = QIcon()
        icon7.addFile(u":/gfx/gfx/pz.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_RunPZ.setIcon(icon7)
        self.pushButton_RunPZ.setIconSize(QSize(35, 35))
        self.checkBox_DebugMode = QCheckBox(self.centralWidget)
        self.checkBox_DebugMode.setObjectName(u"checkBox_DebugMode")
        self.checkBox_DebugMode.setGeometry(QRect(470, 70, 101, 20))
        self.groupBox_EFKEnhanced = QGroupBox(self.centralWidget)
        self.groupBox_EFKEnhanced.setObjectName(u"groupBox_EFKEnhanced")
        self.groupBox_EFKEnhanced.setGeometry(QRect(15, 275, 576, 86))
        self.radioButton_EFKStandard = QRadioButton(self.groupBox_EFKEnhanced)
        self.radioButton_EFKStandard.setObjectName(u"radioButton_EFKStandard")
        self.radioButton_EFKStandard.setGeometry(QRect(115, 40, 216, 20))
        self.radioButton_EFKEnhanced = QRadioButton(self.groupBox_EFKEnhanced)
        self.radioButton_EFKEnhanced.setObjectName(u"radioButton_EFKEnhanced")
        self.radioButton_EFKEnhanced.setGeometry(QRect(115, 20, 216, 20))
        self.radioButton_EFKEnhanced.setChecked(True)
        self.label_CPULogo = QLabel(self.groupBox_EFKEnhanced)
        self.label_CPULogo.setObjectName(u"label_CPULogo")
        self.label_CPULogo.setGeometry(QRect(30, 20, 51, 51))
        self.label_CPULogo.setText(u"")
        self.label_CPULogo.setPixmap(QPixmap(u":/gfx/gfx/performance.png"))
        self.label_CPULogo.setScaledContents(True)
        self.radioButton_EFKNoModif = QRadioButton(self.groupBox_EFKEnhanced)
        self.radioButton_EFKNoModif.setObjectName(u"radioButton_EFKNoModif")
        self.radioButton_EFKNoModif.setGeometry(QRect(115, 60, 216, 20))
        self.label_alert = QLabel(self.groupBox_EFKEnhanced)
        self.label_alert.setObjectName(u"label_alert")
        self.label_alert.setGeometry(QRect(350, 10, 206, 71))
        self.label_alert.setFont(font6)
        self.label_SignAlert = QLabel(self.groupBox_EFKEnhanced)
        self.label_SignAlert.setObjectName(u"label_SignAlert")
        self.label_SignAlert.setGeometry(QRect(325, 25, 21, 51))
        self.label_SignAlert.setPixmap(QPixmap(u":/gfx/gfx/accolade.png"))
        self.label_SignAlert.setScaledContents(True)
        self.label_UpdateAvailable_2 = QLabel(self.centralWidget)
        self.label_UpdateAvailable_2.setObjectName(u"label_UpdateAvailable_2")
        self.label_UpdateAvailable_2.setGeometry(QRect(120, 365, 146, 21))
        self.label_UpdateAvailable_2.setTextFormat(Qt.RichText)
        self.label_UpdateAvailable_2.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.centralWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(350, 5, 81, 96))
        self.radioButton_France = QRadioButton(self.groupBox)
        self.radioButton_France.setObjectName(u"radioButton_France")
        self.radioButton_France.setGeometry(QRect(15, 5, 56, 26))
        self.radioButton_France.setText(u"")
        icon8 = QIcon()
        icon8.addFile(u":/gfx/gfx/france.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_France.setIcon(icon8)
        self.radioButton_France.setIconSize(QSize(32, 32))
        self.radioButton_France.setCheckable(True)
        self.radioButton_France.setChecked(False)
        self.radioButton_English = QRadioButton(self.groupBox)
        self.radioButton_English.setObjectName(u"radioButton_English")
        self.radioButton_English.setGeometry(QRect(15, 35, 56, 26))
        self.radioButton_English.setText(u"")
        icon9 = QIcon()
        icon9.addFile(u":/gfx/gfx/royaumeunis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_English.setIcon(icon9)
        self.radioButton_English.setIconSize(QSize(32, 32))
        self.radioButton_English.setCheckable(True)
        self.radioButton_English.setChecked(False)
        self.radioButton_Chine = QRadioButton(self.groupBox)
        self.radioButton_Chine.setObjectName(u"radioButton_Chine")
        self.radioButton_Chine.setGeometry(QRect(15, 65, 56, 26))
        self.radioButton_Chine.setText(u"")
        icon10 = QIcon()
        icon10.addFile(u":/gfx/gfx/chine.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_Chine.setIcon(icon10)
        self.radioButton_Chine.setIconSize(QSize(32, 32))
        self.radioButton_Chine.setCheckable(True)
        self.radioButton_Chine.setChecked(True)
        self.label_version = QLabel(self.centralWidget)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setEnabled(True)
        self.label_version.setGeometry(QRect(215, 80, 91, 16))
#if QT_CONFIG(tooltip)
        self.label_version.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.label_version.setText(u"v 0.0.0000")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.checkBox_unlock = QCheckBox(self.centralWidget)
        self.checkBox_unlock.setObjectName(u"checkBox_unlock")
        self.checkBox_unlock.setGeometry(QRect(90, 685, 161, 20))
        Fenetre_Principale.setCentralWidget(self.centralWidget)

        self.retranslateUi(Fenetre_Principale)

        self.tabWidget_FenetrePrincipale.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Fenetre_Principale)
    # setupUi

    def retranslateUi(self, Fenetre_Principale):
        Fenetre_Principale.setWindowTitle(QCoreApplication.translate("Fenetre_Principale", u"Escape From Knox County Launcher", None))
#if QT_CONFIG(tooltip)
        self.tabWidget_FenetrePrincipale.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.groupBox_ModList.setTitle(QCoreApplication.translate("Fenetre_Principale", u"MOD Manager", None))
        self.label.setText(QCoreApplication.translate("Fenetre_Principale", u"<html><head/><body><p align=\"center\">Ajout Profil <span style=\" font-weight:700;\">STANDARD</span> et <span style=\" font-weight:700;\">ADVANCED</span> \u00e0 <span style=\" font-weight:700; font-style:italic;\">Lua/saved_modlists.txt</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Fenetre_Principale", u"Pr\u00e9reglage Difficult\u00e9", None))
        self.label_difficultEASY.setText(QCoreApplication.translate("Fenetre_Principale", u"Facile (EFK_Easy)", None))
        self.label_difficultSTD.setText(QCoreApplication.translate("Fenetre_Principale", u"Standard (EFK_STD)", None))
        self.label_difficultHARD.setText(QCoreApplication.translate("Fenetre_Principale", u"Difficile (EFK_Hard)", None))
        self.tabWidget_FenetrePrincipale.setTabText(self.tabWidget_FenetrePrincipale.indexOf(self.tab), QCoreApplication.translate("Fenetre_Principale", u"Installation", None))
        self.checkBox_LOGWarn.setText(QCoreApplication.translate("Fenetre_Principale", u"WARN", None))
        self.checkBox_LOGDebug.setText(QCoreApplication.translate("Fenetre_Principale", u"DEBUG", None))
        self.checkBox_LOG.setText(QCoreApplication.translate("Fenetre_Principale", u"LOG", None))
        self.tabWidget_FenetrePrincipale.setTabText(self.tabWidget_FenetrePrincipale.indexOf(self.tab_Log), QCoreApplication.translate("Fenetre_Principale", u"Log", None))
        self.groupBox_maj.setTitle(QCoreApplication.translate("Fenetre_Principale", u"Mise a Jour EFK Launcher", None))
        self.pushButton_MajEFK.setText(QCoreApplication.translate("Fenetre_Principale", u"Maj EFK Launcher", None))
        self.label_MajEFKLauncherTexte.setText(QCoreApplication.translate("Fenetre_Principale", u"<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">MaJ EFK :</span></p><p>Pour mettre a jour <span style=\" font-weight:700;\">EFK Launcher</span>,<br/>et les scripts de config EFK.<br/></p><p><br/></p></body></html>", None))
        self.label_noConnexion.setText(QCoreApplication.translate("Fenetre_Principale", u"<html><head/><body><p><img src=\":/gfx/gfx/supprimer.png\" width=\"22\"/><span style=\" font-size:12pt; vertical-align:super;\">Serveur MAJ non trouv\u00e9</span></p></body></html>", None))
        self.label_UpdateAvailable.setText(QCoreApplication.translate("Fenetre_Principale", u"<html><head/><body><p><img src=\":/gfx/gfx/danger.png\" width=\"20\"/><span style=\" font-size:14pt; font-weight:700; color:#ff5500; vertical-align:super;\">Mise a jour disponible</span></p></body></html>", None))
        self.groupBox_UninstallEFK.setTitle(QCoreApplication.translate("Fenetre_Principale", u"D\u00e9sinstaller EFK", None))
        self.pushButton_UninstallEFK.setText(QCoreApplication.translate("Fenetre_Principale", u"Desinstaller EFK", None))
        self.label_UninstallEFK.setText(QCoreApplication.translate("Fenetre_Principale", u"<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">Pour desintaller EFK :<br/></span>1 - Quitter Project Zomboid<br/>2 - Se D\u00e9sabonner \u00e0 la <a href=\"https://steamcommunity.com/workshop/filedetails/?id=3048855836\"><span style=\" text-decoration: underline; color:#0000ff;\">collection Steam EFK<br/></span></a>3 - Cliquer sur <span style=\" font-weight:700;\">Desinstaller EFK<br/></span>4 - Une fois le EFK Launcher Ferm\u00e9<br/>Supprimer votre repertoire local du <span style=\" font-weight:700;\">EFK Launcher</span></p><p><span style=\" font-weight:700;\"><br/></span></p></body></html>", None))
        self.tabWidget_FenetrePrincipale.setTabText(self.tabWidget_FenetrePrincipale.indexOf(self.tab_Options), QCoreApplication.translate("Fenetre_Principale", u"Options", None))
        self.label_3.setText(QCoreApplication.translate("Fenetre_Principale", u"Idea : ", None))
        self.label_8.setText(QCoreApplication.translate("Fenetre_Principale", u"Code :", None))
        self.label_9.setText(QCoreApplication.translate("Fenetre_Principale", u"Traduction :", None))
        self.label_13.setText(QCoreApplication.translate("Fenetre_Principale", u"Source Code :", None))
        self.label_15.setText(QCoreApplication.translate("Fenetre_Principale", u"Project : ", None))
        self.groupBox_3.setTitle("")
        self.tabWidget_FenetrePrincipale.setTabText(self.tabWidget_FenetrePrincipale.indexOf(self.tab_2), QCoreApplication.translate("Fenetre_Principale", u"A Propos", None))
        self.groupBox_UserDir.setTitle(QCoreApplication.translate("Fenetre_Principale", u"Repertoires Utilisateur", None))
        self.label_4.setText(QCoreApplication.translate("Fenetre_Principale", u"Profil PZ :", None))
        self.label_5.setText(QCoreApplication.translate("Fenetre_Principale", u"Sauvegardes :", None))
        self.pushButton_SetRepertoireSaveGame.setText(QCoreApplication.translate("Fenetre_Principale", u"choisir", None))
        self.label_6.setText(QCoreApplication.translate("Fenetre_Principale", u"Exe PZ :", None))
        self.pushButton_SetExePZ.setText(QCoreApplication.translate("Fenetre_Principale", u"choisir", None))
        self.label_Titre.setText(QCoreApplication.translate("Fenetre_Principale", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:24pt; font-weight:700;\">ESCAPE FROM<br/>KNOX COUNTY</span></p></body></html>", None))
        self.pushButton_WIPE.setText(QCoreApplication.translate("Fenetre_Principale", u"WIPE MAP", None))
        self.label_Titre_2.setText(QCoreApplication.translate("Fenetre_Principale", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; text-decoration: underline; color:#aa0000;\">IMPORTANT :</span><span style=\" font-weight:700; text-decoration: underline;\"><br/></span><span style=\" font-weight:700;\">- </span>Entre 2 raids<br/>- personnage dans la base<br/>- Quitter PZ ou au Menu principal</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.commandLinkButton_Twitch.setToolTip(QCoreApplication.translate("Fenetre_Principale", u"Chaine Twitch de Tancred terror", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.commandLinkButton_Youtube.setToolTip(QCoreApplication.translate("Fenetre_Principale", u"Chaine YOUTUBE de Tancred terror", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.commandLinkButton_Discord.setToolTip(QCoreApplication.translate("Fenetre_Principale", u"DISCORD de Tancred terror", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.commandLinkButton_STEAM.setToolTip(QCoreApplication.translate("Fenetre_Principale", u"La collection de mods EFKC", None))
#endif // QT_CONFIG(tooltip)
        self.commandLinkButton_STEAM.setText(QCoreApplication.translate("Fenetre_Principale", u"Abonnements \u00e0 la collection STEAM ESCAPE FROM KNOX COUNTY", None))
        self.pushButton_RunPZ.setText(QCoreApplication.translate("Fenetre_Principale", u"RUN PZ", None))
        self.checkBox_DebugMode.setText(QCoreApplication.translate("Fenetre_Principale", u"Mode DEBUG", None))
        self.groupBox_EFKEnhanced.setTitle(QCoreApplication.translate("Fenetre_Principale", u"EFK Performances impact", None))
        self.radioButton_EFKStandard.setText(QCoreApplication.translate("Fenetre_Principale", u"EFK Standard (Low CPU Power)", None))
        self.radioButton_EFKEnhanced.setText(QCoreApplication.translate("Fenetre_Principale", u"EFK Enhanced (High CPU Power)", None))
#if QT_CONFIG(tooltip)
        self.label_CPULogo.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.radioButton_EFKNoModif.setText(QCoreApplication.translate("Fenetre_Principale", u"No Modif (For Modders Only)", None))
        self.label_alert.setText(QCoreApplication.translate("Fenetre_Principale", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; text-decoration: underline; color:#aa0000;\">IMPORTANT :</span><span style=\" font-weight:700; text-decoration: underline;\"><br/></span>If you're not a Modder,<br/>Please make a choice EFK Enhanced<br/>or EFK Standard <span style=\" font-weight:700; text-decoration: underline;\">Before</span> Launch PZ</p></body></html>", None))
        self.label_SignAlert.setText("")
        self.label_UpdateAvailable_2.setText(QCoreApplication.translate("Fenetre_Principale", u"<html><head/><body><p><img src=\":/gfx/gfx/danger.png\" width=\"20\"/><span style=\" font-size:14pt; font-weight:700; color:#ff5500; vertical-align:super;\">Mise a jour disponible</span></p></body></html>", None))
        self.groupBox.setTitle("")
#if QT_CONFIG(tooltip)
        self.radioButton_France.setToolTip(QCoreApplication.translate("Fenetre_Principale", u"French", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.radioButton_English.setToolTip(QCoreApplication.translate("Fenetre_Principale", u"French", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.radioButton_Chine.setToolTip(QCoreApplication.translate("Fenetre_Principale", u"French", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_unlock.setText(QCoreApplication.translate("Fenetre_Principale", u"D\u00e9verrouille Bouton", None))
    # retranslateUi

