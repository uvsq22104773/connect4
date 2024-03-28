#######################################################################################################
"""""""""""""""""""""""""""""""""PUISSANCE 4"""""""""""""""""""""""""""""""""""""""
from tkinter import *; import time

# créer la fenêtre et l'appelle Puissance 4
fenetre = Tk()
fenetre.title("Puissance 4")

# met les images du fichier que l'on va utiliser dans des variables
# si erreur vérifier que soit le fichier Puissance4 ne soit dans aucun fichier sinon mettre tout les fichiers avant le png dans lequel il est; exemple: dans la version actuel le fichier Puissance4 est dans un fichier appelé python sur le bureau
RondG, RondR, RondJ, RondV = PhotoImage(file ='Puissance4/button/grey.png'), PhotoImage(file ='Puissance4/game_board/red/red.png'), PhotoImage(file ='Puissance4/game_board/yellow/yellow.png'), PhotoImage(file ='Puissance4/game_board/blue/nothing.png')
WhiteW, WhiteI, WhiteE, WhiteN, WhiteT = PhotoImage(file ='Puissance4/game_board/blue/blue_w.png'), PhotoImage(file ='Puissance4/game_board/blue/blue_i.png'), PhotoImage(file ='Puissance4/game_board/blue/blue_e.png'), PhotoImage(file ='Puissance4/game_board/blue/blue_n.png'), PhotoImage(file ='Puissance4/game_board/blue/blue_t.png')
RedR, RedE, RedD = PhotoImage(file ='Puissance4/game_board/red/red_r.png'), PhotoImage(file ='Puissance4/game_board/red/red_e.png'), PhotoImage(file ='Puissance4/game_board/red/red_d.png')
YellowY, YellowE, YellowL, YellowO, YellowW = PhotoImage(file ='Puissance4/game_board/yellow/yellow_y.png'), PhotoImage(file ='Puissance4/game_board/yellow/yellow_e.png'), PhotoImage(file ='Puissance4/game_board/yellow/yellow_l.png'), PhotoImage(file ='Puissance4/game_board/yellow/yellow_o.png'), PhotoImage(file ='Puissance4/game_board/yellow/yellow_w.png')
Replay, Replay2, Exit, RedTurn, YellowTurn = PhotoImage(file ='Puissance4/button/replay/replay.png'), PhotoImage(file='Puissance4/button/replay/replay2.png'), PhotoImage(file ='Puissance4/button/exit.png'), PhotoImage(file ='Puissance4/game_board/red/red_turn.png'), PhotoImage(file ='Puissance4/game_board/yellow/yellow_turn.png')
ConnectC_bold, ConnectO, ConnectN_italic, ConnectN, ConnectE_bold, ConnectC, ConnectT_bold, Connect4_italic =  PhotoImage(file ='Puissance4/connect4/c-bold.png'), PhotoImage(file ='Puissance4/connect4/o.png'), PhotoImage(file ='Puissance4/connect4/n-italic.png'), PhotoImage(file ='Puissance4/connect4/n.png'), PhotoImage(file ='Puissance4/connect4/e-bold.png'), PhotoImage(file ='Puissance4/connect4/c.png'), PhotoImage(file ='Puissance4/connect4/t-bold.png'), PhotoImage(file ='Puissance4/connect4/4-italic.png')

# créer une liste des images utilisés pour le score
RedScore=[]
for i in range(10): RedScore.append(PhotoImage(file='Puissance4/score/red/score_red'+str(i)+'.png'))

YellowScore=[]
for i in range(10): YellowScore.append(PhotoImage(file='Puissance4/score/yellow/score_yellow'+str(i)+'.png'))

# met les scores et le tour à 0
winred, winyellow, y=0, 0, 0

# p ce remplie au fur et a mesure que des pions sont joués
# les 4 servent à empêcher certain bugs
p=[ [0,0,0,0,0,0,0,4],
    [0,0,0,0,0,0,0,4],
    [0,0,0,0,0,0,0,4],
    [0,0,0,0,0,0,0,4],
    [0,0,0,0,0,0,0,4],
    [0,0,0,0,0,0,0,4],
    [4,4,4,4,4,4,4,4]]

# affiche le nom du jeu à gauche
c_bold=Label(fenetre,image=ConnectC_bold); c_bold.grid(row=0,column=0)
o=Label(fenetre,image=ConnectO); o.grid(row=1,column=0)
n_italic=Label(fenetre,image=ConnectN_italic); n_italic.grid(row=2,column=0)
n=Label(fenetre,image=ConnectN); n.grid(row=3,column=0)
e_bold=Label(fenetre,image=ConnectE_bold); e_bold.grid(row=4,column=0)
c=Label(fenetre,image=ConnectC);c.grid(row=5,column=0)
t_bold=Label(fenetre,image=ConnectT_bold); t_bold.grid(row=6,column=0)
# créer les 7 boutons de jeu en haut du plateau
# 7 premiers boutons de la première ligne
boutons=[]
for colonne in range(7): boutons.append(Button(fenetre,command=lambda n=colonne: tour(n))); boutons[colonne].configure(image=RondG); boutons[colonne].grid(row=0,column=colonne+1)

# créer le bouton qui ferme la fenêtre
# première ligne huitième colonne
boutons.append(Button(fenetre,command=lambda n=7: exit())); boutons[7].configure(image=Exit); boutons[7].grid(row=0,column=8)

# créer le bouton pour recommencer la partie
# deuxième ligne huitième colonne
boutons.append(Button(fenetre,command=lambda n=8: remisea0())); boutons[8].configure(image=Replay); boutons[8].grid(row=1,column=8)

# créer le plateau de jeu
grille=[]
for ligne in range(len(p)-1): 
    grille.append([])
    for colonne in range(len(p[ligne])-1): grille[ligne].append(Label(fenetre,image=RondV)), grille[ligne][colonne].grid(row=ligne+1,column=colonne+1)

# affiche qui doit jouer
# commence par le rouge
# troisième ligne huitième colonne
turn=Label(fenetre, image=RedTurn); turn.grid(row=2,column=8)
# affiche nombre de victoire rouge
# quatrième ligne huitième colonne
yellow_score=Label(fenetre,image=YellowScore[0]); yellow_score.grid(row=3,column=8)
# affiche nombre de victoire jaune
# cinquième ligne huitième colonne
red_score=Label(fenetre,image=RedScore[0]); red_score.grid(row=4,column=8)
# pour éviter un décalage d'affiche à la première victoire
# place le bouton
rejouer=Button(fenetre, command=lambda: remisea0()); rejouer.configure(image=Replay2); rejouer.grid(row=2, column=4)
# retire le bouton
grille[1][3]=Label(fenetre,image=RondV); grille[1][3].grid(row=2,column=4)

# fonction du bouton première ligne huitième colonne
# ferme la fenêtre du jeu
def exit(): fenetre.destroy()

# fonction du bouton deuxième ligne huitième colonne et du bouton qui apparaît à la fin de la partie
# recommence une partie
def remisea0():
    # p est le plateau qui se remplie de 1 pour pion jaune et 2 pour pion rouge (seulement sur les 0), y le tour auquel on est, grille est le plateau de la fenêtre, boutons est les boutons de jeu pour fermer la fenêtre et pour rejouer
    global p, y, grille, boutons
    # désactive les boutons de jeu
    for colonne in range(7): boutons[colonne].configure(command=lambda n=colonne: None)
    # remise à zéro du plateau
    p=[ [0,0,0,0,0,0,0,4],
        [0,0,0,0,0,0,0,4],
        [0,0,0,0,0,0,0,4],
        [0,0,0,0,0,0,0,4],
        [0,0,0,0,0,0,0,4],
        [0,0,0,0,0,0,0,4],
        [4,4,4,4,4,4,4,4]]
    # enlève le bouton apparu sur le plateau à la fin de la partie
    # bouton de victoire
    grille[1][3]=Label(fenetre,image=RondV); grille[1][3].grid(row=2,column=4)
    # bouton d'égalité
    grille[0][3]=Label(fenetre,image=RondV); grille[0][3].grid(row=1,column=4)
    # remet l'image du premier joueur a jouer
    turn.config(image=RedTurn)
    # remise à 0 des tours de jeu
    y=0
    # remet le plateau à blanc
    for ligne in range(len(p)-1):
        for colonne in range(len(p[ligne])-1): grille[ligne][colonne].config(image=RondV)
    # réactive les boutons de jeu
    for c in range(7): boutons[c].configure(command=lambda n=c: tour(n))
# définie les tours des joueurs
def tour(c):
    # p est le plateau, y pour savoir qui joue si paire jaune joue si impaire rouge joue
    global p, y
    # ajoute 1 au tour car c'est le prochain tour
    y+=1
    # si le nombre de tour est paire donc si y est paire le joueur jaune joue
    JJ1(c) if y%2==0 else JR2(c)
    # sinon si le tour n'est pas paire donc y est impaire le joueur rouge joue
    pass
# quand une victoire est détecté affiche le gagnant
def victoire(n):
    # boutons est les boutons de la fenêtre, grille est le plateau afficher sur la fenêtre
    global boutons, grille, winyellow, winred, yellow_score, red_score
    # désactive le bouton rejouer à la deucième ligne huitième colonne pour éviter les bug pendant l'animation de victoire
    boutons[8].configure(command=lambda n=8: None)
    # désactive les boutons de jeu
    for colonne in range(7): boutons[colonne].configure(command=lambda n=colonne: None)
    # animation gagnant jaune
    if n==1:
        # ajoute 1 au score jaune
        winyellow+=1
        # affichage de chaque lettre avec 0.2 seconde de decalage entre les lettres
        grille[0][0].config(image=YellowY)
        fenetre.update()# update la fenêtre pour que l'attente soit pris en compte
        time.sleep(0.2)# attend 0.2 seconde
        # change le l'image de score de la fenêtre
        # if évite les erreurs out of range
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
        # joueur gagnant dans la console
        print("Victoire Jaune.")
    # animation gagnant rouge
    if n==2:
        # ajoute 1 au score rouge
        winred+=1
        # affichage de chaque lettre avec 0.2 seconde de decalage entre les lettres
        grille[0][0].config(image=RedR)
        fenetre.update(), time.sleep(0.2)
        # change l'image du score rouge de la fenêtre
        # if évite les erreurs out of range
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
        ###
        # réactive le bouton rejouer de la deuxième ligne huitième colonne
        boutons[8].configure(command=lambda n=8: remisea0())
        ###
        # affiche égalité dans la console
        print("Égalité.")
        ###
    ###
# ce declenche quand y est paire
# tour du joueur jaune
def JJ1(c):
    # test les erreurs
    try:
        # p est le plateau de jeu et y est pour savoir qui joue
        global p, y
        # i=5 car 5 est la dernière ligne du plateau (dans une liste la première variable est 0 donc 0,1,2,3,4,5 fait 6 lignes)
        i=5
        # regarde si un pion est déja dans la colonne si oui regarde sur quel ligne il peut mettre le pion
        while p[i][c]!=0 and i>=0: i-=1 # remonte sur la ligne avant si il y a deja un pion sur la colonne selectionné      
        # place le pion jaune sur le plateau p en remplaçant le 0 correspondant en 1 et remplace l'image de la case correspondante dans grille
        if i>=0:
            p[i][c]=1
            grille[i][c].config(image=RondJ)
            turn.config(image=RedTurn)
############################################################################
# test toute les possibilités de victoire
# si une victoire est détectée renvoie 1 à la fonction victoire qui affiche la victoire jaune
            # detection de victoire horizontale
            if p[i][c-1]==1 and c-1>=0:
                if p[i][c-2]==1 and c-2>=0:
                    if p[i][c-3]==1 and c-3>=0: return victoire(1)
                    elif p[i][c+1]==1 and c+1<=6: return victoire(1)
                elif p[i][c+1]==1 and c+1<=6:
                    if p[i][c+2]==1 and c+2<=6: return victoire(1)
            elif p[i][c+1]==1 and c+1<=6:
                if p[i][c+2]==1 and c+2<=6:
                    if p[i][c+3]==1 and c+3<=6: return victoire(1)
                    elif p[i][c-1]==1 and c-1>=0: return victoire(1)
###############################################################################
            # detection de victoire verticale
            if p[i-1][c]==1 and i-1>=0:
                if p[i-2][c]==1 and i-2>=0:
                    if p[i-3][c]==1 and i-3>=0: return victoire(1)
                    elif p[i+1][c]==1 and i+1<=5: return victoire(1)
                elif p[i+1][c]==1 and i+1<=5:
                    if p[i+2][c]==1 and i+2<=5: return victoire(1)
            elif p[i+1][c]==1 and i+1<=5:
                if p[i+2][c]==1 and i+2<=5:
                    if p[i+3][c]==1 and i+3<=5: return victoire(1)
                    elif p[i-1][c]==1 and i-1>=0: return victoire(1)
##################################################################################
            # detection de victoire diagonale gauche de haut en bas
            if p[i+1][c+1]==1 and i+1<=5 and c+1<=6:
                if p[i+2][c+2]==1 and i+2<=5 and c+2<=6:
                    if p[i+3][c+3]==1 and i+3<=5 and c+3<=6: return victoire(1)
                    elif p[i-1][c-1]==1 and i-1>=0 and c-1>=0: return victoire(1)
                elif p[i-1][c-1]==1 and i-1>=0 and c-1>=0:
                    if p[i-2][c-2]==1 and i-2>=0 and c-2>=0: return victoire(1)
            elif p[i-1][c-1]==1 and i-1>=0 and c-1>=0:
                if p[i-2][c-2]==1 and i-2>=0 and c-2>=0:
                    if p[i-3][c-3]==1 and i-3>=0 and c-3>=0: return victoire(1)
                    elif p[i+1][c+1]==1 and i+1<=5 and c-1>=0: return victoire(1)
                elif p[i+1][c+1]==1 and i+1<=5 and c+1<=6:
                    if p[i+2][c+2]==1 and i+2<=5 and c+2<=6: return victoire(1)
##################################################################################
            # detection de victoire diagonale droite de haut en bas
            if p[i-1][c+1]==1 and i-1>=0 and c+1<=6:
                if p[i-2][c+2]==1 and i-2>=0 and c+2<=6:
                    if p[i-3][c+3]==1 and i-3>=0 and c+3<=6: return victoire(1)
                    elif p[i+1][c-1]==1 and i+1<=5 and c-1>=0: return victoire(1)
                elif p[i+1][c-1]==1 and i+1<=5 and c-1>=0:
                    if p[i+2][c-2]==1 and i+2<=5 and c-2>=0: return victoire(1)
            elif p[i+1][c-1]==1 and i+1<=5 and c-1>=0:
                if p[i+2][c-2]==1 and i+2<=5 and c-2>=0:
                    if p[i+3][c-3]==1 and i+3<=5 and c-3>=0: return victoire(1)
                    elif p[i-1][c+1]==1 and i-1>=0 and c+1<=6: return victoire(1)
                elif p[i-1][c+1]==1 and i-1>=0 and c+1<=6:
                    if p[i-2][c+2]==1 and i-2>=0 and c+2<=6: return victoire(1)
##################################################################################
            # détecte si le plateau est remplie de pion si oui renvoie 3 à la fonction victoire qui fait une égalité
            if 0 not in p[0]: return victoire(3)
        else: y=1 # si la colonne est pleine y est remis à 1 pour que jaune puisse rejouer car il n'a pas placé de pion
    # si l'erreur IndexError est détectée il l'ignore
    except IndexError: pass

# ce declenche quand y est impaire
# tour du joueur rouge
def JR2(c):
    # test les erreurs
    try:
        # p est le plateau de jeu et y est pour savoir qui joue
        global p, y
        # i=5 car 5 est la dernière ligne du plateau (dans une liste la première variable est 0 donc 0,1,2,3,4,5 fait 6 lignes)
        i=5
        # regarde si un pion est déja dans la colonne si oui regarde sur quel ligne il peut mettre le pion
        while p[i][c]!=0 and i>=0: i-=1
            # remonte sur la ligne avant si il y a deja un pion sur la colonne selectionné
        # place le pion rouge sur le plateau p en remplaçant le 0 correspondant en 2 et remplace l'image de la case correspondante dans grille
        if i>=0:
            p[i][c]=2
            grille[i][c].config(image=RondR)
            turn.config(image=YellowTurn)
############################################################################
# test toute les possibilités de victoire
# si une victoire est détectée renvoie 2 à la fonction victoire qui affiche la victoire rouge
            # detection de victoire horizontale
            if p[i][c-1]==2 and c-1>=0:
                if p[i][c-2]==2 and c-2>=0:
                    if p[i][c-3]==2 and c-3>=0: return victoire(2)
                    elif p[i][c+1]==2 and c+1<=6: return victoire(2)
                elif p[i][c+1]==2 and c+1<=6:
                    if p[i][c+2]==2 and c+2<=6: return victoire(2)
            elif p[i][c+1]==2 and c+1<=6:
                if p[i][c+2]==2 and c+2<=6:
                    if p[i][c+3]==2 and c+3<=6: return victoire(2)
                    elif p[i][c-1]==2 and c-1>=0: return victoire(2)
################################################################################
            # detection de victoire verticale
            if p[i-1][c]==2 and i-1>=0:
                if p[i-2][c]==2 and i-2>=0:
                    if p[i-3][c]==2 and i-3>=0: return victoire(2)
                    elif p[i+1][c]==2 and i+1<=5: return victoire(2)
                elif p[i+1][c]==2 and i+1<=5:
                    if p[i+2][c]==2 and i+2<=5: return victoire(2)
            elif p[i+1][c]==2 and i+1<=5:
                if p[i+2][c]==2 and i+2<=5:
                    if p[i+3][c]==2 and i+3<=5: return victoire(2)
                    elif p[i-1][c]==2 and i-1>=0: return victoire(2)
##################################################################################
            # detection de victoire diagonale gauche de haut en bas
            if p[i+1][c+1]==2 and i+1<=5 and c+1<=6:
                if p[i+2][c+2]==2 and i+2<=5 and c+2<=6:
                    if p[i+3][c+3]==2 and i+3<=5 and c+3<=6: return victoire(2)
                    elif p[i-1][c-1]==2 and i-1>=0 and c-1>=0: return victoire(2)
                elif p[i-1][c-1]==2 and i-1>=0 and c-1>=0:
                    if p[i-2][c-2]==2 and i-2>=0 and c-2>=0: return victoire(2)
            elif p[i-1][c-1]==2 and i-1>=0 and c-1>=0:
                if p[i-2][c-2]==2 and i-2>=0 and c-2>=0:
                    if p[i-3][c-3]==2 and i-3>=0 and c-3>=0: return victoire(2)
                    elif p[i+1][c+1]==2 and i+1<=5 and c-1>=0: return victoire(2)
                elif p[i+1][c+1]==2 and i+1<=5 and c+1<=6:
                    if p[i+2][c+2]==2 and i+2<=5 and c+2<=6: return victoire(2)
##################################################################################
            # detection de victoire diagonale droite de haut en bas
            if p[i-1][c+1]==2 and i-1>=0 and c+1<=6:
                if p[i-2][c+2]==2 and i-2>=0 and c+2<=6:
                    if p[i-3][c+3]==2 and i-3>=0 and c+3<=6: return victoire(2)
                    elif p[i+1][c-1]==2 and i+1<=5 and c-1>=0: return victoire(2)
                elif p[i+1][c-1]==2 and i+1<=5 and c-1>=0:
                    if p[i+2][c-2]==2 and i+2<=5 and c-2>=0: return victoire(2)
            elif p[i+1][c-1]==2 and i+1<=5 and c-1>=0:
                if p[i+2][c-2]==2 and i+2<=5 and c-2>=0:
                    if p[i+3][c-3]==2 and i+3<=5 and c-3>=0: return victoire(2)
                    elif p[i-1][c+1]==2 and i-1>=0 and c+1<=6: return victoire(2)
                elif p[i-1][c+1]==2 and i-1>=0 and c+1<=6:
                    if p[i-2][c+2]==2 and i-2>=0 and c+2<=6: return victoire(2)
##################################################################################
            # détecte si le plateau est remplie de pion si oui renvoie 3 à la fonction victoire qui fait une égalité
            if 0 not in p[0]: return victoire(3)
        else: y=0 # si la colonne est pleine y est remis à 0 pour que rouge puisse rejouer car il n'a pas placé de pion
    # si l'erreur IndexError est détectée il l'ignore
    except IndexError: pass
# ouvre la fenêtre
fenetre.mainloop()
#######################################################################################################