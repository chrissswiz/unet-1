# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1589, 639)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("QLabel\n"
"{\n"
"background-color: rgb(221, 221, 221);\n"
"\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ToolButton_2 = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolButton_2.sizePolicy().hasHeightForWidth())
        self.ToolButton_2.setSizePolicy(sizePolicy)
        self.ToolButton_2.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("加载图片.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolButton_2.setIcon(icon)
        self.ToolButton_2.setIconSize(QtCore.QSize(35, 35))
        self.ToolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ToolButton_2.setAutoRaise(True)
        self.ToolButton_2.setObjectName("ToolButton_2")
        self.horizontalLayout_3.addWidget(self.ToolButton_2)
        self.ToolButton_10 = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolButton_10.sizePolicy().hasHeightForWidth())
        self.ToolButton_10.setSizePolicy(sizePolicy)
        self.ToolButton_10.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("读取历史.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolButton_10.setIcon(icon1)
        self.ToolButton_10.setIconSize(QtCore.QSize(35, 35))
        self.ToolButton_10.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ToolButton_10.setAutoRaise(True)
        self.ToolButton_10.setObjectName("ToolButton_10")
        self.horizontalLayout_3.addWidget(self.ToolButton_10)
        self.ToolButton_11 = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolButton_11.sizePolicy().hasHeightForWidth())
        self.ToolButton_11.setSizePolicy(sizePolicy)
        self.ToolButton_11.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("大图识别.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolButton_11.setIcon(icon2)
        self.ToolButton_11.setIconSize(QtCore.QSize(35, 35))
        self.ToolButton_11.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ToolButton_11.setAutoRaise(True)
        self.ToolButton_11.setObjectName("ToolButton_11")
        self.horizontalLayout_3.addWidget(self.ToolButton_11)
        self.ToolButton_13 = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolButton_13.sizePolicy().hasHeightForWidth())
        self.ToolButton_13.setSizePolicy(sizePolicy)
        self.ToolButton_13.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("矩形增加.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolButton_13.setIcon(icon3)
        self.ToolButton_13.setIconSize(QtCore.QSize(35, 35))
        self.ToolButton_13.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ToolButton_13.setAutoRaise(True)
        self.ToolButton_13.setObjectName("ToolButton_13")
        self.horizontalLayout_3.addWidget(self.ToolButton_13)
        self.ToolButton_12 = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolButton_12.sizePolicy().hasHeightForWidth())
        self.ToolButton_12.setSizePolicy(sizePolicy)
        self.ToolButton_12.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("手动添加.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolButton_12.setIcon(icon4)
        self.ToolButton_12.setIconSize(QtCore.QSize(35, 35))
        self.ToolButton_12.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ToolButton_12.setAutoRaise(True)
        self.ToolButton_12.setObjectName("ToolButton_12")
        self.horizontalLayout_3.addWidget(self.ToolButton_12)
        self.ToolButton_14 = QtWidgets.QToolButton(Form)
        self.ToolButton_14.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolButton_14.sizePolicy().hasHeightForWidth())
        self.ToolButton_14.setSizePolicy(sizePolicy)
        self.ToolButton_14.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("矩形删除.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolButton_14.setIcon(icon5)
        self.ToolButton_14.setIconSize(QtCore.QSize(35, 35))
        self.ToolButton_14.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ToolButton_14.setAutoRaise(True)
        self.ToolButton_14.setObjectName("ToolButton_14")
        self.horizontalLayout_3.addWidget(self.ToolButton_14)
        self.ToolButton_15 = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolButton_15.sizePolicy().hasHeightForWidth())
        self.ToolButton_15.setSizePolicy(sizePolicy)
        self.ToolButton_15.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("手动删除.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolButton_15.setIcon(icon6)
        self.ToolButton_15.setIconSize(QtCore.QSize(35, 35))
        self.ToolButton_15.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ToolButton_15.setAutoRaise(True)
        self.ToolButton_15.setObjectName("ToolButton_15")
        self.horizontalLayout_3.addWidget(self.ToolButton_15)
        self.ToolButton = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolButton.sizePolicy().hasHeightForWidth())
        self.ToolButton.setSizePolicy(sizePolicy)
        self.ToolButton.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("区域生长.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolButton.setIcon(icon7)
        self.ToolButton.setIconSize(QtCore.QSize(35, 35))
        self.ToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ToolButton.setAutoRaise(True)
        self.ToolButton.setObjectName("ToolButton")
        self.horizontalLayout_3.addWidget(self.ToolButton)
        self.toolButton_2 = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("水滴.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon8)
        self.toolButton_2.setIconSize(QtCore.QSize(37, 37))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_3.addWidget(self.toolButton_2)
        self.toolButton_3 = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        self.toolButton_3.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("矩形分区.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon9)
        self.toolButton_3.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_3.addWidget(self.toolButton_3)
        self.ToolButton_6 = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolButton_6.sizePolicy().hasHeightForWidth())
        self.ToolButton_6.setSizePolicy(sizePolicy)
        self.ToolButton_6.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("撤销操作.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolButton_6.setIcon(icon10)
        self.ToolButton_6.setIconSize(QtCore.QSize(35, 35))
        self.ToolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ToolButton_6.setAutoRaise(True)
        self.ToolButton_6.setObjectName("ToolButton_6")
        self.horizontalLayout_3.addWidget(self.ToolButton_6)
        self.ToolButton_5 = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolButton_5.sizePolicy().hasHeightForWidth())
        self.ToolButton_5.setSizePolicy(sizePolicy)
        self.ToolButton_5.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("数据保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolButton_5.setIcon(icon11)
        self.ToolButton_5.setIconSize(QtCore.QSize(35, 35))
        self.ToolButton_5.setShortcut("")
        self.ToolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ToolButton_5.setAutoRaise(True)
        self.ToolButton_5.setObjectName("ToolButton_5")
        self.horizontalLayout_3.addWidget(self.ToolButton_5)
        self.toolButton_4 = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy)
        self.toolButton_4.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("掩模保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon12)
        self.toolButton_4.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout_3.addWidget(self.toolButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.SimpleCardWidget = SimpleCardWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SimpleCardWidget.sizePolicy().hasHeightForWidth())
        self.SimpleCardWidget.setSizePolicy(sizePolicy)
        self.SimpleCardWidget.setObjectName("SimpleCardWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.SimpleCardWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.BodyLabel_2 = BodyLabel(self.SimpleCardWidget)
        self.BodyLabel_2.setText("")
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.verticalLayout_2.addWidget(self.BodyLabel_2)
        self.horizontalLayout.addWidget(self.SimpleCardWidget)
        spacerItem1 = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.SimpleCardWidget_2 = SimpleCardWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SimpleCardWidget_2.sizePolicy().hasHeightForWidth())
        self.SimpleCardWidget_2.setSizePolicy(sizePolicy)
        self.SimpleCardWidget_2.setStyleSheet("QLabel\n"
"{\n"
"background-color: rgb(220, 220, 220);\n"
"\n"
"}\n"
"")
        self.SimpleCardWidget_2.setObjectName("SimpleCardWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.SimpleCardWidget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.BodyLabel = BodyLabel(self.SimpleCardWidget_2)
        self.BodyLabel.setText("")
        self.BodyLabel.setObjectName("BodyLabel")
        self.verticalLayout_3.addWidget(self.BodyLabel)
        self.horizontalLayout.addWidget(self.SimpleCardWidget_2)
        spacerItem2 = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame)
        self.SimpleCardWidget_3 = SimpleCardWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.SimpleCardWidget_3.sizePolicy().hasHeightForWidth())
        self.SimpleCardWidget_3.setSizePolicy(sizePolicy)
        self.SimpleCardWidget_3.setObjectName("SimpleCardWidget_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.SimpleCardWidget_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalFrame = QtWidgets.QFrame(self.SimpleCardWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridFrame = QtWidgets.QFrame(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy)
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BodyLabel_6 = BodyLabel(self.gridFrame)
        self.BodyLabel_6.setText("")
        self.BodyLabel_6.setObjectName("BodyLabel_6")
        self.gridLayout_2.addWidget(self.BodyLabel_6, 0, 1, 1, 1)
        self.BodyLabel_7 = BodyLabel(self.gridFrame)
        self.BodyLabel_7.setText("")
        self.BodyLabel_7.setObjectName("BodyLabel_7")
        self.gridLayout_2.addWidget(self.BodyLabel_7, 1, 1, 1, 1)
        self.BodyLabel_3 = BodyLabel(self.gridFrame)
        self.BodyLabel_3.setText("")
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.gridLayout_2.addWidget(self.BodyLabel_3, 1, 0, 1, 1)
        self.BodyLabel_5 = BodyLabel(self.gridFrame)
        self.BodyLabel_5.setText("")
        self.BodyLabel_5.setObjectName("BodyLabel_5")
        self.gridLayout_2.addWidget(self.BodyLabel_5, 0, 0, 1, 1)
        self.BodyLabel_4 = BodyLabel(self.gridFrame)
        self.BodyLabel_4.setText("")
        self.BodyLabel_4.setObjectName("BodyLabel_4")
        self.gridLayout_2.addWidget(self.BodyLabel_4, 0, 2, 1, 1)
        self.verticalFrame = QtWidgets.QFrame(self.gridFrame)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.toolButton = QtWidgets.QToolButton(self.verticalFrame)
        self.toolButton.setStyleSheet("font: 15pt \"Microsoft YaHei UI\";")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("加号.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon13)
        self.toolButton.setIconSize(QtCore.QSize(40, 40))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout_6.addWidget(self.toolButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.verticalFrame, 1, 2, 1, 1)
        self.horizontalLayout_6.addWidget(self.gridFrame)
        self.verticalFrame1 = QtWidgets.QFrame(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame1.sizePolicy().hasHeightForWidth())
        self.verticalFrame1.setSizePolicy(sizePolicy)
        self.verticalFrame1.setObjectName("verticalFrame1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.BodyLabel_11 = BodyLabel(self.verticalFrame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BodyLabel_11.sizePolicy().hasHeightForWidth())
        self.BodyLabel_11.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.BodyLabel_11.setPalette(palette)
        self.BodyLabel_11.setStyleSheet("\n"
"QLabel\n"
"{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"border-radius: 50px;\n"
"border: 2px solid grey;\n"
"background-color: rgb(62, 144, 162);\n"
"\n"
"}")
        self.BodyLabel_11.setAlignment(QtCore.Qt.AlignCenter)
        self.BodyLabel_11.setObjectName("BodyLabel_11")
        self.verticalLayout_8.addWidget(self.BodyLabel_11)
        self.BodyLabel_10 = BodyLabel(self.verticalFrame1)
        self.BodyLabel_10.setText("")
        self.BodyLabel_10.setObjectName("BodyLabel_10")
        self.verticalLayout_8.addWidget(self.BodyLabel_10)
        self.horizontalLayout_6.addWidget(self.verticalFrame1)
        self.verticalFrame2 = QtWidgets.QFrame(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame2.sizePolicy().hasHeightForWidth())
        self.verticalFrame2.setSizePolicy(sizePolicy)
        self.verticalFrame2.setObjectName("verticalFrame2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalFrame2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.BodyLabel_9 = BodyLabel(self.verticalFrame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BodyLabel_9.sizePolicy().hasHeightForWidth())
        self.BodyLabel_9.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 144, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.BodyLabel_9.setPalette(palette)
        self.BodyLabel_9.setStyleSheet("\n"
"QLabel\n"
"{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"border-radius: 50px;\n"
"border: 2px solid grey;\n"
"background-color: rgb(62, 144, 162);\n"
"\n"
"}")
        self.BodyLabel_9.setAlignment(QtCore.Qt.AlignCenter)
        self.BodyLabel_9.setObjectName("BodyLabel_9")
        self.verticalLayout_7.addWidget(self.BodyLabel_9)
        self.TextEdit = TextEdit(self.verticalFrame2)
        self.TextEdit.setObjectName("TextEdit")
        self.verticalLayout_7.addWidget(self.TextEdit)
        self.PrimaryPushButton = PrimaryPushButton(self.verticalFrame2)
        self.PrimaryPushButton.setObjectName("PrimaryPushButton")
        self.verticalLayout_7.addWidget(self.PrimaryPushButton)
        self.horizontalLayout_6.addWidget(self.verticalFrame2)
        self.horizontalLayout_7.addWidget(self.horizontalFrame)
        self.verticalLayout.addWidget(self.SimpleCardWidget_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "中国矿业大学-徐州市第一人民医院智能识别软件"))
        self.ToolButton_2.setText(_translate("Form", "加载图片"))
        self.ToolButton_10.setText(_translate("Form", "读取历史"))
        self.ToolButton_11.setText(_translate("Form", "大图识别"))
        self.ToolButton_13.setText(_translate("Form", "矩形增加"))
        self.ToolButton_12.setText(_translate("Form", "手动添加"))
        self.ToolButton_14.setText(_translate("Form", "矩形删除"))
        self.ToolButton_15.setText(_translate("Form", "手动删除"))
        self.ToolButton.setText(_translate("Form", "区域生长"))
        self.toolButton_2.setText(_translate("Form", "眼底分区"))
        self.toolButton_3.setText(_translate("Form", "矩形占比"))
        self.ToolButton_6.setText(_translate("Form", "撤销操作"))
        self.ToolButton_5.setText(_translate("Form", "数据保存"))
        self.toolButton_4.setText(_translate("Form", "掩模保存"))
        self.toolButton.setText(_translate("Form", "添加影像"))
        self.BodyLabel_11.setText(_translate("Form", "用户信息"))
        self.BodyLabel_9.setText(_translate("Form", "分析结果"))
        self.PrimaryPushButton.setText(_translate("Form", "生成报告"))
from qfluentwidgets import BodyLabel, PrimaryPushButton, SimpleCardWidget, TextEdit

if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets
#     from your_ui_file import Ui_Form  # 导入您的UI文件的类

    app = QtWidgets.QApplication(sys.argv)

    # 设置软件图标
    app.setWindowIcon(QtGui.QIcon("1111.png"))  # 将 "path_to_icon.ico" 替换为图标文件的路径

    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

