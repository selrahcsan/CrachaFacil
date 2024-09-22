# This Python file uses the following encoding: utf-8
import os
import sys
import pandas as pd
import sqlite3

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QDate


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_form import Ui_Widget

resultados = []
posicao_atual = 0

def cria_banco_sql():
    try:
        with sqlite3.connect('cracha.sqlite') as conn:
            cursor = conn.cursor()
        cria_tabela_sql = """
            CREATE TABLE IF NOT EXISTS funcionarios (
            matricula INTEGER PRIMARY KEY NOT NULL,
            nome TEXT,
            nome_completo TEXT,
            cargo TEXT,
            setor TEXT,
            data_admissao DATE,
            foto BLOB
        );
        """
        cursor.execute(cria_tabela_sql)
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
    arquivo = 'cracha.sqlite'
    if os.path.isfile(arquivo):
        msg = QMessageBox()
        msg.setText("Banco de dados já existe!")
        msg.exec()
    else:
        cria_banco_sql()


def deletar_banco():
    arquivo = 'cracha.sqlite'
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
    limpar_formularios()


def voltar_menu_funcionarios():
    limpar_formularios()
    widget.ui.stackedWidget.setCurrentIndex(0)

def menu_atualizar():
    widget.ui.stackedWidget.setCurrentIndex(2)
    widget.ui.dateEdit_atualizar_admissao.date().currentDate()
    carregar_resultados()


def image_upload():
    file_name, _ = QFileDialog.getOpenFileName(None, "Abrir Arquivo", "", "Arquivos de Imagem (*.png *.jpg)")

    if file_name:
        pixmap = QPixmap(file_name)
        widget.ui.image_label.setPixmap(pixmap)
        widget.ui.image_label.setScaledContents(True)
        return file_name


def atualizar_image_upload():
    file_name, _ = QFileDialog.getOpenFileName(None, "Abrir Arquivo", "", "Arquivos de Imagem (*.png *.jpg)")
    if file_name:
        pixmap = QPixmap(file_name)
        widget.ui.image_label_localizar.setPixmap(pixmap)
        widget.ui.image_label_localizar.setScaledContents(True)
        return file_name


def cadastrar():
    limpar_formularios()
    nome = widget.ui.lineEdit_nome.text().split()[0]
    nome_completo = widget.ui.lineEdit_nome.text()
    cargo = widget.ui.lineEdit_cargo.text()
    setor = widget.ui.lineEdit_setor.text()
    matricula = widget.ui.lineEdit_matricula.text()
    data_admissao = widget.ui.dateEdit_admissao.date().toString("yyyy-MM-dd")

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg.setWindowTitle('Imagem Funcionário')
    msg.setText("Adicionar Foto?")
    msg.setDefaultButton(QMessageBox.Yes)
    tem_foto = msg.exec()

    try:
        with sqlite3.connect('cracha.sqlite') as conn:
            cursor = conn.cursor()
        if tem_foto == QMessageBox.Yes:
            file_name = image_upload()
            if file_name:
                imagem = convert_to_binary(file_name)
                cursor.execute('''INSERT INTO funcionarios (matricula, nome, nome_completo, cargo, setor, data_admissao, foto)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''',
                    (matricula, nome, nome_completo, cargo, setor, data_admissao, imagem))
        else:
            cursor.execute('''INSERT INTO funcionarios (matricula, nome, nome_completo, cargo, setor, data_admissao)
                VALUES (?, ?, ?, ?, ?, ?)''',
                (matricula, nome, nome_completo, cargo, setor, data_admissao))
        conn.commit()
        msg = QMessageBox()
        msg.setText("Cadastrado com Sucesso")
        msg.exec()
        limpar_formularios()

    except sqlite3.Error as e:
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Erro")
        msg.setText("Ocorreu um erro ao cadastrar no banco:")
        msg.setInformativeText(f'{e}')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()


def convert_to_binary(filename):
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


def limpar_formularios():
    widget.ui.lineEdit_nome.clear()
    widget.ui.lineEdit_cargo.clear()
    widget.ui.lineEdit_setor.clear()
    widget.ui.lineEdit_matricula.clear()
    widget.ui.dateEdit_admissao.date().currentDate()
    widget.ui.image_label.clear()
    widget.ui.lineEdit_atualizar_matricula.clear()
    widget.ui.lineEdit_atualizar_nome.clear()
    widget.ui.lineEdit_atualizar_cargo.clear()
    widget.ui.lineEdit_atualizar_setor.clear()
    widget.ui.dateEdit_atualizar_admissao.date().currentDate()
    widget.ui.image_label_localizar.clear()



def importar_xls():
    limpar_formularios()
    file_name, _ = QFileDialog.getOpenFileName(None, "Abrir Arquivo", "", "Arquivos de Imagem (*.xls *.xlsx *.ods)")
    if file_name:
        try:
            df = pd.read_excel(file_name)
            df['data_admissao'] = df['data_admissao'].dt.strftime('%Y-%m-%d')

            with sqlite3.connect('cracha.sqlite') as conn:
                cursor = conn.cursor()
            for index, row in df.iterrows():
                nome_completo = row['nome']
                nome = nome_completo.split()[0]
                cursor.execute('''
                    INSERT INTO funcionarios (matricula, nome, nome_completo, cargo, setor, data_admissao)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ''', (row['matricula'], nome, nome_completo, row['cargo'], row['setor'], row['data_admissao']))
            conn.commit()
            conn.close()

            msg = QMessageBox()
            msg.setText("Dados importados com sucesso!")
            msg.exec()

        except Exception as e:
            msg = QMessageBox()
            msg.setText(f"Erro ao importar dados: {e}")
            msg.exec()



def buscar_matricula(matricula):
    limpar_formularios()
    try:
        with sqlite3.connect('cracha.sqlite') as conn:
            cursor = conn.cursor()
        cursor.execute('SELECT nome_completo, cargo, setor, data_admissao, foto FROM funcionarios WHERE matricula = ?', (matricula,))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            widget.ui.lineEdit_atualizar_nome.setText(str(resultado[0]))
            widget.ui.lineEdit_atualizar_cargo.setText(str(resultado[1]))
            widget.ui.lineEdit_atualizar_setor.setText(resultado[2])
            widget.ui.dateEdit_atualizar_admissao.setDate(QDate.fromString(resultado[3], "yyyy-MM-dd"))
            foto_blob = resultado[4]
            if foto_blob:
                pixmap = QPixmap()
                pixmap.loadFromData(foto_blob)
                widget.ui.image_label_localizar.setScaledContents(True)
                widget.ui.image_label_localizar.setPixmap(pixmap)


        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Informação")
            msg.setText("Não Localizado.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

    except sqlite3.Error as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Erro")
        msg.setText("Ocorreu um erro ao consultar o banco:")
        msg.setInformativeText(f'{e}')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()


def localizar_clicked():
    matricula = widget.ui.lineEdit_atualizar_matricula.text()
    if matricula:
        buscar_matricula(matricula)
        widget.ui.editar_localizar.setEnabled(True)
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Aviso")
        msg.setText("Por favor, insira uma matrícula para pesquisar.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

def editar_banco():
    limpar_formularios()
    widget.ui.lineEdit_atualizar_matricula.setFrame(False)
    widget.ui.lineEdit_atualizar_matricula.setReadOnly(True)
    widget.ui.atualizar_localizar.setEnabled(True)
    widget.ui.lineEdit_atualizar_nome.setFrame(True)
    widget.ui.lineEdit_atualizar_nome.setReadOnly(False)
    widget.ui.lineEdit_atualizar_cargo.setFrame(True)
    widget.ui.lineEdit_atualizar_cargo.setReadOnly(False)
    widget.ui.lineEdit_atualizar_setor.setFrame(True)
    widget.ui.lineEdit_atualizar_setor.setReadOnly(False)


def atualizar_banco():
    widget.ui.atualizar_localizar.setEnabled(True)
    widget.ui.lineEdit_atualizar_nome.setFrame(True)
    widget.ui.lineEdit_atualizar_nome.setReadOnly(False)
    widget.ui.lineEdit_atualizar_cargo.setFrame(True)

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg.setWindowTitle('Imagem Funcionário')
    msg.setText("Atualizar Foto do funcionário?")
    msg.setDefaultButton(QMessageBox.Yes)
    tem_foto = msg.exec()

    try:
        with sqlite3.connect('cracha.sqlite') as conn:
            cursor = conn.cursor()
        nome = widget.ui.lineEdit_atualizar_nome.text().split()[0]
        nome_completo = widget.ui.lineEdit_atualizar_nome.text()
        cargo = widget.ui.lineEdit_atualizar_cargo.text()
        setor = widget.ui.lineEdit_atualizar_setor.text()
        matricula = widget.ui.lineEdit_matricula.text()
        data_admissao = widget.ui.dateEdit_atualizar_admissao.date().toString("yyyy-MM-dd")
        matricula = widget.ui.lineEdit_atualizar_matricula.text()

        if tem_foto == QMessageBox.Yes:
            file_name = atualizar_image_upload()
            if file_name:
                imagem = convert_to_binary(file_name)
                cursor.execute('''UPDATE funcionarios SET nome = ?, nome_completo = ?, cargo = ?, setor = ?, data_admissao = ?, foto = ? WHERE matricula = ?''',
                               (nome, nome_completo, cargo, setor, data_admissao, imagem, matricula))
        else:
            cursor.execute('''UPDATE funcionarios SET nome = ?, nome_completo = ?, cargo = ?, setor = ?, data_admissao = ? WHERE matricula = ?''',
                           (nome, nome_completo, cargo, setor, data_admissao, matricula))

        conn.commit()
        msg = QMessageBox()
        msg.setText("Atualizado com Sucesso")
        msg.exec()
        limpar_formularios()

    except sqlite3.Error as e:
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Erro")
        msg.setText("Ocorreu um erro ao atualizar no banco:")
        msg.setInformativeText(f'{e}')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    finally:
        conn.close()


def carregar_resultados():
    global resultados
    try:
        conn = sqlite3.connect('cracha.sqlite')
        cursor = conn.cursor()
        cursor.execute('''SELECT matricula, nome, cargo, setor, data_admissao, foto FROM funcionarios''')
        resultados = cursor.fetchall()
        conn.close()
    except sqlite3.Error as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Erro")
        msg.setText("Ocorreu um erro ao consultar o banco:")
        msg.setInformativeText(f'{e}')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

def mostrar_resultado(posicao):
    limpar_formularios()
    if 0 <= posicao < len(resultados):
        resultado = resultados[posicao]
        widget.ui.lineEdit_atualizar_matricula.setText(str(resultado[0]))
        widget.ui.lineEdit_atualizar_nome.setText(str(resultado[1]))
        widget.ui.lineEdit_atualizar_cargo.setText(str(resultado[2]))
        widget.ui.lineEdit_atualizar_setor.setText(resultado[3])
        widget.ui.dateEdit_atualizar_admissao.setDate(QDate.fromString(resultado[4], "yyyy-MM-dd"))
        foto_blob = resultado[5]
        if foto_blob:
            pixmap = QPixmap()
            pixmap.loadFromData(foto_blob)
            widget.ui.image_label_localizar.setScaledContents(True)
            widget.ui.image_label_localizar.setPixmap(pixmap)
        # else:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Information)
        #     msg.setWindowTitle("Informação")
        #     msg.setText("Nenhum funcionário encontrado.")
        #     msg.setStandardButtons(QMessageBox.Ok)
        #     msg.exec()

def avancar():
    global posicao_atual
    if posicao_atual < len(resultados) - 1:
        posicao_atual += 1
        mostrar_resultado(posicao_atual)

def recuar():
    global posicao_atual
    if posicao_atual > 0:
        posicao_atual -= 1
        mostrar_resultado(posicao_atual)



class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()

    # Botãos Menu Iniciar ------------------------------------------------------------------

    widget.ui.btn_inserir_funcionario.clicked.connect(inserir_funcionarios)
    widget.ui.btn_importar_exel.clicked.connect(importar_xls)
    widget.ui.btn_atualizar.clicked.connect(menu_atualizar)

    # Botãos Funcinários - Cadastrar  ------------------------------------------------------

    widget.ui.voltar.clicked.connect(voltar_menu_funcionarios)
    widget.ui.cadastrar.clicked.connect(cadastrar)
    widget.ui.dateEdit_admissao.setDate(QDate.currentDate())

    # --------------------------------------------------------------------------------------

    # Botãos Funcionários = Atualizar ------------------------------------------------------


    widget.ui.localizar.clicked.connect(localizar_clicked)
    widget.ui.editar_localizar.clicked.connect(editar_banco)
    widget.ui.atualizar_localizar.clicked.connect(atualizar_banco)
    widget.ui.btn_retroceder.clicked.connect(recuar)
    widget.ui.btn_avancar.clicked.connect(avancar)

    # --------------------------------------------------------------------------------------

    # Botãos Configurações -----------------------------------------------------------------

    widget.ui.btn_criar_banco_sqlite.clicked.connect(banco_existe)
    widget.ui.deletar_banco.clicked.connect(deletar_banco)
    widget.ui.voltar_localizar_menu_inicial.clicked.connect(voltar_menu_funcionarios)

    # --------------------------------------------------------------------------------------

    widget.show()
    sys.exit(app.exec())
