#Morpion
import random
import os
import time

    #Tableau
tab = ["",
       " "," "," ",
       " "," "," ",
       " "," "," ",]

    #Méthode
def jeu():
    print (tab[1] , "|" , tab[2], "|" , tab[3])
    print ("----------")
    print (tab[4] , "|" , tab[5], "|" , tab[6])
    print ("----------")
    print(tab[7] , "|" , tab[8] , "|" , tab[9])

def resultat(tab, joueur):
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
    for i in range (1,10):
        if tab[i] == " ":
            tab[i] = joueur
            if resultat(tab,joueur):
                return i
                break
                tab[i] = "x"
            
            elif resultat(tab , joueur):
                tab[i] = "o"
                return i
            else:
                tab[i] = " "
                
        
             
    
    if tab[5] == " ":
        return 5
    while True:
        nbHasard =  random.randint(1,9) #Un numéro au hasard
        return nbHasard
        break
    return 5

    
    
    
   

    #Main
while True:
    jeu()
    nb = int(input("X: "))
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
        
       
    if resultat(tab,"x"):
        jeu()
        print ("Gagné")
        break
        
        
    if resultat(tab,"o"):
        print ("Perdu")
        break
        
    
    if nul(tab):
        print("Nul")
        break

  
           
            
           
   
