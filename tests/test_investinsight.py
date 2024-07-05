from fastapi.testclient import TestClient
from investinsight.app import app

client = TestClient(app)