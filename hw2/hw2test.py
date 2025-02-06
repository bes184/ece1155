# imports
import unittest
import hw2 as hw2

class TestHW2(unittest.TestCase):
    def test_shiftcipher(self):
        print("\n\nShift Cipher Test")
        plaintext = 'SSOEATBENEDUMHALLOHARASTREET'
        k = 5
        ciphertext = 'XXTJFYGJSJIZRMFQQTMFWFXYWJJY'
        print("Ciphertext: ", ciphertext)
        print("Shift:      ", k)
        print("Plaintext:  ", plaintext)
        try:
            self.assertEqual(hw2.shifttext(plaintext, k), ciphertext)
            print("Test passed.")
        except:
            print("Test failed")

    def test_randomsubstitutioncipher(self):
        print("\n\nRandom Subsitution Cipher Test")
        plaintext = 'PENNSYLVANIA'
        [ciphertext, encodedalphabet] = hw2.randomsubstitution(plaintext)
        print("Alphabet:  ", hw2.ALPHABET)
        print("Encoder:   ", encodedalphabet)
        print("Plaintext: ", plaintext)
        print("Cipertext: ", ciphertext)
        decryptedtext = hw2.decryptrandomsubstitution(ciphertext, encodedalphabet)
        try:
            self.assertEqual(decryptedtext, plaintext)
            print("Test passed.")
        except:
            print("Test failed")
        
# if __name__ == '__main__':
#     unittest.main()