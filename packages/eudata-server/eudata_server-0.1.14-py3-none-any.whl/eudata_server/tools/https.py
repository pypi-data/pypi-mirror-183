import json
import rich
import typer
import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import RedirectResponse

from eudata_server.tools.paths import package_dir

app = FastAPI()
cli = typer.Typer(help="HTTPS redirect tool", no_args_is_help=True)

config = json.load(open(package_dir / "config.json", "r"))

@app.route('/{_:path}')
async def https_redirect(request: Request):
    return RedirectResponse(request.url.replace(scheme='https'))

@cli.command(name='https', help='Run a daemon which allows HTTPS redirect')
def https_redirect(
    port: int = typer.Option(8000, "--port", "-p", help='Port to run the server on'),
    host: str = typer.Option('0.0.0.0', "--host", "-ht",  help='Host to run the server on'),
    workers: int = typer.Option(4, "--workers", "-w", help='Number of workers')
    ) -> None:
    """Run a daemon which allows HTTPS redirect"""
    rich.print(f'[dim magenta]Running redirect [/][bold blue]http ==> https[/][yellow] on port [red]{config["server"]["port"]}[/][/]')
    uvicorn.run('eudata_server.tools.https:app', port=port, host=host, workers=workers)