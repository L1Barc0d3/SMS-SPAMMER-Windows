#!/usr/bin/env python3
import os
import sys
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TBOMB_DIR = os.path.join(BASE_DIR, "TBomb")
IMPULSE_DIR = os.path.join(BASE_DIR, "Impulse")

TBOMB_GIT = "https://github.com/TheSpeedX/TBomb.git"
IMPULSE_GIT = "https://github.com/LimerBoy/Impulse.git"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def run_cmd(cmd, cwd=None):
    print(f"Ejecutando comando: {cmd} en {cwd}")
    process = subprocess.Popen(cmd, shell=True, cwd=cwd)
    process.communicate()
    return process.returncode

def clone_or_pull(repo_url, path):
    if os.path.isdir(path):
        print(f"Actualizando repo en {path}...")
        ret = run_cmd("git pull", cwd=path)
        if ret != 0:
            print("Error al actualizar repo.")
            return False
    else:
        print(f"Clonando repo {repo_url} en {path}...")
        ret = run_cmd(f'git clone "{repo_url}" "{path}"')
        if ret != 0:
            print("Error al clonar repo.")
            return False
    if not os.path.isdir(path):
        print(f"ERROR: La carpeta {path} no existe después de la operación.")
        return False
    return True

def install_tbomb_windows():
    if not clone_or_pull(TBOMB_GIT, TBOMB_DIR):
        print("No se pudo obtener TBomb. Abortando.")
        return
    print("En Windows, omitiendo ejecución de install.sh (no disponible).")
    print("Asegúrate de instalar manualmente las dependencias necesarias.")

def install_impulse_windows():
    if not clone_or_pull(IMPULSE_GIT, IMPULSE_DIR):
        print("No se pudo obtener Impulse. Abortando.")
        return
    print("Instalando dependencias de Impulse...")
    if not os.path.isdir(IMPULSE_DIR):
        print(f"ERROR: El directorio {IMPULSE_DIR} no existe.")
        return
    ret = run_cmd("pip install -r requirements.txt", cwd=IMPULSE_DIR)
    if ret != 0:
        print("Error al instalar las dependencias.")

def run_tbomb():
    print("Ejecutando TBomb...")
    if not os.path.isdir(TBOMB_DIR):
        print(f"ERROR: No se encontró la carpeta {TBOMB_DIR}")
        return
    run_cmd("python bomber.py", cwd=TBOMB_DIR)

def run_impulse():
    print("Ejecutando Impulse...")
    if not os.path.isdir(IMPULSE_DIR):
        print(f"ERROR: No se encontró la carpeta {IMPULSE_DIR}")
        return
    run_cmd("python impulse.py --help", cwd=IMPULSE_DIR)

def menu():
    while True:
        clear()
        print("""
███████╗███████╗████████╗███████╗███╗   ███╗███████╗
██╔════╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔════╝
███████╗█████╗     ██║   ███████╗██╔████╔██║███████╗
╚════██║██╔══╝     ██║   ╚════██║██║╚██╔╝██║╚════██║
███████║███████╗   ██║   ███████║██║ ╚═╝ ██║███████║
╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝
""")
        print("Seleccione una opción:\n1) Ejecutar TBomb (Spam SMS)\n2) Ejecutar Impulse (Spam SMS)\n0) Salir\n")
        choice = input("Opción: ").strip()
        if choice == "1":
            install_tbomb_windows()
            run_tbomb()
            input("\nPresiona ENTER para continuar...")
        elif choice == "2":
            install_impulse_windows()
            run_impulse()
            input("\nPresiona ENTER para continuar...")
        elif choice == "0":
            print("Saliendo...")
            sys.exit(0)
        else:
            print("Opción incorrecta.")
            input("Presiona ENTER para intentar de nuevo...")

if __name__ == "__main__":
    menu()
