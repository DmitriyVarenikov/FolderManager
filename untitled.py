# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)
import res

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(482, 442)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.widget_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 25))
        self.widget.setMaximumSize(QSize(16777212, 25))
        self.widget.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_back = QPushButton(self.widget)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setMinimumSize(QSize(25, 0))
        self.btn_back.setMaximumSize(QSize(25, 16777215))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_back.setFont(font)

        self.horizontalLayout.addWidget(self.btn_back)

        self.btn_next = QPushButton(self.widget)
        self.btn_next.setObjectName(u"btn_next")
        sizePolicy.setHeightForWidth(self.btn_next.sizePolicy().hasHeightForWidth())
        self.btn_next.setSizePolicy(sizePolicy)
        self.btn_next.setMinimumSize(QSize(25, 0))
        self.btn_next.setMaximumSize(QSize(25, 16777215))
        self.btn_next.setFont(font)

        self.horizontalLayout.addWidget(self.btn_next)

        self.btn_create_folder = QPushButton(self.widget)
        self.btn_create_folder.setObjectName(u"btn_create_folder")
        sizePolicy.setHeightForWidth(self.btn_create_folder.sizePolicy().hasHeightForWidth())
        self.btn_create_folder.setSizePolicy(sizePolicy)
        self.btn_create_folder.setMinimumSize(QSize(25, 0))
        self.btn_create_folder.setMaximumSize(QSize(25, 16777215))
        self.btn_create_folder.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/folder-plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_create_folder.setIcon(icon)
        self.btn_create_folder.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.btn_create_folder)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QSize(25, 0))
        self.pushButton_4.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.treeWidget = QTreeWidget(self.widget_2)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_3.addWidget(self.treeWidget)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout.addWidget(self.widget_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"<", None))
        self.btn_next.setText(QCoreApplication.translate("Form", u">", None))
        self.btn_create_folder.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"dir", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None));
    # retranslateUi

