# -*- coding: utf-8 -*-
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Leer el archivo CSV
df = pd.read_csv('urls.csv', header=None, names=['URL'])

# Configurar opciones de Chrome para modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# Inicializar el navegador
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navegar a cada URL y capturar una captura de pantalla
for index, row in df.iterrows():
    url = row['URL']
    driver.get(url)
    filename = url.split('/')[-1] #Usar la última parte del url (dividiéndolo por diagonales) como nombre de la screenshot
    time.sleep(2)  # Esperar a que la página cargue completamente
    screenshot_path = f'screenshot_{filename}.png'
    driver.save_screenshot(screenshot_path)
    print(f"Captura de pantalla guardada como {screenshot_path}")

# Cerrar el navegador
driver.quit()