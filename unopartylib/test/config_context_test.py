#! /usr/bin/python3
import pprint
import tempfile
from unopartylib.test import conftest  # this is require near the top to do setup of the test suite
from unopartylib.test.fixtures.params import DEFAULT_PARAMS as DP
from unopartylib.test import util_test
from unopartylib.test.util_test import CURR_DIR

from unopartylib.lib import (blocks, config, util)


FIXTURE_SQL_FILE = CURR_DIR + '/fixtures/scenarios/parseblock_unittest_fixture.sql'
FIXTURE_DB = tempfile.gettempdir() + '/fixtures.parseblock_unittest_fixture.db'


def test_config_context(cp_server):
    assert config.BTC_NAME == "Unobtanium"

    with util_test.ConfigContext(BTC_NAME="Unobtanium Testing"):
        assert config.BTC_NAME == "Unobtanium Testing"

        with util_test.ConfigContext(BTC_NAME="Unobtanium Testing Testing"):
            assert config.BTC_NAME == "Unobtanium Testing Testing"

        assert config.BTC_NAME == "Unobtanium Testing"

    assert config.BTC_NAME == "Unobtanium"


def test_mock_protocol_changes(cp_server):
    assert util.enabled('multisig_addresses') == True

    with util_test.MockProtocolChangesContext(multisig_addresses=False):
        assert util.enabled('multisig_addresses') == False

        with util_test.MockProtocolChangesContext(multisig_addresses=None):
                assert util.enabled('multisig_addresses') == None

        assert util.enabled('multisig_addresses') == False

    assert util.enabled('multisig_addresses') == True
