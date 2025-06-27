import socket
import requests

class Plugin:
    def handle(self, cmd):
        tokens = cmd.strip().split()

        if len(tokens) < 3 or tokens[0] != "osint":
            return False  # Not meant for this plugin

        action, target = tokens[1], tokens[2]
        print(f"[DEBUG] OSINT plugin received: {action} {target}")

        if action == "recon":
            self.recon(target)
        elif action == "resolve":
            self.resolve(target)
        elif action == "whois":
            self.whois(target)
        else:
            print(f"[!] Unknown OSINT action: {action}")
            return False

        return True

    def recon(self, domain):
        print(f"[DEBUG] recon() called with domain: {domain}")
        self.resolve(domain)
        self.whois(domain)

    def resolve(self, domain):
        print(f"[DEBUG] resolve() called with domain: {domain}")
        try:
            ip = socket.gethostbyname(domain)
            print(f"[+] {domain} resolves to {ip}")
        except Exception as e:
            print(f"[-] DNS resolution failed: {e}")

    def whois(self, domain):
        print(f"[DEBUG] whois() called with domain: {domain}")
        try:
            response = requests.get(f"https://api.hackertarget.com/whois/?q={domain}", timeout=10)
            if response.status_code == 200:
                print(response.text)
            else:
                print(f"[-] Failed to retrieve WHOIS info (Status: {response.status_code})")
        except Exception as e:
            print(f"[-] WHOIS request failed: {e}")
