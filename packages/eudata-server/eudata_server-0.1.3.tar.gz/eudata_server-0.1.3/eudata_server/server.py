import os
import json
import uvicorn

from eudata_server.tools.paths import package_dir

config = json.load(open(package_dir / "config.json", "r"))

print(config)

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
    uvicorn.run(
        "eudata_server.api:app",
        workers=workers,
        host=config["server"]["host"],
        port=config["server"]["port"],
        log_level="info",
        ssl_keyfile=config["ssl"]["ssl_key"],
        ssl_certfile=config_ssl["ssl"]["ssl_cert"],
        )

if __name__ == "__main__":
    develop()