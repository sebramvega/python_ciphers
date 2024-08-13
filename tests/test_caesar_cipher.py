import unittest
from ciphers.caesar_cipher import encrypt, decrypt


class TestCaesarCipher(unittest.TestCase):
    def test_encrypt(self):
        # Test encryption with a shift of 3
        self.assertEqual(encrypt("hello", 3), "khoor")
        self.assertEqual(encrypt("HELLO", 3), "khoor")
        self.assertEqual(encrypt("xyz", 3), "abc")
        # Test encryption with no shift
        self.assertEqual(encrypt("hello", 0), "hello")
        # Test encryption with full rotation (shift of 26)
        self.assertEqual(encrypt("hello", 26), "hello")

    def test_decrypt(self):
        # Test decryption with a shift of 3
        self.assertEqual(decrypt("khoor", 3), "hello")
        self.assertEqual(decrypt("KHOOR", 3), "hello")
        self.assertEqual(decrypt("abc", 3), "xyz")
        # Test decryption with no shift
        self.assertEqual(decrypt("hello", 0), "hello")
        # Test decryption with full rotation (shift of 26)
        self.assertEqual(decrypt("hello", 26), "hello")


if __name__ == "__main__":
    unittest.main()
