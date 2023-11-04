# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Alarm.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
	QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
	def setupUi(self, Form):
		if not Form.objectName():
			Form.setObjectName(u"Form")
		Form.resize(561, 352)
		self.verticalLayout_2 = QVBoxLayout(Form)
		self.verticalLayout_2.setObjectName(u"verticalLayout_2")
		self.verticalLayout = QVBoxLayout()
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.label = QLabel(Form)
		self.label.setObjectName(u"label")
		self.label.setMaximumSize(QSize(16777215, 50))
		font = QFont()
		font.setPointSize(24)
		font.setBold(True)
		font.setHintingPreference(QFont.PreferDefaultHinting)
		self.label.setFont(font)
		self.label.setCursor(QCursor(Qt.ArrowCursor))
		self.label.setMouseTracking(False)
		self.label.setFocusPolicy(Qt.NoFocus)
		self.label.setLayoutDirection(Qt.LeftToRight)
		self.label.setStyleSheet(u"color: red")
		self.label.setAlignment(Qt.AlignCenter)

		self.verticalLayout.addWidget(self.label)

		self.progressBar = QProgressBar(Form)
		self.progressBar.setObjectName(u"progressBar")
		self.progressBar.setStyleSheet(u"QProgressBar {\n"
			"    border: 2px solid grey;\n"
			"    border-radius: 5px;\n"
			"    text-align: center;\n"
			"}\n"
			"\n"
			"QProgressBar::chunk {\n"
			"    background-color: #05B8CC; /* \u30d7\u30ed\u30b0\u30ec\u30b9\u30d0\u30fc\u306e\u8272\u3092\u5909\u66f4 */\n"
			"    width: 10px; /* \u30c1\u30e3\u30f3\u30af\u306e\u5e45\u3092\u5909\u66f4 */\n"
			"}")
		self.progressBar.setValue(24)

		self.verticalLayout.addWidget(self.progressBar)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.frame = QFrame(Form)
		self.frame.setObjectName(u"frame")
		self.frame.setFrameShape(QFrame.StyledPanel)
		self.frame.setFrameShadow(QFrame.Raised)
		self.label_3 = QLabel(self.frame)
		self.label_3.setObjectName(u"label_3")
		self.label_3.setGeometry(QRect(20, 40, 211, 141))
		self.label_3.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));")

		self.horizontalLayout.addWidget(self.frame)

		self.frame_2 = QFrame(Form)
		self.frame_2.setObjectName(u"frame_2")
		self.frame_2.setFrameShape(QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QFrame.Raised)
		self.label_4 = QLabel(self.frame_2)
		self.label_4.setObjectName(u"label_4")
		self.label_4.setGeometry(QRect(30, 40, 211, 141))
		self.label_4.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));")

		self.horizontalLayout.addWidget(self.frame_2)


		self.verticalLayout.addLayout(self.horizontalLayout)


		self.verticalLayout_2.addLayout(self.verticalLayout)


		self.retranslateUi(Form)

		QMetaObject.connectSlotsByName(Form)
		# setupUi

	def retranslateUi(self, Form):
		Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
		self.label.setText(QCoreApplication.translate("Form", u"00:00", None))
		self.label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
		self.label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
		# retranslateUi

