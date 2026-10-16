from cryptography.hazmat.primitives.asymmetric import dh

# Step 1: receive the public parameters from Alice
p = int(input("Paste p here: "))
g = int(input("Paste g here: "))
parameter_numbers = dh.DHParameterNumbers(p, g)
parameters = parameter_numbers.parameters()

# Step 3: Bob's secret number b and public number B
bob_private_key = parameters.generate_private_key()
bob_public_key = bob_private_key.public_key()
print("B = " + str(bob_public_key.public_numbers().y))

# Receive Alice's public number A
print()
A = int(input("Paste Alice's A here: "))

# Step 5: rebuild Alice's public key and compute the shared key
alice_public_numbers = dh.DHPublicNumbers(A, parameter_numbers)
alice_public_key = alice_public_numbers.public_key()

bob_shared_key_bytes = bob_private_key.exchange(alice_public_key)
print("Shared Key (according to Bob): " + bob_shared_key_bytes.hex())