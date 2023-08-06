from clickmod.middleware import RequestMiddleware, Request
from clickmod.errors import ApiError

from .auth import rebuild_token


class NonceMiddleware(RequestMiddleware):
    def handle(self, request: Request):
        max_attempts, attempts = 2, 1
        while True:
            try:
                return self.next(request)
            except ApiError as e:
                if e.data.get('code') != 'AUTH_NONCE' or attempts == max_attempts:
                    raise
                # TODO: What if nonce isn't there?
                nonce = e.data['nonce']
                token = request.headers['Authorization'].split()[1].strip()
                token = rebuild_token(token, nonce)
                request.headers['Authorization'] = f"Bearer {token}"
                attempts += 1
                continue
            except Exception:
                raise
