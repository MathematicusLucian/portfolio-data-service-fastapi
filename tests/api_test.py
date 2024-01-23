from fastapi.testclient import TestClient
import unittest

# Modules used by the app
import logging
import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from src.app.main import app

client = TestClient(app)

def test_main_resource():
    response_auth = client.get("/")
    assert response_auth.status_code == 200

def test_child_resource():
    response_auth = client.get("/api/v1/test")
    assert response_auth.status_code == 200