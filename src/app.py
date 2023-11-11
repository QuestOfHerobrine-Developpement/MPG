import os
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pocketmine-MP plug-in generator")
        self.geometry("360x240")
        self.resizable(False, False)
        self.configure(bg="#595656")
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
        self.iconbitmap(default=icon_path)

        self.name = ttk.Entry(self, font=("Arial", 15), style="TEntry")
        self.name.insert(0, "Plug-in name")
        self.name.pack(pady=5)

        self.description = ttk.Entry(self, font=("Arial", 15), style="TEntry")
        self.description.insert(0, "Plug-in description")
        self.description.pack(pady=5)

        self.author = ttk.Entry(self, font=("Arial", 15), style="TEntry")
        self.author.insert(0, "Plug-in author")
        self.author.pack(pady=5)

        self.version = ttk.Entry(self, font=("Arial", 15), style="TEntry")
        self.version.insert(0, "Plug-in version")
        self.version.pack(pady=5)

        self.api = ttk.Entry(self, font=("Arial", 15), style="TEntry")
        self.api.insert(0, "Plug-in api")
        self.api.pack(pady=5)

        self.generate_button = tk.Button(self, text="Generate", font=("Arial", 15), command=self.generate)
        self.generate_button.pack()

    def generate(self, event=None):
        name = self.name.get()
        description = self.description.get()
        author = self.author.get()
        version = self.version.get()
        api = self.api.get()

        name_plugin = name
        src_folder = os.path.join(name_plugin, "src")
        plugin_yml = os.path.join(name_plugin, "plugin.yml")
        config_fol = os.path.join(name_plugin, "resources")
        config_yml = os.path.join(config_fol, "config.yml")
        nameplugin_folder2 = os.path.join(src_folder, name_plugin)
        authorname = os.path.join(nameplugin_folder2, author)
        main_php = os.path.join(authorname, "Main.php")

        os.mkdir(name_plugin)
        os.mkdir(src_folder)
        os.mkdir(config_fol)
        os.mkdir(nameplugin_folder2)
        os.mkdir(authorname)

        with open(plugin_yml, "w") as file:
            file.write("name: " + name + "\n")
            file.write("description: " + description + "\n")
            file.write("author: [ PluginGenerator," + author + " ]\n")
            file.write("version: " + version + "\n")
            file.write("api: " + api + "\n")
            file.write("main: " + name_plugin + "\\" + author + "\\Main" + "\n")

        with open(main_php, "w") as file:
            file.write("<?php\n")
            file.write("\n")
            file.write("namespace " + name_plugin + "\\" + author + ";\n")
            file.write("\n")
            file.write("use pocketmine\\utils\\SingletonTrait;\n")
            file.write("use pocketmine\\plugin\\PluginBase;\n")
            file.write("\n")
            file.write("class Main extends PluginBase {\n")
            file.write("    use SingletonTrait;\n")
            file.write("\n")
            file.write("    public function onEnable(): void {\n")
            file.write("        self::setInstance($this);\n")
            file.write("        $this->getLogger()->notice(\"" + name_plugin + " successfully activated\");\n")
            file.write("        $this->saveDefaultConfig();\n")
            file.write("    }\n")
            file.write("}\n")
