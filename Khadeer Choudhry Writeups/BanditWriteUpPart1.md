# _Bandit Part 1 Write Up_
# _Levels 0->12_
#### By: Khadeer Choudhry

Over the Wire hosts a wide variety of what is called "Wargames" which generally are different games that teach different security concepts. Bandit specifically looks at how to use the terminal more optimally and we will be using the Windows Terminal to complete these levels. This is a beginner game mode, so if you just started doing Security related games and competitions then this is a great place to start. We will be looking at levels 0->12 and stepping you through how to do them.

![Cute Cat](https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/cute-cat-photos-1593441022.jpg?crop=0.669xw:1.00xh;0.166xw,0&resize=640:*)

## Level 0

Level 0 of Bandit requires the user to ssh into the server and enter the password. SSH is a command that connects a person to a to a server by establishing a connection between the two hosts. 
For this level the user has to connect to bandit.labs.overthwire.org on port 2200 with the username as bandit0 and the password as bandit 0.
The user needs to type in into the terminal:
```ssh bandit0@bandit.labs.overthewire.org -p 2220```
The terminal should result in a screen like this:

[![Screenshot-2022-03-24-210809.png](https://i.postimg.cc/0jxPvyHw/Screenshot-2022-03-24-210809.png)](https://postimg.cc/k6jkFqCJ)

Now enter the password bandit0 and the screen should look like this:

[![Screenshot-2022-03-24-214818.png](https://i.postimg.cc/T2WtMcrg/Screenshot-2022-03-24-214818.png)](https://postimg.cc/ThfVngN3)

And viola you just completed the introductory level. Now we can go onto the next level.

## Level 1

Level 1 of Bandit requires the user to read a file inside of the directory they are currently in. The command to read the files inside of the current directory is:
```ls```
When you type ls into the terminal you should see an output that looks like this:

[![Screenshot-2022-03-24-215211.png](https://i.postimg.cc/8PzsfZtr/Screenshot-2022-03-24-215211.png)](https://postimg.cc/4njXrQCJ)

The file that is inside the directory is a file called readme. The cat command is what we will be using to read the file. Cat is a command that is used to read files. To read the file type:
```cat readme```
The password should show as a result.

[![Screenshot-2022-03-25-202618.png](https://i.postimg.cc/W1Hn2LDy/Screenshot-2022-03-25-202618.png)](https://postimg.cc/18D6Hdr0)

Copy the line and exit out of the ssh. To exit out of the ssh type in exit in the terminal and you will subsequently leave the level.

[![Screenshot-2022-03-25-202758.png](https://i.postimg.cc/3N1XVP5n/Screenshot-2022-03-25-202758.png)](https://postimg.cc/8fFfrXC6)

Next type in:
``` ssh bandit1@bandit.labs.overthewire.org -p 2220```
Or to make it easier, the terminal remembers the previous commands so to access the previous commands press the up arrow key until you find the previous ssh line and alter the username number.
Then press enter and paste the password that was found and the level is complete.

## Level 2

Once inside the next level looking at the directory you will notice that the file is just hyphen.

[![Screenshot-2022-03-25-212724.png](https://i.postimg.cc/1Xpfg65T/Screenshot-2022-03-25-212724.png)](https://postimg.cc/vxZQk4nL)

When you do type in:
```cat -```
This doesn't produce anything and the user will have to press:
```ctrl-c```
The result should look like this:

[![Screenshot-2022-03-25-224234.png](https://i.postimg.cc/wB2PzT8d/Screenshot-2022-03-25-224234.png)](https://postimg.cc/kVVwFCgj)

To read files that have a hyphen in the beginning you type:
```cat ./```
So in this regard we type in and the result should look like this:
```cat ./-```

[![Screenshot-2022-03-25-224516.png](https://i.postimg.cc/fydQMnfj/Screenshot-2022-03-25-224516.png)](https://postimg.cc/MfzFYL4v)

This file contains the password so copy the password, then ssh into the next level and paste the password.

## Level 3

Immediately checkin ght edirectory will reveal a file called 'space in this filename'

[![Screenshot-2022-03-25-225137.png](https://i.postimg.cc/g2J4hy11/Screenshot-2022-03-25-225137.png)](https://postimg.cc/N531qXsx)

No worries, instead you use single quotes around the file with spaces in the file, in this case you would type:
```cat 'spaces in this filename'```

[![Screenshot-2022-03-25-233117.png](https://i.postimg.cc/hGwp0JVM/Screenshot-2022-03-25-233117.png)](https://postimg.cc/xkvvf1xb)

Copy the password and paste the password when you ssh onto the next level.

## Level 4

In this level checking the directory will reveal another directory called inhere. Usually, the directory is highlighted in blue.

[![Screenshot-2022-03-25-233440.png](https://i.postimg.cc/GmD2pVq2/Screenshot-2022-03-25-233440.png)](https://postimg.cc/VJY1GGyQ)

To double-check if it is a directory you can use the file command to check if it.

[![Screenshot-2022-03-25-233600.png](https://i.postimg.cc/gr9CtSRS/Screenshot-2022-03-25-233600.png)](https://postimg.cc/BPg7XCmH)

To change directories we will use the command:
```cd```
cd is a command that means change directory so to enter the directory type in:
```cd inhere```
Entering the directory and typing in ls will result in nothing popping up:

[![Bandit3-ls.png](https://i.postimg.cc/t4chmsQg/Bandit3-ls.png)](https://postimg.cc/RWc6WV0r)

This is because the file is hidden and thus will not be found by typing in ls. To find hidden files type in the command:
```ls -a```
This will show hidden files and as a result you will find the hidden file in the directory.

[![Bandit3.png](https://i.postimg.cc/6Tsk0WWb/Bandit3.png)](https://postimg.cc/n9kSVtQq)

Type cat .hidden and the password to the next level will be shown.

## Level 5

At the start of this level, you will notice a directory called inhere. Change to that directory and you will notice a multitude of files with one of them being the one that stores the password. 

[![Bandit4-dir.png](https://i.postimg.cc/90BkGGk0/Bandit4-dir.png)](https://postimg.cc/n9CTxQpf)

Using cat for each of these files is inefficient and not recommended what we can do however is check the files to see if they are the correct ASCII Text file. The command “file” checks the type of file, but simply typing the file for each file is still inefficient. What is recommended is using the file command while using a wildcard. The wildcard is the ‘*’ symbol and that is pretty much a placeholder symbol This placeholder symbol can encapsulate anything so it is wise to put a placeholder at the end. 
The command that we are going to use has a wildcard * which will make sure that each file will be targeted. 
```file ./-file*```

[![Bandit4.png](https://i.postimg.cc/Xvc9NQBr/Bandit4.png)](https://postimg.cc/cKCvX7mW)

The file that contains the password is the ASCII text file which can be read by typing in “cat ./-file07”. With the password obtained move onto the next level.

## Level 6

In this level, once you have entered the inhere directory there will be a vast amount of directories that are layed out. 

[![Bandit5-dir.png](https://i.postimg.cc/fWBP8vLj/Bandit5-dir.png)](https://postimg.cc/BtPN6H2X)

It is impractical to go into each and every single directory and try and find the file manually by using cat or file for each directory. A far more practical way of finding the file is by using the "find" command in linux. It does what it says, it will find the file with what the user specifies. To find the file that has the password type in:
```find -type f -size 1033c```

[![Bandit5.png](https://i.postimg.cc/QNwPTJd6/Bandit5.png)](https://postimg.cc/w350KJJJ)

The -type checks what type of file that the find commands wishes to find and -type f is a regular file. The -size is what it says, it will find the size of the file found and in this case -size 1033c.
Change to the directory specified and cat the hidden file. With the password in hand move onto the next level and enter the password.

## Level 7

This level will have you starting in the home with nothing in the directory. The file is hidden on the system and it is up to the user to find it. The specification are that the file is owned by user bandit7, owned by group bandit6, and it is 33 bytes in size. With that in mind it is best to go to the root of the system to find the file and then with the specification in mind use the file command to find the file. In this case we will use the command:
```find / -user bandit7 -group bandit6 -size 33c```
The -user and -group portion is what it says, it will find the user and group owner of the file and the -size 33c will find a file that is 33 bytes in size. The resulting screen should look like this:

[![Bandit6-dir.png](https://i.postimg.cc/wTJ0CKQz/Bandit6-dir.png)](https://postimg.cc/BXSTFVz7)

It may look confusing at first, but all we are here for is to find the file that doesn't deny permission for the user to read and in this case it is found in "/var/lib/dpkg/info/bandit7.password".

[![Bandit6.png](https://i.postimg.cc/G27fzZnD/Bandit6.png)](https://postimg.cc/cg3TLkH1)

Copy and paste the directory into the cat command and the password for the next level will show.

## Level 8

This level tasks the user to find the password next to the word "millionth" inside data.txt. It is not feasible to cat the file and search the word manually as that would take a considerable amount of time and effort. This is where the command grep comes in handy. Grep parses through the string or the entire file that matches the regex statement made. In this case we need to find the word "millionth" and thus the command we use to find the password is:
```grep "millionth" data.txt```
Grep would return the whole line instead of just the word and the result should look like this:

[![Bandit7.png](https://i.postimg.cc/wBBdMP5W/Bandit7.png)](https://postimg.cc/87xYnZ0W)

With the password found, copy and paste the password and move onto the next level.

## Level 9

This level tasks the user to find the password in the data.txt, however it is the only line that occurs once. It is not feasible to look at the data.txt flat out as it is impossible to tell what only occurs once. We will be using two commands in tandem together for this level. The first command is called sort which sorts the text file into sorted order which in this case would mean that the matching lines would be next to each other. The other command we will be using is the uniq command which filters out the text of repeating lines. This only works if the repeated lines are next to each other thus necessitating the use of sort. To use multiple commands together we need to use a technique called piping which uses the | command. The first command used is on the left side of the pipe and the second command used is on the right side of the pipe. To find the password on this level we need to use the commands together like this:
```sort data.txt | uniq -u```
The result of using this command should look like this:

[![Bandit8.png](https://i.postimg.cc/x1hWjCCd/Bandit8.png)](https://postimg.cc/87dytTL8)

With the password on hand we can move onto the next level.

## Level 10

This level tasks the user to find the password in a file taht has many unknown symbols. Using cat to data.txt will result in this output:

[![Bandit-out.png](https://i.postimg.cc/K8SPZhb2/Bandit-out.png)](https://postimg.cc/Tp0L9Sh7)

Looking through this file and finding the password is highly inefficient and so we can use two commands to find the password. The first command is the string command which returns only the strings in the file and the second command is grep which parses through the text of the specified letter and returns the line that has the letter. We must pipe these commands using | symbol and the command to find the password is as well as the resulting output:
```strings data.txt | grep =```

[![Bandit9.png](https://i.postimg.cc/KvrPvs83/Bandit9.png)](https://postimg.cc/4my7WPtX)

The output tells you the password and it is the second to last line. Copy and paste the password to continue.

## Level 11

For this level, the user needs to find the password in the text file that is encoded in base64. This is where the base64 command comes in handy, the base64 command can encode and decode files into the base64 format which can make storing and transmitting data easier. We must specify the -d in base64 to specify decoding a file. The command to find the password and the result is:
```base64 -d data.txt```

[![Bandit10.png](https://i.postimg.cc/0QnvNsFH/Bandit10.png)](https://postimg.cc/HcrRSfpQ)

Now that the password is found we may continue onto the next level.

## Level 12

For this level, the data.txt is encrypted through rot-13 which is a primitive encryption that switches the letter to the next 13th letter. Using cat on the data.txt would result in this:

[![Bandit11-dir.png](https://i.postimg.cc/g2FbWs27/Bandit11-dir.png)](https://postimg.cc/LnTbkzfk)

The commands that we will be using the tr command or the translate command which translates the given string or text. The command that we will be using to find the password is:
```cat data.txt | tr 'n-za-mN-ZA-M' 'a-zA-Z'```
The result looks like this:

[![Bandit11.png](https://i.postimg.cc/NGZjK106/Bandit11.png)](https://postimg.cc/Wt6vKqgz)


