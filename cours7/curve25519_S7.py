from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# Generate private and public keys for use in the exchange.
Alice_private_key = X25519PrivateKey.generate()
Alice_public_key = Alice_private_key.public_key()
Bob_private_key = X25519PrivateKey.generate()
Bob_public_key = Bob_private_key.public_key()

A_public_key  = Alice_public_key.public_bytes(encoding=serialization.Encoding.Raw,format=serialization.PublicFormat.Raw)
# A_public_key_clean = A_public_key.decode('utf-8')
A_public_key_clean = A_public_key.hex()

# Display Public Key
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Public Key of Alice and Bob : ")
print("------------------------------------------------")
print("\t - Public Key of by Alice : ", Alice_public_key)
print("\t - Public Key of by Alice : ", A_public_key)
print("\t - Public Key of by Alice : ", A_public_key_clean)
# print("\t - Public Key of by Bob   : ", Bob_Shared_Key.hex())

#################################################################################################
# Alice and Bob : Compute Shared Key                                                            #
#################################################################################################

Alice_Shared_Key = Alice_private_key.exchange(Bob_public_key)
Bob_Shared_Key = Bob_private_key.exchange(Alice_public_key)

# Display Shared Key
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Shared Secret between Alice and Bob : ")
print("------------------------------------------------")
print("\t - Shared Key compute by Alice : ", Alice_Shared_Key.hex())
print("\t - Shared Key compute by Bob   : ", Bob_Shared_Key.hex())




















# Perform key derivation with Alice_Shared_Key.
Alice_Derived_Key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
    backend=default_backend(),
).derive(Alice_Shared_Key)

# Perform key derivation with Bob_Shared_Key.
Bob_Derived_Key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
    backend=default_backend(),
).derive(Bob_Shared_Key)

# Display Key Derivation
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Key Derivation of Alice and Bob : ")
print("------------------------------------------------")
print("\t - Key Derivation with Alice_Shared_Key : ", Alice_Derived_Key.hex())
print("\t - Key Derivation with Bob_Shared_Key   : ", Bob_Derived_Key.hex())
