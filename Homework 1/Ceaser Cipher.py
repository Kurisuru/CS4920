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
    shift = int(input("Enter the shift amount: "))
    if choice == 'd':
        shift = -shift
    print("Enter your message (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    output_lines = [caesar_cipher(line, shift) for line in lines]
    output_text = "\n".join(output_lines)
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(output_text)
    output = output_text
    print(f"Result: {output}")