import subprocess
import sys
import os
import json

def run_git_diff(rama_origen, rama_destino):
    gitcheckout_origen = f"git checkout {rama_origen}"
    gitpull = "git pull"
    gitcheckout_destino = f"git checkout {rama_destino}"
    gitpullorigin_destino = f"git pull origin {rama_destino}"
    
    subprocess.run(gitcheckout_origen, shell=True)
    subprocess.run(gitpull, shell=True)
    subprocess.run(gitcheckout_destino, shell=True)
    subprocess.run(gitpull, shell=True)
    subprocess.run(gitcheckout_origen, shell=True)
    subprocess.run(gitpullorigin_destino, shell=True)

    diff_result = f"git diff --name-only --diff-filter=AMR {rama_origen} {rama_destino} > diff.txt"
    subprocess.run(diff_result, shell=True)

def run_sfdx_command():
    subprocess.run(["sfdx org list metadata-types > metadata.json"], shell=True)

def create_xml_and_yaml(diff_filename, metadata_filename, rama_origen):
    with open(diff_filename, 'r') as diff_file:
        diff_lines = diff_file.read().splitlines()

    with open(metadata_filename, 'r') as metadata_file:
        metadata = json.load(metadata_file)

    members = []
    yaml_data = 'projectPath: ./Vlocity\n'
    yaml_data += 'continueAfterError: true\n'
    yaml_data += 'autoUpdateSettings: true\n'
    yaml_data += '\nmanifest:\n'

    for line in diff_lines:
        if line.startswith('force-app/main/default'):
            parts = line.split('/')
            name1 = parts[4]
            for item in metadata["metadataObjects"]:
                if item['xmlName'] == name1:
                    # Obtén el nombre del archivo sin extensión
                    filename_no_ext = os.path.splitext(name1)[0]
                    members.append(filename_no_ext)
                    yaml_data += f'- {parts[3]}/{filename_no_ext}\n'
                    break

    xml_data = f'<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_data += f'<Package xmlns="http://soap.sforce.com/2006/04/metadata">\n'
    xml_data += f'    <types>\n'
    
    for member in members:
        xml_data += f'        <members>{member}</members>\n'
        
    xml_data += f'        <name>LightningComponentBundle</name>\n'
    xml_data += f'    </types>\n'
    xml_data += f'    <version>57.0</version>\n'
    xml_data += f'</Package>'

    yaml_data += '\nOverrideSettings:\n'
    yaml_data += 'DataPacks:\n'
    yaml_data += 'Catalog:\n'
    yaml_data += 'Product2:\n'
    yaml_data += 'MaxDeploy: 1\n'

    with open(f'{rama_origen}.xml', 'w') as xml_file:
        xml_file.write(xml_data)

    with open(f'{rama_origen}.yaml', 'w') as yaml_file:
        yaml_file.write(yaml_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: script.py <rama_origen> <rama_destino>")
        sys.exit(1)

    rama_origen = sys.argv[1]
    rama_destino = sys.argv[2]

    run_git_diff(rama_origen, rama_destino)
    run_sfdx_command()
    create_xml_and_yaml('diff.txt', 'metadata.json', rama_origen)