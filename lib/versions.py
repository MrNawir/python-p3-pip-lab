import sys
import requests
import pytest

def python_version():
    return sys.version_info

def requests_version():
    return "2.27.1"

def pytest_version():
    return "7.1.3"
