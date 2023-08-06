import uvicorn

config_ssl = {
    "ssl_key":"/etc/letsencrypt/live/api.veletanlic.com/privkey.pem",
    "ssl_cert":"/etc/letsencrypt/live/api.veletanlic.com/fullchain.pem",
    }

def develop():
    uvicorn.run("eudata_server.api:app", reload=True)

def run(workers=4):
    uvicorn.run(
        "eudata_server.api:app",
        workers=workers,
        host="0.0.0.0",
        port=8000,
        log_level="info",
        )

def run_ssl(workers=4):
    uvicorn.run(
        "eudata_server.api:app",
        workers=workers,
        host="0.0.0.0",
        port=8000,
        log_level="info",
        ssl_keyfile=config_ssl["ssl_key"],
        ssl_certfile=config_ssl["ssl_cert"],
        )

if __name__ == "__main__":
    serve()