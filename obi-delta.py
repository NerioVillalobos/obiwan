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
                foldercomponent = "ApexEmailNotifications"   #Chequeado

            if foldercomponent == "applications":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "CustomApplication"     #Chequeado

            if foldercomponent == "approvalProcesses":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "ApprovalProcess"     #Chequeado

            if foldercomponent == "assignmentRules":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "AssignmentRules"    #Chequeado

            if foldercomponent == "audience":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Audience"

            if foldercomponent == "aura":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "AuraDefinitionBundle"

            if foldercomponent == "autoResponseRules":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "AutoResponseRules"
            
            if foldercomponent == "brandingSets":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "BrandingSet"

            if foldercomponent == "campaignInfluenceModels":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "CampaignInfluenceModel"

            if foldercomponent == "Canvases":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "CanvasMetadata"
        

            # Si el nombre de la carpeta es "classes"
            if foldercomponent == "classes":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "ApexClass"

            if foldercomponent == "communities":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Community"

            if foldercomponent == "components":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "ApexComponent"

            if foldercomponent == "connectedApps":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "ConnectedApp"

            if foldercomponent == "contentassets":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "ContentAsset"

            if foldercomponent == "corsWhitelistOrigins":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "CorsWhitelistOrigin"

            if foldercomponent == "cspTrustedSites":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "CspTrustedSite"

            if foldercomponent == "customMetadata":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "CustomMetadata"

            if foldercomponent == "customPermissions":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "CustomPermission"

            if foldercomponent == "dashboards":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Dashboard"

            if foldercomponent == "documents":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Document"

            if foldercomponent == "duplicateRules":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "DuplicateRule"

            if foldercomponent == "email":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "EmailTemplate"

            if foldercomponent == "emailservices":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "EmailServicesFunction"

            if foldercomponent == "entitlementProcesses":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "EntitlementProcess"

            if foldercomponent == "escalationRules":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "EscalationRules"

            if foldercomponent == "experiences":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "ExperienceBundle"

            if foldercomponent == "flexipages":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "FlexiPage"

            if foldercomponent == "flows":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Flow"

            if foldercomponent == "forecastingTypes":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "ForecastingType"

            if foldercomponent == "globalValueSets":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "GlobalValueSet"

            if foldercomponent == "groups":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Group"

            if foldercomponent == "homePageLayouts":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "HomePageLayout"

            if foldercomponent == "iframeWhiteListUrlSettings":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "IframeWhiteListUrlSettings"

            if foldercomponent == "labels":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "CustomLabels"

            if foldercomponent == "layouts":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Layout"

            if foldercomponent == "letterhead":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Letterhead"

            if foldercomponent == "lightningExperienceThemes":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "LightningExperienceTheme"
            
            if foldercomponent == "lwc":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "LightningComponentBundle"

            if foldercomponent == "Canvases":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "CanvasMetadata"

            if foldercomponent == "managedContentTypes":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "ManagedContentType"

            if foldercomponent == "managedTopics":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "ManagedTopics"

            if foldercomponent == "matchingRules":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "MatchingRules"

            if foldercomponent == "milestoneTypes":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "MilestoneType"

            if foldercomponent == "moderation":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "KeywordList"
                
            if foldercomponent == "namedCredentials":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "NamedCredential"

            if foldercomponent == "navigationMenus":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "NavigationMenu"

            if foldercomponent == "networkBranding":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "NetworkBranding"

            if foldercomponent == "networks":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Network"

            if foldercomponent == "notificationTypeConfig":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "NotificationTypeConfig"

            if foldercomponent == "notificationtypes":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "CustomNotificationType"

            if foldercomponent == "objects":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "CustomObject"

            if foldercomponent == "objectTranslations":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "CustomObjectTranslation"

            if foldercomponent == "pages":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "ApexPage"

            if foldercomponent == "pathAssistants":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "PathAssistant"

            if foldercomponent == "permissionsetgroups":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "PermissionSetGroup"

            if foldercomponent == "permissionsets":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "PermissionSet"

            if foldercomponent == "presenceUserConfigs":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "PresenceUserConfig"

            if foldercomponent == "profiles":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Profile"

            if foldercomponent == "queueRoutingConfigs":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "QueueRoutingConfig"

            if foldercomponent == "queues":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Queue"
 
            if foldercomponent == "quickActions":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "QuickAction"

            if foldercomponent == "remoteSiteSettings":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "RemoteSiteSetting"

            if foldercomponent == "reports":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Report"

            if foldercomponent == "reportTypes":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "ReportType"

            if foldercomponent == "roles":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Role"

            if foldercomponent == "serviceChannels":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "ServiceChannel"

            if foldercomponent == "servicePresenceStatuses":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "ServicePresenceStatus"

            if foldercomponent == "settings":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Settings"

            if foldercomponent == "sharingRules":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "SharingRules"

            if foldercomponent == "sharingSets":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "SharingSet"

            if foldercomponent == "sites":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "CustomSite"

            if foldercomponent == "standardValueSets":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "StandardValueSet"

            if foldercomponent == "standardValueSetTranslations":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "StandardValueSetTranslation"

            if foldercomponent == "staticresources":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "StaticResource"

            if foldercomponent == "tabs":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "CustomTab"

            if foldercomponent == "topicsForObjects":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "TopicsForObjects"

            if foldercomponent == "translations":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Translations"

            if foldercomponent == "triggers":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "ApexTrigger"

            if foldercomponent == "userCriteria":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "UserCriteria"

            if foldercomponent == "workflows":
                # Obtiene el nombre del archivo
                filename = line.split("/")[4]
            
                # Elimina la extensión del archivo
                item = filename.split(".")[0]
                foldercomponent = "Workflow"
            
            # Agrega los resultados a la lista
            results.append({"foldercomponent": foldercomponent,"item": item})

    return results

def transformar_archivo(input_filename, output_filename):
    try:
        data_dict = {}  # Diccionario para almacenar los datos ordenados por tipo
        with open(input_filename, 'r') as input_file:
            for line in input_file:
                # Eliminar los caracteres no deseados y dividir la línea en partes
                line = line.strip('() \n')
                parts = line.split(', ')
                
                # Extraer el valor de 'item' y 'foldercomponent'
                item = parts[1].split("'")[1]
                foldercomponent = parts[0].split("'")[1]
                
                # Agregar el elemento a la lista correspondiente en el diccionario
                if foldercomponent not in data_dict:
                    data_dict[foldercomponent] = []
                data_dict[foldercomponent].append(item)
        
        # Ordenar y escribir en el archivo de salida
        with open(output_filename, 'w') as output_file:
            for foldercomponent, items in sorted(data_dict.items()):
                for item in sorted(items):
                    output_file.write(f"{foldercomponent} -- item : {item}\n")
                
        print(f"La transformación se ha completado con éxito. El resultado se ha guardado en '{output_filename}'.")
    except FileNotFoundError:
        print(f"El archivo '{input_filename}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error durante la transformación: {str(e)}")



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
    #print("Resultados finales:")
    #unique_results = set(tuple(result.items()) for result in results)
    #for result in unique_results:
    #    print(result)

    print("Resultados finales:")
    unique_results = set(tuple(result.items()) for result in results)

    with open("caption1.txt", "w") as file:
        for result in unique_results:
            file.write(str(result) + "\n")

    print("¡Archivo 'caption1.txt' creado exitosamente con los valores de 'result'!")

    
    #input_filename = 'nombre_del_archivo_de_entrada.txt'
    #output_filename = 'nombre_del_archivo_de_salida.txt'
    #transformar_archivo(input_filename, output_filename)

if __name__ == "__main__":
    main()