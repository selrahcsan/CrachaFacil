# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QTabWidget,
    QWidget)
import rc_ImgsResource

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setWindowModality(Qt.WindowModality.WindowModal)
        Widget.resize(1094, 445)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMaximumSize(QSize(1094, 445))
        font = QFont()
        font.setPointSize(20)
        Widget.setFont(font)
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 1081, 441))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setIconSize(QSize(30, 30))
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.stackedWidget = QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 1011, 441))
        self.menu_funcionarios = QWidget()
        self.menu_funcionarios.setObjectName(u"menu_funcionarios")
        self.groupBox = QGroupBox(self.menu_funcionarios)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 30, 331, 351))
        self.btn_inserir_funcionario = QPushButton(self.groupBox)
        self.btn_inserir_funcionario.setObjectName(u"btn_inserir_funcionario")
        self.btn_inserir_funcionario.setGeometry(QRect(30, 40, 281, 291))
        icon = QIcon()
        icon.addFile(u":/PNG/Imgs/portal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inserir_funcionario.setIcon(icon)
        self.btn_inserir_funcionario.setIconSize(QSize(256, 256))
        self.groupBox_2 = QGroupBox(self.menu_funcionarios)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(340, 30, 331, 351))
        self.btn_importar_exel = QPushButton(self.groupBox_2)
        self.btn_importar_exel.setObjectName(u"btn_importar_exel")
        self.btn_importar_exel.setGeometry(QRect(10, 40, 301, 291))
        icon1 = QIcon()
        icon1.addFile(u":/PNG/Imgs/excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_importar_exel.setIcon(icon1)
        self.btn_importar_exel.setIconSize(QSize(256, 256))
        self.groupBox_3 = QGroupBox(self.menu_funcionarios)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(680, 30, 331, 351))
        self.btn_atualizar = QPushButton(self.groupBox_3)
        self.btn_atualizar.setObjectName(u"btn_atualizar")
        self.btn_atualizar.setGeometry(QRect(10, 40, 311, 291))
        icon2 = QIcon()
        icon2.addFile(u":/PNG/Imgs/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_atualizar.setIcon(icon2)
        self.btn_atualizar.setIconSize(QSize(256, 256))
        self.stackedWidget.addWidget(self.menu_funcionarios)
        self.inserir_usuarios = QWidget()
        self.inserir_usuarios.setObjectName(u"inserir_usuarios")
        self.image_label = QLabel(self.inserir_usuarios)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(690, 90, 181, 231))
        self.image_label.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_label.setMargin(-1)
        self.label_7 = QLabel(self.inserir_usuarios)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(700, 10, 251, 71))
        font1 = QFont()
        font1.setPointSize(48)
        font1.setBold(True)
        self.label_7.setFont(font1)
        self.voltar = QPushButton(self.inserir_usuarios)
        self.voltar.setObjectName(u"voltar")
        self.voltar.setGeometry(QRect(490, 350, 181, 51))
        icon3 = QIcon()
        icon3.addFile(u":/Imgs/Imgs/warning.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.voltar.setIcon(icon3)
        self.voltar.setIconSize(QSize(35, 35))
        self.layoutWidget = QWidget(self.inserir_usuarios)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 90, 661, 247))
        self.formLayout_2 = QFormLayout(self.layoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_nome = QLineEdit(self.layoutWidget)
        self.lineEdit_nome.setObjectName(u"lineEdit_nome")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_nome)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_cargo = QLineEdit(self.layoutWidget)
        self.lineEdit_cargo.setObjectName(u"lineEdit_cargo")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_cargo)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_setor = QLineEdit(self.layoutWidget)
        self.lineEdit_setor.setObjectName(u"lineEdit_setor")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_setor)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_matricula = QLineEdit(self.layoutWidget)
        self.lineEdit_matricula.setObjectName(u"lineEdit_matricula")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_matricula)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.dateEdit_admissao = QDateEdit(self.layoutWidget)
        self.dateEdit_admissao.setObjectName(u"dateEdit_admissao")
        self.dateEdit_admissao.setCalendarPopup(True)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.dateEdit_admissao)

        self.label_6 = QLabel(self.inserir_usuarios)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(870, 0, 141, 131))
        self.label_6.setPixmap(QPixmap(u":/Imgs/Imgs/users.ico"))
        self.label_6.setScaledContents(True)
        self.cadastrar = QPushButton(self.inserir_usuarios)
        self.cadastrar.setObjectName(u"cadastrar")
        self.cadastrar.setGeometry(QRect(690, 350, 181, 51))
        icon4 = QIcon()
        icon4.addFile(u":/Imgs/Imgs/check.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cadastrar.setIcon(icon4)
        self.cadastrar.setIconSize(QSize(35, 35))
        self.stackedWidget.addWidget(self.inserir_usuarios)
        self.atualizar_funcionarios = QWidget()
        self.atualizar_funcionarios.setObjectName(u"atualizar_funcionarios")
        self.image_label_localizar = QLabel(self.atualizar_funcionarios)
        self.image_label_localizar.setObjectName(u"image_label_localizar")
        self.image_label_localizar.setGeometry(QRect(690, 90, 181, 231))
        self.image_label_localizar.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_label_localizar.setMargin(-1)
        self.layoutWidget1 = QWidget(self.atualizar_funcionarios)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 90, 661, 235))
        self.formLayout_4 = QFormLayout(self.layoutWidget1)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.lineEdit_atualizar_matricula = QLineEdit(self.layoutWidget1)
        self.lineEdit_atualizar_matricula.setObjectName(u"lineEdit_atualizar_matricula")
        self.lineEdit_atualizar_matricula.setFocusPolicy(Qt.FocusPolicy.WheelFocus)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_atualizar_matricula)

        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_atualizar_nome = QLineEdit(self.layoutWidget1)
        self.lineEdit_atualizar_nome.setObjectName(u"lineEdit_atualizar_nome")
        self.lineEdit_atualizar_nome.setFrame(False)
        self.lineEdit_atualizar_nome.setReadOnly(True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lineEdit_atualizar_nome)

        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_atualizar_cargo = QLineEdit(self.layoutWidget1)
        self.lineEdit_atualizar_cargo.setObjectName(u"lineEdit_atualizar_cargo")
        self.lineEdit_atualizar_cargo.setFrame(False)
        self.lineEdit_atualizar_cargo.setReadOnly(True)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.lineEdit_atualizar_cargo)

        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_15)

        self.lineEdit_atualizar_setor = QLineEdit(self.layoutWidget1)
        self.lineEdit_atualizar_setor.setObjectName(u"lineEdit_atualizar_setor")
        self.lineEdit_atualizar_setor.setFrame(False)
        self.lineEdit_atualizar_setor.setReadOnly(True)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.lineEdit_atualizar_setor)

        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_17)

        self.dateEdit_atualizar_admissao = QDateEdit(self.layoutWidget1)
        self.dateEdit_atualizar_admissao.setObjectName(u"dateEdit_atualizar_admissao")
        self.dateEdit_atualizar_admissao.setFrame(False)
        self.dateEdit_atualizar_admissao.setReadOnly(True)
        self.dateEdit_atualizar_admissao.setCalendarPopup(True)

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.dateEdit_atualizar_admissao)

        self.layoutWidget2 = QWidget(self.atualizar_funcionarios)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 340, 861, 46))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_retroceder = QPushButton(self.layoutWidget2)
        self.btn_retroceder.setObjectName(u"btn_retroceder")
        icon5 = QIcon()
        icon5.addFile(u":/Imgs/Imgs/move - Copia.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_retroceder.setIcon(icon5)
        self.btn_retroceder.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.btn_retroceder)

        self.btn_avancar = QPushButton(self.layoutWidget2)
        self.btn_avancar.setObjectName(u"btn_avancar")
        icon6 = QIcon()
        icon6.addFile(u":/Imgs/Imgs/move.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_avancar.setIcon(icon6)
        self.btn_avancar.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.btn_avancar)

        self.localizar = QPushButton(self.layoutWidget2)
        self.localizar.setObjectName(u"localizar")
        icon7 = QIcon()
        icon7.addFile(u":/Imgs/Imgs/magnifier.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.localizar.setIcon(icon7)
        self.localizar.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.localizar)

        self.editar_localizar = QPushButton(self.layoutWidget2)
        self.editar_localizar.setObjectName(u"editar_localizar")
        self.editar_localizar.setEnabled(False)
        icon8 = QIcon()
        icon8.addFile(u":/Imgs/Imgs/editor.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editar_localizar.setIcon(icon8)
        self.editar_localizar.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.editar_localizar)

        self.atualizar_localizar = QPushButton(self.layoutWidget2)
        self.atualizar_localizar.setObjectName(u"atualizar_localizar")
        self.atualizar_localizar.setEnabled(False)
        self.atualizar_localizar.setIcon(icon2)
        self.atualizar_localizar.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.atualizar_localizar)

        self.voltar_localizar_menu_inicial = QPushButton(self.layoutWidget2)
        self.voltar_localizar_menu_inicial.setObjectName(u"voltar_localizar_menu_inicial")
        self.voltar_localizar_menu_inicial.setIcon(icon3)
        self.voltar_localizar_menu_inicial.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.voltar_localizar_menu_inicial)

        self.label_8 = QLabel(self.atualizar_funcionarios)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(870, 0, 141, 131))
        self.label_8.setPixmap(QPixmap(u":/Imgs/Imgs/users.ico"))
        self.label_8.setScaledContents(True)
        self.label_9 = QLabel(self.atualizar_funcionarios)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(570, 10, 311, 71))
        self.label_9.setFont(font1)
        self.stackedWidget.addWidget(self.atualizar_funcionarios)
        icon9 = QIcon()
        icon9.addFile(u":/Imgs/Imgs/users.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab_2, icon9, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox_6 = QGroupBox(self.tab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 40, 331, 351))
        self.btn_criar_banco_sqlite = QPushButton(self.groupBox_6)
        self.btn_criar_banco_sqlite.setObjectName(u"btn_criar_banco_sqlite")
        self.btn_criar_banco_sqlite.setGeometry(QRect(30, 40, 281, 291))
        icon10 = QIcon()
        icon10.addFile(u":/PNG/Imgs/bancoDeDados.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_criar_banco_sqlite.setIcon(icon10)
        self.btn_criar_banco_sqlite.setIconSize(QSize(256, 256))
        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(350, 40, 331, 351))
        self.deletar_banco = QPushButton(self.groupBox_5)
        self.deletar_banco.setObjectName(u"deletar_banco")
        self.deletar_banco.setGeometry(QRect(20, 40, 291, 291))
        icon11 = QIcon()
        icon11.addFile(u":/PNG/Imgs/bancoDeDados_deletar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deletar_banco.setIcon(icon11)
        self.deletar_banco.setIconSize(QSize(256, 256))
        icon12 = QIcon()
        icon12.addFile(u":/Imgs/Imgs/settings.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab, icon12, "")

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Inserir", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Importar", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"Atualizar", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Inserir", None))
        self.voltar.setText(QCoreApplication.translate("Widget", u"Voltar", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Nome :", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Cargo :", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Setor :  ", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Matr\u00edcula :", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Admiss\u00e3o :", None))
        self.label_6.setText("")
        self.cadastrar.setText(QCoreApplication.translate("Widget", u"Cadastrar", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"Matr\u00edcula :", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"Nome :", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"Cargo :", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"Setor :  ", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"Admiss\u00e3o :", None))
        self.localizar.setText(QCoreApplication.translate("Widget", u"Localizar", None))
        self.editar_localizar.setText(QCoreApplication.translate("Widget", u"Editar", None))
        self.atualizar_localizar.setText(QCoreApplication.translate("Widget", u"Atualizar", None))
        self.voltar_localizar_menu_inicial.setText(QCoreApplication.translate("Widget", u"Voltar", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("Widget", u"Atualizar :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Funcion\u00e1rios", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Widget", u"Criar Banco", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Widget", u"Deletar Banco", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Configura\u00e7\u00f5es", None))
    # retranslateUi

