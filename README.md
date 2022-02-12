# DSA-Challenge1
#### This is a very interesting project on Data Structures and Algorithms
Advances in digital content transmission have increased in the past few years. Security and privacy issues of the transmitted data have become an important concern in multimedia technology
So i have desgined an Encrytption/Decryption algorithm to to protect the videos, so that the algorithm may digitally hide your videos to avoid unauthorised interception and viewing. To safeguard the material, videos are encrypted with an encoding method. Without the proper authorization, no one can watch the encrypted videos.

# How the algorithm is made.
This is the most important part of the whole project.
Logic behind algorithm is really very simple and straightforward.
I have first generated 5 strings and they are totally random.
I will be using strings ascii values to do xor operation on the file.
After that i did xor operation on the file bytes with each 5 strings ascii values.
For encryption/decryption most used operator is xor(^) thats why i used this and it was very easy to understand.

# Encryption/Decryption:
The process of converting plaintext to ciphertext is called enciphering or encryption; restoring plaintext from ciphertext is deciphering or decryption. Both the encryption and decryption algorithms take a key (K) and plaintext/ciphertext as input. In the case of images, plaintext is a set of pixel values arranged in an orderly manner. Encrypting images/videos constitutes reordering these pixel values so that they convey no visual information about the original image. An image/video can also be encrypted in the compressed domain. In this case, the DCT coefficients are encrypted in such a way that the content is made illegible for the unauthorized. Only an authorized user can get back the original content using the decryption algorithm


# Follow the procedure to use.
### Step 1.
#### Install python greter than 3.6 and less than 3.9 

### Step 2.
#### Run main.py file in the terminal.
![image](https://user-images.githubusercontent.com/90147205/153707330-b2f444c6-b376-44e4-90a3-6d714e6c77e6.png)


### Step 3.
#### Enter 1 if you want to do encryption of a file.
#### Enter 2 if you want to do decryption of the file.
![image](https://user-images.githubusercontent.com/90147205/153707343-3c094b56-ddba-4cc5-9cc3-51a8881b959f.png)


### Suppose you entered 1
### Step 3.1
#### Enter the filename in double quotes with proper location and hit enter.
![image](https://user-images.githubusercontent.com/90147205/153707372-a0e803ff-0157-40dd-bc02-e4e10000956d.png)
#### You will get further details in the screeen.

### Suppose you entered 2.
### Step 3.1
### Enter the filename in double quotes with proper location and hit enter.
![image](https://user-images.githubusercontent.com/90147205/153707566-e3dc100c-a757-448c-a2b9-22a16d8b3e90.png)

### Step 3.2
### Enter the particular key file location associated with the file in double quotation.
![image](https://user-images.githubusercontent.com/90147205/153707605-eba01b17-8785-4a77-9d32-a97ee30deb37.png)
#### You will get further details in the screeen.
# Your feedbacks are always welcomed.
# Thank You!
