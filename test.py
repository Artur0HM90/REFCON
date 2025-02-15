import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar el navegadorimport sys
import webbrowser
import time
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Diccionario con usuarios y contraseñas
credenciales = {
    "RANRAHIRCA": ("usuario1", "password1"),
    "TAMBRA": ("usuario2", "password2"),
    "CHILCA": ("usuario3", "password3"),
    "HUARCA": ("usuario4", "password4"),
    "HUASHAO": ("usuario5", "password5"),
    "ARHUAY": ("usuario6", "password6"),
    "MATACOTO": ("usuario7", "password7"),
    "PUTACA": ("usuario8", "password8"),
    "PUNAP": ("usuario9", "password9"),
    "RAYAN": ("usuario10", "password10"),
}

# Función para abrir el enlace y llenar usuario/contraseña
def abrir_enlace(puesto):
    usuario, contrasena = credenciales.get(puesto, ("", ""))

    # Configurar Selenium
    options = webdriver.ChromeOptions()
    options.headless = False
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Abrir la página
    driver.get("https://refcon.minsa.gob.pe/refconv02/")

    # Esperar que cargue la página
    time.sleep(3)

    # Localizar los campos de usuario y contraseña
    usuario_input = driver.find_element(By.NAME, "mlkuser")
    contrasena_input = driver.find_element(By.NAME, "mlkpass")

    # Ingresar los datos
    usuario_input.send_keys(usuario)
    contrasena_input.send_keys(contrasena)

    # Presionar Enter para iniciar sesión
    contrasena_input.send_keys(Keys.RETURN)

    # Mantener abierto hasta que el usuario cierre
    input(f"Sesión iniciada en {puesto}. Presiona Enter para cerrar...")
    driver.quit()

# Configurar la aplicación de PyQt
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("REFCON - MRYUNGAY")
window.setGeometry(100, 100, 300, 450)

layout = QVBoxLayout()
layout.setSpacing(10)
layout.setContentsMargins(20, 20, 20, 20)
layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

# Etiqueta principal
label = QLabel("ELIGE EL PUESTO")
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
label.setStyleSheet("font-size: 14px; font-weight: bold;")
layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)

# Crear botones para cada puesto
for puesto in credenciales.keys():
    button = QPushButton(puesto)
    button.setFixedSize(150, 30)
    button.clicked.connect(lambda checked, p=puesto: abrir_enlace(p))
    layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

# Aplicar layout a la ventana
window.setLayout(layout)
window.show()
sys.exit(app.exec())
options = webdriver.ChromeOptions()
options.headless = False  # Mantiene la interfaz visible
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Abrir la página
driver.get("https://refcon.minsa.gob.pe/refconv02/")

# Esperar un poco para que cargue la página
time.sleep(3)

# Localizar los campos de usuario y contraseña
usuario_input = driver.find_element(By.NAME, "mlkuser")  # Usando el atributo 'name'
contrasena_input = driver.find_element(By.NAME, "mlkpass")  # Usando el atributo 'name'

# Ingresar datos
usuario_input.send_keys("tu_usuario")
contrasena_input.send_keys("tu_contraseña")

# Presionar Enter para iniciar sesión (o buscar el botón de login y hacer clic)
contrasena_input.send_keys(Keys.RETURN)

# Mantener el navegador abierto hasta que el usuario lo cierre
input("Presiona Enter para salir...")
driver.quit()