#######################################################################################################
""""""""""""""""""""""""""""""""" PUISSANCE 4 """""""""""""""""""""""""""""""""""""""
from tkinter import *; import time; import random

# créer la fenêtre et l'appelle Puissance 4
fenetre = Tk(); fenetre.title("Connect 4")

# met les images du fichier que l'on va utiliser dans des variables
# si il y a une erreur, vérifier que vous avez bien ouvert le fichier Puissance4, et pas juste le document .py
RondG, RondR, RondJ, RondV = PhotoImage(file ='button/grey.png'), PhotoImage(file ='game_board/red/red.png'), PhotoImage(file ='game_board/yellow/yellow.png'), PhotoImage(file ='game_board/blue/nothing.png')
WhiteW, WhiteI, WhiteE, WhiteN, WhiteT = PhotoImage(file ='game_board/blue/blue_w.png'), PhotoImage(file ='game_board/blue/blue_i.png'), PhotoImage(file ='game_board/blue/blue_e.png'), PhotoImage(file ='game_board/blue/blue_n.png'), PhotoImage(file ='game_board/blue/blue_t.png')
RedR, RedE, RedD = PhotoImage(file ='game_board/red/red_r.png'), PhotoImage(file ='game_board/red/red_e.png'), PhotoImage(file ='game_board/red/red_d.png')
YellowY, YellowE, YellowL, YellowO, YellowW = PhotoImage(file ='game_board/yellow/yellow_y.png'), PhotoImage(file ='game_board/yellow/yellow_e.png'), PhotoImage(file ='game_board/yellow/yellow_l.png'), PhotoImage(file ='game_board/yellow/yellow_o.png'), PhotoImage(file ='game_board/yellow/yellow_w.png')
Replay, Replay2, Exit, RedTurn, YellowTurn, Load, Save, Undo = PhotoImage(file ='button/replay/replay.png'), PhotoImage(file='button/replay/replay2.png'), PhotoImage(file ='button/exit.png'), PhotoImage(file ='game_board/red/red_turn.png'), PhotoImage(file ='game_board/yellow/yellow_turn.png'), PhotoImage(file='button/load.png'), PhotoImage(file='button/save.png'), PhotoImage(file='button/undo.png')
ConnectC_bold, ConnectO, ConnectN_italic, ConnectN, ConnectE_bold, ConnectC, ConnectT_bold, Connect4_italic =  PhotoImage(file ='connect4/c-bold.png'), PhotoImage(file ='connect4/o.png'), PhotoImage(file ='connect4/n-italic.png'), PhotoImage(file ='connect4/n.png'), PhotoImage(file ='connect4/e-bold.png'), PhotoImage(file ='connect4/c.png'), PhotoImage(file ='connect4/t-bold.png'), PhotoImage(file ='connect4/4-italic.png')

# créer une liste des images utilisés pour le score
RedScore=[]
for i in range(10): RedScore.append(PhotoImage(file='score/red/score_red'+str(i)+'.png'))

YellowScore=[]
for i in range(10): YellowScore.append(PhotoImage(file='score/yellow/score_yellow'+str(i)+'.png'))

# garde tout les coups
match=[]

# met les scores et le tour à 0
winred, winyellow, y=0, 0, random.randint(0,1)

# p ce remplie au fur et a mesure que des pions sont joués
p=[ [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]]


# affiche le nom du jeu à gauche
c_bold=Label(fenetre,image=ConnectC_bold); c_bold.grid(row=0,column=0)
o=Label(fenetre,image=ConnectO); o.grid(row=1,column=0)
n_italic=Label(fenetre,image=ConnectN_italic); n_italic.grid(row=2,column=0)
n=Label(fenetre,image=ConnectN); n.grid(row=3,column=0)
e_bold=Label(fenetre,image=ConnectE_bold); e_bold.grid(row=4,column=0)
c=Label(fenetre,image=ConnectC);c.grid(row=5,column=0)
t_bold=Label(fenetre,image=ConnectT_bold); t_bold.grid(row=6,column=0)
# créer les 7 boutons de jeu en haut du plateau (7 premiers boutons de la première ligne)
boutons=[]
for colonne in range(7): boutons.append(Button(fenetre,command=lambda n=colonne: tour(n))); boutons[colonne].configure(image=RondG); boutons[colonne].grid(row=0,column=colonne+1)

# créer le bouton qui ferme la fenêtre (première ligne huitième colonne)
boutons.append(Button(fenetre,command=lambda n=7: exit())); boutons[7].configure(image=Exit); boutons[7].grid(row=0,column=9)

# créer le bouton pour recommencer la partie (deuxième ligne huitième colonne)
boutons.append(Button(fenetre,command=lambda n=8: remisea0())); boutons[8].configure(image=Replay); boutons[8].grid(row=1,column=9)

# créer le bouton pour annuler les coups précédent
boutons.append(Button(fenetre,command=lambda n=9: undo())); boutons[9].configure(image=Undo); boutons[9].grid(row=2,column=9)

# créer le bouton pour sauvegarder une partie
boutons.append(Button(fenetre,command=lambda n=10: save())); boutons[10].configure(image=Save); boutons[10].grid(row=4, column=9)

# créer le bouton pour charger la partie sauvegarder
boutons.append(Button(fenetre, command=lambda n=11: load())); boutons[11].configure(image=Load); boutons[11].grid(row=3, column=9)

# créer le plateau de jeu
grille=[]
for ligne in range(len(p)): 
    grille.append([])
    for colonne in range(len(p[ligne])): grille[ligne].append(Label(fenetre,image=RondV)), grille[ligne][colonne].grid(row=ligne+1,column=colonne+1)

# affiche qui doit jouer, commence par le rouge (troisième ligne huitième colonne)
if y==0: turn=Label(fenetre, image=RedTurn); turn.grid(row=2,column=8)
else: turn=Label(fenetre, image=YellowTurn); turn.grid(row=2,column=8)
# affiche nombre de victoire rouge
# quatrième ligne huitième colonne
yellow_score=Label(fenetre,image=YellowScore[0]); yellow_score.grid(row=3,column=8)
# affiche nombre de victoire jaune
# cinquième ligne huitième colonne
red_score=Label(fenetre,image=RedScore[0]); red_score.grid(row=4,column=8)
# pour éviter un décalage d'affichage à la première victoire, on place le bouton
rejouer=Button(fenetre, command=lambda: remisea0()); rejouer.configure(image=Replay2); rejouer.grid(row=2, column=4)
# puis on retire le bouton
grille[1][3]=Label(fenetre,image=RondV); grille[1][3].grid(row=2,column=4)

# fonction du bouton première ligne huitième colonne, pour fermer la denètre
def exit(): fenetre.destroy()

# fonction du bouton deuxième ligne huitième colonne et du bouton qui apparaît à la fin de la partie, recommencer une partie
def remisea0():
    # p est le plateau qui se remplie de 1 pour pion jaune et 2 pour pion rouge (seulement sur les 0), y le tour auquel on est, grille est le plateau de la fenêtre, boutons est les boutons de jeu pour fermer la fenêtre et pour rejouer
    global p, y, grille, boutons, match
    # désactive les boutons de jeu
    for colonne in range(7): boutons[colonne].configure(command=lambda n=colonne: None)
    # remise à zéro du plateau
    p=[ [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]
    match=[]
    # enlève le bouton apparu sur le plateau à la fin de la partie
    # bouton apparu pour la victoire
    grille[1][3]=Label(fenetre,image=RondV); grille[1][3].grid(row=2,column=4)
    # bouton apparu pour l'égalité
    grille[0][3]=Label(fenetre,image=RondV); grille[0][3].grid(row=1,column=4)
    # remise à 0 des tours de jeu
    y=random.randint(0,1)
    # remet l'image du premier joueur a jouer
    turn.config(image=RedTurn) if y==0 else turn.config(image=YellowTurn)
    # remet le plateau à blanc
    for ligne in range(len(p)):
        for colonne in range(len(p[ligne])): grille[ligne][colonne].config(image=RondV)
    # réactive les boutons de jeu
    for c in range(7): boutons[c].configure(command=lambda n=c: tour(n))
    boutons[9].configure(command=lambda n=9: undo())
    boutons[10].configure(command=lambda n=10: save())
# définie les tours des joueurs
def tour(c):
    # p est le plateau, y pour savoir qui joue si paire jaune joue si impaire rouge joue
    global p, y
    # ajoute 1 au tour car c'est le prochain tour
    y+=1
    # si le nombre de tour est paire donc si y est paire le joueur jaune joue, sinon si le tour n'est pas paire donc y est impaire le joueur rouge joue
    JJ1(c) if y%2==0 else JR2(c)
# annule les coups précédent
def undo():
    global match, y, p
    if len(match)>0:
        i, j, n, b = match[-1]  
        # change l'image du joueur qui doit jouer
        turn.config(image=RedTurn) if p[i][j]==2 else turn.config(image=YellowTurn)
        # supprime le pion, remet un 0 dans la liste plateau, supprime le dernier element de la liste qui suit les coups joué
        grille[i][j].config(image=RondV); p[i][j]=0; del match[-1]; y-=1
    else: pass
# sauvegarder une partie
def save():
    s=open("save.txt", "w")
    for i in range(len(match)):
        for j in range(len(match[i])):  
            s.write(str(match[i][j]) + " ")
        s.write("\n")
# charge la partie sauvegarder
def load():
    global match, y
    remisea0()
    i=0
    s=open("save.txt", "r")
    for ligne in s:
        match.append([])
        liste=ligne.split()
        for j in range(len(liste)):
            match[i].append(int(liste[j]))
        i+=1
    for i in range(len(match)):
        a, b, c, d = match[i]
        p[a][b]=c
        grille[a][b].config(image=RondJ) if c==1 else grille[a][b].config(image=RondR)
    y=d
    turn.config(image=YellowTurn) if y%2 else turn.config(image=RedTurn)
    
# quand une victoire est détecté affiche le gagnant
def victoire(n):
    # boutons est les boutons de la fenêtre, grille est le plateau afficher sur la fenêtre
    global boutons, grille, winyellow, winred, yellow_score, red_score
    # désactive le bouton rejouer à la deucième ligne huitième colonne pour éviter les bug pendant l'animation de victoire
    boutons[8].configure(command=lambda n=8: None)
    # désactive les boutons de jeu
    for colonne in range(7): boutons[colonne].configure(command=lambda n=colonne: None)
    # désactive le bouton undo
    boutons[9].configure(command=lambda n=9: None)
    # désactive le bouton save
    boutons[10].configure(command=lambda n=10: None)
    # désactive le bouton load
    boutons[11].configure(command=lambda n=11: None)
    # animation gagnant jaune
    if n==1:
        # ajoute 1 au score jaune
        winyellow+=1
        # affichage de chaque lettre avec 0.2 seconde de decalage entre les lettres
        grille[0][0].config(image=YellowY)
        fenetre.update()# update la fenêtre pour que l'attente soit pris en compte
        time.sleep(0.2)# attend 0.2 seconde
        # change le l'image de score de la fenêtre, if évite les erreurs out of range
        if winyellow<10: yellow_score.config(image=YellowScore[winyellow])
        grille[0][1].config(image=YellowE), fenetre.update(), time.sleep(0.2)
        grille[0][2].config(image=YellowL), fenetre.update(), time.sleep(0.2)
        grille[0][3].config(image=YellowL), fenetre.update(), time.sleep(0.2)
        grille[0][4].config(image=YellowO), fenetre.update(), time.sleep(0.2)
        grille[0][5].config(image=YellowW), fenetre.update(), time.sleep(0.2)
        grille[1][0].config(image=WhiteW), fenetre.update(), time.sleep(0.2)
        grille[1][1].config(image=WhiteI), fenetre.update(), time.sleep(0.2)
        grille[1][2].config(image=WhiteN), fenetre.update(), time.sleep(0.2)
        # affichage du bouton pour rejouer
        rejouer=Button(fenetre, command=lambda: remisea0()); rejouer.configure(image=Replay2); rejouer.grid(row=2, column=4)
        # réactive le bouton rejouer de la deuxième ligne huitième colonne
        boutons[8].configure(command=lambda n=8: remisea0())
        # réactive le bouton load
        boutons[11].configure(command=lambda n=11: load())
        # joueur gagnant dans la console
        print("Victoire Jaune.")
    # animation gagnant rouge
    if n==2:
        # ajoute 1 au score rouge
        winred+=1
        # affichage de chaque lettre avec 0.2 seconde de decalage entre les lettres
        grille[0][0].config(image=RedR)
        fenetre.update(), time.sleep(0.2)
        # change l'image du score rouge de la fenêtre, if évite les erreurs out of range
        if winred<10: red_score.config(image=RedScore[winred])
        grille[0][1].config(image=RedE), fenetre.update(), time.sleep(0.2)
        grille[0][2].config(image=RedD), fenetre.update(), time.sleep(0.2)
        grille[1][0].config(image=WhiteW), fenetre.update(), time.sleep(0.2)
        grille[1][1].config(image=WhiteI), fenetre.update(), time.sleep(0.2)
        grille[1][2].config(image=WhiteN), fenetre.update(), time.sleep(0.2)
        # affichage du bouton rejouer
        rejouer=Button(fenetre, command=lambda: remisea0()); rejouer.configure(image=Replay2); rejouer.grid(row=2, column=4)
        # réactive le bouton rejouer de la deuxième ligne huitième colonne
        boutons[8].configure(command=lambda n=8: remisea0())
        # réactive le bouton load
        boutons[11].configure(command=lambda n=11: load())
        # joueur gagnant dans la console
        print("Victoire Rouge.")

    # en cas de plateau plein sans gagnant
    if n==3:
        # affichage de chaque lettre avec 0.2 seconde de decalage entre les lettres
        fenetre.update(), time.sleep(0.2)
        grille[0][0].config(image=WhiteT), fenetre.update(), time.sleep(0.2)
        grille[0][1].config(image=WhiteI), fenetre.update(), time.sleep(0.2)
        grille[0][2].config(image=WhiteE), fenetre.update(), time.sleep(0.2)
        # affichage du bouton rejouer
        rejouer=Button(fenetre, command=lambda: remisea0()); rejouer.configure(image=Replay2); rejouer.grid(row=1, column=4)
        # réactive le bouton rejouer de la deuxième ligne huitième colonne
        boutons[8].configure(command=lambda n=8: remisea0())
        # affiche égalité dans la console
        print("Égalité.")
# ce declenche quand y est paire
# tour du joueur jaune
def JJ1(c):
    # p est le plateau de jeu et y est pour savoir qui joue
    global p, y, match
    # i=5 car 5 est la dernière ligne du plateau (dans une liste la première variable est 0 donc 0,1,2,3,4,5 fait 6 lignes)
    i=5
    # regarde si un pion est déja dans la colonne si oui regarde sur quel ligne il peut mettre le pion
    while p[i][c]!=0 and i>=0: i-=1 # remonte sur la ligne avant si il y a deja un pion sur la colonne selectionné      
    # place le pion jaune sur le plateau p en remplaçant le 0 correspondant en 1 et remplace l'image de la case correspondante dans grille
    if i>=0:
        p[i][c]=1
        grille[i][c].config(image=RondJ)
        match.append([i, c, 1, y])
        turn.config(image=RedTurn)
############################################################################
# test toute les possibilités de victoire, si une victoire est détectée renvoie 1 à la fonction victoire qui affiche la victoire jaune
        # detection de victoire horizontale
        if c-1>=0 and p[i][c-1]==1 and c-2>=0 and p[i][c-2]==1 and c-3>=0 and p[i][c-3]==1: return victoire(1)
        if c-1>=0 and p[i][c-1]==1 and c-2>=0 and p[i][c-2]==1 and c+1<=6 and p[i][c+1]==1: return victoire(1)
        if c-1>=0 and p[i][c-1]==1 and c+1<=6 and p[i][c+1]==1 and c+2<=6 and p[i][c+2]==1: return victoire(1)
        if c+1<=6 and p[i][c+1]==1 and c+2<=6 and p[i][c+2]==1 and c+3<=6 and p[i][c+3]==1: return victoire(1)
        if c+1<=6 and p[i][c+1]==1 and c+2<=6 and p[i][c+2]==1 and c-1>=0 and p[i][c-1]==1: return victoire(1)
###############################################################################
        # detection de victoire verticale
        if i+1<=5 and p[i+1][c]==1 and i+2<=5 and p[i+2][c]==1 and i+3<=5 and p[i+3][c]==1: return victoire(1)
##################################################################################
        # detection de victoire diagonale gauche de haut en bas
        if i+1<=5 and c+1<=6 and p[i+1][c+1]==1 and i+2<=5 and c+2<=6 and p[i+2][c+2]==1 and i+3<=5 and c+3<=6 and p[i+3][c+3]==1: return victoire(1)
        if i+1<=5 and c+1<=6 and p[i+1][c+1]==1 and i+2<=5 and c+2<=6 and p[i+2][c+2]==1 and i-1>=0 and c-1>=0 and p[i-1][c-1]==1: return victoire(1)
        if i+1<=5 and c+1<=6 and p[i+1][c+1]==1 and i-1>=0 and c-1>=0 and p[i-1][c-1]==1 and i-2>=0 and c-2>=0 and p[i-2][c-2]==1: return victoire(1)
        if i-1>=0 and c-1>=0 and p[i-1][c-1]==1 and i-2>=0 and c-2>=0 and p[i-2][c-2]==1 and i-3>=0 and c-3>=0 and p[i-3][c-3]==1: return victoire(1)
        if i-1>=0 and c-1>=0 and p[i-1][c-1]==1 and i-2>=0 and c-2>=0 and p[i-2][c-2]==1 and i+1<=5 and c-1>=0 and p[i+1][c+1]==1: return victoire(1)
        if i-1>=0 and c-1>=0 and p[i-1][c-1]==1 and i+1<=5 and c+1<=6 and p[i+1][c+1]==1 and i+2<=5 and c+2<=6 and p[i+2][c+2]==1: return victoire(1)
##################################################################################
        # detection de victoire diagonale droite de haut en bas
        if i-1>=0 and c+1<=6 and p[i-1][c+1]==1 and i-2>=0 and c+2<=6 and p[i-2][c+2]==1 and i-3>=0 and c+3<=6 and p[i-3][c+3]==1: return victoire(1)
        if i-1>=0 and c+1<=6 and p[i-1][c+1]==1 and i-2>=0 and c+2<=6 and p[i-2][c+2]==1 and i+1<=5 and c-1>=0 and p[i+1][c-1]==1: return victoire(1)
        if i-1>=0 and c+1<=6 and p[i-1][c+1]==1 and i+1<=5 and c-1>=0 and p[i+1][c-1]==1 and i+2<=5 and c-2>=0 and p[i+2][c-2]==1: return victoire(1)
        if i+1<=5 and c-1>=0 and p[i+1][c-1]==1 and i+2<=5 and c-2>=0 and p[i+2][c-2]==1 and i+3<=5 and c-3>=0 and p[i+3][c-3]==1: return victoire(1)
        if i+1<=5 and c-1>=0 and p[i+1][c-1]==1 and i+2<=5 and c-2>=0 and p[i+2][c-2]==1 and i-1>=0 and c+1<=6 and p[i-1][c+1]==1: return victoire(1)
        if i+1<=5 and c-1>=0 and p[i+1][c-1]==1 and i-1>=0 and c+1<=6 and p[i-1][c+1]==1 and i-2>=0 and c+2<=6 and p[i-2][c+2]==1: return victoire(1)
##################################################################################
        # détecte si le plateau est remplie de pion si oui renvoie 3 à la fonction victoire qui fait une égalité
        if 0 not in p[0]: return victoire(3)
    else: y=1 # si la colonne est pleine y est remis à 1 pour que jaune puisse rejouer car il n'a pas placé de pion
# ce declenche quand y est impaire
# tour du joueur rouge
def JR2(c):
    # p est le plateau de jeu et y est pour savoir qui joue
    global p, y, match
    # i=5 car 5 est la dernière ligne du plateau (dans une liste la première variable est 0 donc 0,1,2,3,4,5 fait 6 lignes)
    i=5
    # regarde si un pion est déja dans la colonne si oui regarde sur quel ligne il peut mettre le pion, sinon remonte sur la ligne avant si il y a deja un pion sur la colonne selectionné
    while p[i][c]!=0 and i>=0: i-=1
    # place le pion rouge sur le plateau p en remplaçant le 0 correspondant en 2 et remplace l'image de la case correspondante dans grille
    if i>=0:
        p[i][c]=2
        grille[i][c].config(image=RondR)
        match.append([i, c, 2, y])
        turn.config(image=YellowTurn)
############################################################################
# test toute les possibilités de victoire, si une victoire est détectée renvoie 2 à la fonction victoire qui affiche la victoire rouge 
        # detection de victoire horizontale
        if c-1>=0 and p[i][c-1]==2 and c-2>=0 and p[i][c-2]==2 and c-3>=0 and p[i][c-3]==2: return victoire(2)
        if c-1>=0 and p[i][c-1]==2 and c-2>=0 and p[i][c-2]==2 and c+1<=6 and p[i][c+1]==2: return victoire(2)
        if c-1>=0 and p[i][c-1]==2 and c+1<=6 and p[i][c+1]==2 and c+2<=6 and p[i][c+2]==2: return victoire(2)
        if c+1<=6 and p[i][c+1]==2 and c+2<=6 and p[i][c+2]==2 and c+3<=6 and p[i][c+3]==2: return victoire(2)
        if c+1<=6 and p[i][c+1]==2 and c+2<=6 and p[i][c+2]==2 and c-1>=0 and p[i][c-1]==2: return victoire(2)
################################################################################
        # detection de victoire verticale
        if i+1<=5 and p[i+1][c]==2 and i+2<=5 and p[i+2][c]==2 and i+3<=5 and p[i+3][c]==2: return victoire(2)
##################################################################################
        # detection de victoire diagonale gauche de haut en bas
        if i+1<=5 and c+1<=6 and p[i+1][c+1]==2 and i+2<=5 and c+2<=6 and p[i+2][c+2]==2 and i+3<=5 and c+3<=6 and p[i+3][c+3]==2: return victoire(2)
        if i+1<=5 and c+1<=6 and p[i+1][c+1]==2 and i+2<=5 and c+2<=6 and p[i+2][c+2]==2 and i-1>=0 and c-1>=0 and p[i-1][c-1]==2: return victoire(2)
        if i+1<=5 and c+1<=6 and p[i+1][c+1]==2 and i-1>=0 and c-1>=0 and p[i-1][c-1]==2 and i-2>=0 and c-2>=0 and p[i-2][c-2]==2: return victoire(2)
        if i-1>=0 and c-1>=0 and p[i-1][c-1]==2 and i-2>=0 and c-2>=0 and p[i-2][c-2]==2 and i-3>=0 and c-3>=0 and p[i-3][c-3]==2: return victoire(2)
        if i-1>=0 and c-1>=0 and p[i-1][c-1]==2 and i-2>=0 and c-2>=0 and p[i-2][c-2]==2 and i+1<=5 and c-1>=0 and p[i+1][c+1]==2: return victoire(2)
        if i-1>=0 and c-1>=0 and p[i-1][c-1]==2 and i+1<=5 and c+1<=6 and p[i+1][c+1]==2 and i+2<=5 and c+2<=6 and p[i+2][c+2]==2: return victoire(2)
##################################################################################
        # detection de victoire diagonale droite de haut en bas
        if i-1>=0 and c+1<=6 and p[i-1][c+1]==2 and i-2>=0 and c+2<=6 and p[i-2][c+2]==2 and i-3>=0 and c+3<=6 and p[i-3][c+3]==2: return victoire(2)
        if i-1>=0 and c+1<=6 and p[i-1][c+1]==2 and i-2>=0 and c+2<=6 and p[i-2][c+2]==2 and i+1<=5 and c-1>=0 and p[i+1][c-1]==2: return victoire(2)
        if i-1>=0 and c+1<=6 and p[i-1][c+1]==2 and i+1<=5 and c-1>=0 and p[i+1][c-1]==2 and i+2<=5 and c-2>=0 and p[i+2][c-2]==2: return victoire(2)
        if i+1<=5 and c-1>=0 and p[i+1][c-1]==2 and i+2<=5 and c-2>=0 and p[i+2][c-2]==2 and i+3<=5 and c-3>=0 and p[i+3][c-3]==2: return victoire(2)
        if i+1<=5 and c-1>=0 and p[i+1][c-1]==2 and i+2<=5 and c-2>=0 and p[i+2][c-2]==2 and i-1>=0 and c+1<=6 and p[i-1][c+1]==2: return victoire(2)
        if i+1<=5 and c-1>=0 and p[i+1][c-1]==2 and i-1>=0 and c+1<=6 and p[i-1][c+1]==2 and i-2>=0 and c+2<=6 and p[i-2][c+2]==2: return victoire(2)
##################################################################################
        # détecte si le plateau est remplie de pion si oui renvoie 3 à la fonction victoire qui fait une égalité
        if 0 not in p[0]: return victoire(3)
    else: y=0 # si la colonne est pleine y est remis à 0 pour que rouge puisse rejouer car il n'a pas placé de pion
# ouvre la fenêtre
fenetre.mainloop()
#######################################################################################################
