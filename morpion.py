#Morpion
import random
import os
import time

    #Tableau


tab = ["",
       " "," "," ",
       " "," "," ",
       " "," "," "]


    #Méthode
def titre():
    print ("""
                                                                               
                                        
 __  __  ___  ____  ____ ___ ___  _   _ 
|  \/  |/ _ \|  _ \|  _ |_ _/ _ \| \ | |
| |\/| | | | | |_) | |_) | | | | |  \| |
| |  | | |_| |  _ <|  __/| | |_| | |\  |
|_|  |_|\___/|_| \_|_|  |___\___/|_| \_|       
       _           _                   
      |_) _  __   | \|_  o __  _  _ |_ 
      |  (_| |    |_/| | | | |(/__> | |
                                                                                                                 
                                                                             
                                                                                                        
""")
def jeu():
    titre()
    print (tab[1] , "|" , tab[2], "|" , tab[3])
    print ("----------")
    print (tab[4] , "|" , tab[5], "|" , tab[6])
    print ("----------")
    print(tab[7] , "|" , tab[8] , "|" , tab[9])

def victoire(tab, joueur):
    if tab[1] == joueur and tab[2] == joueur and tab[3] == joueur or \
       tab[4] == joueur and tab[5] == joueur and tab[6] == joueur or \
       tab[7] == joueur and tab[8] == joueur and tab[9] == joueur or \
       tab[1] == joueur and tab[4] == joueur and tab[7] == joueur or \
       tab[2] == joueur and tab[5] == joueur and tab[8] == joueur or \
       tab[3] == joueur and tab[6] == joueur and tab[9] == joueur or \
       tab[1] == joueur and tab[5] == joueur and tab[9] == joueur or \
       tab[3] == joueur and tab[5] == joueur and tab[7] == joueur:
        return True
    else:
        return False

def nul(tab):
    if " " in tab:
        return False
    else:
        return True


    #IA 
def IA(tab, joueur):
    if tab[5] == " " :
        return 5            
    for i in range (1,10):
        if tab[i] == " ":
            tab[i] = joueur
            if victoire(tab,joueur):
                
                print(" verification : gagnant")
                time.sleep(1)
                return i
                break
            else:
                  tab[i] = " "
        if tab[i] == " ":
            tab[i] = "x"
            if victoire (tab,"x"):
                tab[i] = "o"
                print ("verification : perdant")
                time.sleep(1)
    
                return i
                break
            else:
                tab[i] = " "
               
    while True:

        nbHasard = random.randint(1,9)
        if tab[nbHasard] == " ":

            print ("hasard ", nbHasard)
            time.sleep(1)
            return nbHasard
        if tab[i] != " ":
            return 0
                  
    
   
""" 
  #reset
def reset():
    tab = [""," "," "," "," "," "," "," "," "," "]
    
    return tab
"""             
        
    
    #Main
while True:

    os.system("clear")
    jeu()
   
    
    nb = int(input("X: "))
    if nb < 10:
        if tab[nb] == " ":
            tab[nb] = "x"
            while True:
            #nb2 =int(input("0: "))
                nb2 = IA(tab,"o")
                if tab[nb2] == " ":
                    tab[nb2] = "o"
                break
        
                if nul(tab):
                    jeu()
                    break
        else:
            print ("C'est déjà pris")
            time.sleep(1)
    else:
        print("Veuillez rentrer un nombre 1 et 9")
        time.sleep(1)
        
       
    if victoire(tab,"x"):
        os.system("clear")
        jeu()
        print ("Victoire")
        rejouer = str(input("une nouvelle partie ? (O/N) : ").upper())
        if rejouer == "O":
             tab = [""," "," "," "," "," "," "," "," "," "]
             continue  
        else:
            break
        
        
    if victoire(tab,"o"):
        os.system("clear")
        jeu()
        print ("Défaite")
        rejouer = str(input("une nouvelle partie ? (O/N) : ").upper())
        if rejouer == "O":
            tab = [""," "," "," "," "," "," "," "," "," "]
            #reset()
            continue 
        else:
            break
        
    
    if nul(tab):
        os.system("clear")
        jeu()
        print("Nul")
        rejouer = str(input("une nouvelle partie ? (O/N) : ").upper())
        if rejouer == "O":
             tab = [""," "," "," "," "," "," "," "," "," "]
             continue
        else:
            break

  
           
    
