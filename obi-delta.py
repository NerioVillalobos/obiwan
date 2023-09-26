import argparse
import subprocess
import os
import git  # Importa la biblioteca gitpython

def is_git_repository():
    try:
        repo = git.Repo(search_parent_directories=True)
        return True
    except git.exc.InvalidGitRepositoryError:
        return False

def run_git_diff(rama_origen, rama_destino):
    if not is_git_repository():
        print("No se puede ejecutar, No estás dentro de un repositorio Git.")
        return

    gitcheckout_origen = f"git checkout {rama_origen}"
    gitpull = "git pull"
    gitcheckout_destino = f"git checkout {rama_destino}"
    gitpullorigin_destino = f"git pull origin {rama_destino}"

    subprocess.run(gitcheckout_origen, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(gitpull, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(gitcheckout_destino, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(gitpull, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(gitcheckout_origen, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(gitpullorigin_destino, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    diff_result = f"git diff --name-only --diff-filter=AMR {rama_destino} {rama_origen} > diff.txt"
    subprocess.run(diff_result, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def main():
    parser = argparse.ArgumentParser(description="Captura valores Branch_Origen y Branch_Destino")
    parser.add_argument("Branch_Origen", nargs='?', help="Valor para Branch_Origen")
    parser.add_argument("Branch_Destino", nargs='?', help="Valor para Branch_Destino")

    args = parser.parse_args()

    # Accede a los valores proporcionados
    branch_origen = args.Branch_Origen
    branch_destino = args.Branch_Destino

    if branch_origen is None or branch_destino is None:
        user_input = input("Ingresa el Branch Origen y el Branch Destino. ¿Quieres salir? (Presiona Enter para salir, o ingresa los valores): ")
        if user_input == "":
            return

    if not is_git_repository():
        print("No se puede ejecutar run_git_diff porque no estás dentro de un repositorio Git.")
        return

    print(f"Procesando Delta...")
    print(f"Branch Origen: {branch_origen}")
    print(f"Branch Destino: {branch_destino}")
    print(f"Ubicando las diferencias...")

    # Llama a la función run_git_diff con los valores capturados
    run_git_diff(branch_origen, branch_destino)

if __name__ == "__main__":
    main()
