#! /usr/bin/python3
import tempfile
import pytest

from unopartylib.test import conftest  # this is require near the top to do setup of the test suite
from unopartylib.test import util_test
from unopartylib.test.util_test import CURR_DIR
from unopartylib import server
from unopartylib.lib import (config, check, database)


def test_book(testnet):
    """Reparse all the transactions in the database to see check blockhain's integrity."""
    util_test.reparse(testnet=testnet)
