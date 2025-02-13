# Doom-in-turtlebot
Doom en TurtleBot, el nombre ya lo dice xd. Doom in TurtleBot in English xd

## 🚀 Control de TurtleBot3 con DOOM 🎮  

Tutorial para correr Doom en un TurtleBot. Como un TurtleBot3 es esencialmente una Raspberry Pi con algunos componentes adicionales, no era muy complicado. Lo que se hizo fue crear un módulo de ROS para controlar el TurtleBot de manera remota desde SSH, lo que permite correr Doom a través del puerto de escucha de los motores y el ROS del TurtleBot. En resumen, se corre DOOM en un TurtleBot3 de una forma más cool (subiré un video más adelante en algún sitio xd).  

## 🛠 **1️⃣ Instalación**  
El nombre `red_follower` proviene de un proyecto que tenía en el mismo paquete de persecución por colores.

### **En la PC remota**  
Lo primero es inicializar el TurtleBot, de preferencia siguiendo este tutorial de la página oficial:  
https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/

Luego, clona el repositorio y ejecuta los siguientes comandos en la máquina remota:
```bash
sudo apt update && sudo apt install ros-noetic-rosbridge-server ros-noetic-joy
pip install pynput
