import click
from clickmod import ClickModApp

from .auth import build_token, resolve_public_key_by_fingerprint
from .middleware import NonceMiddleware
from .errors import RegistrationError


def plugin(app: ClickModApp):
    app.add_request_middleware(NonceMiddleware)

    @app.main.command()
    @click.argument("email")
    def register(email):
        app.api_request("register", "post", {"email": email}, error_class=RegistrationError)

    @app.main.group()
    def public_keys():
        pass

    @public_keys.command("add")
    @click.option("--email", envvar=f"{app.envname}_EMAIL")
    @click.argument("fingerprint")
    def add_public_key(email, fingerprint):
        token = build_token(email)
        public_key = resolve_public_key_by_fingerprint(fingerprint)
        r = app.api_request(
            "publickeys",
            "post",
            {"public_key": public_key},
            headers={"Authorization": f"Bearer {token}"},
        )
        print(r.json())


    @public_keys.command("list")
    @click.option("--email", envvar=f"{app.envname}_EMAIL")
    def list_public_keys(email):
        token = build_token(email)
        r = app.api_request("publickeys", "get", headers={"Authorization": f"Bearer {token}"})
        print(r.json())
