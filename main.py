import os
import random
import string

print("Options: ")
print("1) Enter 1 for encrypting a new file :")
print("2) Enter 2 for decrypting a file :")
options = int(input())


def Encrypt(filename):
    file = open(filename, 'rb')
    data = file.read()
    file.close()

    data = bytearray(data)

    # Getting folder location
    tar_word = "\\"
    # .rindex gives the last location of the character
    res = filename_with_location.rindex(tar_word)
    Folder_Location = filename_with_location[0:res + 1]

    key_file = open(Folder_Location + "my_key.key", 'w')
    for i in range(5):
        key_file.write(random.choice(string.ascii_letters))
    key_file.close()
    print("\nGenerated your key in a file named 'my_key.key'.")
    print("Keep it safe to access the file.\n")

    with open(Folder_Location + 'my_key.key', 'r') as my_key:
        key_data = my_key.read()

    print("Encryption going on\nPlease wait.")
    key_data = [ord(key_val) for key_val in (key_data)]
    for key in key_data:
        for index, value in enumerate(data):
            data[index] = value ^ key

    filename = filename_with_location[res + 1:]
    file = open(Folder_Location + "--Encrypted--" + filename, "wb")
    file.write(data)
    file.close()

    encrypted_file_name = "--Encrypted--" + filename
    print(f"Successfully encrypted the file with name '{encrypted_file_name}'")


def Decrypt():
    filename_with_location = input("Enter filename with double quotations and proper location.\n")
    filename_with_location = filename_with_location[1: len(
        filename_with_location) - 1]

    file = open(filename_with_location, 'rb')
    data = file.read()
    file.close

    data = bytearray(data)

    Key_Location = input("Enter the particular key file location associated with the file in double quotation.\n")
    Key_Location = Key_Location[1: len(Key_Location) - 1]

    # Reading the key or password u can say
    with open(Key_Location, 'r') as my_key:
        key_data = my_key.read()

    key_data = [ord(key_val) for key_val in (key_data)]
    for key in key_data:
        for index, value in enumerate(data):
            data[index] = value ^ key

    # Generating Folder location
    tar_word = "\\"

    # .rindex gives the last location of the character
    res = filename_with_location.rindex(tar_word)
    Folder_Location = filename_with_location[0:res + 1]
    filename = filename_with_location[res + 1:]

    file = open(Folder_Location + "--Decrypted--" + filename, "wb")
    file.write(data)
    file.close()

    print("\n")
    Decrypted_file_name = "--Decrypted--" + filename
    print(f"Successfully Decrypted the file with name '{Decrypted_file_name}'")


# Encrypting a file
if options == 1:

    filename_with_location = input(
        "\nEnter filename with proper location and in double quotation marks.\n")
    filename_with_location = filename_with_location[1: len(
        filename_with_location) - 1]

    Encrypt(filename_with_location)



# For Decryption of a particular file
elif options == 2:
    print("\n")
    Decrypt()

else:
    print("Please enter a valid option.\n")
