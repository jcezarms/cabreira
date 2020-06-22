import requests


class SafeSession(requests.Session):
    """Request session wrapper and handler. Sets global request behaviors.
    """

    def __init__(self):
        super().__init__()
        self.hooks = {
            'response': lambda r, *args, **kwargs: r.raise_for_status()
        }
