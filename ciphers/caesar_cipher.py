# Define the alphabet letters that will be used in the cipher
letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)  # Calculate the total number of letters in the alphabet


def encrypt(plaintext, key):
    """
    Encrypts the plaintext using the Caesar cipher with the given key.
    """
    ciphertext = ""
    for letter in plaintext:
        letter = letter.lower()  # Convert letter to lowercase for consistency
        if not letter == " ":
            index = letters.find(letter)  # Find the index of the letter in the alphabet
            if index == -1:  # If the letter is not found, keep it unchanged
                ciphertext += letter
            else:
                new_index = index + key  # Shift the index by the key value
                if new_index >= num_letters:
                    new_index -= num_letters  # Wrap around if the index exceeds the alphabet length
                ciphertext += letters[
                    new_index
                ]  # Add the encrypted letter to the ciphertext
    return ciphertext


def decrypt(ciphertext, key):
    """
    Decrypts the ciphertext using the Caesar cipher with the given key.
    """
    plaintext = ""
    for letter in ciphertext:
        letter = letter.lower()  # Convert letter to lowercase for consistency
        if not letter == " ":
            index = letters.find(letter)  # Find the index of the letter in the alphabet
            if index == -1:  # If the letter is not found, keep it unchanged
                plaintext += letter
            else:
                new_index = index - key  # Reverse the shift by the key value
                if new_index < 0:
                    new_index += num_letters  # Wrap around if the index is negative
                plaintext += letters[
                    new_index
                ]  # Add the decrypted letter to the plaintext
    return plaintext


# Main program starts here
print()
print("*** CAESAR CIPHER PROGRAM ***")
print()

# Ask the user if they want to encrypt or decrypt
print("Would you like to encrypt or decrypt?")
user_input = input("e/d: ").lower()
print()

if user_input == "e":
    print('You selected "Encryption"')
    print()
    key = int(input("Enter the key (1 through 26): "))  # Get the key from the user
    text = input("Enter the text to encrypt: ")  # Get the text to encrypt
    ciphertext = encrypt(text, key)  # Encrypt the text
    print(f"CIPHERTEXT: {ciphertext}")

elif user_input == "d":
    print('You selected "Decryption"')
    print()
    key = int(input("Enter the key (1 through 26): "))  # Get the key from the user
    text = input("Enter the text to decrypt: ")  # Get the text to decrypt
    plaintext = decrypt(text, key)  # Decrypt the text
    print(f"PLAINTEXT: {plaintext}")

else:
    # Handle invalid input
    print(
        'Invalid choice. You must enter "e" for encryption or "d" for decryption to proceed'
    )
