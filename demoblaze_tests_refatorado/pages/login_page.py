from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_login = (By.ID, "login2")
        self.input_username = (By.ID, "loginusername")
        self.input_password = (By.ID, "loginpassword")
        self.btn_confirm = (By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        self.nome_usuario = (By.ID, "nameofuser")
        self.modal = (By.ID, "logInModal")
        self.logout_btn = (By.ID, "logout2")

    def abrir_modal(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_login)).click()
        time.sleep(1)

    def logar(self, usuario, senha):
        self.driver.find_element(*self.input_username).clear()
        self.driver.find_element(*self.input_username).send_keys(usuario)
        self.driver.find_element(*self.input_password).clear()
        self.driver.find_element(*self.input_password).send_keys(senha)
        self.driver.find_element(*self.btn_confirm).click()

    def obter_alerta(self):
        return WebDriverWait(self.driver, 5).until(EC.alert_is_present())

    def obter_usuario_logado(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.nome_usuario)).text

    def fechar_modal(self):
        self.driver.execute_script("$('#logInModal').modal('hide');")
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element(self.modal))
        time.sleep(1)

    def logout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout_btn)).click()
        time.sleep(2)
