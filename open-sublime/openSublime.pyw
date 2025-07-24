import sys
import os
import subprocess

def main():
    if len(sys.argv) < 2:
        return

    caminho = sys.argv[1]

    # Se clicou em arquivo, pega a pasta
    if os.path.isfile(caminho):
        pasta = os.path.dirname(caminho)
    else:
        pasta = caminho  # Já é uma pasta

    # Caminho do Sublime
    sublime_path = r"C:\Program Files\Sublime Text\subl.exe"

    # Abre o Sublime na pasta
    subprocess.Popen([sublime_path, pasta], shell=True)

if __name__ == "__main__":
    main()
