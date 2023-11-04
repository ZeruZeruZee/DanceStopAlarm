# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateAlarm.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QFrame,
    QGroupBox, QHBoxLayout, QLayout, QLineEdit,
    QSizePolicy, QSlider, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(321, 354)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(321, 354))
        Dialog.setMaximumSize(QSize(321, 500))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(16777215, 51))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 3, -1, -1)
        self.lineEdit = QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_5.addWidget(self.lineEdit)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMaximumSize(QSize(16777215, 51))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(9, 3, -1, 9)
        self.timeEdit = QTimeEdit(self.groupBox)
        self.timeEdit.setObjectName(u"timeEdit")

        self.verticalLayout_2.addWidget(self.timeEdit)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 51))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 3, -1, -1)
        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_3.addWidget(self.comboBox)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_5 = QGroupBox(Dialog)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.groupBox_5.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(9, 3, -1, 9)
        self.horizontalSlider = QSlider(self.groupBox_5)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setAcceptDrops(False)
        self.horizontalSlider.setInputMethodHints(Qt.ImhNone)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(10)

        self.horizontalLayout_2.addWidget(self.horizontalSlider)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setBaseSize(QSize(0, 50))
        self.doubleSpinBox.setMaximum(100.000000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(16777215, 78))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 3, -1, -1)
        self.isLoop = QCheckBox(self.groupBox_3)
        self.isLoop.setObjectName(u"isLoop")

        self.verticalLayout_4.addWidget(self.isLoop)

        self.frame = QFrame(self.groupBox_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_1 = QCheckBox(self.frame)
        self.checkBox_1.setObjectName(u"checkBox_1")

        self.horizontalLayout.addWidget(self.checkBox_1)

        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.frame)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.frame)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.frame)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.frame)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.horizontalLayout.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.frame)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.horizontalLayout.addWidget(self.checkBox_7)


        self.verticalLayout_4.addWidget(self.frame)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"\u540d\u524d", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"\u65b0\u898f\u30a2\u30e9\u30fc\u30e0", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u6642\u9593", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u97f3\u697d", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"\u30af\u30ea\u30a2\u6761\u4ef6", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u7e70\u308a\u8fd4\u3057", None))
        self.isLoop.setText(QCoreApplication.translate("Dialog", u"\u7e70\u308a\u8fd4\u3059", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"\u6708", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"\u706b", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"\u6c34", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"\u6728", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"\u91d1", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"\u571f", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"\u65e5", None))
    # retranslateUi

