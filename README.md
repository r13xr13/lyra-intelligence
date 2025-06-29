# apt‑lyra‑core

> 🤖 **AI-Enhanced Operator Framework**  
> A modular command-line intelligence system built for cybernetic workflows, ethical automation, and autonomous recon operations.

---

## 🧬 What is APT-LYRA-CORE?

**`apt-lyra-core`** is your tactical command surface a modular, AI-integrated CLI framework designed for professional operators, researchers, devs, and security detals.

It acts as a **local automation harness** for reconnaissance, scanning, and future modules like adversary simulation, all while respecting boundaries and emphasizing **safe, transparent operation**.

Crafted for **offline-first** and **airgapped security labs**, LYRA empowers you to:

- Run OSINT tasks without browser clutter  
- Build, load, and extend plugins for new workflows  
- Integrate with local LLMs for autonomous CLI reasoning  
- Enforce strict ethical control: no exploits, no payloads (Exploit & Payload Plugins are available for professional use only)

> Think of it as your **autonomous security companion** modular, scriptable, and fully yours to command.

---

## 🚀 Features

- 🧩 **Modular plugin system** Easily expand with your own tools  
- 🔎 **OSINT engine** Domain recon, DNS resolution, WHOIS lookups  
- 🧠 **AI-ready interface** Built for future integration with LLM agents  
- 🛡️ **Safe-mode architecture** Zero offensive payloads or exploits  
- 🔧 **Offline capable** No hidden telemetry, no cloud lock-in  

---

## 🔍 Live Recon in Action

> LYRA executing an OSINT recon on `walmart.com` using embedded plugins inside the Exegol container runtime:

![LYRA Recon Screenshot](https://raw.githubusercontent.com/r13xr13/apt-lyra-core/main/assets/lyra.png)

🧩 Plugins active:
- `osint`: Resolves domain, fetches WHOIS
- `scan`: (extendable) for active service mapping

💡 Command used:
```bash
PYTHONPATH=. python3 -m lyra.cli

## 🔐 WHOIS API Key Required

The OSINT module supports WHOIS lookups via [WhoisXMLAPI](https://user.whoisxmlapi.com/products), and **requires an API key**.

### ⚙️ How to enable WHOIS:

1. Register and obtain your free or paid API key from WhoisXMLAPI  
2. Open `lyra/plugins/osint.py`  
3. Replace the placeholder inside the `whois()` method:

```python
api_key = "YOUR_API_KEY_HERE"

(Optional) For safer key handling:

Export your key as an environment variable:

export WHOIS_API_KEY="your_actual_key"

Modify the code to read the key:

import os
api_key = os.getenv("WHOIS_API_KEY")

---

📦 Installation

git clone https://github.com/r13xr13/apt-lyra-core.git
cd apt-lyra-core
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

⚡ Usage

Start the CLI interface:

PYTHONPATH=. python3 -m lyra.cli

Once inside the lyra> shell, try:

osint recon example.com
osint resolve example.com
osint whois example.com

🧠 Extend It

The plugins/ directory is yours. Clone an existing module, rename it, and add your custom logic.

To create a new plugin:

Add a Python file in lyra/plugins/

Define a Plugin class with a handle(self, cmd) method

LYRA will auto-load and dispatch it at startup

📡 Coming Soon

Autonomous GPT-based recon flows

Real-time vulnerability triage from local logs

Threat actor pattern matching

CLI-triggered browserless crawling

🧭 Philosophy

LYRA is built for agency and transparency.
You control the stack.
You own the data.
You shape the intelligence.

-r13
