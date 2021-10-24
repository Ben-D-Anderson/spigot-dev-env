from shutil import copy
import sys
import os

if len(sys.argv) < 2:
    print('Error: No plugin jar supplied, please pass it as an argument to the program.')
    print('Usage: python3 pluginstall.py <plugin_jar>')
    exit()

plugin_jar = sys.argv[1]
if not os.path.exists(plugin_jar):
    print('Error: Could not find plugin jar "' + plugin_jar + '"')
    exit()

servers_dir = os.path.join(os.getcwd(), 'servers')
servers = os.listdir(servers_dir)
for server in servers:
    if os.path.isdir(os.path.join(servers_dir, server)):
        plugins_directory = os.path.join(servers_dir, server, 'plugins')
        if not os.path.isdir(plugins_directory):
            os.mkdir(plugins_directory)
        copy(plugin_jar, plugins_directory)

print('Plugin successfully installed to all servers.')