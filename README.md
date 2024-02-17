# Creación de un programa que realiza diversas tareas funcionando como un bot de Telegram

![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![VSCode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

## 💻 Funcionalidades del proyecto

- `Funcionalidad 1`: Llamadas a varias APIs  
- `Funcionalidad 2`: Conversión de formatos CSV a JSON y viceversa  
- `Funcionalidad 3`: Scraping de varias webs  
- `Funcionalidad 4`: Consulta BBDD MySQL

## 📁 Acceso al proyecto

Puedes clonar el repositorio con 

`-git clone {URL del repositorio}`

## 🛠️ Abre y ejecuta el proyecto

### Creacion y activación de un env en conda

`-conda create -n bots python=3.9`

`conda activate bots`

### Instalación de la libreria principal para interactuar coa API de Telegram

`-pip install python-telegram-bot`

### Exportar listado de librerias instaladas

`-pip freeze`

`-pip freeze > requirements.txt`

### Importa listaxe de librarías instaladas

`-pip install -r requirements.txt`

### Creacion de un TOKEN

Introducir el TOKEN generado en el archivo `token.txt`

### Desde terminal

`-python main.py`

## ⚙️Comandos

`/start`

`/tiempo`

`/apod`

`/txistaco`

`/perro`

`/diario`

`/cartelera`

`/inferno`

## Instrucciones dockerizacion

`-docker build -t user_hub/nome_imaxe:latest .`

`-docker login -u user_hub`

**--Se requerira el password--**

`-docker image push  user_hub/nome_imaxe:latest`

`-docker image rm user_hub/nome_imaxe:latest`

`-docker run user_hub/nome_imaxe:latest`

**--Se recomienda crear CI/CD para crear automatizacion en Github y crear una nueva imagen en cada push--**

## Enlace imagen DOCKER

`https://hub.docker.com/repository/docker/pedropatinodev/telegrambot/general`
