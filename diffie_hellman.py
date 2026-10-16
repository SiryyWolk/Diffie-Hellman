from cryptography.hazmat.primitives.asymmetric import dh

# Diffie-Hellman key exchange allows two parties to derive a shared
# secret over an insecure channel without prior shared keys.
# 512-bit is insecure; use 2048+ in practice.

# Step 1: Alice and Bob agree on a set of parameters (g and p)
import time
start = time.time()
parameters = dh.generate_parameters(generator=2, key_size=1024)
print("Parameter generation took", round(time.time() - start, 1), "seconds")
parameter_numbers = parameters.parameter_numbers()
print("g = " + str(parameter_numbers.g))
print("p = " + str(parameter_numbers.p))

# Step 2: Alice generates a public-private key pair and sends the
# public-key to Bob.

print()
print("Generating Alice's public-private key pair...")
alice_private_key = parameters.generate_private_key()
alice_private_key_private_numbers = alice_private_key.private_numbers()
print("a = " + str(alice_private_key_private_numbers.x))

alice_public_key = alice_private_key.public_key()
alice_public_numbers = alice_public_key.public_numbers()
print("A = " + str(alice_public_numbers.y))

# Step 3: Bob generates a public-private key pair and sends the
# public-key to Alice.

print()
print("Generating Bob's public-private key pair...")
bob_private_key = parameters.generate_private_key()
bob_private_key_private_numbers = bob_private_key.private_numbers()
print("b = " + str(bob_private_key_private_numbers.x))

bob_public_key = bob_private_key.public_key()
bob_public_numbers = bob_public_key.public_numbers()
print("B = " + str(bob_public_numbers.y))

# Step 4: Alice computes the shared key using information only she
# knows.

alice_shared_key_bytes = alice_private_key.exchange(bob_public_key)
print()
print("Shared Key (according to Alice): " + alice_shared_key_bytes.hex())

# Step 5: Bob computes the shared key using information only he
# knows.

bob_shared_key_bytes = bob_private_key.exchange(alice_public_key)
print()
print("Shared Key (according to Bob): " + bob_shared_key_bytes.hex())
