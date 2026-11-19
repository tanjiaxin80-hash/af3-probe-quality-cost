"""Verify this release's SHA-256 manifest, using only the standard library."""
from pathlib import Path
import hashlib

root = Path(__file__).resolve().parent
checked = 0
for line in (root / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
    digest, name = line.split("  ", 1)
    path = (root / name).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise SystemExit("Missing or invalid manifest entry: " + name)
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise SystemExit("SHA-256 mismatch: " + name)
    checked += 1
print("Verified SHA-256 for " + str(checked) + " files.")
