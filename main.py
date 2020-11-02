from ecdsa import SigningKey

message = b"Hellow world"

sk = SigningKey.generate()  # uses NIST192p
vk = sk.verifying_key
signature = sk.sign(message)
print("Signature(r,s) is " + str(signature))
assert vk.verify(signature, message)
