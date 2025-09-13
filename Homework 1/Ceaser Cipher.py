import os

def caesar_cipher(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            char = char.lower()
            base = ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

if __name__ == "__main__":

    choice = input("Type 'e' to encrypt, 'd' to decrypt: ").strip().lower()
    shift = int(input("Enter the shift amount: "))
    if choice == 'd':
        shift = -shift

    input_file = input("Enter the input file path: ").strip()
    while not os.path.isfile(input_file):
        print("File not found. Please enter a valid file path.")
        input_file = input("Enter the input file path: ").strip()

    output_file = input("Enter the output file name: ").strip()

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    output_lines = [caesar_cipher(line.rstrip('\n'), shift) for line in lines]
    output_text = "\n".join(output_lines)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_text)

    print(f"Result written to {output_file}")