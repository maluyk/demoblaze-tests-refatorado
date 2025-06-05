import time
from utils.base_test import BaseTest
from pages.cadastro_page import CadastroPage
from pages.login_page import LoginPage

class TestDemoblaze(BaseTest):

    def test_cenario_1_cadastro_valido(self):
        cadastro = CadastroPage(self.driver)
        cadastro.abrir_modal()
        cadastro.cadastrar("Ravena2025", "sara2023")
        alert = cadastro.obter_alerta()
        texto = alert.text
        alert.accept()
        cadastro.fechar_modal()
        assert texto == "Sign up successful."

    def test_cenario_2_cadastro_username_vazio(self):
        cadastro = CadastroPage(self.driver)
        cadastro.abrir_modal()
        cadastro.cadastrar("", "sara2023")
        alert = cadastro.obter_alerta()
        texto = alert.text
        alert.accept()
        cadastro.fechar_modal()
        assert texto != "Sign up successful."

    def test_cenario_3_cadastro_senha_vazia(self):
        cadastro = CadastroPage(self.driver)
        cadastro.abrir_modal()
        cadastro.cadastrar("Ravena2025", "")
        alert = cadastro.obter_alerta()
        texto = alert.text
        alert.accept()
        cadastro.fechar_modal()
        assert texto != "Sign up successful."

    def test_cenario_4_login_valido(self):
        login = LoginPage(self.driver)
        login.abrir_modal()
        login.logar("Ravena2025", "sara2023")
        time.sleep(2)
        texto = login.obter_usuario_logado()
        login.fechar_modal()
        assert "Welcome" in texto

    def test_cenario_5_login_username_incorreto(self):
        login = LoginPage(self.driver)
        login.logout()
        login.abrir_modal()
        login.logar("sara2005", "sara2023")
        alert = login.obter_alerta()
        texto = alert.text
        alert.accept()
        login.fechar_modal()
        assert "User does not exist." in texto or "Wrong password." in texto

    def test_cenario_6_login_senha_errada(self):
        login = LoginPage(self.driver)
        login.abrir_modal()
        login.logar("Ravena2025", "senha errada123")
        alert = login.obter_alerta()
        texto = alert.text
        alert.accept()
        login.fechar_modal()
        assert texto == "Wrong password."

    def test_cenario_7_login_senha_vazia(self):
        login = LoginPage(self.driver)
        login.abrir_modal()
        login.logar("Ravena2025", "")
        alert = login.obter_alerta()
        texto = alert.text
        alert.accept()
        login.fechar_modal()
        assert texto == "Please fill the Password."

    def test_cenario_8_login_usuario_vazio(self):
        login = LoginPage(self.driver)
        login.abrir_modal()
        login.logar("", "sara2023")
        alert = login.obter_alerta()
        texto = alert.text
        alert.accept()
        login.fechar_modal()
        assert texto == "Please fill the Username."

    def test_cenario_9_login_dados_nao_cadastrados(self):
        login = LoginPage(self.driver)
        login.abrir_modal()
        login.logar("naocadastrado123", "naocadastrado123")
        alert = login.obter_alerta()
        texto = alert.text
        alert.accept()
        login.fechar_modal()
        assert texto == "User and password does not match."

    def test_cenario_10_login_campos_vazios(self):
        login = LoginPage(self.driver)
        login.abrir_modal()
        login.logar("", "")
        alert = login.obter_alerta()
        texto = alert.text
        alert.accept()
        login.fechar_modal()
        assert texto == "Please fill User and Password."
