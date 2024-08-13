### Ciphers

- **Caesar Cipher (`caesar_cipher.py`)**:
  - A substitution cipher where each letter in the plaintext is shifted by a fixed number of places down or up the alphabet.

- **Atbash Cipher (`atbash_cipher.py`)**:
  - A substitution cipher where the alphabet is reversed. The first letter is substituted with the last letter, the second with the second-to-last, and so on.

- **Affine Cipher (`affine_cipher.py`)**:
  - A more complex substitution cipher that uses a mathematical function to encrypt each letter of the alphabet.

### Tests

The `tests/` directory contains unit tests for each cipher implementation using the `unittest` framework. These tests help verify that the ciphers work as expected.

### Usage

#### Caesar Cipher

To use the Caesar Cipher for encryption or decryption:

```bash
python ciphers/caesar_cipher.py

To use the Atbash Cipher for encryption or decryption:

```bash
python ciphers/atbash_cipher.py

To use the Affine Cipher for encryption or decryption:

```bash
python ciphers/affine_cipher.py

To run the unit tests, navigate to the project root directory and use the following command:

```bash
python -m unittest discover tests

### License
This project is open-source and available under the MIT License.