"""Deterministic synthetic artifact. No network or deployment credentials."""
import hashlib
import json


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def build(version):
    if version not in ("v1", "v2"):
        raise ValueError("unsupported synthetic version")
    return encode({"schema": 1, "version": version, "routes": {"/": "synthetic " + version, "/health": "ok"}})


def verify(data, expected_digest):
    if not isinstance(expected_digest, str) or len(expected_digest) != 64 or digest(data) != expected_digest:
        raise ValueError("artifact SHA-256 mismatch")
    value = json.loads(data)
    if value != json.loads(build(value.get("version"))):
        raise ValueError("unexpected artifact schema or contents")
    return value
