"""
This is a collection of default transaction data used to test various components.
"""

UNIT = 100000000

"""This structure is used throughout the test suite to populate transactions with standardized and tested data."""
#removed pubkey hash, may need to be re-added.
DEFAULT_PARAMS = {
    'addresses': [
        ['Ukn3L4dgG13R3dSdxLvAAJizeiaW7cyUFz', 'cUuSAEXmiYMpu2Eu8QR52NzpsYB5MayhaX312ERZA5sUFQrMcaPY', '02cc8d98faf3bbe40b552be2d6dee21c54f14d7bbaf8e8b5867c9809658b85877d'],
        ['Ubq467qkiW2UvjD5Uhi23XKKyo7UcKAZTJ', 'cVprLzpeu5GdpjS8QkjB28YV2Hws3GK5eYmTtehDvY8ca4wjseVU', '02d577d18c9e2ac72c9bf7f5315e8eb579da19932e1a1c2d0a41524cb1b1109b0d'],
        ['UXJo7MANGsCfJM8LwRdkRsWWBxw6Tdshxt', 'cUsVQA8ZLtXottTgX1UpkmA4LyTNRdPtMW77uo8efXxNRmWuUYSR', '0312aa06fe0e0921369dd139ca6afd016ff9e0b5aad875730f7363ab8ac41cc6de'],
        ['UZ1XAmDF6Br2JKxahJWhuHzGawK7zxPtYW', 'cR93X24nNQwmXFBP1M1LRCr1qzy3ntQ4dhivBMtcwv5CnDwAb8c3', '029b9ea7a174c83e3a19038be991c61704ee325a451c1088bd5ee20f25b4ab9778'],
        ['UghGAbjYf5PoPcT5qFbxZ7VQb4MmvoPJeb', 'cNZd35p5P28urNGbJxDWeio1Az4Ubf2PtW4EPwjoVgPwgdUkqctC', '031a1cb595dd1c82a133c95331ceadc8fb6a67f087be67918a105743ea8f963b52'],
        ['UWskqPBEfw5sX5h6VKcTqqzBtiVBj2xBcQ', 'cQc5jyEuB4UvP4cUKALdKQTXB2HQXxRXcc2yrxYQUr8QLk8rzdHV', '028bc039d11b0f0a011ac13a58d8358e20b2e94a5f83045d64884ed996aa2e461e'],
        ['UWhVEVTAxrWsSMRPioQCqscAoUKhq42WQf', 'cV8ZpATSSkFF8rdsUepti5WotDj4bqGcVYXb82xTYuTscK95Rt5j', '03ea7e6a32ebe34979ad3c2be4f8ff2fe71316899f5cb134c94acd945e23edc223'],
        ['UShuxcmo5nojGPYqmsi6wbab81NZocdhtg', '', ''], # Empty address for testing purposes [ 'cVM1qQSP2exM9mHrsinN7wKZXZUvog56dhcWzanfXzmscNbHVPMd', '02c3ec578a7ff69a91756b63a47269294afd28113c5762fca9f95e60fdc49050e8']
        ['UkUTb6dHLNZstq27N4eJBkurpMXFRuv2M8', 'cW3nKqAPmmjJbrjqAdCk1SLSGAzyhWEoDXQ1fK6pV9xajKbgCfne', '02d980ad0429af8f575a4935fb1d210ceeb3d75d36510c0d6788142700d066f6a5']
    ],
    'quantity': UNIT,
    'small': round(UNIT / 2),
    'expiration': 10,
    'fee_required': 900000,
    'fee_provided': 1000000,
    'fee_multiplier': .05,
    'unspendable': 'UUnoPartyXburnTestnetXXXXXXXXFEeN4',
    'burn_start': 2000,
    'burn_end': 400000,
    'burn_quantity': int(.62 * UNIT),
    'burn_verysmall_quantity': int(.0001 * UNIT),
    'default_block_index': 2000 + 501,
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
P2SH_ADDR = [
    'DEyXVRPjTKZVP7nkcHkXCHJyZb78wLvVJC'  # 2of2 Ukn3L4dgG13R3dSdxLvAAJizeiaW7cyUFz Ubq467qkiW2UvjD5Uhi23XKKyo7UcKAZTJ
    'D9xjPTUFrNPUTNKPnS3UXnMSLd6sNgR7Jf', # 2of3 Ukn3L4dgG13R3dSdxLvAAJizeiaW7cyUFz Ubq467qkiW2UvjD5Uhi23XKKyo7UcKAZTJ UXJo7MANGsCfJM8LwRdkRsWWBxw6Tdshxt
]

#P2WPKH_ADDR = [
#    'tb1qw508d6qejxtdg4y5r3zarvary0c5xw7kxpjzsx'
#]
