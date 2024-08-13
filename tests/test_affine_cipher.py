import unittest
from ciphers.affine_cipher import affine_encrypt, affine_decrypt


class TestAffineCipher(unittest.TestCase):
    def test_affine_encrypt(self):
        # Test Affine encryption with a=5, b=8
        self.assertEqual(affine_encrypt("HELLO", 5, 8), "RCLLA")
        self.assertEqual(affine_encrypt("hello", 5, 8), "RCLLA")
        self.assertEqual(affine_encrypt("AFFINE CIPHER", 5, 8), "IHHWVC SWFRCP")
        # Test with non-alphabetic characters (should remain unchanged)
        self.assertEqual(affine_encrypt("HELLO 123!", 5, 8), "RCLLA 123!")
        # Test with different keys
        self.assertEqual(affine_encrypt("TEST", 7, 3), "ZLZA")

    def test_affine_decrypt(self):
        # Test Affine decryption with a=5, b=8
        self.assertEqual(affine_decrypt("RCLLA", 5, 8), "HELLO")
        self.assertEqual(affine_decrypt("IHHWVC SWFRCP", 5, 8), "AFFINE CIPHER")
        # Test with non-alphabetic characters (should remain unchanged)
        self.assertEqual(affine_decrypt("RCLLA 123!", 5, 8), "HELLO 123!")
        # Test with different keys
        self.assertEqual(affine_decrypt("ZLZA", 7, 3), "TEST")


if __name__ == "__main__":
    unittest.main()
