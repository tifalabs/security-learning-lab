import hashlib

text = input("Enter text to hash: ")

hash_result = hashlib.sha256(text.encode()).hexdigest()

print("\nSHA-256 Hash:")
print(hash_result)