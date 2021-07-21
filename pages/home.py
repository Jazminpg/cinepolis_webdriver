from selenium.webdriver.common.by import By
from touches.randoms import randomSelectChoice

class HomePage:
    URL = 'https://cinepolis.com/'
    CITIES = (By.CSS_SELECTOR, '#cmbCiudades')
    CINES = (By.CSS_SELECTOR, '#cmbComplejos')

    def __init__(self, driver):
        self.driver = driver
    def load(self):
        self.driver.get(self.URL)
    def city(self):
        randomSelectChoice(self.driver, self.CITIES)
    def cine(self):
        randomSelectChoice(self.driver, self.CINES)

