# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SARTopoKMLConverter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *



class Ui_SARTopoKMLConverter(object):
    def setupUi(self, SARTopoKMLConverter):
        if not SARTopoKMLConverter.objectName():
            SARTopoKMLConverter.setObjectName(u"SARTopoKMLConverter")
        SARTopoKMLConverter.resize(948, 436)
        self.centralwidget = QWidget(SARTopoKMLConverter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(44, 22, 45, 42)
        self.vlHeader = QWidget(self.centralwidget)
        self.vlHeader.setObjectName(u"vlHeader")
        self.headerLayout = QVBoxLayout(self.vlHeader)
        self.headerLayout.setSpacing(4)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(0, 0, 0, 0)
        self.lblTitle = QLabel(self.vlHeader)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setMinimumSize(QSize(0, 17))
        self.lblTitle.setMaximumSize(QSize(183, 17))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lblTitle.setPalette(palette)
        font = QFont()
        font.setPointSize(13)
        self.lblTitle.setFont(font)

        self.headerLayout.addWidget(self.lblTitle)

        self.hlHeader2_2 = QWidget(self.vlHeader)
        self.hlHeader2_2.setObjectName(u"hlHeader2_2")
        self.hlHeader2 = QHBoxLayout(self.hlHeader2_2)
        self.hlHeader2.setSpacing(631)
        self.hlHeader2.setObjectName(u"hlHeader2")
        self.hlHeader2.setContentsMargins(0, 0, 0, 0)
        self.lblLogo = QLabel(self.hlHeader2_2)
        self.lblLogo.setObjectName(u"lblLogo")
        self.lblLogo.setEnabled(True)
        self.lblLogo.setMinimumSize(QSize(190, 32))
        self.lblLogo.setMaximumSize(QSize(190, 32))
        self.lblLogo.setPixmap(QPixmap(u"assets/g2/usr.png"))
        self.lblLogo.setScaledContents(True)

        self.hlHeader2.addWidget(self.lblLogo)

        self.btnClose = QPushButton(self.hlHeader2_2)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(38, 38))
        self.btnClose.setMaximumSize(QSize(38, 38))
        icon = QIcon()
        icon.addFile(u"assets/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClose.setIcon(icon)
        self.btnClose.setIconSize(QSize(15, 15))

        self.hlHeader2.addWidget(self.btnClose)


        self.headerLayout.addWidget(self.hlHeader2_2)


        self.verticalLayout_3.addWidget(self.vlHeader)

        self.vlMain = QWidget(self.centralwidget)
        self.vlMain.setObjectName(u"vlMain")
        self.mainLayout = QVBoxLayout(self.vlMain)
        self.mainLayout.setSpacing(20)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 33, 0, 0)
        self.hlSource_2 = QWidget(self.vlMain)
        self.hlSource_2.setObjectName(u"hlSource_2")
        self.hlSource = QHBoxLayout(self.hlSource_2)
        self.hlSource.setSpacing(20)
        self.hlSource.setObjectName(u"hlSource")
        self.hlSource.setContentsMargins(0, 0, 0, 0)
        self.lblSource = QLabel(self.hlSource_2)
        self.lblSource.setObjectName(u"lblSource")
        self.lblSource.setMinimumSize(QSize(138, 0))
        self.lblSource.setMaximumSize(QSize(138, 16777215))
        self.lblSource.setLineWidth(1)

        self.hlSource.addWidget(self.lblSource)

        self.txtSource = QLineEdit(self.hlSource_2)
        self.txtSource.setObjectName(u"txtSource")
        self.txtSource.setMinimumSize(QSize(635, 46))
        self.txtSource.setMaximumSize(QSize(635, 46))

        self.hlSource.addWidget(self.txtSource)

        self.btnChooseSource = QPushButton(self.hlSource_2)
        self.btnChooseSource.setObjectName(u"btnChooseSource")
        self.btnChooseSource.setMinimumSize(QSize(46, 46))
        self.btnChooseSource.setMaximumSize(QSize(46, 46))
        icon1 = QIcon()
        icon1.addFile(u"assets/folder2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnChooseSource.setIcon(icon1)
        self.btnChooseSource.setIconSize(QSize(15, 15))

        self.hlSource.addWidget(self.btnChooseSource)


        self.mainLayout.addWidget(self.hlSource_2)

        self.hlOutput_2 = QWidget(self.vlMain)
        self.hlOutput_2.setObjectName(u"hlOutput_2")
        self.hlOutput = QHBoxLayout(self.hlOutput_2)
        self.hlOutput.setSpacing(20)
        self.hlOutput.setObjectName(u"hlOutput")
        self.hlOutput.setContentsMargins(0, 0, 0, 0)
        self.lblOutput = QLabel(self.hlOutput_2)
        self.lblOutput.setObjectName(u"lblOutput")
        self.lblOutput.setMinimumSize(QSize(138, 0))
        self.lblOutput.setMaximumSize(QSize(138, 16777215))

        self.hlOutput.addWidget(self.lblOutput)

        self.txtOutputFile = QLineEdit(self.hlOutput_2)
        self.txtOutputFile.setObjectName(u"txtOutputFile")
        self.txtOutputFile.setMinimumSize(QSize(635, 46))
        self.txtOutputFile.setMaximumSize(QSize(635, 46))

        self.hlOutput.addWidget(self.txtOutputFile)

        self.btnChooseOutput = QPushButton(self.hlOutput_2)
        self.btnChooseOutput.setObjectName(u"btnChooseOutput")
        self.btnChooseOutput.setMinimumSize(QSize(46, 46))
        self.btnChooseOutput.setMaximumSize(QSize(46, 46))
        self.btnChooseOutput.setIcon(icon1)
        self.btnChooseOutput.setIconSize(QSize(15, 15))

        self.hlOutput.addWidget(self.btnChooseOutput)


        self.mainLayout.addWidget(self.hlOutput_2)

        self.hlOutputOptions = QWidget(self.vlMain)
        self.hlOutputOptions.setObjectName(u"hlOutputOptions")
        self.hlOptions = QHBoxLayout(self.hlOutputOptions)
        self.hlOptions.setSpacing(20)
        self.hlOptions.setObjectName(u"hlOptions")
        self.hlOptions.setContentsMargins(0, 0, 0, 0)
        self.lblOutputoption = QLabel(self.hlOutputOptions)
        self.lblOutputoption.setObjectName(u"lblOutputoption")
        self.lblOutputoption.setMinimumSize(QSize(138, 0))
        self.lblOutputoption.setMaximumSize(QSize(138, 16777215))

        self.hlOptions.addWidget(self.lblOutputoption)

        self.hlOptions_2 = QWidget(self.hlOutputOptions)
        self.hlOptions_2.setObjectName(u"hlOptions_2")
        self.horizontalLayout_12 = QHBoxLayout(self.hlOptions_2)
        self.horizontalLayout_12.setSpacing(15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btnDJI = QCheckBox(self.hlOptions_2)
        self.btnDJI.setObjectName(u"btnDJI")
        self.btnDJI.setMinimumSize(QSize(84, 36))
        self.btnDJI.setMaximumSize(QSize(84, 36))

        self.horizontalLayout_12.addWidget(self.btnDJI)

        self.btnKMZ = QCheckBox(self.hlOptions_2)
        self.btnKMZ.setObjectName(u"btnKMZ")
        self.btnKMZ.setMinimumSize(QSize(84, 36))
        self.btnKMZ.setMaximumSize(QSize(84, 36))

        self.horizontalLayout_12.addWidget(self.btnKMZ)

        self.btnGPX = QCheckBox(self.hlOptions_2)
        self.btnGPX.setObjectName(u"btnGPX")
        self.btnGPX.setMinimumSize(QSize(84, 36))
        self.btnGPX.setMaximumSize(QSize(84, 36))

        self.horizontalLayout_12.addWidget(self.btnGPX)

        self.btnJSON = QCheckBox(self.hlOptions_2)
        self.btnJSON.setObjectName(u"btnJSON")
        self.btnJSON.setMinimumSize(QSize(84, 36))
        self.btnJSON.setMaximumSize(QSize(84, 36))

        self.horizontalLayout_12.addWidget(self.btnJSON)

        self.optionSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.optionSpacer)


        self.hlOptions.addWidget(self.hlOptions_2)


        self.mainLayout.addWidget(self.hlOutputOptions)

        self.hlProgress_2 = QWidget(self.vlMain)
        self.hlProgress_2.setObjectName(u"hlProgress_2")
        self.hlProgress = QHBoxLayout(self.hlProgress_2)
        self.hlProgress.setObjectName(u"hlProgress")
        self.hlProgress.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.hlProgress_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 23))
        self.progressBar.setMaximumSize(QSize(16777215, 23))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)

        self.hlProgress.addWidget(self.progressBar)


        self.mainLayout.addWidget(self.hlProgress_2)

        self.hlFooter_2 = QWidget(self.vlMain)
        self.hlFooter_2.setObjectName(u"hlFooter_2")
        self.hlFooter = QHBoxLayout(self.hlFooter_2)
        self.hlFooter.setSpacing(0)
        self.hlFooter.setObjectName(u"hlFooter")
        self.hlFooter.setContentsMargins(0, 0, 0, 0)
        self.vlVersion = QWidget(self.hlFooter_2)
        self.vlVersion.setObjectName(u"vlVersion")
        self.verticalLayout = QVBoxLayout(self.vlVersion)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.vlVersion)
        self.label.setObjectName(u"label")
        font1 = QFont()
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font-size:14px; \n"
"color: #676767; \n"
"text-align: bottom left;")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label)


        self.hlFooter.addWidget(self.vlVersion)

        self.btnStart = QPushButton(self.hlFooter_2)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setMinimumSize(QSize(146, 45))
        self.btnStart.setMaximumSize(QSize(146, 45))

        self.hlFooter.addWidget(self.btnStart)

        self.vlLink = QWidget(self.hlFooter_2)
        self.vlLink.setObjectName(u"vlLink")
        self.verticalLayout_2 = QVBoxLayout(self.vlLink)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.hlLink = QWidget(self.vlLink)
        self.hlLink.setObjectName(u"hlLink")
        self.horizontalLayout = QHBoxLayout(self.hlLink)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton = QToolButton(self.hlLink)
        self.toolButton.setObjectName(u"toolButton")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setUnderline(True)
        self.toolButton.setFont(font2)
        self.toolButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton.setMouseTracking(True)
        self.toolButton.setTabletTracking(True)

        self.horizontalLayout.addWidget(self.toolButton)


        self.verticalLayout_2.addWidget(self.hlLink)


        self.hlFooter.addWidget(self.vlLink)

        self.hlFooter.setStretch(0, 100)
        self.hlFooter.setStretch(1, 40)
        self.hlFooter.setStretch(2, 100)

        self.mainLayout.addWidget(self.hlFooter_2)


        self.verticalLayout_3.addWidget(self.vlMain)

        SARTopoKMLConverter.setCentralWidget(self.centralwidget)

        self.retranslateUi(SARTopoKMLConverter)

        QMetaObject.connectSlotsByName(SARTopoKMLConverter)
    # setupUi

    def retranslateUi(self, SARTopoKMLConverter):
        SARTopoKMLConverter.setWindowTitle(QCoreApplication.translate("SARTopoKMLConverter", u"SARTopoKMLConveter", None))
        self.lblTitle.setText(QCoreApplication.translate("SARTopoKMLConverter", u"SARTopo KML Converter", None))
        self.lblLogo.setText("")
        self.btnClose.setText("")
        self.lblSource.setText(QCoreApplication.translate("SARTopoKMLConverter", u"Source Folder:", None))
        self.btnChooseSource.setText("")
        self.lblOutput.setText(QCoreApplication.translate("SARTopoKMLConverter", u"Output File:", None))
        self.btnChooseOutput.setText("")
        self.lblOutputoption.setText(QCoreApplication.translate("SARTopoKMLConverter", u"Output File:", None))
        self.btnDJI.setText(QCoreApplication.translate("SARTopoKMLConverter", u"DJI", None))
        self.btnKMZ.setText(QCoreApplication.translate("SARTopoKMLConverter", u"KMZ", None))
        self.btnGPX.setText(QCoreApplication.translate("SARTopoKMLConverter", u"GPX", None))
        self.btnJSON.setText(QCoreApplication.translate("SARTopoKMLConverter", u"JSON", None))
        self.progressBar.setFormat(QCoreApplication.translate("SARTopoKMLConverter", u"%p%   ", None))
        self.label.setText(QCoreApplication.translate("SARTopoKMLConverter", u"Ver 1.10", None))
        self.btnStart.setText(QCoreApplication.translate("SARTopoKMLConverter", u"Start", None))
        self.toolButton.setText(QCoreApplication.translate("SARTopoKMLConverter", u"Usri.ca", None))
    # retranslateUi

