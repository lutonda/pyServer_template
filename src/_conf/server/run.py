from src._conf.server import config
if __name__ == "__main__":
    app.run(
        host=config.host
        , port=config.port
        , debug=config.debug)