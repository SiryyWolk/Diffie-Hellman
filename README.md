# Diffie–Hellman Key Exchange in Python

A small demonstration of the Diffie–Hellman key agreement protocol using Python's [`cryptography`](https://cryptography.io) package. The original single-file demo is split into two programs, one for Alice and one for Bob, so you can run them in separate terminals and copy numbers between them, just like two machines exchanging public values over a network.

Written as part of a university cryptography practical. For learning only, not for production use.

## How the protocol works

1. Alice and Bob agree on public parameters: a prime `p` and a base `g`.
2. Alice picks a secret number `a` and sends Bob `A = g^a mod p`.
3. Bob picks a secret number `b` and sends Alice `B = g^b mod p`.
4. Alice computes `K = B^a mod p`.
5. Bob computes `K = A^b mod p`.

Both arrive at the same value `g^(ab) mod p`, but neither secret (`a` or `b`) is ever sent. An eavesdropper only sees `p`, `g`, `A` and `B`.

## Files

| File | Purpose |
|------|---------|
| `diffie_hellman.py` | Original demo: both parties in one script |
| `alice_diffie_hellman.py` | Alice's side: generates `p` and `g`, computes `A`, then the shared key |
| `bob_diffie_hellman.py` | Bob's side: receives `p` and `g`, computes `B`, then the shared key |

## Requirements

- Python 3.8 or newer
- The `cryptography` package

```bash
python -m pip install cryptography
```

## Usage

### Single-file demo

```bash
python diffie_hellman.py
```

### Two-terminal version

Open two terminals in the project folder.

**Terminal 1 (Alice)**

```bash
python alice_diffie_hellman.py
```

Alice prints `p`, `g` and `A`, then waits for Bob's number.

**Terminal 2 (Bob)**

```bash
python bob_diffie_hellman.py
```

1. Paste `p` and `g` from Alice's terminal when prompted.
2. Bob prints `B` and waits for Alice's number.

**Finish the exchange**

1. Copy `B` from Bob's terminal into Alice's terminal and press Enter. Alice prints her shared key.
2. Copy `A` from Alice's terminal into Bob's terminal and press Enter. Bob prints his shared key.
3. Compare the two hex strings. They should be identical.

> Keep both programs running until the exchange is finished. Each secret number only exists in memory while its program is running.

## Experiments

Change `key_size` in `dh.generate_parameters(generator=2, key_size=512)` to 512, 1024 or 2048 and observe:

- **Running time:** parameter generation gets much slower as the key size grows, because finding a large suitable prime is expensive.
- **Key sizes:** `p` and the public keys grow in line with `key_size`.

You can measure both with `time.time()` and `.bit_length()`.

## Optional: deriving a symmetric key

The raw shared secret is not uniformly random, so in practice it is passed through a key derivation function such as HKDF before use:

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b"handshake data",
).derive(shared_key_bytes)
```

Both parties must use the same parameters to get the same derived key.

## Security notes

- **512-bit parameters are insecure.** They are used here only so the demo runs quickly. Use 2048 bits or larger in real systems.
- **No authentication.** Plain Diffie–Hellman does not verify who you are talking to, so it is vulnerable to man-in-the-middle attacks. Real protocols combine it with signatures or certificates.
- **Prefer modern constructions.** Real-world systems typically use elliptic-curve variants (such as X25519) via well-reviewed libraries and protocols like TLS.

## Licence

Add a licence of your choice (for example MIT) if you plan to share this publicly.
