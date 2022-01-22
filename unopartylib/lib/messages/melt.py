#! /usr/bin/python3
import json
import struct
import decimal
import logging
# import math # Temporarily Disable DEV FUNDS
logger = logging.getLogger(__name__)

D = decimal.Decimal
from fractions import Fraction

from unopartylib.lib import (config, exceptions, util)

"""Melt asset to earn locked asset inside special assets."""

ID = 160

def initialise (db):
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS melts(
                      tx_index INTEGER PRIMARY KEY,
                      tx_hash TEXT UNIQUE,
                      block_index INTEGER,
                      source TEXT,
                      melted INTEGER,
                      earned INTEGER,
                      status TEXT,
                      FOREIGN KEY (tx_index, tx_hash, block_index) REFERENCES transactions(tx_index, tx_hash, block_index))
                   ''')
    cursor.execute('''CREATE INDEX IF NOT EXISTS
                      status_idx ON melts (status)
                   ''')
    cursor.execute('''CREATE INDEX IF NOT EXISTS
                      address_idx ON melts (source)
                   ''')

def validate (db, source, destination, quantity, block_index, asset):
    problems = []
    asset_id = None

    if asset == config.BTC:
        problems.append('cannot melt %s' % config.BTC)
        return None, problems

    # Check destination address.
    if destination != config.UNSPENDABLE:
        problems.append('wrong destination address')

    if not isinstance(quantity, int):
        problems.append('quantity must be in satoshis')
        return problems

    if quantity < 0: problems.append('negative quantity')

    # Check if user has enough of asset to melt
    cursor = db.cursor()
    cursor.execute('''SELECT quantity FROM balances \
                      WHERE address = ? and asset = ?''', (source,asset,))
    available = cursor.fetchall()

    if len(available) == 0:
        problems.append('address doesn\'t has the asset %s' % asset)
    elif len(available) >= 1 and available[0]['quantity'] < escrow_quantity:
        problems.append('address doesn\'t has enough balance of %s (%i < %i)' % (asset, available[0]['quantity'], quantity))

    # Try to make sure that the melted assets won't go to waste.
    # Check if asset is meltable
    cursor.execute('''SELECT * FROM assets WHERE asset_name = ?''', (asset_name,))
    assets = list(cursor)

    if len(problems) == 0:
        meltable = util.is_meltable(db, asset)
        asset_id = util.generate_asset_id(asset, block_index)
        if asset_id == 0:
            problems.append('cannot melt %s' % asset) # How can we test this on a test vector?
        if meltable == False:
            problems.append('cannot melt %s, because its not meltable' % asset)

    cursor.close()
    if len(problems) > 0:
        return None, problems
    else:
        return asset_id, None

def compose (db, source, quantity, asset):
    cursor = db.cursor()
    destination = config.UNSPENDABLE
    assetid, problems = validate(db, source, destination, quantity, util.CURRENT_BLOCK_INDEX, asset)
    if problems: raise exceptions.ComposeError(problems)
    cursor.close()

    data = message_type.pack(ID)
    data += struct.pack(FORMAT, assetid, quantity, asset)
    return (source, [], data)

def parse (db, tx, message):
    melt_parse_cursor = db.cursor()

    #TODO: unpack message: WIP
    try:
        action_address = tx['source']
        assetid, quantity, asset = struct.unpack(FORMAT, message[0:LENGTH])
        asset = util.generate_asset_name(assetid, util.CURRENT_BLOCK_INDEX)
        status = 'valid'
    except (exceptions.UnpackError, struct.error) as e:
        assetid, quantity, asset = None, None, None
        status = 'invalid: could not unpack'

    if config.TESTNET or config.REGTEST:
        problems = []
        status = 'valid'

        if status == 'valid':
            problems = validate(db, tx['source'], tx['destination'], tx['btc_amount'], tx['block_index'], asset)
            if problems: status = 'invalid: ' + '; '.join(problems)

        if status == 'valid':
            earned = round(util.get_asset_backing_qty(db, asset)*quantity)
            # Burn the users asset
            util.debit(db, tx['source'], asset, quantity, action='melt', event=tx['tx_hash'])
            # Credit the Burn Address
            addr = config.UNSPENDABLE_TESTNET if config.TESTNET else config.UNSPENDABLE_REGTEST
            util.credit(db, addr, util.get_asset_backing(db, asset), earned, action='burn', event=tx['tx_hash'])
            # Credit source address with earned asset from melting
            util.credit(db, tx['source'], util.get_asset_backing(db, asset), earned, action='burn', event=tx['tx_hash'])

        else:
            earned = 0

        tx_index = tx['tx_index']
        tx_hash = tx['tx_hash']
        block_index = tx['block_index']
        source = tx['source']

    else:
        earned = round(util.get_asset_backing_qty(db, asset)*quantity)
        # Burn the users asset
        util.debit(db, tx['source'], asset, quantity, action='melt asset', event=tx['tx_hash'])
        # Credit the Burn Address
        util.credit(db, config.UNSPENDABLE_MAINNET, util.get_asset_backing(db, asset), earned, action='burn', event=tx['tx_hash'])
        # Credit source address with earned asset from melting
        util.credit(db, tx['source'], util.get_asset_backing(db, asset), earned, action='melt', event=tx['tx_hash'])

        tx_index = tx['tx_index']
        tx_hash = tx['tx_hash']
        block_index = tx['block_index']
        source = tx['source']
        status = 'valid'

    # Add parsed transaction to message-type–specific table.
    # TODO: store sent in table
    bindings = {
        'tx_index': tx_index,
        'tx_hash': tx_hash,
        'block_index': block_index,
        'melted': quantity,
        'source': source,
        'earned': earned,
        'status': status,
    }
    if "integer overflow" not in status:
        sql = 'insert into melts values(:tx_index, :tx_hash, :block_index, :source, :melted, :earned, :status)'
        melt_parse_cursor.execute(sql, bindings)
    else:
        logger.warn("Not storing [melt] tx [%s]: %s" % (tx['tx_hash'], status))
        logger.debug("Bindings: %s" % (json.dumps(bindings), ))

    melt_parse_cursor.close()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
