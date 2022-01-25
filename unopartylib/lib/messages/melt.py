#! /usr/bin/python3
import json
import struct
import decimal
import logging
from unopartylib.lib import message_type

FORMAT = '>QQ'
LENGTH = 16
logger = logging.getLogger(__name__)

D = decimal.Decimal
from fractions import Fraction

from unopartylib.lib import (config, exceptions, util)

"""Melt asset to earn locked asset inside special assets."""

ID = 160

def initialise (db):
    cursor = db.cursor()

def validate (db, source, destination, quantity, block_index, asset):
    problems = []
    asset_id = None

    if asset == config.BTC:
        problems.append('cannot melt %s' % config.BTC)
        return None, problems

    # Check destination address.
    print('destination(validate): {}'.format(destination))
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
    elif len(available) >= 1 and available[0]['quantity'] < quantity:
        problems.append('address does not have enough balance of %s (%i < %i)' % (asset, available[0]['quantity'], quantity))

    # Try to make sure that the melted assets won't go to waste.
    # Check if asset is meltable
    cursor.execute('''SELECT * FROM assets WHERE asset_name = ?''', (asset,))
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
    data += struct.pack(FORMAT, assetid, quantity)
    return (source, [], data)


def parse (db, tx, message):
    melt_parse_cursor = db.cursor()

    #TODO: unpack message: WIP
    try:
        action_address = tx['source']
        assetid, quantity = struct.unpack(FORMAT, message[0:LENGTH])
        asset = util.generate_asset_name(assetid, util.CURRENT_BLOCK_INDEX)
        status = 'valid'
    except (exceptions.UnpackError, struct.error) as e:
        assetid, quantity = None, None
        status = 'invalid: could not unpack'

    #get backing_asset
    backing_asset = util.get_asset_backing(db, asset)
    backing = util.get_asset_backing_qty(db, asset)
    if config.TESTNET or config.REGTEST:
        problems = []
        status = 'valid'

        if status == 'valid':
            assetid, problems = validate(db, tx['source'], config.UNSPENDABLE, quantity, tx['block_index'], asset)
            if problems: status = 'invalid: ' + '; '.join(problems)

        if status == 'valid':
            melted = backing*quantity
            # burn the asset that is being melted
            util.debit(db, tx['source'], asset, quantity, action='send', event=tx['tx_hash'])
            util.credit(db, config.UNSPENDABLE, asset, quantity, action='send', event=tx['tx_hash'])
            # send backing from unspendable storage address to the user who melted
            util.debit(db, config.UNSPENDSTORAGE, backing_asset, melted, action='send', event=tx['tx_hash'])
            util.credit(db, tx['source'], backing_asset, melted, action='send', event=tx['tx_hash'])

        else:
            stored = 0
            melted = 0

        tx_index = tx['tx_index']
        tx_hash = tx['tx_hash']
        block_index = tx['block_index']
        source = tx['source']

    else:
        melted = backing*quantity
        # burn the asset that is being melted
        util.debit(db, tx['source'], asset, quantity, action='send', event=tx['tx_hash'])
        util.credit(db, config.UNSPENDABLE, asset, quantity, action='send', event=tx['tx_hash'])
        # send backing from unspendable storage address to the user who melted
        util.debit(db, config.UNSPENDSTORAGE, backing_asset, melted, action='send', event=tx['tx_hash'])
        util.credit(db, tx['source'], backing_asset, melted, action='send', event=tx['tx_hash'])

        tx_index = tx['tx_index']
        tx_hash = tx['tx_hash']
        block_index = tx['block_index']
        source = tx['source']
        status = 'valid'

    # Add parsed transaction to message-type–specific table.
    send_bindings = {
        'tx_index': tx_index,
        'tx_hash': tx_hash,
        'block_index': block_index,
        'source': source,
        'destination': config.UNSPENDABLE,
        'asset': asset,
        'quantity': quantity,
        'status': status,
    }

    if "integer overflow" not in status and "quantity must be in satoshis" not in status:
        sendsql = 'insert into sends (tx_index, tx_hash, block_index, source, destination, asset, quantity, status, memo) values(:tx_index, :tx_hash, :block_index, :source, :destination, :asset, :quantity, :status, NULL)'
        melt_parse_cursor.execute(sendsql, send_bindings)
    else:
        logger.warn("Not storing [melt] tx [%s]: %s" % (tx['tx_hash'], status))
        logger.debug("Bindings: %s" % (json.dumps(bindings), ))
    melt_parse_cursor.close()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
