# Solution to secret

text_encrypted = None
text_decrypted = ""

with open("message.txt", "r") as f:
    text_encrypted = f.read()

print(text_encrypted)

for word in text_encrypted.split(" "):
    char = ""
    ascii_char = ""
    count_chars = 0
    for c in word:
        if count_chars == 0:
            # Convert to text
            if len(ascii_char) > 0:
                char = char + chr(int(ascii_char))
            ascii_char = ""
            if c.startswith("5") or c.startswith("6") or c.startswith("7") or c.startswith("8") or c.startswith("9"):
                print("Pass")
                # Two digits (97-99)
                count_chars = 2
            elif c.startswith("1"):
                # Three digits (100-122)
                count_chars = 3
        ascii_char = ascii_char + c
        count_chars -= 1
    # Convert to text
    if len(ascii_char) > 0:
        char = char + chr(int(ascii_char))
    ascii_char = ""
    text_decrypted += char + " "

print(text_decrypted)