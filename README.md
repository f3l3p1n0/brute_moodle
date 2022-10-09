#############################################
# Script PoC for Moodle Login - by f3l3p1n0 #
#############################################

Este script ha sido creado con fines educativos. 
Consiste en realizar fuerza bruta en el login de cualquier página que implemente Moodle.


Simplemente debes colocar la url del sitio web, el mensaje de error que reporta cuando las credenciales son inválidas y 
los diccionarios de usuarios y contraseñas. (Más adelante subiré el código para crear diccionarios)

Ejemplo de uso:

<ol>
  <li> - Introduce la url del moodle a escanear: https://url_moodle </li>
  <li> - Introduce la frase de error de inicio incorrecto: Inicio de sesión incorrecto, vuelve a intentarlo </li>
  <li> - Ruta ubicación diccionario users: C:\Users\"your_user"\Desktop\dicc\user.txt </li>
  <li> - Ruta ubicación diccionario passwords: C:\Users\Marc-PC\Desktop\dicc\pass.txt </li>
</ol>

Esperas a que encuentre la clave y usuario válidos.

[![Ejemplo.png](https://i.postimg.cc/JzLsB3WH/Ejemplo.png)](https://postimg.cc/8jZp26cT)

Pd: Este script se adapta mejor en Linux.

