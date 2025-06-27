import subprocess

class Plugin:
    def handle(self, cmd):
        if cmd.startswith("scan"):
            parts = cmd.split()
            if len(parts) < 2:
                print("[-] Usage: scan <target>")
                return
            target = parts[1]
            self.scan(target)

    def scan(self, target):
        print(f"[+] Initiating scan on: {target}")
        # Example: run nmap scan silently and print results
        try:
            result = subprocess.run(
                ["nmap", "-sV", target], capture_output=True, text=True, timeout=60
            )
            if result.returncode == 0:
                print(result.stdout)
            else:
                print(f"[-] Scan failed with exit code {result.returncode}")
        except Exception as e:
            print(f"[-] Scan execution error: {e}")
