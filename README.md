# auto_ospf_config_generator_network_automation
Automated OSPF Configuration Generator for a network topology with Cisco routers. This project built with YAML to store router data, JINJA2 to create generalized configuration template, and Python as orchestrator to generate OSPF configs for each router automatically.

Here are the details:

Automated OSPF Configuration Generator (Cisco IOS)

Python · YAML · Jinja2 · IaC · NetDevOps

This project implements a simple yet structured network automation workflow for generating OSPF configurations for Cisco IOS routers. All router metadata is stored in a YAML inventory file, processed through a Jinja2-based template (stored as a .txt file), and rendered by a Python script into ready-to-use configuration files.

The goal is to demonstrate Infrastructure-as-Code (IaC) principles for network automation in a lab environment: structured data modeling, template-driven configuration, and automated reproducibility.

Features:

- YAML-based router inventory (devices_cisco.yaml)

- Jinja2 OSPF template stored as .txt (cisco_template.txt)

- Python rendering script (generate_cisco_configs.py)

- Auto-generated configs stored in output_cisco/

- Clean separation of data, templates, and logic (modularity)

- Suitable for GNS3, EVE-NG, Cisco Packet Tracer, or CML labs

Project Structure:

project-root/
├── devices_cisco.yaml        # Router definitions & OSPF parameters
├── cisco_template.txt        # Jinja2 template (stored as .txt)
├── generate_cisco_configs.py # Main automation script
├── output_cisco/             # Auto-generated config files
└── README.md


How the Automation Works:

1. Inventory (devices_cisco.yaml)

Contains all device attributes:

hostname

loopback IP + mask

router ID

interface list (name, description, IP/mask, network/wildcard)

2. Template (cisco_template.txt)

Although stored as .txt, this file contains full Jinja2 syntax.
It defines loopback config, interface config, and OSPF process behavior.

3. Python Script (generate_cisco_configs.py)

The script:

- Loads the YAML inventory

- Loads the Jinja2 template

- Renders one configuration per router

- Saves output files under output_cisco/

Key script sections:

- YAML loader

- Jinja2 environment setup

- Per-router rendering function

- Dry-run execution flow

Run with: python generate_cisco_configs.py


Generated files (example):

output_cisco/
├── R1.cfg
├── R2.cfg
└── R3.cfg


About Configuration Deployment (Important):

This project only generates Cisco IOS configurations automatically.
It does not push them to routers, because this repository is designed as a simulation / lab automation demo.

However, in a real environment, automated configuration deployment can easily be added using:

- Netmiko

- Paramiko

- NAPALM

- Nornir

Example deployment snippet:

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.1",
    "username": "admin",
    "password": "admin",
}

config_lines = open("output_cisco/R1.cfg").read().splitlines()

with ConnectHandler(**device) as conn:
    conn.send_config_set(config_lines)
    conn.save_config()


This would allow full automation: SSH connection → push config → save.

Future Enhancements:

Add automatic config deployment (Netmiko / Nornir)

Add input validation + error handling

Multi-area OSPF support

Vendor-agnostic templates (Juniper, Nokia SR OS, Arista)

Unit tests for template rendering

Turn project into a scalable NetDevOps pipeline


Summary: This repository provides a clear, modular, and extendable example of applying Infrastructure-as-Code techniques to network automation. By combining YAML, Jinja2, and Python, it establishes a foundation 





for more advanced automation workflows and multi-vendor configuration engines.

