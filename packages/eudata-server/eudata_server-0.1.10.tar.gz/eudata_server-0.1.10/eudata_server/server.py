import os
import sys
import json
import rich
import uvicorn

from rich.console import Console
from rich.prompt import Prompt, Confirm

from eudata_server.tools.paths import package_dir

console = Console(markup=True)

config = json.load(open(package_dir / "config.json", "r"))

def develop():
    uvicorn.run("eudata_server.api:app", reload=True)

def run(workers=4):
    uvicorn.run(
        "eudata_server.api:app",
        workers=workers,
        host=config["server"]["host"],
        port=config["server"]["port"],
        log_level="info",
        )

def run_ssl(workers=4):
    if len(sys.argv) > 1:
        keyfile = sys.argv[1]
    if len(sys.argv) > 2:
        certfile = sys.argv[2]
    console.print(f"[dim magenta]Default keyfile: [/][yellow]{config['ssl']['ssl_key']}[/]")
    console.print(f"[dim magenta]Default keyfile: [/][yellow]{config['ssl']['ssl_cert']}[/]")
    
    ok = Confirm.ask(f"[bold magenta] Use default credentials ?[/]")

    if ok:
        keyfile = config["ssl"]["ssl_key"]
        certfile = config["ssl"]["ssl_cert"]
    else:
        keyfile = Prompt.ask("[bold magenta] Enter [yellow]SSL key[/] file path[/]", default=config["ssl"]["ssl_key"])
        certfile = Prompt.ask("[bold magenta] Enter [yellow]SSL cert[/] file path[/]", default=config["ssl"]["ssl_cert"])
        save = Confirm.ask("[bold yellow] Save config?[/]")
    
    if save:
        config["ssl"]["ssl_key"] = keyfile
        config["ssl"]["ssl_cert"] = certfile
        json.dump(config, open(package_dir / "config.json", "w"), indent=4)

    console.print(f"🚀🚀 [bold red]Starting server[/] [magenta]with {workers} workers[/]")

    uvicorn.run(
        "eudata_server.api:app",
        workers=workers,
        host=config["server"]["host"],
        port=config["server"]["port"],
        log_level="info",
        ssl_keyfile=keyfile,
        ssl_certfile=certfile,
        )

if __name__ == "__main__":
    develop()