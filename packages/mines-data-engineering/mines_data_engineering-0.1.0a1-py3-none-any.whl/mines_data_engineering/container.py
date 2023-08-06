from spython.main import get_client

class Service:
    container: str

    def __init__(self):
        self.client = get_client()

    def start(self):
        self.client.pull(image=self.container)

    def run(self):
        raise NotImplementedError

class MongoDB(Service):
    container = "docker://mongo:latest"

    def __init__(self):
        super().__init__()

    def run(self):
        self.client.run(image=self.container, writable=True, bind="/tmp:/data/db")
