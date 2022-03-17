import encryption
import stdiomask
import HashPasswords
import multiprocessor
import os

def registerUser():
  exit_req = ['quit', 'q', 'exit', 'leave', 'cancel']
  afirm = ['yes', 'y']
  tempFile = input("Enter Full Name: ") + '\n'
  if tempFile[:-1] in exit_req:
    exit_status = input(f'You said "{tempFile[:-1]}", would you like to quit? (y/n) ')
    if exit_status in afirm: 
      return -1
    
  tempFile += input("Enter Email Address: ").lower()

  numTries = 3
  while(numTries > 0):
    print("Password must:\n\tBE:  \t8 to 25 chars\n\tHAVE:\tAt least one uppercase letter\n\tHAVE:\tAt least one lowercase letter\n\tHAVE:\tAt least one diget")

    pswd1, len_and_contains_up_low_dig = encryption.calculateKey(stdiomask.getpass(prompt='Enter Password: ').encode())

    if not len_and_contains_up_low_dig:
      print('That password is missing or failing one or more of the requirements...\n')
      continue

    
    if pswd1 != encryption.calculateKey(stdiomask.getpass(prompt='Re-Enter Password: ').encode())[0]:
      numTries = numTries - 1
      if (numTries > 0):
        print("Passwords do not match. Try again.")
      else:
        print("Too many mismatched password attempts. Exiting...")
        leave(False)
      continue
    
    break

  print("Passwords match")
  salt, pepper, pickle = HashPasswords.condiments()
  bytes_object = encryption.encrypt_bytes(tempFile.encode(), HashPasswords.calcMaster(pswd1, salt, pepper, pickle))
  user_file = 'userData.encrypted'
  with open(user_file, 'wb') as uf:
    uf.write(bytes_object)

  print("User registered.\n")

  
  
def login():
  email = ""
  numGuesses = 3
  sal, pep = HashPasswords.getCondiments()

  curHash = HashPasswords.calcPeperHash('pswd'.encode(), sal, pep)
  print('\n*Email is NOT case-sensitive*',end='')
  while (numGuesses > 0):
    email = input("\nEnter Email Address: ")
    if email.lower() == 'quit':
      inp = input("You enterd " + email + " ... are you trying to quit the program? (y/n) ")
      while inp != 'n' and inp != 'y' :
        print(inp + " is not 'y' or 'n'")
        inp = input("You enterd " + email + " ... are you trying to quit the program? (y/n) ")
      if inp == 'y':
        leave(False)

    usrin = encryption.calculateKey(stdiomask.getpass(prompt='Enter Password: ').encode())[0]
    login_success, og_name, og_email = multiprocessor.authenticate_login(usrin, sal, pep, 'userData', email.lower())
    if not login_success:
      numGuesses -= 1
      if (numGuesses > 0):
        print("Incorrect email or password, please try again.")
      else:
        print("Too many incorrect email and password attempts. Exiting...")
        leave(False)
      continue

    
    curHash = HashPasswords.calcPeperHash(usrin, sal, pep)
    break

  return curHash, og_name, og_email



def leave(isError):
  if not isError:
    quit()

def getNumUsers() -> int:
  if os.path.exists('userData.encrypted'):
    return 1
  return 0