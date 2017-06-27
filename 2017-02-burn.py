from getpass import getpass
from pprint import pprint
from bitshares import BitShares
from bitshares.instance import set_shared_bitshares_instance
from bitshares.vesting import Vesting
from bitshares.market import Market
from bitshares.amount import Amount

account = "multisig-worker-2017-01"
proposer = "chainsquad"

bitshares = BitShares(
    nobroadcast=False,
    bundle=True,
    proposer=proposer,
    proposal_expiration=60 * 60 * 24 * 2,
    proposal_review=60 * 60,
)
set_shared_bitshares_instance(bitshares)

bitshares.wallet.unlock(getpass())

fees = 0.01213 + 0.21851

print("Burning BTS")
bitshares.reserve(
    Amount(6401109.50898 - fees, "BTS"),
    account=account
)

print("Send USD to committee-account")
bitshares.transfer(
    "committee-account",
    2349.6014, "USD",
    account=account
)

pprint(bitshares.broadcast())
