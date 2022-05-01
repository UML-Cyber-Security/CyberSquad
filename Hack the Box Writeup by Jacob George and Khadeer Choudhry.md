# Hack the Box Writeup
*Written by Jacob George and Khadeer Choudhry*
>*Hack The Box is a massive, online cybersecurity training platform, allowing individuals, companies, universities and all kinds of organizations around the world to level up their hacking skills. Each week new content is added and allows users to have hands on penetration testing by gamefieing the challenges with points, badges, first blood, multiplayer battles, progress bars, “Hall of Fame” scoreboards, ranks, teams, and more.*

## Meow 

This box gave a basic introduction to pinging IP's, port scanning using Nmap, & using telnet which allowed me to access the root login and get the flag. Task 5 meow wanted the player to use the ping command where I was able to send a request over the network to the HTB IP. Task 6 made the user practice Nmap, which will scan the IP for open ports. Task 8 made the user use the telnet command, which will open a command line on a remote computer. I used telnet with the HTB IP and logged in as the root user. If you list all the files for the root user, one of the files will be the flag.txt, which can be displayed using the cat command.

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970157568007761930/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970157568246812782/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970157568485904394/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970157568729178132/unknown.png)

# Fawn

This box introduced to the player the basics of file-transferring protocols as well as introducing the player to basic FTP programs and commands. When scanning for available ports on the HTB IP using Nmap, port 21 was open that allows the player to use the command FTP. When using the command “ftp <IP of HTB>”, you are allowed to set up a remote connection that can access the other remote computers' files, allowing you to transfer over files to your own local machine. The basic Linux commands work while FTP is running. By listing the files and finding the file you want, you can use the get command followed by the file name to transfer the file to your machine. 

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970157433043427348/unknown.png)

# Dancing

The main concept introduced in this box was a Server Message Block which gives the player another opportunity to practice an example of the client-server model. When using the smbclient, you can specify flags to perform certain actions. For example, the -L flag can be used to list the contents of the share. Once you can access the shares you can cd into different directories, download the files using the get command and find the flag.

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970157206299357244/unknown.png)
  
![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970157205502431262/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970157205800239114/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970157206030909481/unknown.png)

# Appointment

This box introduces basic SQL (Structured Query Language) injection attacks and demonstrates how dangerous specific SQL injections can be. If you put in the HTB IP into a web browser, you will be taken to a login page where you can attempt to brute force the login, or perform an injection where you put the username in single quotes followed by the # symbol, which is normally used to comment out parts of code. As long as the username has that specific format, the password can be anything and the flag can be easily obtainable.

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970157887185883196/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970157886808399882/unknown.png)
  
![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970157886464479282/unknown.png)


# Sequel

This box has the player practice a community-developed MySQL program called MariaDB, which displays certain tables of databases. In a way, this program is like a giant directory where in order to get the flag you have to just go into the said directory and find it. 

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970158073408811048/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970158073731756072/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970158074046349372/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970158074381869066/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970158074641928253/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970158074922938368/unknown.png)


# Crocodile

This box lets the user test their knowledge of basic ftp commands. The player has to transfer over a list of allowed usernames and allowed passwords once they’ve scanned for ports and used the get command in ftp. Then in order to brute force the login for a specific URL, the player has to use gobuster. Using gobuster will scan specific directories the user needs to find the flag. Once gobuster is run, they can find a .php file called login, where if they type the HTB IP/login.php, will take them to the login page where they can start brute-forcing the logins and passwords found earlier. 

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970158031746793472/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970158031927132230/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970158032115879966/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970158032329781268/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970158032539508816/unknown.png)

![alt text](https://cdn.discordapp.com/attachments/815005925093933117/970158032774397972/unknown.png)
