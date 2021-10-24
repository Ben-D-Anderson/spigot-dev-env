import json
import requests
import os
from subprocess import STDOUT, DEVNULL, run

def install_buildtools(directory):
    buildtools = requests.get('https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar')
    with open(os.path.join(directory, 'BuildTools.jar'), "wb") as file:
        file.write(buildtools.content)

def create_eula(directory):
    with open(os.path.join(directory, 'eula.txt'), 'w') as eula:
        eula.write('eula=true')

def create_dir(directory, base_dir='.'):
    directory = os.path.join(base_dir, directory)
    if not os.path.isdir(directory):
        os.mkdir(directory)

def compile_spigot_craftbukkit(directory, mc_version, java_versions):
    java_path = java_versions[mc_version['java_version']]
    minecraft_version = mc_version['minecraft_version']
    run([java_path, '-jar', 'BuildTools.jar', '--compile', 'craftbukkit', '--compile', 'spigot', '--rev', minecraft_version], stdout=DEVNULL, stdin=DEVNULL, stderr=STDOUT, cwd=directory)

def create_server(directory, mc_version, java_versions):
    java_path = java_versions[mc_version['java_version']]
    server_jar = os.path.join(directory, 'spigot-' + mc_version['minecraft_version'] + '.jar')
    run([java_path, '-jar', server_jar, 'nogui'], stdout=DEVNULL, stderr=STDOUT, cwd=directory, input=b'stop\n')

with open('config.json', 'r') as config_file:
    config = json.loads(config_file.read())

current_path = os.getcwd()
java_versions = config['java_versions']
mc_versions = config['mc_versions']
create_dir('servers', base_dir=current_path)

for mc_version in mc_versions:
    print('[' + mc_version['nms_version'] + '] Installing ' + mc_version['minecraft_version'])
    directory = os.path.join(current_path, 'servers', mc_version['nms_version'])
    create_dir(directory)
    install_buildtools(directory)
    print('[' + mc_version['nms_version'] + '] Compiling Spigot and CraftBukkit')
    compile_spigot_craftbukkit(directory, mc_version, java_versions)
    print('[' + mc_version['nms_version'] + '] Creating Server Files')
    create_eula(directory)
    create_server(directory, mc_version, java_versions)
    print('[' + mc_version['nms_version'] + '] Installation Complete')
    print('')
print('--------------------------------------------------------')
print('Spigot Development Environment Installation Finished!')
print('--------------------------------------------------------')