import unittest
from core.artifact import build, digest, verify
from adapters.simulated import SimulatedDeployment


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.v1, self.v2 = build("v1"), build("v2")
        self.adapter = SimulatedDeployment()

    def baseline(self):
        self.adapter.deploy(self.v1, digest(self.v1), authorized=True)

    def test_deterministic(self):
        self.assertEqual(build("v1"), build("v1"))

    def test_schema_and_routes(self):
        self.assertEqual(verify(self.v1, digest(self.v1))["routes"], {"/": "synthetic v1", "/health": "ok"})

    def test_deploy_health_rollback(self):
        self.baseline()
        self.adapter.deploy(self.v2, digest(self.v2), authorized=True)
        self.assertEqual(self.adapter.digest, digest(self.v2))
        self.assertEqual(self.adapter.rollback(authorized=True)["version"], "v1")
        self.assertEqual(self.adapter.active, self.v1)

    def test_corruption_is_atomic(self):
        self.baseline()
        with self.assertRaises(ValueError):
            self.adapter.deploy(self.v2 + b"corrupt", digest(self.v2), authorized=True)
        self.assertEqual(self.adapter.active, self.v1)

    def test_health_failure_is_atomic(self):
        self.baseline()
        with self.assertRaises(ValueError):
            self.adapter.deploy(self.v2, digest(self.v2), authorized=True, fail_health=True)
        self.assertEqual(self.adapter.active, self.v1)

    def test_unauthorized_rejected(self):
        with self.assertRaises(PermissionError):
            self.adapter.deploy(self.v1, digest(self.v1))
        self.assertIsNone(self.adapter.active)

    def test_missing_baseline_rejected(self):
        with self.assertRaises(ValueError):
            self.adapter.rollback(authorized=True)

    def test_rollback_authorization(self):
        self.baseline()
        self.adapter.deploy(self.v2, digest(self.v2), authorized=True)
        with self.assertRaises(PermissionError):
            self.adapter.rollback()
        self.assertEqual(self.adapter.active, self.v2)

    def test_unknown_schema_even_with_matching_hash(self):
        data = b'{"version":"v1","schema":99}\n'
        with self.assertRaises(ValueError):
            verify(data, digest(data))


if __name__ == "__main__":
    unittest.main()
