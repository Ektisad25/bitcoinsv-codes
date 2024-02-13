from bsvlib import Wallet
from bsvlib.constants import Chain

w = Wallet(chain=Chain.MAIN)

w.add_key('your_privatekey_here')
print(w.get_balance(refresh=True))



# Encode token metadata into bytes without including the OP_RETURN opcode
token_metadata = [
    bytes.fromhex('425356464f524b00'),                 # BSVFORK PROTOCOLID do not change it 
    bytes.fromhex('01'),                 # length of token_type (1 byte)
    bytes.fromhex('53454e44'),                 # SEND HEX do not change it

    bytes.fromhex('paste_genesis_hash_here'),                 # paste your genesis hash here

    bytes.fromhex('4f'),                 # amount to send converted to hex

]


outputs = [('address_to_send', 100)]

# Create the transaction with OP_RETURN output containing token metadata
# Manually include the OP_RETURN opcode in the pushdatas list
tx = w.create_transaction(outputs=outputs, pushdatas=token_metadata, combine=True)

# Create the transaction with OP_RETURN output containing token metadata
# Manually include the OP_RETURN opcode in the pushdatas list
print(tx.broadcast())
