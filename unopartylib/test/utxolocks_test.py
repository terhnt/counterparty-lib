#! /usr/bin/python3
import pytest
import binascii
from io import BytesIO
import bitcoin
import tempfile

from unopartylib.test import conftest  # this is require near the top to do setup of the test suite
from unopartylib.test.util_test import CURR_DIR

from unopartylib.lib import (transaction)
from unopartylib.lib.messages import send


FIXTURE_SQL_FILE = CURR_DIR + '/fixtures/scenarios/parseblock_unittest_fixture.sql'
FIXTURE_DB = tempfile.gettempdir() + '/fixtures.parseblock_unittest_fixture.db'
FIXTURE_OPTIONS = {
    'utxo_locks_max_addresses': 2000
}


def construct_tx(db, source, destination, disable_utxo_locks=False, custom_inputs=None):
    tx_info = send.compose(db, source, destination, 'XUP', 1)
    return transaction.construct(db, tx_info, disable_utxo_locks=disable_utxo_locks, custom_inputs=custom_inputs)


def test_utxolocks(server_db):
    transaction.initialise()  # reset UTXO_LOCKS

    """it shouldn't use the same UTXO"""
    tx1hex = construct_tx(server_db, "uhnfYZMo4KAyWqWtfq4RoaWnnzH889ki22", "uhnfYZMo4KAyWqWtfq4RoaWnnzH889ki22")
    tx2hex = construct_tx(server_db, "uhnfYZMo4KAyWqWtfq4RoaWnnzH889ki22", "uhnfYZMo4KAyWqWtfq4RoaWnnzH889ki22")

    tx1f = BytesIO(binascii.unhexlify(tx1hex))
    tx1 = bitcoin.core.CTransaction.stream_deserialize(tx1f)

    tx2f = BytesIO(binascii.unhexlify(tx2hex))
    tx2 = bitcoin.core.CTransaction.stream_deserialize(tx2f)

    assert (tx1.vin[0].prevout.hash, tx1.vin[0].prevout.n) != (tx2.vin[0].prevout.hash, tx2.vin[0].prevout.n)


def test_utxolocks_custom_input(server_db):
    transaction.initialise()  # reset UTXO_LOCKS

    """it should use the same UTXO"""
    custom_inputs = [{
        'txid': '5f70c1b4b7e55ce7f7a28a2287c95acd2017418b98f730538b8f4078b130f165',
        'txhex': '020000000b656dd7239dd72c754118f78385cc056b769be719d60335268536000000000065f130b178408f8b5330f7988b411720cd5ac987228aa2f7e75ce5b7b4c1705f6b596152d3fc371b7243fa290101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0d02f401026402062f503253482fffffffff01a08601000000000023210277f0ea2122bee3fd131e8bfb888974d07b80b1fa232f86a0a04b942ee176b35bac00000000',
        'amount': 0.001,
        'vout': 0,
        'confirmations': 1743584,
        'scriptPubKey': '76a9148d6ae8a3b381663118b4e1eff4cfc7d0954dd6ec88ac',
        'address': 'uhnfYZMo4KAyWqWtfq4RoaWnnzH889ki22'
    }]

    tx1hex = construct_tx(server_db, "uhnfYZMo4KAyWqWtfq4RoaWnnzH889ki22", "uhnfYZMo4KAyWqWtfq4RoaWnnzH889ki22", custom_inputs=custom_inputs)
    tx2hex = construct_tx(server_db, "uhnfYZMo4KAyWqWtfq4RoaWnnzH889ki22", "uhnfYZMo4KAyWqWtfq4RoaWnnzH889ki22", custom_inputs=custom_inputs)

    tx1f = BytesIO(binascii.unhexlify(tx1hex))
    tx1 = bitcoin.core.CTransaction.stream_deserialize(tx1f)

    tx2f = BytesIO(binascii.unhexlify(tx2hex))
    tx2 = bitcoin.core.CTransaction.stream_deserialize(tx2f)

    assert (tx1.vin[0].prevout.hash, tx1.vin[0].prevout.n) == (tx2.vin[0].prevout.hash, tx2.vin[0].prevout.n)


def test_disable_utxolocks(server_db):
    transaction.initialise()  # reset UTXO_LOCKS

    """with `disable_utxo_locks=True` it should use the same UTXO"""
    tx1hex = construct_tx(server_db, "uhnfYZMo4KAyWqWtfq4RoaWnnzH889ki22", "uhnfYZMo4KAyWqWtfq4RoaWnnzH889ki22", disable_utxo_locks=True)
    tx2hex = construct_tx(server_db, "uhnfYZMo4KAyWqWtfq4RoaWnnzH889ki22", "uhnfYZMo4KAyWqWtfq4RoaWnnzH889ki22", disable_utxo_locks=True)

    tx1f = BytesIO(binascii.unhexlify(tx1hex))
    tx1 = bitcoin.core.CTransaction.stream_deserialize(tx1f)

    tx2f = BytesIO(binascii.unhexlify(tx2hex))
    tx2 = bitcoin.core.CTransaction.stream_deserialize(tx2f)

    assert (tx1.vin[0].prevout.hash, tx1.vin[0].prevout.n) == (tx2.vin[0].prevout.hash, tx2.vin[0].prevout.n)
