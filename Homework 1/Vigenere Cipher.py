def vigenere_cipher(message, keyword, encrypt=True, auto_key=False):
    result = ""
    keyword = keyword.lower()
    if auto_key:
        keyword += ''.join([c.lower() for c in message if c.isalpha()])
    keyword_length = len(keyword)
    keyword_indices = [ord(k) - ord('a') for k in keyword]
    keyword_pos = 0

    for char in message:
        if char.isalpha():
            char = char.lower()
            base = ord('a')
            shift = keyword_indices[keyword_pos % keyword_length]
            if not encrypt:
                shift = -shift
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
            keyword_pos += 1
        else:
            result += char
    return result

if __name__ == "__main__":
    choice = input("Type 'e' to encrypt, 'd' to decrypt: ").strip().lower()
    encrypt = (choice == 'e')
    choice_auto = input("Use auto-key? (y/n): ").strip().lower()
    auto_key = (choice_auto == 'y')
    print("Enter your message (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    keyword = lines[0].strip()
    output_lines = [vigenere_cipher(line, keyword, encrypt, auto_key) for line in lines[1:]]
    output_text = "\n".join(output_lines)
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(output_text)
    output = output_text
    print(f"Result: {output}")