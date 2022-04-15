OverTheWire Bandit Levels 0-14 Writeup

Jacob George

This is my write-up of OverTheWire Bandit Wargame, which focuses on learning Linux skills and basic security concepts. I completed levels 0 - 13.

Level 0 - Level 1:
![image7.png](https://www.dropbox.com/s/2djwr291opldhl9/image7.png?dl=0&raw=1)
The Password was stored in a readme file and used cat to display the password

Level 1 - 2:
![image4.png](https://www.dropbox.com/s/c7rlwt6bvrfsy4j/image4.png?dl=0&raw=1)
The file with the password was named "-" so I had to read the password by using: cat <-

Level 2 - 3:
![image15.png](https://www.dropbox.com/s/5dbdywp20p7kmqn/image15.png?dl=0&raw=1)
The file with the password had spaces in the filename. Files with spaces in it can be read with cat using: cat 'spaces in this filename'

Level 3 - 4:
![image11.png](https://www.dropbox.com/s/0o9ba3k1damauif/image11.png?dl=0&raw=1)
The file with the password was stored in the inhere directory. To view hidden files I used: ls -a

Level 4 - 5:
![image1.png](https://www.dropbox.com/s/9wc10d8s3ufioq4/image1.png?dl=0&raw=1)
The password was stored in a human-readable file (ASCII). I had to find the file by using the file command: file ./-file0* . This will scan each file and tell me which one is human-readable

Level 5 - 6:
![image3.png](https://www.dropbox.com/s/wtpe9mo7uh51wt8/image3.png?dl=0&raw=1)
The file with the password had very specific properties. It was human readable, 1033 bytes, and not executable. I had to locate the file by using the find command: find -type f -size 1033c ! -executable

Level 6 - 7:
![image2.png](https://www.dropbox.com/s/rgmd4y221ithet1/image2.png?dl=0&raw=1)
This file was owned by a specific group of Bandits and belonged to a specific user. I used the find command again to specify the user, group, and size to find out in which directory I had to go to:

find / -user Bandit7 -group Bandit6 -size 33c 2>/dev/null

Level 7 - 8:
![image9.png](https://www.dropbox.com/s/6pcw3stz8sqdsii/image9.png?dl=0&raw=1)
The level made me use the grep command, which I used to search a file for whole words (the use of -w flag): grep -w millionth data.txt

Level 8 - 9:
![image14.png](https://www.dropbox.com/s/ys7vbnl4npvx0qz/image14.png?dl=0&raw=1)
The password is the only line of text that only occurs once. Since there were many duplicates I had to use sort and uniq when using cat: cat data.txt | sort | uniq -c -u

Level 9 - 10:
![image6.png](https://www.dropbox.com/s/4dd627pbg0l9u7b/image6.png?dl=0&raw=1)
I had to use the strings command, which returns strings of each printable character inside files. Grep was used to specify the '=' character: strings data.txt | grep ===

Level 10 - 11:
![image5.png](https://www.dropbox.com/s/if6lkhsye2duehw/image5.png?dl=0&raw=1)
The password in the data.txt file was encoded using base 64. To access the data I had to use decode in base64: cat data.txt | base64 –-decode

Level 11 - 12:
![image8.png](https://www.dropbox.com/s/033sitvej069w7f/image8.png?dl=0&raw=1)
Since all lowercase (a-z) & uppercase letters (A-Z) were rotated by 13 positions, I had to use tr, which can be used for translating characters: cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'

Level 12 - 13:
![image12.png](https://www.dropbox.com/s/vvkg41bnane69tv/image12.png?dl=0&raw=1)![image10.png](https://www.dropbox.com/s/o3bkdoj5ygiu3ey/image10.png?dl=0&raw=1)
This was by far the longest level I had to do. It revolved creating a hexdump for a file (the original data.txt) repeatedly zipping and unzipping it until I reached the correct file that was human-readable

Level 13 - 14:
![image13.png](https://www.dropbox.com/s/yn2n1ra26v2abqa/image13.png?dl=0&raw=1)
For this level there was not a password but a private key, which I used to ssh into Bandit14:
ssh Bandit14@localhost -i sshkey.private
