from p2pool.bitcoin import networks

PARENT = networks.nets['litecoin_testnet']
SHARE_PERIOD = 4 # seconds
CHAIN_LENGTH = 20*60//3 # shares
REAL_CHAIN_LENGTH = 20*60//3 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'cca5e24ec6408b1e'.decode('hex')
PREFIX = 'ad9614f6466a39cf'.decode('hex')
P2P_PORT = 19338
MIN_TARGET = 2**256//50 - 1
MAX_TARGET = 2**256//50 - 1
PERSIST = False
WORKER_PORT = 19327
BOOTSTRAP_ADDRS = 'forre.st'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
# You can enable push notifications thru pushover.net
USE_PUSHOVER_BLOCK = False #Change to true only if you have added your token and key below
USE_PUSHOVER_SHARE = False #Change to true only if you have added your token and key below
PUSHOVER_APP_TOKEN = 'ADD YOUR APP TOKEN HERE'
PUSHOVER_USER_KEY = 'ADD YOUR USER KEY HERE'
# You can enable push notifications thru pushover.net
USE_PUSHOVER_BLOCK = False #Change to true only if you have added your token and key below
USE_PUSHOVER_SHARE = False #Change to true only if you have added your token and key below
PUSHOVER_APP_TOKEN = 'ADD YOUR APP TOKEN HERE'
PUSHOVER_USER_KEY = 'ADD YOUR USER KEY HERE'
