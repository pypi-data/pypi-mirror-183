from contextlib import contextmanager

from gnupg import GPG


@contextmanager
def gnupg():
    gpg = GPG()
    yield gpg
