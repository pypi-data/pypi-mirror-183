from .app import app


def entrypoint():
    app.main(auto_envvar_prefix=app.envname)
