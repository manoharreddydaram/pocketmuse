# tests/test_smoke.py
# Simple smoke test that makes the package importable for CI/local checks.
# We add the repo root to sys.path so pytest can import 'app' reliably.

import sys, os, importlib

# Ensure repo root (one level up from tests/) is on sys.path
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

def test_import_app_package():
    # This should import the module file without instantiating any client.
    # Avoids contacting external APIs during import.
    importlib.import_module("app.llm_client")
