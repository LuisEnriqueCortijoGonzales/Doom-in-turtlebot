# Doom-in-turtlebot
Doom en TurtleBot, el nombre ya lo dice xd. Doom in TurtleBot in English xd

Tutorial para correr Doom en un TurtleBot. Como un TurtleBot3 es esencialmente una Raspberry Pi con algunos componentes adicionales, no era muy complicado ni interesante. Lo que se hizo fue crear un módulo de ROS para controlar el TurtleBot de manera remota desde SSH, lo que permite correr Doom a través del puerto de escucha de los motores y el ROS del TurtleBot. En resumen, se corre DOOM en un TurtleBot3 de una forma más chevere (subiré un video más adelante en algún sitio xd).  

## 🛠 **1️⃣ Instalación**  
El nombre `red_follower` proviene de un proyecto mio que tenía en el mismo paquete de persecución por colores.

### **En la PC remota**  
Lo primero es inicializar el TurtleBot, de preferencia siguiendo este tutorial de la página oficial:  
https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/

Luego, clona el repositorio y ejecuta los siguientes comandos en la máquina remota:
```bash
sudo apt update && sudo apt install ros-noetic-rosbridge-server ros-noetic-joy
pip install pynput
```
###**En el TurtleBot**
Conéctate al TurtleBot a través de SSH:
```bash
ssh ubuntu@TURTLEBOT_IP
```
Ejecuta los siguientes comandos:
```bash
sudo apt update && sudo apt install chocolate-doom
cd ~/catkin_ws/src
catkin_create_pkg red_follower rospy std_msgs sensor_msgs cv_bridge geometry_msgs
cd ~/catkin_ws
catkin_make
source devel/setup.bash
mkdir -p ~/catkin_ws/src/red_follower/scripts
mv ~/TU_REPO/doom_turtlebot.py ~/catkin_ws/src/red_follower/scripts/
chmod +x ~/catkin_ws/src/red_follower/scripts/doom_turtlebot.py
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo usermod -a -G input $USER
sudo chmod 777 /dev/input/event*
```
###**Ejecución**
En la PC remota:

```bash
export TURTLEBOT3_MODEL=burger
roscore
python3 keyboard_publisher.py
```

En el TurtleBot:

```bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_bringup turtlebot3_core.launch
rosrun red_follower doom_turtlebot.py
```
Agradecimientos al profe Victor y al profe Deza por el turtlebot y a GPT por la ayuda en el debugeo xd
