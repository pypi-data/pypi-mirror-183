import subprocess

def https_router(port: int = 8000, workers: int = 4):
    subprocess.run([
        "uvicorn",
        "eudata_server.tools.https:app",
        f"--port={port}",
        "--host=0.0.0.0",
        f"--workers {workers}"
    ])