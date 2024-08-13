def affine_encrypt(text, a, b):
    """
    Encrypts the given text using the Affine cipher with the keys 'a' and 'b'.
    The formula used is: E(x) = (a * x + b) mod 26
    """

    def encrypt_char(char):
        if char.isalpha():
            x = ord(char.upper()) - ord("A")  # Convert character to 0-25 index
            encrypted = (a * x + b) % 26  # Apply the affine encryption formula
            return chr(encrypted + ord("A"))  # Convert back to letter
        return char  # Non-alphabetic characters are unchanged

    return "".join(encrypt_char(c) for c in text)  # Encrypt the entire text


def affine_decrypt(ciphertext, a, b):
    """
    Decrypts the given ciphertext using the Affine cipher with the keys 'a' and 'b'.
    The formula used is: D(y) = a_inv * (y - b) mod 26
    where a_inv is the modular multiplicative inverse of 'a' mod 26.
    """

    def mod_inverse(a, m):
        # Find the modular multiplicative inverse of 'a' mod 'm'
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    def decrypt_char(char):
        if char.isalpha():
            y = ord(char.upper()) - ord("A")  # Convert character to 0-25 index
            a_inv = mod_inverse(a, 26)  # Get the modular inverse of 'a'
            decrypted = (a_inv * (y - b)) % 26  # Apply the affine decryption formula
            return chr(decrypted + ord("A"))  # Convert back to letter
        return char  # Non-alphabetic characters are unchanged

    return "".join(decrypt_char(c) for c in ciphertext)  # Decrypt the entire text


print()
print("*** AFFINE CIPHER PROGRAM ***")
print()

# User input
choice = (
    input("Would you like to (E)ncrypt or (D)ecrypt using the Affine Cipher? ")
    .strip()
    .upper()
)
text = input("Enter the text: ").strip()  # Get the text from the user
a = int(input("Enter the value for 'a' (must be coprime with 26): "))  # Get 'a' value
b = int(input("Enter the value for 'b': "))  # Get 'b' value

if choice == "E":
    result = affine_encrypt(text, a, b)  # Encrypt the text
elif choice == "D":
    result = affine_decrypt(text, a, b)  # Decrypt the text
else:
    result = "Invalid choice. Please enter 'E' for encryption or 'D' for decryption."

print(f"Result: {result}")
