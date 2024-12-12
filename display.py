from time import sleep
from tqdm import tqdm


def display_intro():
  print(". _______________________________________________________  .")
  print("|                                                          |")
  print("|                 WELCOME TO MY RECOMMAN-                  |")
  print("|                      DATION ENGINE                       |")
  print("|                                                          |")
  print("|                          BEGIN                           |")
  print("|                                                          |")
  print(". ________________________________________________________ .")
  
def progress_bar():
  for i in tqdm(range(1000)):
    sleep(.005)