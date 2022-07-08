from cryptography.fernet import Fernet

while True:

    datab = input("Text to encode\n>").encode('UTF-8')

    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encoded_text = cipher_suite.encrypt(datab)
    decoded_text = cipher_suite.decrypt(encoded_text)
    print("key:\n" + key.decode('UTF-8'))
    print("Encoded text:\n" + encoded_text.decode('UTF-8'))
    input("Press Enter to Encrypt Another Line\n>")
