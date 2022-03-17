import multiprocessing
import LoadBar
from HashPasswords import pass_compare_with_pickle

def authenticate_login(pswd, sal, pep, file, email):
  print('Creating login token...')
  __name__ = "__main__"
  if __name__ == "__main__":
    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    p1 = multiprocessing.Process(target=LoadBar.exe, args=[])
    p2 = multiprocessing.Process(target=pass_compare_with_pickle, args=(pswd, sal, pep, file, email, return_dict))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

  status, name, email = return_dict.values()[0]
  LoadBar.writeResult(status)
  return status, name, email