from pprint import pprint
from bitshares import BitShares
from bitshares.instance import set_shared_bitshares_instance
from bitshares.vesting import Vesting
from bitshares.price import Price
from bitshares.market import Market
from bitshares.amount import Amount

account = "multisig-worker-2017-01"
proposer = "chainsquad"
vesting_id = "1.13.1188"

bitshares = BitShares(
    nobroadcast=False,
    bundle=True,
    proposer=proposer,
    expiration=86400
)
set_shared_bitshares_instance(bitshares)
market = Market("USD:BTS")
price = Price(market["quote"]["options"]["core_exchange_rate"])

bitshares.wallet.unlock("<supersecret>")
vesting = Vesting(vesting_id)

print("Claiming Vesting Balance: %s" % vesting.claimable)
bitshares.vesting_balance_withdraw(
    vesting["id"],
    amount=vesting.claimable,
    account=account
)

print("Buying as much bitUSD at price up to %s" % (
    price * 0.95,
))
market.buy(
    price * 0.95,
    Amount(4350, "USD"),
    killfill=True,
    account=account
)

print("TLM fee")
bitshares.transfer(
    "chainsquad",
    100, "USD",
    account=account
)

print("Worker fee")
bitshares.transfer(
    "chainsquad",
    150, "USD",
    account=account
)

print("Coding fee - first month")
bitshares.transfer(
    "chainsquad",
    4000, "USD",
    account=account
)

print("Uptick API node")
bitshares.transfer(
    "chainsquad",
    100, "USD",
    account=account
)

pprint(bitshares.broadcast())
