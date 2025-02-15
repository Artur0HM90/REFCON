# REFCON - MRYUNGAY

Este proyecto es una aplicación de escritorio basada en **PyQt6** y **Selenium** que permite a los usuarios seleccionar un puesto y autocompletar los campos de inicio de sesión en la página de **REFCON**.

## Requisitos

- **Python 3.8 o superior**
- **Google Chrome** instalado
- **Chromedriver** compatible con la versión de Chrome

## Instalación

Asegúrate de tener Python y `pip` actualizados antes de comenzar la instalación.

### macOS

1. Instalar **Homebrew** (si no lo tienes):
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Instalar Python y dependencias:
   ```sh
   brew install python3
   pip3 install -r requirements.txt
   ```
3. Instalar Chrome (si no lo tienes):
   ```sh
   brew install --cask google-chrome
   ```
4. Instalar ChromeDriver:
   ```sh
   brew install chromedriver
   ```
5. Ejecutar la aplicación:
   ```sh
   python3 app.py
   ```

### Windows

1. Instalar Python desde [python.org](https://www.python.org/downloads/).
2. Instalar las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
3. Descargar e instalar **Google Chrome** desde [aqui](https://www.google.com/chrome/).
4. Descargar el **ChromeDriver** compatible con la versión de Chrome desde [aqui](https://sites.google.com/chromium.org/driver/), extraerlo y agregar la ruta a las variables de entorno.
5. Ejecutar la aplicación:
   ```sh
   python app.py
   ```

### Linux (Ubuntu/Debian)

1. Instalar Python y dependencias:
   ```sh
   sudo apt update && sudo apt install -y python3 python3-pip
   pip3 install -r requirements.txt
   ```
2. Instalar Google Chrome:
   ```sh
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
   sudo dpkg -i google-chrome-stable_current_amd64.deb
   sudo apt --fix-broken install
   ```
3. Instalar ChromeDriver:
   ```sh
   sudo apt install -y chromium-chromedriver
   ```
4. Ejecutar la aplicación:
   ```sh
   python3 app.py
   ```

## Uso

Al ejecutar el programa, aparecerá una ventana con los nombres de los puestos. Al hacer clic en un botón, se abrirá Google Chrome, accederá automáticamente al sitio **REFCON** e ingresará las credenciales correspondientes.

## Dependencias

Las dependencias necesarias están en el archivo `requirements.txt`, pero incluyen:

```txt
selenium
webdriver-manager
PyQt6
```

Para instalarlas manualmente:

```sh
pip install selenium webdriver-manager PyQt6
```

## Notas

- Para evitar problemas con **ChromeDriver**, asegúrate de que la versión de Chrome coincida con la de ChromeDriver.
- En Windows, si ChromeDriver no está en el `PATH`, puedes moverlo a `C:\Windows\System32\` o especificar su ruta en el código.

## Autor

Desarrollado por **[Artur0HM90]** 🚀

