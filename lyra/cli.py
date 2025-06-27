import sys
from lyra.core import PluginManager

def main():
    pm = PluginManager()

    # 🔍 Check for command-line args
    if len(sys.argv) > 1:
        # Example: python3 -m lyra.cli osint recon example.com
        command = " ".join(sys.argv[1:])
        pm.dispatch(command)
        return

    # 🧠 Fallback: Interactive shell
    while True:
        try:
            cmd = input("lyra> ").strip()
            if cmd.lower() in ("exit", "quit"):
                break
            pm.dispatch(cmd)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
