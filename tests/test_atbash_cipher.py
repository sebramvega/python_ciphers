import unittest
from ciphers.atbash_cipher import atbash_cipher


class TestAtbashCipher(unittest.TestCase):
    def test_atbash_cipher(self):
        # Test Atbash cipher with basic input
        self.assertEqual(atbash_cipher("HELLO"), "SVOOL")
        self.assertEqual(atbash_cipher("hello"), "SVOOL")
        self.assertEqual(atbash_cipher("GSRH RH Z HVXIVG"), "THIS IS A SECRET")
        # Test Atbash cipher with full alphabet
        self.assertEqual(
            atbash_cipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ZYXWVUTSRQPONMLKJIHGFEDCBA"
        )
        # Test Atbash cipher with non-alphabetic characters
        self.assertEqual(atbash_cipher("123!"), "123!")
        self.assertEqual(atbash_cipher(""), "")  # Test with empty string


if __name__ == "__main__":
    unittest.main()
