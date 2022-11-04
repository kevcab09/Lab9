from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome('C:/Users/50768/Documents/GitHub/Lab9/chromedriver.exe')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")

#Busca la barra de busqueda, ingres el texto "HP Pavilon azul", y le da submit.
Busqueda = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
time.sleep(5)
TextoBusqueda = ("HP Pavilon azul")
Busqueda.send_keys(TextoBusqueda)
time.sleep(5)
Busqueda.submit()

#Busca el primer elemento, le da click y luego
primer_elemento = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "HP Pavilion - Laptop IPS FHD de 14 pulgadas (modelo 2022), Intel Core i3-1125G4 (Beats i7-1065G7), 16GB RAM, SSD de 512GB, lector de huellas dactilares, batería de larga duración, cámara web, HDMI, WiFi, Bluetooth, Win10")))
primer_elemento.click()
time.sleep(5)
cantidad = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "quantity")))
cantidad.send_keys("2")
time.sleep(5)
Agregar_a_carrito = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))
Agregar_a_carrito.click()
time.sleep(3)
ir_a_carrito = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Ir al Carrito")))
ir_a_carrito.click()

time.sleep(100)
driver.close()
