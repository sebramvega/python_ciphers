def atbash_cipher(text):
    """
    Encrypts or decrypts the given text using the Atbash cipher.
    The Atbash cipher reverses the alphabet, mapping A to Z, B to Y, etc.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reversed_alphabet = alphabet[::-1]  # Reverse the alphabet

    # Create a mapping dictionary from each letter to its reversed counterpart
    cipher_mapping = {alphabet[i]: reversed_alphabet[i] for i in range(len(alphabet))}

    # Process the text
    result = []
    for char in text.upper():
        if char in cipher_mapping:
            result.append(cipher_mapping[char])  # Substitute with reversed letter
        else:
            result.append(char)  # Non-alphabetic characters are unchanged

    return "".join(result)  # Return the final encrypted/decrypted text


# User input
plaintext = input("Enter the text to encrypt/decrypt using Atbash Cipher: ")
ciphertext = atbash_cipher(plaintext)  # Encrypt/Decrypt the text using Atbash cipher
print(f"Result: {ciphertext}")
