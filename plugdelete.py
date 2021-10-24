import sys
import os

if len(sys.argv) < 2:
    print('Error: No plugin jar specified, please pass it as an argument to the program.')
    print('Usage: python3 pluginstall.py <plugin_jar_name>')
    exit()

plugin_jar = sys.argv[1]
servers_dir = os.path.join(os.getcwd(), 'servers')
servers = os.listdir(servers_dir)
servers.sort()
for server in servers:
    if os.path.isdir(os.path.join(servers_dir, server)):
        plugins_directory = os.path.join(servers_dir, server, 'plugins')
        if not os.path.isdir(plugins_directory):
            os.mkdir(plugins_directory)
        plugin_file = plugins_directory + '/' + plugin_jar
        if os.path.exists(plugin_file):
            os.remove(plugin_file)
            print('[-] Plugin jar "' + plugin_jar + '" deleted from server ' + server)
        else:
            print('[!] Plugin jar "' + plugin_jar + '" not found in server ' + server)