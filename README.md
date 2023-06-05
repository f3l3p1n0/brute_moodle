
<h3>Script PoC for Moodle Login - by f3l3p1n0 </h3>
<hr>
<p>Este script ha sido creado con fines educativos.</p>
<p>Consiste en realizar fuerza bruta en el login de cualquier página que implemente Moodle.</p>
<p>Simplemente debes colocar la url del sitio web, el mensaje de error que reporta cuando las credenciales son inválidas y 
los diccionarios de usuarios y contraseñas. (Más adelante subiré el código para crear diccionarios)</p>
<hr>
<h3>Ejemplo de uso</h3>
<ol>
  <li> Introduce la url del moodle a escanear: https://url_moodle </li>
  <li> Introduce la frase de error de inicio incorrecto: Inicio de sesión incorrecto, vuelve a intentarlo </li>
  <li> Ruta ubicación diccionario users: C:\Users\"your_user"\Desktop\dicc\user.txt </li>
  <li> Ruta ubicación diccionario passwords: C:\Users\"your_user"\Desktop\dicc\pass.txt </li>
</ol>
<br>
<img src="https://i.postimg.cc/JzLsB3WH/Ejemplo.png" width="600" height="500">
<hr>
<h3>Posibles problemas a tener en cuenta</h3>
<h5>Deberás tener en cuenta los valores de los inputs del formulario</h5>
<p>En mi caso quiero atacar el siguiente formulario de ejemplo:<p>
<img src="https://i.postimg.cc/5NLPyv48/2023-06-05-19-39.png">
<p>Deberé de tener en cuenta el nombre del input del token (<strong>logintoken</strong>), usuario (<strong>username</strong>) y contraseña (<strong>password</strong>).</p>
<p>Por tanto, deberás de tener en cuenta si el formulario que deseas atacar presentan los mismos nombres en los respectivos inputs o de lo contrario son diferentes.</p>
