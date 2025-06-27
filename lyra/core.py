import importlib

class PluginManager:
    def __init__(self):
        self.plugins = {}
        for name in ["osint", "scan"]:
            self.load(name)

    def load(self, name):
        try:
            module = importlib.import_module(f"lyra.plugins.{name}")
            self.plugins[name] = module.Plugin()
            print(f"[+] Loaded plugin: {name}")
        except Exception as e:
            print(f"[!] Failed to load plugin '{name}': {e}")

    def dispatch(self, cmd):
        for plugin in self.plugins.values():
            if hasattr(plugin, "handle") and plugin.handle(cmd):
                return
        print("[!] Unknown command or plugin not loaded.")
