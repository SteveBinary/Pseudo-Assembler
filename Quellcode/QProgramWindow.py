# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QCodeEditor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("P.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("Code Editor")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.button_start.setFont(font)
        self.button_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_start.setText("Start")
        self.button_start.setAutoRepeatDelay(100)
        self.button_start.setAutoDefault(False)
        self.button_start.setDefault(False)
        self.button_start.setFlat(False)
        self.button_start.setObjectName("button_start")
        self.horizontalLayout_3.addWidget(self.button_start)
        self.button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_stop.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_stop.setFont(font)
        self.button_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_stop.setObjectName("button_stop")
        self.horizontalLayout_3.addWidget(self.button_stop)
        self.button_weiter = QtWidgets.QPushButton(self.centralwidget)
        self.button_weiter.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_weiter.setFont(font)
        self.button_weiter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_weiter.setText("Weiter")
        self.button_weiter.setAutoRepeat(True)
        self.button_weiter.setAutoRepeatDelay(500)
        self.button_weiter.setAutoRepeatInterval(40)
        self.button_weiter.setObjectName("button_weiter")
        self.horizontalLayout_3.addWidget(self.button_weiter)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Editor = CodeEditor(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Editor.sizePolicy().hasHeightForWidth())
        self.Editor.setSizePolicy(sizePolicy)
        self.Editor.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Editor.setFont(font)
        self.Editor.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.Editor.setPlainText("")
        self.Editor.setTabStopDistance(22.0)
        self.Editor.setObjectName("Editor")
        self.horizontalLayout_5.addWidget(self.Editor)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("Speicherwerk")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.Speicher = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Speicher.sizePolicy().hasHeightForWidth())
        self.Speicher.setSizePolicy(sizePolicy)
        self.Speicher.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.Speicher.setFont(font)
        self.Speicher.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.Speicher.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Speicher.setTabKeyNavigation(False)
        self.Speicher.setProperty("showDropIndicator", False)
        self.Speicher.setDragDropOverwriteMode(False)
        self.Speicher.setAlternatingRowColors(True)
        self.Speicher.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.Speicher.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.Speicher.setRowCount(0)
        self.Speicher.setColumnCount(0)
        self.Speicher.setObjectName("Speicher")
        self.Speicher.horizontalHeader().setCascadingSectionResizes(True)
        self.Speicher.horizontalHeader().setHighlightSections(False)
        self.Speicher.horizontalHeader().setMinimumSectionSize(30)
        self.Speicher.horizontalHeader().setStretchLastSection(False)
        self.Speicher.verticalHeader().setVisible(False)
        self.Speicher.verticalHeader().setCascadingSectionResizes(True)
        self.Speicher.verticalHeader().setHighlightSections(False)
        self.Speicher.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.Speicher)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText("Steuerwerk")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_13.addWidget(self.label_3)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_13.addWidget(self.line_7)
        self.label_which_cycle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_which_cycle.setFont(font)
        self.label_which_cycle.setText("IDLE")
        self.label_which_cycle.setObjectName("label_which_cycle")
        self.horizontalLayout_13.addWidget(self.label_which_cycle)
        self.horizontalLayout_13.setStretch(0, 5)
        self.horizontalLayout_13.setStretch(2, 20)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        spacerItem = QtWidgets.QSpacerItem(254, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setText("Befehlszähler")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setText("Befehlsregister")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setText("Dekodierer")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_befehlszaehler = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_befehlszaehler.setFont(font)
        self.label_befehlszaehler.setText("0")
        self.label_befehlszaehler.setObjectName("label_befehlszaehler")
        self.verticalLayout_4.addWidget(self.label_befehlszaehler)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_befehlsreg_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_befehlsreg_1.setMinimumSize(QtCore.QSize(0, 0))
        self.label_befehlsreg_1.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_befehlsreg_1.setFont(font)
        self.label_befehlsreg_1.setText("0")
        self.label_befehlsreg_1.setObjectName("label_befehlsreg_1")
        self.horizontalLayout_12.addWidget(self.label_befehlsreg_1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_12.addWidget(self.line_5)
        self.label_befehlsreg_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_befehlsreg_2.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_befehlsreg_2.setFont(font)
        self.label_befehlsreg_2.setText("0")
        self.label_befehlsreg_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_befehlsreg_2.setObjectName("label_befehlsreg_2")
        self.horizontalLayout_12.addWidget(self.label_befehlsreg_2)
        self.horizontalLayout_12.setStretch(0, 2)
        self.horizontalLayout_12.setStretch(2, 2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(7)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_dekodierer_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_dekodierer_1.setMinimumSize(QtCore.QSize(0, 0))
        self.label_dekodierer_1.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_dekodierer_1.setFont(font)
        self.label_dekodierer_1.setText("0")
        self.label_dekodierer_1.setWordWrap(True)
        self.label_dekodierer_1.setObjectName("label_dekodierer_1")
        self.horizontalLayout_11.addWidget(self.label_dekodierer_1)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_11.addWidget(self.line_6)
        self.label_dekodierer_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_dekodierer_2.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_dekodierer_2.setFont(font)
        self.label_dekodierer_2.setText("0")
        self.label_dekodierer_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_dekodierer_2.setObjectName("label_dekodierer_2")
        self.horizontalLayout_11.addWidget(self.label_dekodierer_2)
        self.horizontalLayout_11.setStretch(0, 2)
        self.horizontalLayout_11.setStretch(2, 2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 10)
        self.horizontalLayout_8.setStretch(3, 5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.verticalLayout_8.setStretch(0, 10)
        self.verticalLayout_3.addLayout(self.verticalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(254, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText("Rechenwerk")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(254, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setText("Akku")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_9.addWidget(self.label_16)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_9.addWidget(self.line_8)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setText("Operand")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_9.addWidget(self.label_17)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.label_accu = QtWidgets.QLabel(self.centralwidget)
        self.label_accu.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_accu.setFont(font)
        self.label_accu.setText("0")
        self.label_accu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_accu.setWordWrap(True)
        self.label_accu.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_accu.setObjectName("label_accu")
        self.horizontalLayout_6.addWidget(self.label_accu)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.label_operation = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_operation.setFont(font)
        self.label_operation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_operation.setText("")
        self.label_operation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_operation.setObjectName("label_operation")
        self.horizontalLayout_6.addWidget(self.label_operation)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.label_operand = QtWidgets.QLabel(self.centralwidget)
        self.label_operand.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_operand.setFont(font)
        self.label_operand.setScaledContents(False)
        self.label_operand.setAlignment(QtCore.Qt.AlignCenter)
        self.label_operand.setWordWrap(False)
        self.label_operand.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_operand.setObjectName("label_operand")
        self.horizontalLayout_6.addWidget(self.label_operand)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.horizontalLayout_6.setStretch(1, 100)
        self.horizontalLayout_6.setStretch(5, 100)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_6.addWidget(self.line_10)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setText("Ergebnis")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_10.addWidget(self.label_19)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_10.addWidget(self.line_9)
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setText("0")
        self.label_result.setWordWrap(True)
        self.label_result.setObjectName("label_result")
        self.horizontalLayout_10.addWidget(self.label_result)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.verticalLayout_6.setStretch(1, 10)
        self.verticalLayout_6.setStretch(3, 10)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        spacerItem9 = QtWidgets.QSpacerItem(254, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem9)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText("Ein - / Ausgabewerk")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        spacerItem10 = QtWidgets.QSpacerItem(254, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText("Eingaberegister ")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.input_reg = QtWidgets.QLineEdit(self.centralwidget)
        self.input_reg.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_reg.setFont(font)
        self.input_reg.setInputMask("")
        self.input_reg.setText("")
        self.input_reg.setMaxLength(32767)
        self.input_reg.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_reg.setDragEnabled(True)
        self.input_reg.setClearButtonEnabled(False)
        self.input_reg.setObjectName("input_reg")
        self.horizontalLayout_2.addWidget(self.input_reg)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setText("Ausgaberegister")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.output_reg = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_reg.setFont(font)
        self.output_reg.setMaxLength(9999999)
        self.output_reg.setDragEnabled(True)
        self.output_reg.setReadOnly(True)
        self.output_reg.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.output_reg.setClearButtonEnabled(False)
        self.output_reg.setObjectName("output_reg")
        self.horizontalLayout.addWidget(self.output_reg)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem11)
        self.verticalLayout_3.setStretch(16, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(2, 10)
        self.horizontalLayout_4.setStretch(4, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.menuDatei.setFont(font)
        self.menuDatei.setObjectName("menuDatei")
        self.menuDemo = QtWidgets.QMenu(self.menuDatei)
        self.menuDemo.setObjectName("menuDemo")
        self.menuHilfe = QtWidgets.QMenu(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuHilfe.sizePolicy().hasHeightForWidth())
        self.menuHilfe.setSizePolicy(sizePolicy)
        self.menuHilfe.setSeparatorsCollapsible(False)
        self.menuHilfe.setObjectName("menuHilfe")
        self.menuAninmation = QtWidgets.QMenu(self.menubar)
        self.menuAninmation.setObjectName("menuAninmation")
        self.menuVollst_ndig = QtWidgets.QMenu(self.menuAninmation)
        self.menuVollst_ndig.setEnabled(True)
        self.menuVollst_ndig.setObjectName("menuVollst_ndig")
        self.menuOptionen = QtWidgets.QMenu(self.menubar)
        self.menuOptionen.setObjectName("menuOptionen")
        MainWindow.setMenuBar(self.menubar)
        self.actionNeu = QtWidgets.QAction(MainWindow)
        self.actionNeu.setText("Neu")
        self.actionNeu.setObjectName("actionNeu")
        self.action_ffnen = QtWidgets.QAction(MainWindow)
        self.action_ffnen.setText("Öffnen")
        self.action_ffnen.setObjectName("action_ffnen")
        self.actionSpeichernAls = QtWidgets.QAction(MainWindow)
        self.actionSpeichernAls.setText("Speichern unter")
        self.actionSpeichernAls.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionSpeichernAls.setObjectName("actionSpeichernAls")
        self.actionDokumentation = QtWidgets.QAction(MainWindow)
        self.actionDokumentation.setText("Dokumentation")
        self.actionDokumentation.setShortcut("")
        self.actionDokumentation.setShortcutVisibleInContextMenu(False)
        self.actionDokumentation.setObjectName("actionDokumentation")
        self.actionBefehlssatz_ver_ndern = QtWidgets.QAction(MainWindow)
        self.actionBefehlssatz_ver_ndern.setText("Befehlssatz anpassen")
        self.actionBefehlssatz_ver_ndern.setObjectName("actionBefehlssatz_ver_ndern")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setText("Info")
        self.actionInfo.setObjectName("actionInfo")
        self.actionQuersumme = QtWidgets.QAction(MainWindow)
        self.actionQuersumme.setText("Quersumme")
        self.actionQuersumme.setObjectName("actionQuersumme")
        self.actionFakult_t = QtWidgets.QAction(MainWindow)
        self.actionFakult_t.setText("Fakultät")
        self.actionFakult_t.setObjectName("actionFakult_t")
        self.actionSumme_a_bis_b_ohne_Schleife = QtWidgets.QAction(MainWindow)
        self.actionSumme_a_bis_b_ohne_Schleife.setText("Summe a bis b ohne Schleife")
        self.actionSumme_a_bis_b_ohne_Schleife.setObjectName("actionSumme_a_bis_b_ohne_Schleife")
        self.actionSumme_a_bis_b_mit_Schleife = QtWidgets.QAction(MainWindow)
        self.actionSumme_a_bis_b_mit_Schleife.setText("Summe a bis b mit Schleife")
        self.actionSumme_a_bis_b_mit_Schleife.setObjectName("actionSumme_a_bis_b_mit_Schleife")
        self.actionDurchschnitt_dreier_Zahlen_floor = QtWidgets.QAction(MainWindow)
        self.actionDurchschnitt_dreier_Zahlen_floor.setObjectName("actionDurchschnitt_dreier_Zahlen_floor")
        self.action1s = QtWidgets.QAction(MainWindow)
        self.action1s.setCheckable(True)
        self.action1s.setChecked(False)
        self.action1s.setEnabled(True)
        self.action1s.setText("1s")
        self.action1s.setObjectName("action1s")
        self.action2s = QtWidgets.QAction(MainWindow)
        self.action2s.setCheckable(True)
        self.action2s.setText("2s")
        self.action2s.setObjectName("action2s")
        self.action3s = QtWidgets.QAction(MainWindow)
        self.action3s.setCheckable(True)
        self.action3s.setText("3s")
        self.action3s.setObjectName("action3s")
        self.action4s = QtWidgets.QAction(MainWindow)
        self.action4s.setCheckable(True)
        self.action4s.setText("4s")
        self.action4s.setObjectName("action4s")
        self.action5s = QtWidgets.QAction(MainWindow)
        self.action5s.setCheckable(True)
        self.action5s.setText("5s")
        self.action5s.setObjectName("action5s")
        self.action6s = QtWidgets.QAction(MainWindow)
        self.action6s.setCheckable(True)
        self.action6s.setObjectName("action6s")
        self.action7s = QtWidgets.QAction(MainWindow)
        self.action7s.setCheckable(True)
        self.action7s.setObjectName("action7s")
        self.action8s = QtWidgets.QAction(MainWindow)
        self.action8s.setCheckable(True)
        self.action8s.setObjectName("action8s")
        self.action9s = QtWidgets.QAction(MainWindow)
        self.action9s.setCheckable(True)
        self.action9s.setObjectName("action9s")
        self.action10s = QtWidgets.QAction(MainWindow)
        self.action10s.setCheckable(True)
        self.action10s.setText("10s")
        self.action10s.setObjectName("action10s")
        self.actionVNPhasen = QtWidgets.QAction(MainWindow)
        self.actionVNPhasen.setCheckable(True)
        self.actionVNPhasen.setObjectName("actionVNPhasen")
        self.action0s = QtWidgets.QAction(MainWindow)
        self.action0s.setCheckable(True)
        self.action0s.setChecked(True)
        self.action0s.setText("0s")
        self.action0s.setObjectName("action0s")
        self.actionSpeichern_als = QtWidgets.QAction(MainWindow)
        self.actionSpeichern_als.setObjectName("actionSpeichern_als")
        self.actions = QtWidgets.QAction(MainWindow)
        self.actions.setObjectName("actions")
        self.actionZahl_der_angezeigten_Speicherzellen = QtWidgets.QAction(MainWindow)
        self.actionZahl_der_angezeigten_Speicherzellen.setText("Zahl der angezeigten Speicherzellen")
        self.actionZahl_der_angezeigten_Speicherzellen.setObjectName("actionZahl_der_angezeigten_Speicherzellen")
        self.actionSpeichern = QtWidgets.QAction(MainWindow)
        self.actionSpeichern.setText("Speichern")
        self.actionSpeichern.setObjectName("actionSpeichern")
        self.actionDurchschnitt_beliebig_vieler_Zahlen = QtWidgets.QAction(MainWindow)
        self.actionDurchschnitt_beliebig_vieler_Zahlen.setObjectName("actionDurchschnitt_beliebig_vieler_Zahlen")
        self.actionZahl_der_angezeigten_Speicherzellen_2 = QtWidgets.QAction(MainWindow)
        self.actionZahl_der_angezeigten_Speicherzellen_2.setObjectName("actionZahl_der_angezeigten_Speicherzellen_2")
        self.actionBefehlssatz_anpassen = QtWidgets.QAction(MainWindow)
        self.actionBefehlssatz_anpassen.setObjectName("actionBefehlssatz_anpassen")
        self.menuDemo.addAction(self.actionFakult_t)
        self.menuDemo.addAction(self.actionQuersumme)
        self.menuDemo.addAction(self.actionSumme_a_bis_b_mit_Schleife)
        self.menuDemo.addAction(self.actionSumme_a_bis_b_ohne_Schleife)
        self.menuDemo.addAction(self.actionDurchschnitt_dreier_Zahlen_floor)
        self.menuDemo.addAction(self.actionDurchschnitt_beliebig_vieler_Zahlen)
        self.menuDatei.addAction(self.actionNeu)
        self.menuDatei.addAction(self.action_ffnen)
        self.menuDatei.addAction(self.actionSpeichern)
        self.menuDatei.addAction(self.actionSpeichernAls)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.menuDemo.menuAction())
        self.menuHilfe.addAction(self.actionDokumentation)
        self.menuHilfe.addAction(self.actionInfo)
        self.menuVollst_ndig.addAction(self.action0s)
        self.menuVollst_ndig.addAction(self.action1s)
        self.menuVollst_ndig.addAction(self.action2s)
        self.menuVollst_ndig.addAction(self.action3s)
        self.menuVollst_ndig.addAction(self.action4s)
        self.menuVollst_ndig.addAction(self.action5s)
        self.menuVollst_ndig.addAction(self.action10s)
        self.menuAninmation.addAction(self.menuVollst_ndig.menuAction())
        self.menuAninmation.addSeparator()
        self.menuAninmation.addAction(self.actionVNPhasen)
        self.menuOptionen.addAction(self.actionBefehlssatz_anpassen)
        self.menuOptionen.addAction(self.actionZahl_der_angezeigten_Speicherzellen_2)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuAninmation.menuAction())
        self.menubar.addAction(self.menuOptionen.menuAction())
        self.menubar.addAction(self.menuHilfe.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pseudo Assembler"))
        self.button_start.setShortcut(_translate("MainWindow", "Ctrl+Space"))
        self.button_stop.setText(_translate("MainWindow", "Beenden"))
        self.label_operand.setText(_translate("MainWindow", "0"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.menuDemo.setTitle(_translate("MainWindow", "Demo"))
        self.menuHilfe.setTitle(_translate("MainWindow", "Hilfe"))
        self.menuAninmation.setTitle(_translate("MainWindow", "Ablauf"))
        self.menuVollst_ndig.setTitle(_translate("MainWindow", "Vollständig"))
        self.menuOptionen.setTitle(_translate("MainWindow", "Optionen"))
        self.actionNeu.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_ffnen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSpeichernAls.setShortcut(_translate("MainWindow", "Ctrl+Alt+S"))
        self.actionDurchschnitt_dreier_Zahlen_floor.setText(_translate("MainWindow", "Durchschnitt dreier Zahlen"))
        self.action6s.setText(_translate("MainWindow", "6s"))
        self.action7s.setText(_translate("MainWindow", "7s"))
        self.action8s.setText(_translate("MainWindow", "8s"))
        self.action9s.setText(_translate("MainWindow", "9s"))
        self.actionVNPhasen.setText(_translate("MainWindow", "VN-Phasen"))
        self.actionSpeichern_als.setText(_translate("MainWindow", "Speichern als"))
        self.actionSpeichern_als.setShortcut(_translate("MainWindow", "Ctrl+Alt+S"))
        self.actions.setText(_translate("MainWindow", "s"))
        self.actionSpeichern.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionDurchschnitt_beliebig_vieler_Zahlen.setText(_translate("MainWindow", "Durchschnitt beliebig vieler Zahlen"))
        self.actionZahl_der_angezeigten_Speicherzellen_2.setText(_translate("MainWindow", "Zahl der angezeigten Speicherzellen"))
        self.actionBefehlssatz_anpassen.setText(_translate("MainWindow", "Befehlssatz anpassen"))
from codeeditor import CodeEditor


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())