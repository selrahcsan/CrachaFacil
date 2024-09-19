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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QTabWidget, QWidget)

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
        self.importar_exel.setGeometry(QRect(10, 80, 101, 24))
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
        self.Atualizar_funcionarios = QWidget()
        self.Atualizar_funcionarios.setObjectName(u"Atualizar_funcionarios")
        self.stackedWidget.addWidget(self.Atualizar_funcionarios)
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
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.inserir_funcionario.setText(QCoreApplication.translate("Widget", u"Inserir", None))
        self.importar_exel.setText(QCoreApplication.translate("Widget", u"Importar do Exel", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Inserir Funcion\u00e1rios : ", None))
        self.cadastrar.setText(QCoreApplication.translate("Widget", u"Cadastrar", None))
        self.voltar.setText(QCoreApplication.translate("Widget", u"Voltar", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Nome :", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Cargo :", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Setor :  ", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Matr\u00edcula :", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Admiss\u00e3o :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Funcion\u00e1rios", None))
        self.criar_banco_sqlite.setText(QCoreApplication.translate("Widget", u"Criar Banco", None))
        self.deletar_banco.setText(QCoreApplication.translate("Widget", u"Deletar Banco", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Configura\u00e7\u00f5es", None))
    # retranslateUi

