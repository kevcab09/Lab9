from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("C:/Users/Kevin Caballero/Downloads/chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")
search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "field-keywords")))
time.sleep(3)
buscar = ("HP Pavilion azul")
search_input.send_keys(buscar)
time.sleep(3)
search_input.submit()
componente = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div["
                                                                                    "1]/div[1]/div/span[1]/div["
                                                                                    "1]/div["
                                                                                    "3]/div/div/div/div/div/div/div"
                                                                                    "/div[2]/div/div/div["
                                                                                    "1]/h2/a/span")))
componente.click()
time.sleep(3)
amount = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "quantity")))
amount.send_keys("2")
time.sleep(7)
agregar_al_carrito = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "submit.add-to-cart")))
agregar_al_carrito.click()
time.sleep(3)
ir_al_carrito = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "sw-gtc")))
ir_al_carrito.click()

time.sleep(10)
driver.quit()
