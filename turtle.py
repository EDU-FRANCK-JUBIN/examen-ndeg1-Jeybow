# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:30:26 2019

@author: Jérémie
"""

import turtle as t
import random

def course(tortue):
    if tortue.position()[0] < position_arrive:
        tortue.forward(random.randint(0, 5))
        if tortue.position()[0] >= position_arrive:
            return True
        else:
            return False
        
def listProno(prono):
    return prono.split(',')

# Initialisation du jeu
ts = t.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")
ts.setup(width=1400, height=800, startx=0, starty=0)


# Déclarez les 5 tortues et positionnez-les sur leurs hexagones respectifs
position_arrive = 1380/2

ma_tortue = t.Turtle()
ma_tortue.shape("turtle")
ma_tortue.color('White')
ma_tortue.up()
ma_tortue.goto(-655, 320)
ma_tortue.down()

michelangelo = t.Turtle()
michelangelo.color('Orange')
michelangelo.shape("turtle")
michelangelo.up()
michelangelo.goto(-655, 160)
michelangelo.down()

leonardo = t.Turtle()
leonardo.color('Blue')
leonardo.shape("turtle")
leonardo.up()
leonardo.goto(-655, 0)
leonardo.down()

raphael = t.Turtle()
raphael.color('Red')
raphael.shape("turtle")
raphael.up()
raphael.goto(-655, -150)
raphael.down()

splinter = t.Turtle()
splinter.color('Grey')
splinter.shape("turtle")
splinter.up()
splinter.goto(-655, -300)
splinter.down()

# Demander de saisir dans la console les prédictions des joeurus 1 et 2 dans le format 1,2,3
joueur_1 = input("Joueur 1, saisissez vos pronostics des 3 premières tortues : ")
joueur_2 = input("Joueur 2, saisissez vos pronostics des 3 premières tortues : ")
Pronostic_Joueur_1 = listProno(joueur_1)
Pronostic_Joueur_2 = listProno(joueur_2)

# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui représente le nombre de pixels du déplacement vers la droite
classement = ["Empty", "Empty", "Empty", "Empty", "Empty"]
tmp_start = 0
numero_nom_tortue = {
    1: 'ma_tortue',
    2: 'michelangelo',
    3: 'leonardo',
    4: 'raphael',
    5: 'splinter'
}

while(ma_tortue.position()[0] < position_arrive or
      michelangelo.position()[0] < position_arrive or
      leonardo.position()[0] < position_arrive or
      raphael.position()[0] < position_arrive or
      splinter.position()[0] < position_arrive):

    if course(ma_tortue):
        classement[tmp_start] = 1
        tmp_start += 1
    if course(michelangelo):
        classement[tmp_start] = 2
        tmp_start += 1
    if course(leonardo):
        classement[tmp_start] = 3
        tmp_start += 1
    if course(raphael):
        classement[tmp_start] = 4
        tmp_start += 1
    if course(splinter):
        classement[tmp_start] = 5
        tmp_start += 1

print(classement)

# Comparer les résultats de la course avec les pronostics des joueurs
if classement[0:4] == joueur_1:
    print("le pronostic du joueur 1 est bon")

if classement[0:4] == joueur_2:
    print("le pronostic du joueur 2 est bon")

# et afficher le résultat de la course
print("Resultat de la course : 1. {}({}) // 2. {}({}) // 3. {}({}) // 4. {}({}) // 5. {}({})".format(numero_nom_tortue[classement[0]],classement[0],numero_nom_tortue[classement[1]],classement[1],
numero_nom_tortue[classement[2]],classement[2],numero_nom_tortue[classement[3]],classement[3],numero_nom_tortue[classement[4]],classement[4]))

# et le joueur gagnant avec la tortue arbitre et l'instruction turtle.Write à la position 0,0
arbitre = t.Turtle()
arbitre.goto(0, 0)
arbitre.color("Black")
arbitre.write("Le joueur {} à savoir {} a gagné".format(classement[0],numero_nom_tortue[classement[0]]), move=True)

t.mainloop()
