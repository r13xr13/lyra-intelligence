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
        """
        Perform WHOIS lookup using WhoisXMLAPI with an API key.

        NOTE:
        Replace `api_key` with your own API key from WhoisXMLAPI.
        Protect your key; do NOT commit it in public repos.
        """
        print(f"[DEBUG] whois() called with domain: {domain}")
        api_key = "1324574732u2bheuwe933u3j32823j"  # Insert your actual API key here
        url = (
            f"https://www.whoisxmlapi.com/whoisserver/WhoisService?"
            f"apiKey={api_key}&domainName={domain}&outputFormat=JSON"
        )
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                print(f"[+] WHOIS data for {domain}:")
                registrar = data.get("WhoisRecord", {}).get("registrarName", "N/A")
                creation_date = data.get("WhoisRecord", {}).get("createdDate", "N/A")
                print(f"    Registrar: {registrar}")
                print(f"    Created On: {creation_date}")
                # Extend here: add printing more fields as desired
            else:
                print(f"[-] Failed to retrieve WHOIS info (Status: {response.status_code})")
        except Exception as e:
            print(f"[-] WHOIS request failed: {e}")
