#Developed by: Nokky07

#Mr Hughes Story

#Project Started 16/09/22





#imports
import time
import os
import art
import random
import functions

#clear Function
def clear():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")


#Variables
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m"
black = "\033[0;30m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"

functions.clear()


#Story Starts Here (MAIN)
def chapter1():
  #UI Player Stats

  PHealth = 50  #Players Health
  BHealth = 100  #Boss Health
  print(Red + art.Chapter1)
  print("-------------------------------------------------------------------")
  time.sleep(1)
  clear()
  print(
    Blue +
    "\n\nAnother day at Our Lady's Highschool. Mr Hughes, a HighSchool Computing Science educator who teaches python-like coding to his students, works in the computing science classroom. However, one of his students Cristian Micu, a rebel against the laws of our all-powerful God Mr Hughes treats him as an opponent."
  )

  Enter = input(Green +
                "\n\n(Enter) - Continue\n\n\n Press Or Type An Option: ")

  if Enter == "" or Enter == "Enter":
    clear()
  else:
    print(Red + "\n\nInvalid Option Try Again!")
    print(art.inv)
    time.sleep(1)
    clear()
    chapter1()
  print(
    Blue +
    "\n\nCristain Micu had been working on a python program for months and needed help one day and asked from the teacher how would you fix this line of code? Mr Hughes proceeds to help Cristian but since it was April fools day he deleted it and Cristian didn't know what CTRL-Z does at the time of the incident. Cristian starts to argue with the person he shouldn't mess with."
  )
  Enter = input(Green +
                "\n\n(Enter) - Continue\n\n\n Press Or Type An Option: ")

  if Enter == "" or Enter == "Enter":
    clear()
  else:
    print(Red + "\n\nInvalid Option Try Again!")
    print(art.inv)
    time.sleep(1)
    clear()
    chapter1()

  clear()
  print(Blue + "           ")
  time.sleep(0.1)
  clear()
  print("|         |")
  time.sleep(0.1)
  clear()
  print("||       ||")
  time.sleep(0.1)
  clear()
  print("|||     |||")
  time.sleep(0.1)
  clear()
  print("||||   ||||")
  time.sleep(0.1)
  clear()
  print("||||| |||||")
  time.sleep(0.1)
  clear()
  print("|||||||||||")
  time.sleep(0.1)
  clear()
  print("|||||F|||||")
  time.sleep(0.1)
  clear()
  print("|||| Fi||||")
  time.sleep(0.1)
  clear()
  print("|||s Fig|||")
  time.sleep(0.1)
  clear()
  print("||ss Figh||")
  time.sleep(0.1)
  clear()
  print("|oss Fight|")
  time.sleep(0.1)
  clear()
  print("Boss Fight")
  time.sleep(0.5)
  clear()

  def bossfight(PHealth, BHealth):
    #Boss Fight Arrays
    Defend = [art.B21, art.B22, art.B23, art.B24, art.B25, art.B26]
    Insult = [art.B11, art.B12, art.B13, art.B14, art.B15, art.B16]
    Heal = [art.B31, art.B32, art.B33]
    print(blue + art.BossFight)
    BOSS1 = input(
      blue +
      "\n\nATK - Insult!\n\n---------------------------- \n\nDEF - Defend!\n\n---------------------------- \n\nHEL - Heal!\n\n\n Select An Option: "
    )
    if BOSS1 == "ATK":

      for i in range(1):
        BOSSS1 = random.choice(Insult)
        print(Red + "\n\n" + BOSSS1)

        if BOSSS1 == art.B11:
          PHealth = PHealth - 10
          print(Red + f"\nYour Health Is Now {PHealth}HP")
          time.sleep(1)
          clear()

          if BHealth <= 0:
            break
            clear()
            print(art.win1)
          if PHealth <= 0:
            break
            clear()
            print(art.dead)
            bossfight(100, 100)

          bossfight(PHealth, BHealth)
        elif BOSSS1 == art.B12:
          BHealth = BHealth - 5
          print(Red + f"\nBrian's Health Is Now {BHealth}HP")
          time.sleep(1)
          clear()

          if BHealth <= 0:
            break
            clear()
            print(art.win1)
          if PHealth <= 0:
            break
            clear()
            print(art.dead)
            
          bossfight(PHealth, BHealth)
        elif BOSSS1 == art.B13:
          PHealth = PHealth - 5
          print(Red + f"\nYour Health Is Now {PHealth}HP")
          time.sleep(1)
          clear()

          if BHealth <= 0:
            break
            clear()
            print(art.win1)
          if PHealth <= 0:
            break
            clear()
            print(art.dead)
            
          bossfight(PHealth, BHealth)
        elif BOSSS1 == art.B14:
          BHealth = BHealth - 30
          print(Red + f"\nBrian's Health Is Now {BHealth}HP")
          time.sleep(1)
          clear()

          if BHealth <= 0:
            break
            clear()
            print(art.win1)
          if PHealth <= 0:
            break
            clear()
            print(art.dead)
            
          bossfight(PHealth, BHealth)
        elif BOSSS1 == art.B15:
          PHealth = PHealth - 15
          print(Red + f"\nYour Health Is Now {PHealth}HP")
          time.sleep(1)
          clear()

          if BHealth <= 0:
            break
            clear()
            print(art.win1)
          if PHealth <= 0:
            break
            clear()
            print(art.dead)
            
          bossfight(PHealth, BHealth)
        elif BOSSS1 == art.B16:
            BHealth = BHealth - 20
            print(Red + f"\nBrian's Health Is Now {BHealth}HP")
            time.sleep(1)
            clear()

            if BHealth <= 0:
              break                
              clear()
              print(art.win1)
            if PHealth <= 0:
              break
              clear()
              print(art.dead)
              
            bossfight(PHealth, BHealth)

    elif BOSS1 == "DEF":
      for i in range(1):
        BOSSS1 = random.choice(Defend)
        print(Red + "\n\n" + BOSSS1)
        if BOSSS1 == art.B21:
          PHealth = PHealth - 2
          print(Red + f"\nYour Health Is Now {PHealth}HP")
          time.sleep(0.5)
          bossfight(PHealth, BHealth)
        elif BOSSS1 == art.B22:
          BHealth = BHealth - 5
          print(Red + f"\nBrian's Health Is Now {BHealth}HP")
          clear()
          time.sleep(0.5)
          bossfight(PHealth, BHealth)
        elif BOSSS1 == art.B23:
          PHealth = PHealth - 10
          print(Red + f"\nYour Health Is Now {PHealth}HP")
          time.sleep(0.5)
          clear()
          bossfight(PHealth, BHealth)
        elif BOSSS1 == art.B24:
          BHealth = BHealth - 30
          PHealth = BHealth - 30
          print(Red + f"\nBrian's Health Is Now {BHealth}HP")
          print(Red + f"\nYour Health Is Now {PHealth}HP")
          time.sleep(0.5)
          clear()
          bossfight(PHealth, BHealth)

        elif BOSSS1 == art.B25:
          PHealth = PHealth - 5
          print(Red + f"\nYour Health Is Now {PHealth}HP")
          time.sleep(0.5)
          clear()
          bossfight(PHealth, BHealth)
        elif BOSSS1 == art.B26:
          BHealth = BHealth - 20
          PHealth = PHealth - 10
          print(Red + f"\nBrian's Health Is Now {BHealth}HP")
          print(Red + f"\nYour Health Is Now {PHealth}HP")
          time.sleep(0.5)
          clear()
          bossfight(PHealth, BHealth)
        if BHealth <= 0:
          break
          clear()
          print(art.win1)
        if PHealth <= 0:
          break
          clear()
          print(art.dead)
          bossfight(100, 100)

    elif BOSS1 == "3" and not PHealth == 50:
      BOSSS1 = random.choice(Heal)
      print(green + "\n\n" + BOSSS1)

      if BOSSS1 == art.B31 and not PHealth == 50:
        PHealth = PHealth + 2
        print(green + f"\nYour Health Is Now {PHealth}HP")
        time.sleep(0.5)
        clear()
        bossfight(PHealth, BHealth)
      elif BOSSS1 == art.B32 and not PHealth == 50:
        BHealth = BHealth + 5
        print(green + f"\nBrian's Health Is Now {BHealth}HP")
        time.sleep(0.5)
        clear()
        bossfight(PHealth, BHealth)
      elif BOSSS1 == art.B33 and not PHealth == 50:
        PHealth = PHealth + 10.,
        print(green + f"\nYour Health Is Now {PHealth}HP")
        time.sleep(0.5)
        clear()
        bossfight(PHealth, BHealth)
      else:
        print(Red + "You Are Max Health!")
        clear()
        bossfight()
    else:
      print(Red + "\n\nInvalid Option Try Again!")
      print(art.inv)
      time.sleep(1)
      clear()
      bossfight(100, 100)
    
    if BHealth <= 0:
      clear()
      print(art.win1)
    if PHealth <= 0:
      clear()
      print(art.dead)
      bossfight(100, 100)
    
  

  bossfight(100, 100)


chapter1()


def chapter2():
  print(blue + ("Cristian had made Mr Hughes tired "))
