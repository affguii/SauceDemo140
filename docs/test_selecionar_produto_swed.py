# 1 - Bibliotecas 
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe (Opcional)
class Teste_Produtos():

 # 2.1  Atributos
    url = "https://www.saucedemo.com"                  # endereco do site alvo

# 2.2 Funcoes e Metodos 
    def setup_method(self,method):                                              # método de inicializacao dos testes
        self.driver = webdriver.Chrome()                                          # instancia o objeto do selenium WebDriver como Chrome
        self.driver.implicitly_wait(10)                                         # define o tempo de espera padrao por elementos em 10 segundos    

    def teardown_method(self,method):                                           # método de finalizacao dos testes
        self.driver.quit()                                                      # encerra / destrói o objeto do Selenium WebDriver da memória

    def test_selecionar_produto(self):                                          # método de teste
        self.driver.get(self.url)                                               # abre o navegador 
        self.driver.find_element(By.ID,"user-name").send_keys("stand_user")     # escreve no campo user-name
        self.driver.find_element(By.NAME,"password").send_keys("secret_sauce")   # escreve a senha