import argparse
import subprocess
import os
import git  # Importa la biblioteca gitpython


def leer_diff_txt():
    diff_file = open("diff.txt", "r")
    diff_lines = diff_file.readlines()
    diff_file.close()

    # Crea una lista vacía para almacenar los resultados
    results = []

    # Itera sobre las líneas del archivo diff
    for line in diff_lines:
        # Si la línea contiene "force-app/main/default"
        if "force-app/main/default" in line:
            # Obtiene el nombre de la carpeta del componente
            foldercomponent = line.split("/")[3]

            if foldercomponent == "apexEmailNotifications":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "applications":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "approvalProcesses":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "assignmentRules":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "audience":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "aura":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "autoResponseRules":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
            
            if foldercomponent == "brandingSets":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "campaignInfluenceModels":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "Canvases":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
        

            # Si el nombre de la carpeta es "classes"
            if foldercomponent == "classes":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "communities":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "components":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "connectedApps":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "contentassets":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "corsWhitelistOrigins":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "cspTrustedSites":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "customMetadata":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "customPermissions":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "dashboards":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "documents":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "duplicateRules":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "email":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "emailservices":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "entitlementProcesses":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "escalationRules":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "experiences":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "flexipages":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "flows":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "forecastingTypes":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "globalValueSets":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "groups":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "homePageLayouts":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "iframeWhiteListUrlSettings":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "labels":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "layouts":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "letterhead":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "lightningExperienceThemes":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
            
            if foldercomponent == "lwc":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "Canvases":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "managedContentTypes":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "managedTopics":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "matchingRules":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "milestoneTypes":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "moderation":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                
            if foldercomponent == "namedCredentials":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "navigationMenus":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "networkBranding":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "networks":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "notificationTypeConfig":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "notificationtypes":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "objects":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "objectTranslations":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "pages":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "pathAssistants":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "permissionsetgroups":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "permissionsets":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "presenceUserConfigs":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "profiles":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "queueRoutingConfigs":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "queues":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "quickActions":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "remoteSiteSettings":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "reports":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "reportTypes":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "roles":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "serviceChannels":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "servicePresenceStatuses":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "settings":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "sharingRules":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "sharingSets":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "sites":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "standardValueSets":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "standardValueSetTranslations":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "staticresources":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "tabs":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "topicsForObjects":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "translations":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "triggers":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "userCriteria":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]

            if foldercomponent == "workflows":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
            
            # Agrega los resultados a la lista
            results.append({"foldercomponent": foldercomponent,"item": item})

    return results


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
    
    # Llama a la función leer_diff_txt y guarda los resultados
    results = leer_diff_txt()

    # Imprime todos los resultados al final
    print("Resultados finales:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()