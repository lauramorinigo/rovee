import pytest
import sys
import os

# Ensure Python can find app.py in the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app as flask_app

@pytest.fixture
def client():
    # Configure app for testing
    flask_app.config['TESTING'] = True
    
    # Create a fresh client for every test
    with flask_app.test_client() as client:
        yield client