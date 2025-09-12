import numpy as np

def caesar_cipher(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

if __name__ == "__main__":
    choice = input("Type 'e' to encrypt, 'd' to decrypt: ").strip().lower()
    message = input("Enter your message: ")
    shift = np.mod(int(input("Enter the shift amount: ")), 26) 
    if choice == 'd':
        shift = -shift
    output = caesar_cipher(message, shift)
    print(f"Result: {output}")