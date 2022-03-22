# CryptoPals Crytography Challenges
**by Sean Cox and Ahmed Shaheen**

CrytoPals is a set of coding challenges focused around modern cryptography. It can be done in any language but we choose to do it in Python as Python is a very high level language and also has a lot of built in libraries for cryptography. we are approaching these challenges with the intention of improving our Python skills, as well as to gain a deeper understanding of both conceptual and fundamental cryptographic concepts. The challenges are split up into 8 sets of 8 challenges each, ranging from relatively simple to very difficult. This is a writeup explaining how we solved the first 4 challenges in set 1.

**The challenges can be found at [https://cryptopals.com/](https://cryptopals.com/)**

## Set 1, Challenge 1

This challenge is relatively simple. It asks us to write a program to convert a given hex string into base64. There are numerous ways to do this, but after some research, we decided to use the python library codecs.

    import  codecs

This library allowed us to write this function: 

    def  hex_to_b64(hex): 
    return  codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
This one line function first encodes the parameter string ‘hex’ into hex using the codecs.encode() function, and then decodes it into base64 using the codecs.decode() function.

    hex  =  "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(hex_to_b64(hex))

Setting the variable hex equal to the example hex string and printing out the return value of the hex_to_b64 function, we get the resulting base64 string.

	
![](https://lh4.googleusercontent.com/g_JzSmleuhHfKMdxcis8psODdUPKS9v-t1G3Lu-haxJQb-LUJAAUFCrIeh6FEQb3pith0xvuvfbaUYzgRzHjUBysXQf3GYqu4KgJkhCd473TwHkHeAtRqp9XfVm26mO-jnOxLMRj)

## Set 1, Challenge 2
This challenge is also pretty simple. We are asked to make a function that takes two equal length buffers and produces their XOR output. We are given two strings that, when XOR'd together, should produce a third given string. To accomplish this, we wrote the function fixed_XOR()

    def  fixed_XOR(hex1, hex2):
	    num  =  int(hex1,base=16)  ^  int(hex2,base=16)
	    return  hex(num)
The function takes two strings, hex1 and hex2 as parameters. It then produces a number, num, by converting the hex strings to base-16 integers and then XOR'ing them together. It then returns the hex value of the num. Calling the function with the two given input strings... 

    hex1  =  "1c0111001f010100061a024b53535009181c"
    hex2  =  "686974207468652062756c6c277320657965"
    print(fixed_XOR(hex1, hex2))

Gives us the expected output: 

![](https://lh6.googleusercontent.com/xb-vPsLi2SDYbqGo9OlSt73xZOfN6e2zThXvkI02OFliEkhkOM06vqRY-XJA_u2BgL-G9FLGZO_bAqXhy0-N_RO0NvNsbP5hfzxYt5o2MhF9rpJUz2VP2Tnz06REbhPO5-qlOHat)

## Set 1, Challenge 3
This is where it starts becoming slightly more difficult. We are asked to, given a hex encoded string, find a single character that it has been XOR'd against to produce a message. To accomplish this, we need to XOR all possible characters against the string, and then devise some way of 'scoring' the answers to find the correct message. To accomplish this, we implemented the function single_bit_xor().

First, we will use best_score to track the best score, and then use this to return the correct message. We start by setting this to 0. We set the variables message and key to null to start. 

       def  single_bit_xor(hex):
	    best_score  =  0
	    message  =  None
	    key  =  None
From there, we set the ciphertext and ascii_table variables. For the ciphertext, we simply convert the hex to bytes. ascii_table will be used as the basis for our scoring For this, we  use the list() function, with the range (97, 122) + [32]. This is all the lowercase english letters plus the space key. We will go on to use this as a comparison to find which string contains the most letters and thus is the correct string. 

    ciphertext  =  bytes.fromhex(hex)
    ascii_table  =  list(range(97, 122))  + [32]
We then start a for loop, with a range of 256, which is all the characters in the ascii table. 

    for  letter  in  range(256):
within this for loop is the bulk of our code. First, we convert the given letter to raw bytes. We then stretch this value for the entire length of the ciphertext 

    byte_str  =  letter.to_bytes(1, byteorder='big')  *  len(ciphertext)
   We then find the given plaintext by XOR'ing the letter with the cyphertext. 
  

     plaintext  =  bytes([ x^y  for (x,y) in  zip(ciphertext, byte_str)])


Now is time to calculate the score of this given plaintext. We do this with the sum() function. We will simply add up all the values when a character in the plaintext is found in the ascii table. The more English letters, the higher the score will be. 

    score  =  sum([j  in  ascii_table  for  j  in  plaintext])
We now calculate the best score. using an if statement, we determine if the given score for letter is higher or lower then the previous best. If it is higher, then we make that the new best score, set the message to the decoded string and set the key to the letter.

    if  score  >  best_score  or  not  best_score:
	    best_score  =  score
	    message  =  plaintext.decode("utf-8", "ignore")
	    key  =  chr(letter)
Once the for loop is complete we simply return the key and message.

    return  key, message
now calling the function with the given string...

    print(single_bit_xor("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))
We get the  output: 

![](https://lh3.googleusercontent.com/5iAJAnnQWc4TIfwII1PHb3k2O_STzzvP7TOm06Bq25eeyAgCsgLPD7NoR0P33I9LsZb2D2_TE1BH3rC9xKM2Wao7FlA1rHU6sbTzPnPeS-XbLtjvT3bhfvBJA20Y5ao_exOUJjeG)

The full function: 

    def  single_bit_xor(hex):
    best_score  =  0
    message  =  None
    key  =  None
    ciphertext  =  bytes.fromhex(hex)
    ascii_table  =  list(range(97, 122))  + [32]
    for  letter  in  range(256):
	    byte_str  =  letter.to_bytes(1, byteorder='big')  *  len(ciphertext)
		plaintext  =  bytes([ x^y  for (x,y) in  zip(ciphertext, byte_str)])
		score  =  sum([j  in  ascii_table  for  j  in  plaintext])
		if  score  >  best_score  or  not  best_score:
			best_score  =  score
			message  =  plaintext.decode("utf-8", "ignore")
			key  =  chr(letter)
	return  key, message

 
## Set 1, Challenge 4
This one mainly uses the function from challenge 3. We are given a file with hundreds of lines of hex encoded strings, and are tasked with XOR'ing them with a single character until we find the message, similar to challenge 3. The difference here is that not every string will have a valid message, in fact only one will. First, we need to be able to deal with the file, which for the purpose of this assingment I named s1c4text.txt. 

    import  fileinput
    import  linecache
By importing these two libraries we will be able to deal with the file. Now, we need to iterate through each line in the file, run our function from challenge 3, and save the best score, which is ultimately what we will print. To do this, we make a small change to the single_bit_xor function, now returning the best score aswell. 

    return  key, message, best_score

now, we set two variable which will be used to keep track of the best score and find the correct line in the file.

    oldBest  =  0
    i  =  0
   Now we begin to iterate through the file with a for loop. Each time we increment *i* by 1, and load in the current line to the singe_bit_xor() function. Then, if the score is better then the old best score, we set that score to the oldBest and set a variable keyAt equal to *i*. This will allow us to track the line where the correct message is found. 
   

    for  line  in  fileinput.input(files  ='s1c4text.txt'):
	    i  =  i  +  1
	    key, message, best  =  single_bit_xor(line)
	    if(best  >  oldBest):
		    oldBest  =  best
		    keyAt  =  i
Then, calling the function, and using the linecache.getline function, we return and print the proper message and key.

    print(single_bit_xor(linecache.getline('s1c4text.txt', keyAt)))
This gives us the correct output: 

![](https://lh6.googleusercontent.com/n0Bjbg02XtHhB2xHFhlmC0OEGlqmIEje_6xlOVePNyq9vFmM21vBHf-NW53486yc5tqwFkbWX4mUNCTJHH9BJ8nTlMrufF4WuSOmKd0aAnrQCJhtlp1k5tJmOlI0oQT0Nx1qjUA2)

