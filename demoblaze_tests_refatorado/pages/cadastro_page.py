from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CadastroPage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_signup = (By.ID, "signin2")
        self.input_username = (By.ID, "sign-username")
        self.input_password = (By.ID, "sign-password")
        self.btn_confirm = (By.XPATH, "//button[contains(@class,'btn') and contains(text(),'Sign up')]")
        self.modal = (By.ID, "signInModal")

    def abrir_modal(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_signup)).click()
        time.sleep(1)

    def cadastrar(self, usuario, senha):
        self.driver.find_element(*self.input_username).clear()
        self.driver.find_element(*self.input_username).send_keys(usuario)
        self.driver.find_element(*self.input_password).clear()
        self.driver.find_element(*self.input_password).send_keys(senha)
        self.driver.find_element(*self.btn_confirm).click()

    def fechar_modal(self):
        self.driver.execute_script("$('#signInModal').modal('hide');")
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element(self.modal))
        time.sleep(1)

    def obter_alerta(self):
        return WebDriverWait(self.driver, 5).until(EC.alert_is_present())
