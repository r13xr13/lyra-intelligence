import importlib

class PluginManager:
    def __init__(self):
        self.plugins = {}

    def load(self, name):
        try:
            module = importlib.import_module(f"lyra.plugins.{name}")
            self.plugins[name] = module.Plugin()
            print(f"[+] Loaded {name}")
        except Exception as e:
            print(f"[!] Failed to load plugin {name}: {e}")

    def dispatch(self, cmd):
        if cmd.startswith("load "):
            _, name = cmd.split(maxsplit=1)
            self.load(name)
        else:
            for plugin in self.plugins.values():
                if hasattr(plugin, "handle"):
                    plugin.handle(cmd)
