import os
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

#SETTINGS
DEVICES_FILE = "devices_cisco.yaml"
TEMPLATE_FILE = "cisco_template.txt"
OUTPUT_DIR = "output_cisco"


#LOAD DEVICES FROM YAML (READ YAML FILE)
def load_devices(yaml_path: str):
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) #dictionary / key-value

    routers = data.get("routers", [])
    if not routers:
        raise ValueError("No routers found in devices_cisco.yaml")

    return routers


#PREPARE JINJA2 ENVIRONMENT (LOAD THE TEMPLATE BY JINJA2 LIB)
def get_template(template_path: str):
    env = Environment(
        loader=FileSystemLoader(searchpath="."),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env.get_template(template_path)


#GENERATE OSPF CONFIG FOR EACH ROUTER
def generate_config_for_router(router: dict, template, output_dir: Path):
    hostname = router["hostname"]
    loopback_ip = router["loopback_ip"]
    loopback_mask = router["loopback_mask"]
    router_id = router["router_id"]
    interfaces = router.get("interfaces", [])

    rendered = template.render(
        hostname=hostname,
        loopback_ip=loopback_ip,
        loopback_mask=loopback_mask,
        router_id=router_id,
        interfaces=interfaces,
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    out_file = output_dir / f"{hostname}.cfg"

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(rendered)

    return out_file


#MAIN (DRY RUN)
def main():
    print("=== CISCO IOS OSPF CONFIG GENERATOR (DRY RUN) ===")
    print(f"Working directory: {os.getcwd()}")

    routers = load_devices(DEVICES_FILE)
    print(f"Loaded {len(routers)} routers from {DEVICES_FILE}")

    template = get_template(TEMPLATE_FILE)

    output_dir = Path(OUTPUT_DIR)
    generated_files = []

    for router in routers:
        out_file = generate_config_for_router(router, template, output_dir)
        generated_files.append(out_file)
        print(f"Generated config for {router['hostname']} -> {out_file}")

    print("\nGeneration completed successfully.")
    print(f"Total configs: {len(generated_files)}")
    print(f"Output directory: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
