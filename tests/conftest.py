import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--local", action="store_true", help="Run tests on real Internet Box in same network"
    )
