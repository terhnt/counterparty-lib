"""
This is a collection of default transaction data used to test various components.
"""

UNIT = 100000000

"""This structure is used throughout the test suite to populate transactions with standardized and tested data."""
#removed pubkey hash, may need to be re-added. these are also Prototanium adresses
DEFAULT_PARAMS = {
    'addresses': [
        ['UYyyYsKsdw48H5edicJvFatDQS8N8oRH5P', 'cVxmsemyry3ahoEcRiQndmpoG4YDEDM9WrjC2pP8NDMgjUz2vVGz', '031004F9AD4765CBE04179EAEC4D9E6316C0406C3FBD5A9D88E7AFE6A914AA811C'],
        ['Uho8WpgwNpis4LzREdvESRbXToc7qFeXCN', 'cSoZgZaDK5b3nwXG6ffY1VXqxVVp89ptakYkJkEj3wLJQT7svwVm', '03AC92735260A85B4BA1ABF6826CD9CCEEFCA674DE13C73F553623B22E8799391E'],
        ['URmVGUPMCTjPAeqVdVfRznCDQGq7cqNNGj', 'cVpBjdfFVikyYqcQdbMvwqRop8WiKJPyTcDdfRpr5P7oDKrWnQnx', '034A638981190CAEE6FD2EE5E244097F940FCBED3F3EFBD1EE683D256C268A8549'],
        ['UdcgfBkMHzDVZFpMAUou6mm6ux7ns6Y9AH', 'cRFVY5sdKxAwnfsXV5eRAjdFUFJbffQjPtuzj1H17t5X1x2xwmLT', '0333C34964B125D95EC10438D7F677F1DB74C2256F5DB287116A09316D5477DFA4'],
        ['UX6e4ougRNzqbL7FHfkwCaqqDUToPkn89Y', 'cMkHcBjHovpjz64pgubsaGtNK4Ss6BZyeD1VY8pWpWNkh3XrtiTy', '036FE4D43604326C6D87A5F9FB445A4FB097D77AA49A4984EAAF97365DA0BFC333'],
        ['UeevnNJxybp9BcApxvHmZ9PzzRGqZ2PDqn', 'cPjmjcCxRQ1Q5oVAbSfwRtxKjhSyDZBcWW7w9Cs4DxF1wyxYREWr', '025E306D859A5E24064D0B3C089C78F3AD809B7AC5A5A69073C6D93FFE20BCBBC8'],
        ['UU7iwGSuqRRnJicS75778Tgm3Sb2jU8HR6', 'cUpzJ5eKopGshczwGVwYFUSGGvaJ3BS3fwHYh77mHWTxtqxj1oxY', '03BE592AC709AEA7633ABF1CD72AFA81727966C698B73F01FC044ED3199B386A5E'],
        ['UR8mnGmHMfdpsDZomn5QJzphLAM7AtWQ7o', '', ''], # Empty address for testing purposes
        ['UV4YXZegX1Ltp7ZXJ4zu3PpqQPDdtApuYq', 'cNgtc9fyMVC53r8RPuseNzMwQ2R4HUrEtSVKCxMXdgyPUC8VcP9W', '03E81051579073A84AFAF68FB7CEE29798B58CEFB75DC6C4AF4FABB6A236E64757']
    ],
    'quantity': UNIT,
    'small': round(UNIT / 2),
    'expiration': 10,
    'fee_required': 900000,
    'fee_provided': 1000000,
    'fee_multiplier': .05,
    'unspendable': 'UUnoPartyXburnTestnetXXXXXXXXFEeN4',
    'burn_start': 310000,
    'burn_end': 4017708,
    'burn_quantity': int(.62 * UNIT),
    'burn_verysmall_quantity': int(.0001 * UNIT),
    'default_block_index': 310000 + 501,
    'default_block_hash': '2d62095b10a709084b1854b262de77cb9f4f7cd76ba569657df8803990ffbfc6c12bca3c18a44edae9498e1f0f054072e16eef32dfa5e3dd4be149009115b4b8' #TODO: need to update this value
}
#pubkeyhash - removed from lines 36/37
DEFAULT_PARAMS['privkey'] = {addr: priv for (addr, priv, pub) in DEFAULT_PARAMS['addresses']}
DEFAULT_PARAMS['pubkey'] = {addr: pub for (addr, priv, pub) in DEFAULT_PARAMS['addresses']}
ADDR = [a[0] for a in DEFAULT_PARAMS['addresses']]
SHORT_ADDR_BYTES = ['6f' + a[1] for a in DEFAULT_PARAMS['addresses']]
DP = DEFAULT_PARAMS
MULTISIGADDR = [
    '1_{}_{}_2'.format(ADDR[0], ADDR[1]),
    '1_{}_{}_2'.format(ADDR[2], ADDR[1]),
    '1_{}_{}_2'.format(ADDR[0], ADDR[2]),

    '2_{}_{}_2'.format(ADDR[0], ADDR[1]),
    '2_{}_{}_2'.format(ADDR[2], ADDR[1]),

    '1_{}_{}_{}_3'.format(ADDR[0], ADDR[2], ADDR[1]),
    '1_{}_{}_{}_3'.format(ADDR[0], ADDR[2], ADDR[3]),

    '2_{}_{}_{}_3'.format(ADDR[0], ADDR[2], ADDR[1]),
    '2_{}_{}_{}_3'.format(ADDR[0], ADDR[2], ADDR[3]),

    '3_{}_{}_{}_3'.format(ADDR[0], ADDR[2], ADDR[1]),
    '3_{}_{}_{}_3'.format(ADDR[0], ADDR[2], ADDR[3])
]

#TODO: GET Pay to script / segwit testnet addresses
#P2SH_ADDR = [
#    '2MyJHMUenMWonC35Yi6PHC7i2tkS7PuomCy', # 2of2 mn6q3dS2EnDUx3bmyWc6D4szJNVGtaR7zc mtQheFaSfWELRB2MyMBaiWjdDm6ux9Ezns
#    '2N6P6d3iypnnud4YJDfHZ6kc513N8ezWmPx', # 2of3 mn6q3dS2EnDUx3bmyWc6D4szJNVGtaR7zc mtQheFaSfWELRB2MyMBaiWjdDm6ux9Ezns mnfAHmddVibnZNSkh8DvKaQoiEfNsxjXzH
#]

#P2WPKH_ADDR = [
#    'tb1qw508d6qejxtdg4y5r3zarvary0c5xw7kxpjzsx'
#]
