import subprocess

def https_router(port: int = 4000, workers: int = 4, shell: bool = False):
    subprocess.Popen([
        "rhttps", "-p", f"{port}", "-w", f"{workers}"
    ])