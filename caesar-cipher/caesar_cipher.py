def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decode":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char

    return result


text = input("Enter text: ")
shift = int(input("Enter shift number: "))
mode = input("Encode or decode? ").lower()

if mode not in ["encode", "decode"]:
    print("Invalid mode. Choose encode or decode.")
else:
    output = caesar_cipher(text, shift, mode)
    print("\nResult:")
    print(output)