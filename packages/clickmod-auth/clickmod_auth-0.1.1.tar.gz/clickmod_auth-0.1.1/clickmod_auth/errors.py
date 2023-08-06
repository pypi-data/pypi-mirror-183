from clickmod import ApiError


class RegistrationError(ApiError):
    def _registration_disabled(self):
        self.console.print("Registration is currently [red]temporarily disabled[/red].")

    def _email_unregistered(self):
        self.console.print(
            "The provided [red]email[/red] has [red]not yet been registered[/red] with the OpenPGP key servers."
        )
        self.console.print(
            "Please visit [cyan]https://keys.openpgp.org[/cyan] for information on registering your email and"
            " public key."
        )

    def _duplicate_email(self):
        self.console.print("The provided [red]email[/red] has [red]already been registered[/red].")
        self.console.print(
            "If you [cyan]have[/cyan] the associated private key installed on your machine, you should be able to"
            " access Himitsu straight away."
        )
        self.console.print(
            "If you [cyan]do not have[/cyan] the associated private key installed on your machine, please transfer"
            " the private key to your current machine."
        )

    def _duplicate_public_key(self):
        self.console.print(
            "The [red]public key[/red] associated with the provided email has [red]already has been registered[/red]."
        )
        self.console.print("If you believe this is a [cyan]mistake[/cyan], please contact support.")
