from lyra.core import PluginManager

def main():
    pm = PluginManager()
    while True:
        try:
            cmd = input("lyra> ").strip()
            if cmd in ("exit", "quit"):
                break
            pm.dispatch(cmd)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
