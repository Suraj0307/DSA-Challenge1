from cryptography.fernet import Fernet

print("Options: ")
print("1) Enter 1 for encrypting a new file :")
print("2) Enter 2 for decrypting a file :")
options = int(input())

# Encrypting a file
if options == 1:

    filename_with_location = input(
        "\nEnter filename with location to be encrypted.\n")
    filename_with_location = filename_with_location[1: len(
        filename_with_location) - 1]

    key = Fernet.generate_key()

    # Generating Folder location
    tar_word = "\\"

    # .rindex gives the last location of the character
    res = filename_with_location.rindex(tar_word)
    Folder_Location = filename_with_location[0:res + 1]

    with open(Folder_Location + 'my_key.key', 'wb') as mykey:
        mykey.write(key)

    print("\nGenerated your key in a file named 'my_key.key'.")
    print("Keep it safe to access the file.\n")

    # Reading the key
    with open(Folder_Location + "\\" + 'my_key.key', 'rb') as mykey:
        key = mykey.read()

    # Encryption process started
    f = Fernet(key)

    # Encrypting the file
    with open(filename_with_location, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    filename = filename_with_location[res + 1:]
    with open(Folder_Location + "__Encrypted__" + filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    encrypted_file_name = Folder_Location + "__Encrypted__" + filename
    print(f"Successfully encrypted the file with name '{encrypted_file_name}'")


# For Decryption of a particular file
elif options == 2:
    print("\n")
    filename_with_location = input("Enter filename with location to be Decrypted.\n")
    filename_with_location = filename_with_location[1: len(
        filename_with_location) - 1]

    print("\n")
    Key_Location = input("Enter the particular key file location associated with the file\n")
    Key_Location = Key_Location[1: len(Key_Location) - 1]

    # Decrypting the file to access the original content
    # Reading the key or password u can say
    with open(Key_Location, 'rb') as mykey:
        key = mykey.read()

    f = Fernet(key)
    # print(key)

    # Accessing the encrypted file
    with open(filename_with_location, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    # print(encrypted)
    decrypted = f.decrypt(encrypted)
    # We have accessed the encrypted content present

    # Writing into a new file

    # Generating Folder location
    tar_word = "\\"

    # .rindex gives the last location of the character
    res = filename_with_location.rindex(tar_word)
    Folder_Location = filename_with_location[0:res + 1]
    filename = filename_with_location[res + 1:]

    with open(Folder_Location + "..Decrypted.." + filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    print("\n")
    Decrypted_file_name = Folder_Location + "..Decrypted.." + filename
    print(f"Successfully Decrypted the file with name '{Decrypted_file_name}'")

else:
    print("Please enter a valid option.\n")
