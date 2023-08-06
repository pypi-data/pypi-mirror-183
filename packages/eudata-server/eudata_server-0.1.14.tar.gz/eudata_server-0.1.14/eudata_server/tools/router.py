import subprocess

def https_router(port: int, workers: int = 4):
    subprocess.run([
        "rhttps", "-p", f"{port}", "-w", f"{workers}"
    ], shell=True
    )