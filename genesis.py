from bsvlib import Wallet
from bsvlib.constants import Chain

w = Wallet(chain=Chain.MAIN)

w.add_key('your_private_key_here')
print(w.get_balance(refresh=True))


# Encode token metadata into bytes without including the OP_RETURN opcode
token_metadata = [
    bytes.fromhex('425356464f524b00'),                 # BSVFORK do not changeit
    bytes.fromhex('01'),                 # fungible token do not change it
    bytes.fromhex('47454e45534953'),                 # hex used for Genesis do not change it
    bytes.fromhex('5443686174'),                # token symbol
    bytes.fromhex('54726565436861746169'),                 # token name
    bytes.fromhex('00'),                 # token image url
    bytes.fromhex('00'),                 # token document url
    bytes.fromhex('00'),                 # token website url
    bytes.fromhex('02'),                 # from script do not change it
    bytes.fromhex('00000000000f4240'),                 # amount to mint

]

# Create the transaction with OP_RETURN output containing token metadata
# Manually include the OP_RETURN opcode in the pushdatas list
tx = w.create_transaction(pushdatas=token_metadata, combine=True)

# Broadcast the transaction
print(tx.broadcast())
