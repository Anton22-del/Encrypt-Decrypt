from cryptography.fernet import Fernet

while True:
    try:
        encoded_text = input("Code to Decrypt:\n>").encode('UTF-8')
        key = input("Encryption Key:\n>").encode('UTF-8')

        cipher_suite = Fernet(key)
        decoded_text = cipher_suite.decrypt(encoded_text)
        print("Decoded text:\n" + decoded_text.decode('UTF-8'))
    except:
        print("Decoding Failed, try another Key?")
    input("Press Enter to Decode Another Line\n>")
