import sys

"""Variables prefixed with `DEFAULT` should be able to be overridden by
configuration file and command‐line arguments."""

UNIT = 100000000        # The same across assets.


# Versions
VERSION_MAJOR = 9
VERSION_MINOR = 59
VERSION_REVISION = 4
VERSION_STRING = str(VERSION_MAJOR) + '.' + str(VERSION_MINOR) + '.' + str(VERSION_REVISION)


# Unoparty protocol
TXTYPE_FORMAT = '>I'
SHORT_TXTYPE_FORMAT = 'B'

TWO_WEEKS = 2 * 7 * 24 * 3600
MAX_EXPIRATION = 4 * 2016   # Two months

MEMPOOL_BLOCK_HASH = 'mempool'
MEMPOOL_BLOCK_INDEX = 9999999


# SQLite3
MAX_INT = 2**63 - 1


# Unobtanium Core
OP_RETURN_MAX_SIZE = 80  # bytes


# Currency agnosticism
BTC = 'UNO'
XCP = 'XUP'

BTC_NAME = 'Unobtanium'
XCP_NAME = 'Unoparty'
APP_NAME = XCP_NAME.lower()

# Counterparty Ports
DEFAULT_RPC_PORT_REGTEST = 24120
DEFAULT_RPC_PORT_TESTNET = 14120
DEFAULT_RPC_PORT = 4120

# Unobtanium Client Ports
DEFAULT_BACKEND_PORT_REGTEST = 18445
DEFAULT_BACKEND_PORT_TESTNET = 65531
DEFAULT_BACKEND_PORT = 65535

# Addrindexrs Ports
DEFAULT_INDEXD_PORT_REGTEST = 28122
DEFAULT_INDEXD_PORT_TESTNET = 18122
DEFAULT_INDEXD_PORT = 8122

# Protocol Changes
PROTOCOL_MELT_MAINNET = 800000
PROTOCOL_MELT_TESTNET = 7320
PROTOCOL_MELT_REGTEST = 1

# Burnaddress
UNSPENDABLE_REGTEST = '1UnopartyxBurnxAddrXXXXXXXXXX42dPh'
UNSPENDABLE_TESTNET = 'UUnoPartyXburnTestnetXXXXXXXXFEeN4'
UNSPENDABLE_MAINNET = 'uNopartyXburnXXXXXXXXXXXXXXXWJmsqn'

# Storageaddress - pretty much burn addresses but will store unoparty backed assets before melting
UNSPENDSTORAGE_REGTEST = '1UnopartystorageaddressXXXXXXkxGFV'
UNSPENDSTORAGE_TESTNET = 'UUnopartystorageaddressXXXXXVNZKFF'
UNSPENDSTORAGE_MAINNET = 'uUnopartystorageaddressXXXXXTLgaam'

# Hardcoded development fund - each uno burned will give a % of XUP to development/maintenance address
DEV_FUND_ADDR_REGTEST = '1MHBMEXpWkX5GesyyCD2NGfyFekmyBfGsd'
DEV_FUND_ADDR_TESTNET = 'UPxPzftYTiWyNa3Y6Aamyr8unu6xpEsdwK'
DEV_FUND_ADDR_MAINNET = 'uVVuwXm2mDK9pr9XkWT5k7ihQyoSC8y2MW' # Controlled by terhnt

DEV_FUND_PERCENT = 0.25 # 25% - an additional 25% of each burn reward goes to development
DEV_FUND = True

MAX_BURN = 5 # Maximum amount of UNO that one address can burn
REWARD_RATE = 2000 # base reward of XUP for burning unobtanium

ADDRESSVERSION_TESTNET = b'\x44'
P2SH_ADDRESSVERSION_TESTNET = b'\x1E'
PRIVATEKEY_VERSION_TESTNET = b'\xef'
ADDRESSVERSION_MAINNET = b'\x82'
P2SH_ADDRESSVERSION_MAINNET = b'\x1E'
PRIVATEKEY_VERSION_MAINNET = b'\xE0'
ADDRESSVERSION_REGTEST = b'\x00'
P2SH_ADDRESSVERSION_REGTEST = b'\x05'
PRIVATEKEY_VERSION_REGTEST = b'\x80'
MAGIC_BYTES_TESTNET = b'\x01\x02\x03\x04'   # For bip-0010
MAGIC_BYTES_MAINNET = b'\x03\xd5\xb5\x03'   # For bip-0010
MAGIC_BYTES_REGTEST = b'\x04\x03\x02\x01'

BLOCK_FIRST_TESTNET_TESTCOIN = 1600
BURN_START_TESTNET_TESTCOIN = BLOCK_FIRST_TESTNET_TESTCOIN
BURN_END_TESTNET_TESTCOIN = 400000     # A Long Time!

BLOCK_FIRST_TESTNET = 15000
#BLOCK_FIRST_TESTNET_HASH = '000007b02afb00ae826d948d88f4973c00073425f965917f6298b6d280bde021'
BURN_START_TESTNET = BLOCK_FIRST_TESTNET
BURN_END_TESTNET = BURN_END_TESTNET_TESTCOIN   # A Long Time!

BLOCK_FIRST_MAINNET_TESTCOIN = 278270
BURN_START_MAINNET_TESTCOIN = 278310
BURN_END_MAINNET_TESTCOIN = 2500000     # A long time.

BLOCK_FIRST_MAINNET = 1800120
BLOCK_FIRST_MAINNET_HASH = '000004c2fc5fffb810dccc197d603690099a68305232e552d96ccbe8e2c52b75'
BURN_START_MAINNET = 1810000
BURN_END_MAINNET = BURN_START_MAINNET + (30*24*60/3) # 30 days burn period with 3 min target time per block.

BLOCK_FIRST_REGTEST = 0
#BLOCK_FIRST_REGTEST_HASH = '3868bcc735f32cdd9b42971cdee7bc620c50fada5e3ac5fdfd35630aaf2eb64e'
BURN_START_REGTEST = 101
BURN_END_REGTEST = 150000000

BLOCK_FIRST_REGTEST_TESTCOIN = 0
BURN_START_REGTEST_TESTCOIN = 101
BURN_END_REGTEST_TESTCOIN = 150

# Protocol defaults
# NOTE: If the DUST_SIZE constants are changed, they MUST also be changed in counterblockd/lib/config.py as well
    # TODO: This should be updated, given their new configurability.
# TODO: The dust values should be lowered by 90%, once transactions with smaller outputs start confirming faster: <https://github.com/mastercoin-MSC/spec/issues/192>
DEFAULT_REGULAR_DUST_SIZE = 5430         # TODO: This is just a guess. I got it down to 5530 satoshis.
DEFAULT_MULTISIG_DUST_SIZE = 7800        # <https://unobtaniumtalk.org/index.php?topic=528023.msg7469941#msg7469941>
DEFAULT_OP_RETURN_VALUE = 0
DEFAULT_FEE_PER_KB_ESTIMATE_SMART = 1024
DEFAULT_FEE_PER_KB = 25000               # sane/low default, also used as minimum when estimated fee is used
ESTIMATE_FEE_PER_KB = True               # when True will use `estimatesmartfee` from unobtaniumd instead of DEFAULT_FEE_PER_KB
ESTIMATE_FEE_CONF_TARGET = 3
ESTIMATE_FEE_MODE = 'CONSERVATIVE'

# UI defaults
DEFAULT_FEE_FRACTION_REQUIRED = .009   # 0.90%
DEFAULT_FEE_FRACTION_PROVIDED = .01    # 1.00%


DEFAULT_REQUESTS_TIMEOUT = 20   # 20 seconds
DEFAULT_RPC_BATCH_SIZE = 20     # A 1 MB block can hold about 4200 transactions.

# Custom exit codes
EXITCODE_UPDATE_REQUIRED = 5


DEFAULT_CHECK_ASSET_CONSERVATION = True

BACKEND_RAW_TRANSACTIONS_CACHE_SIZE = 20000
BACKEND_RPC_BATCH_NUM_WORKERS = 6

UNDOLOG_MAX_PAST_BLOCKS = 100 #the number of past blocks that we store undolog history

DEFAULT_UTXO_LOCKS_MAX_ADDRESSES = 1000
DEFAULT_UTXO_LOCKS_MAX_AGE = 3.0 #in seconds

ADDRESS_OPTION_REQUIRE_MEMO = 1
ADDRESS_OPTION_MAX_VALUE = ADDRESS_OPTION_REQUIRE_MEMO # Or list of all the address options
OLD_STYLE_API = True

API_LIMIT_ROWS = 1000
MEMPOOL_TXCOUNT_UPDATE_LIMIT=60000

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
