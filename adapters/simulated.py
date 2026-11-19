"""In-memory adapter only; never performs a real deployment."""
from core.artifact import verify


class SimulatedDeployment:
    def __init__(self):
        self.active = None
        self.digest = None
        self.previous = None

    @staticmethod
    def health(value):
        return value["routes"]["/health"] == "ok" and value["routes"]["/"].endswith(value["version"])

    def deploy(self, data, expected_digest, *, authorized=False, fail_health=False):
        if not authorized:
            raise PermissionError("explicit simulation authorization required")
        value = verify(data, expected_digest)
        if fail_health or not self.health(value):
            raise ValueError("candidate health failed; active state unchanged")
        self.previous = (self.active, self.digest)
        self.active, self.digest = data, expected_digest
        return value

    def rollback(self, *, authorized=False):
        if not authorized:
            raise PermissionError("explicit simulation rollback authorization required")
        if self.previous is None or self.previous[0] is None:
            raise ValueError("no verified baseline")
        data, expected = self.previous
        value = verify(data, expected)
        if not self.health(value):
            raise ValueError("baseline unhealthy; rollback refused")
        self.active, self.digest = data, expected
        self.previous = None
        return value
