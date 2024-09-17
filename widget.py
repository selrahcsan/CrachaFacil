# This Python file uses the following encoding: utf-8
import os
import sys
import sqlite3

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

def cria_banco_sql():
    try:
        conn = sqlite3.connect('cracha.db')
        cursor = conn.cursor()
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS funcionarios (
            matricula INTEGER PRIMARY KEY NOT NULL,
            nome TEXT NOT NULL,
            cargo TEXT NOT NULL,
            setor TEXT NOT NULL,
            data_admissao DATE NOT NULL,
            foto BLOB
        );
        """
        cursor.execute(create_table_sql)
        conn.commit()
        conn.close()
        msg = QMessageBox()
        msg.setText("Banco Criado com sucesso.")
        msg.exec()

    except sqlite3.Error as e:
        msg = QMessageBox()
        msg.setText(f"Erro ao criar o banco de dados: {e}")
        msg.exec()

def banco_existe():
    arquivo = 'cracha.db'
    if os.path.isfile(arquivo):
        msg = QMessageBox()
        msg.setText("Banco de dados já existe!")
        msg.exec()
    else:
        cria_banco_sql()

def deletar_banco():
    arquivo = 'cracha.db'
    try:
        if os.path.exists(arquivo):
            os.remove(arquivo)
            msg = QMessageBox()
            msg.setText("Banco deletado com sucesso")
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setText("Banco não encontrado")
            msg.exec()
    except Exception as e:
        msg = QMessageBox()
        msg.setText(f"Banco nao pode ser deletado! {e}")
        msg.exec()


def inserir_funcionarios():
    widget.ui.stackedWidget.setCurrentIndex(1)




def voltar_menu_funcionarios():
    widget.ui.stackedWidget.setCurrentIndex(0)


def cadastrar():
    nome = widget.ui.lineEdit_nome.text()
    cargo = widget.ui.lineEdit_cargo.text()
    setor = widget.ui.lineEdit_setor.text()
    matricula = widget.ui.lineEdit_matricula.text()
    data_admissao = widget.ui.dateEdit_admissao.date().toString("yyyy-MMdd")
    try:
        conn = sqlite3.connect('cracha.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO funcionarios (matricula, nome, cargo, setor, data_admissao)
            VALUES (?, ?, ?, ?, ?)''', (matricula, nome, cargo, setor, data_admissao, ))
        conn.commit()
        conn.close()
        msg = QMessageBox()
        msg.setText("Cadastrado com Sucesso")
        msg.exec()
        widget.ui.lineEdit_nome.clear()

    except sqlite3.Error as e:
        print(f"Erro ao cadastrar funcionário: {e}")

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.ui.criar_banco_sqlite.clicked.connect(banco_existe)
    widget.ui.deletar_banco.clicked.connect(deletar_banco)
    widget.ui.inserir_funcionario.clicked.connect(inserir_funcionarios)
    widget.ui.voltar.clicked.connect(voltar_menu_funcionarios)
    widget.ui.cadastrar.clicked.connect(cadastrar)

    widget.show()
    sys.exit(app.exec())
