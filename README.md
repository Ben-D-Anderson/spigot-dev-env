# spigot-dev-env

This repository provides scripts to automatically compile all Spigot and CraftBukkit versions using Spigot's BuildTools - which will also install them all to your local maven repository (with NMS API included).
The `servinstall.py` script will also create servers for all Minecraft versions and the `pluginstall.py` script can be used to install a Minecraft plugin jar to the `plugins` folder of all the servers.

## Usage
First clone this git repository to your computer by running the following command:
```bash
git clone https://github.com/Ben-D-Anderson/spigot-dev-env.git
```

Navigate into the created folder `spigot-dev-env` with the following command:
```bash
cd spigot-dev-env
```

Ensure you follow the necessary steps for your operating system as described by the [Spigot BuildTools prerequisites](https://www.spigotmc.org/wiki/buildtools/#prerequisites).

Open `config.json` and set the paths to the java executable files on your system for each java version in the `java_versions` section.
Java 8 is required to build versions up to (but not including) 1.17 and Java 16 is required for all higher versions (including 1.17).

Example for Windows:
```json
"java_versions":{
  "8":"C:\\Windows\\Program Files\\Java\\jre1.8.0_221\\bin\\java.exe",
  "16":"C:\\Windows\\Program Files\\Java\\jre16.0.2\\bin\\java.exe"
}
```

Example for Unix:
```json
"java_versions":{
  "8":"/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java",
  "16":"/usr/lib/jvm/java-16-openjdk-amd64/bin/java"
}
```

Paths will vary for each user so make sure you locate your Java installations and update the `config.json` accordingly.

You can now build all the Spigot and Craftbukkit versions referenced in the `config.yml` under the `mc_versions` section using the following command:
```bash
python3 servinstall.py
```
This command will create Minecraft servers for all installed Spigot versions, and place them in the `servers` directory - this can make testing a multi-version plugin much easier.
It will also install the Spigot and CraftBukkit versions with the NMS API to your local maven repository so they can be easily referenced in your `pom.xml` during plugin development.
See the following example for 1.8:
```xml
<dependency>
    <groupId>org.bukkit</groupId>
    <artifactId>craftbukkit</artifactId>
    <version>1.8-R0.1-SNAPSHOT</version>
    <scope>provided</scope>
</dependency>
<dependency>
    <groupId>org.spigotmc</groupId>
    <artifactId>spigot-api</artifactId>
    <version>1.8-R0.1-SNAPSHOT</version>
    <scope>provided</scope>
</dependency>
```
The `servinstall.py` script uses BuildTools to compile Spigot and CraftBukkit and can take a long time as a result, on my machine it took a total of ~50 minutes for all versions to be installed.

A script has also been provided in this repository to effortlessly deploy a Minecraft plugin to all of the generated servers using the following command:
```bash
python3 pluginstall.py <plugin_jar_path>
```
The `pluginstall.py` script simply copies the plugin specified into the `plugins` folder of each folder in the `servers` folder.

A script has also been provided in this repository to effortlessly remove a Minecraft plugin from all of the generated servers using the following command:
```bash
python3 plugdelete.py <plugin_jar_name>
```
The `plugdelete.py` script simply deletes the plugin specified from the `plugins` folder of each folder in the `servers` folder.
