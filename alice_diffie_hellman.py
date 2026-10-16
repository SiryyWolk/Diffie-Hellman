from cryptography.hazmat.primitives.asymmetric import dh

# Step 1: generate the public parameters (these are not secret)
print("Generating parameters; this can take some time...")
parameters = dh.generate_parameters(generator=2, key_size=1024)
parameter_numbers = parameters.parameter_numbers()
print("p = " + str(parameter_numbers.p))
print("g = " + str(parameter_numbers.g))

# Step 2: Alice's secret number a and public number A
alice_private_key = parameters.generate_private_key()
alice_public_key = alice_private_key.public_key()
print("A = " + str(alice_public_key.public_numbers().y))

# Wait for Bob's public number B
print()
B = int(input("Paste Bob's B here: "))

# Step 4: rebuild Bob's public key from the integer and compute the shared key
bob_public_numbers = dh.DHPublicNumbers(B, parameter_numbers)
bob_public_key = bob_public_numbers.public_key()

alice_shared_key_bytes = alice_private_key.exchange(bob_public_key)
print("Shared Key (according to Alice): " + alice_shared_key_bytes.hex())