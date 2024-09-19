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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QStackedWidget, QTabWidget, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(592, 325)
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 561, 301))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.stackedWidget = QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 511, 281))
        self.menu_funcionarios = QWidget()
        self.menu_funcionarios.setObjectName(u"menu_funcionarios")
        self.inserir_funcionario = QPushButton(self.menu_funcionarios)
        self.inserir_funcionario.setObjectName(u"inserir_funcionario")
        self.inserir_funcionario.setGeometry(QRect(10, 30, 101, 24))
        self.importar_exel = QPushButton(self.menu_funcionarios)
        self.importar_exel.setObjectName(u"importar_exel")
        self.importar_exel.setGeometry(QRect(10, 70, 101, 24))
        self.atualizar = QPushButton(self.menu_funcionarios)
        self.atualizar.setObjectName(u"atualizar")
        self.atualizar.setGeometry(QRect(10, 110, 101, 24))
        self.stackedWidget.addWidget(self.menu_funcionarios)
        self.inserir_usuarios = QWidget()
        self.inserir_usuarios.setObjectName(u"inserir_usuarios")
        self.image_label = QLabel(self.inserir_usuarios)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(360, 50, 151, 191))
        self.image_label.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_label.setMargin(-1)
        self.label_7 = QLabel(self.inserir_usuarios)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 261, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_7.setFont(font)
        self.cadastrar = QPushButton(self.inserir_usuarios)
        self.cadastrar.setObjectName(u"cadastrar")
        self.cadastrar.setGeometry(QRect(0, 230, 80, 24))
        self.voltar = QPushButton(self.inserir_usuarios)
        self.voltar.setObjectName(u"voltar")
        self.voltar.setGeometry(QRect(90, 230, 80, 24))
        self.layoutWidget = QWidget(self.inserir_usuarios)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 50, 351, 171))
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

        self.stackedWidget.addWidget(self.inserir_usuarios)
        self.atualizar_funcionarios = QWidget()
        self.atualizar_funcionarios.setObjectName(u"atualizar_funcionarios")
        self.image_label_2 = QLabel(self.atualizar_funcionarios)
        self.image_label_2.setObjectName(u"image_label_2")
        self.image_label_2.setGeometry(QRect(360, 50, 151, 191))
        self.image_label_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_label_2.setMargin(-1)
        self.label_12 = QLabel(self.atualizar_funcionarios)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(9, 0, 311, 31))
        self.label_12.setFont(font)
        self.localizar_mais_um = QPushButton(self.atualizar_funcionarios)
        self.localizar_mais_um.setObjectName(u"localizar_mais_um")
        self.localizar_mais_um.setGeometry(QRect(430, 250, 80, 24))
        self.widget = QWidget(self.atualizar_funcionarios)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 50, 351, 151))
        self.formLayout_4 = QFormLayout(self.widget)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.lineEdit_atualizar_matricula = QLineEdit(self.widget)
        self.lineEdit_atualizar_matricula.setObjectName(u"lineEdit_atualizar_matricula")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_atualizar_matricula)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_atualizar_nome = QLineEdit(self.widget)
        self.lineEdit_atualizar_nome.setObjectName(u"lineEdit_atualizar_nome")
        self.lineEdit_atualizar_nome.setReadOnly(True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lineEdit_atualizar_nome)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_atualizar_cargo = QLineEdit(self.widget)
        self.lineEdit_atualizar_cargo.setObjectName(u"lineEdit_atualizar_cargo")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.lineEdit_atualizar_cargo)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_15)

        self.lineEdit_atualizar_setor = QLineEdit(self.widget)
        self.lineEdit_atualizar_setor.setObjectName(u"lineEdit_atualizar_setor")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.lineEdit_atualizar_setor)

        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_17)

        self.dateEdit_atualizar_admissao = QDateEdit(self.widget)
        self.dateEdit_atualizar_admissao.setObjectName(u"dateEdit_atualizar_admissao")
        self.dateEdit_atualizar_admissao.setCalendarPopup(True)

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.dateEdit_atualizar_admissao)

        self.widget1 = QWidget(self.atualizar_funcionarios)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 210, 351, 31))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.widget1)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.voltar_2 = QPushButton(self.widget1)
        self.voltar_2.setObjectName(u"voltar_2")

        self.horizontalLayout.addWidget(self.voltar_2)

        self.cadastrar_2 = QPushButton(self.widget1)
        self.cadastrar_2.setObjectName(u"cadastrar_2")

        self.horizontalLayout.addWidget(self.cadastrar_2)

        self.pushButton_3 = QPushButton(self.widget1)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.stackedWidget.addWidget(self.atualizar_funcionarios)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayout = QFormLayout(self.tab)
        self.formLayout.setObjectName(u"formLayout")
        self.criar_banco_sqlite = QPushButton(self.tab)
        self.criar_banco_sqlite.setObjectName(u"criar_banco_sqlite")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.criar_banco_sqlite)

        self.deletar_banco = QPushButton(self.tab)
        self.deletar_banco.setObjectName(u"deletar_banco")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.deletar_banco)

        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.inserir_funcionario.setText(QCoreApplication.translate("Widget", u"Inserir", None))
        self.importar_exel.setText(QCoreApplication.translate("Widget", u"Importar do Exel", None))
        self.atualizar.setText(QCoreApplication.translate("Widget", u"Atualizar ", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Inserir Funcion\u00e1rios : ", None))
        self.cadastrar.setText(QCoreApplication.translate("Widget", u"Cadastrar", None))
        self.voltar.setText(QCoreApplication.translate("Widget", u"Voltar", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Nome :", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Cargo :", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Setor :  ", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Matr\u00edcula :", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Admiss\u00e3o :", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"Atualizar Funcion\u00e1rios : ", None))
        self.localizar_mais_um.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"Matr\u00edcula :", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"Nome :", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"Cargo :", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"Setor :  ", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"Admiss\u00e3o :", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"Localizar", None))
        self.voltar_2.setText(QCoreApplication.translate("Widget", u"Editar", None))
        self.cadastrar_2.setText(QCoreApplication.translate("Widget", u"Atualizar", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Menu Inicial", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Funcion\u00e1rios", None))
        self.criar_banco_sqlite.setText(QCoreApplication.translate("Widget", u"Criar Banco", None))
        self.deletar_banco.setText(QCoreApplication.translate("Widget", u"Deletar Banco", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Configura\u00e7\u00f5es", None))
    # retranslateUi

