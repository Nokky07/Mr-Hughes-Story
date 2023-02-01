#Developed by: Nokky07

#Mr Hughes Story

#Project Started 16/09/22



#Imports
import time
import os
import random
import art

#Clear Function
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


#Menu Screen
def menu():

  time.sleep(0.1)
  print(Red + art.Title)
  time.sleep(0.1)
  print(Red +
        "｜         ｜  ｜         ｜  ｜         ｜  ｜         ｜  ｜         ｜  ")
  time.sleep(0.1)

  #Input

  print(Blue + "\n\n\nWelcome Please Choose An Option\n ")
  time.sleep(0.1)

  print(Green + "----------------------------\n")
  time.sleep(0.1)

  choose = input(
    Green +
    "(1) - Start\n\n---------------------------- \n\n(2) - Creator\n\n---------------------------- \n\n(3) - Difficulty\n\n\n Select An Option: "
  )

  #Loading Screen

  if choose == "1":
    clear()
    print(art.L3)
    time.sleep(1)
    clear()

    #Creators Info
  elif choose == "3":
    clear()
    print(blue + art.Diff)
    time.sleep(0.1)
    print(blue + art.N64)
    time.sleep(0.1)
    diff = input(
      Blue +
      "(1) - Easy\n\n---------------------------- \n\n(2) - Normal\n\n---------------------------- \n\n(3) - Hard\n\n---------------------------- \n\n(4) - Menu\n\n\n Select An Option: "
    )

    if diff == "1":
      BHealth = 100
      clear()
      print(Green + art.DE)
      time.sleep(1.5)
      clear()
      menu()
    elif diff == "2":
      BHealth = 150
      clear()
      print(Orange + art.DN)
      time.sleep(1.5)
      clear()
      menu()
    elif diff == "3":
      BHealth = 200
      clear()
      print(Red + art.DH)
      time.sleep(1.5)
      clear()
      menu()
    elif diff == "4":
      clear()
      menu()

  elif choose == "2":
    clear()
    print(art.Nokky07)
    time.sleep(0.1)
    print(
      "-----------------------------------------------------------------\n")
    time.sleep(0.1)
    print(art.Computer)
    time.sleep(0.1)
    print(
      "-----------------------------------------------------------------\n")
    time.sleep(0.1)

    print(Red +
          "Youtube: https://www.youtube.com/channel/UCzzGpscAqcUi10T4u-sWyyg")
    time.sleep(0.1)
    print(art.YT)
    time.sleep(0.1)
    print(
      "-----------------------------------------------------------------\n")
    time.sleep(0.1)
    print(Blue + "Please Choose An Option\n")
    time.sleep(0.1)
    print(Green + "----------------------------\n")
    time.sleep(0.1)
    user = input(
      "(1) - Menu\n\n---------------------------- \n\n\n Select An Option: ")
    if user == "1":
      clear()
      menu()
  else:

    print(Red + "\n\nInvalid Option Try Again!")
    print(art.inv)
    time.sleep(1)
    clear()
    menu()


menu()