# -*- coding: cp1252 -*-
import pygame,random,os
from pygame.locals import *

#Salut, modification du fichier de dom

reference_entrainement = ['n']
distracteurs_entrainement = ['l','m','o']
reference_parties = ['b']
distracteurs_partie1 = ['x','y','z']
distracteurs_partie2 = ['p','d','q']

nombre_essais_entrainement = 10
nombre_essais_parties = 11

consignes = "\nCONSIGNES\n\nBonjour connard, bienvenue à mon expérience de merde. Je te propose de commencer à te concentrer sérieusement, parce que si tu ne fais pas bien cette tâche, \
autant te jeter du haut de la tour Eiffel pour débarasser le monde de ton inutile carcasse.\n\n\nAppuyez sur espace pour commencer."

#bibliothèque nécessaire à la fonction text_input : mappe les codes ascii aux lettres correspondantes.
_keys = {97: 'q', 98: 'b', 99: 'c', 100: 'd', 101 : 'e', \
         102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', \
         107: 'k', 108: 'l', 59: 'm', 110: 'n', 111: 'o',\
         112: 'p', 113: 'a', 114: 'r', 115: 's', 116: 't',\
         117: 'u', 118: 'v', 119: 'z', 120: 'x', 121: 'y',\
         122: 'w', 57: '9', 56: '8', 55: '7', 54: '6', 53: '5',\
         52: '4', 51: '3', 50: '2', 49: '1', 48: '0', 32: '_',\
         K_KP0: '0',K_KP1: '1',K_KP2: '2',K_KP3: '3',K_KP4: '4',\
         K_KP5: '5',K_KP6: '6',K_KP7: '7',K_KP8: '8',K_KP9: '9'}

def ecrire (phrase, police, taille, (x,y), color_font,color_background=None):      #attention pas de flip dans cette fonction
    police = pygame.font.SysFont(police, taille)
    surface=police.render(phrase, 1, color_font)
    rectangle = surface.get_rect()
    rectangle.center = (x,y)
    if color_background==None:
        pass
    else:
        screen.fill(color_background)
    screen.blit(surface, rectangle)

def lignes_rouges():
    police = pygame.font.SysFont("lucida console", W/14)
    d=police.render('d', 1, (0, 0, 0))
    large=d.get_width()
    haute=d.get_height()
    pygame.draw.line(screen, (255,0,0), [W/2,H/2-haute], [W/2,H/2+haute], 2)
    pygame.draw.line(screen, (255,0,0), [W/2-large,H/2-haute], [W/2-large,H/2+haute], 2)

def barrage(reference_letter, distractive_letters, essais):
    #récupère la taille d'une lettre (lucida console est monospace)
    police = pygame.font.SysFont("lucida console", W/14)
    d=police.render('d', 1, (0, 0, 0))
    large=d.get_width()
    haute=d.get_height()

    #construit une liste d'octets bpdqbpdq aléatoire 
    letters = reference_letter + distractive_letters
    listetemp = 2 * letters
    listedef = []
    while len(listedef)<= (essais+34):
        random.shuffle(listetemp)
        if not listedef:
            for j in range (8):
                listedef.append(listetemp[j])
        else:
            if (listetemp[0]==listedef[len(listedef)-1] and listetemp[0]==listedef[len(listedef)-2]) or (listetemp[0]==listedef[len(listedef)-1] and listetemp[1]==listedef[len(listedef)-1]): #évite les répétions de 3 fois la même lettre
                pass
            else:
                for j in range (8):
                    listedef.append(listetemp[j])

    #Créations des essais         
    for j in range (essais):
        pygame.event.set_allowed(pygame.KEYDOWN)
        #on créé/recréé les listes, pour les vider plus facilement que si c'était des strings
        affiche=[2]
        affiche2=[2]
        affiche[:] = []
        affiche2[:] = []
        #Construit des listes successives de 34 items en incrémentant
        for i in range (34):
            affiche.append(listedef[i+j])
            affiche2=''.join(affiche)            
                       

        #Affichage de la liste
        ecrire(affiche2,"lucida console", W/14,(W/2,H/2),(0, 0, 0),(190, 190, 190))
        lignes_rouges()
        pygame.display.flip()
        t0=pygame.time.get_ticks()

        #Réponse
        response = ''
        while response == '':
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    raise Exception
                elif event.type == KEYDOWN and event.key == K_b:
                    if affiche[16]==letters[0]:
                        response = '1'
                    else:
                        response = '0'
                elif event.type == KEYDOWN and event.key == K_n:
                    if affiche[16]==letters[0]:
                        response = '0'                      
                    else:
                        response = '1'
            t1 = pygame.time.get_ticks()

        #On bloque le clavier pour éviter de pouvoir répondre pendant....
        pygame.event.set_blocked(KEYDOWN)

        #...que la liste bouge à l'écran
        for k in range (large/7):
            ecrire(affiche2,"lucida console", W/14,(W/2-(k*7),H/2),(0, 0, 0),(190, 190, 190))
            lignes_rouges()
            pygame.display.flip()

        TR = t1 - t0

        #récupère l'écart par rapport à la dernière lettre référence
        ecart = ''
        x=1
        while ecart == '':
            if affiche[16-x]==letters[0]:
                if x>j:
                    ecart = None
                else:
                    ecart = x-1
            else:
                x=x+1
        
        if distractive_letters == ['l','m','o']:
            print>>data, suj+';'+init+';'+sexe+';'+ age+';'+ lateralisation+';'+'entrainement'+';'+str(reference_letter)+';'+ str(distractive_letters)+';'+affiche[16]+';'+ response+';'+ str(TR)+';'+ str(j+1)+';'+str(ecart)
        elif distractive_letters == ['x','y','z']:
            print>>data, suj+';'+init+';'+sexe+';'+ age+';'+ lateralisation+';'+'partie1'+';'+str(reference_letter)+';'+ str(distractive_letters)+';'+affiche[16]+';'+ response+';'+ str(TR)+';'+ str(j+1)+';'+str(ecart)
        else:
            print>>data, suj+';'+init+';'+sexe+';'+ age+';'+ lateralisation+';'+'partie2'+';'+str(reference_letter)+';'+ str(distractive_letters)+';'+affiche[16]+';'+ response+';'+ str(TR)+';'+ str(j+1)+';'+str(ecart)
        


def text_input(question,(x,y)):#fait comme raw_input mais en blittant avec pygame, (x,y) controle les coordonnées d'affichage. Nécessite la bibliothèque _keys
    output=''
    boucle=True
    while boucle:
        police = pygame.font.SysFont("arial", W/30)
        surface=police.render(question, 1, (0,0,0))
        rectangle = (x,y)
        size = surface.get_size()
        pygame.draw.rect(screen, (220, 220, 220), (x,y,size[0],size[1]))
        screen.blit(surface, rectangle)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in _keys and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    output=output+_keys[event.key].upper()
                    question = question + _keys[event.key].upper()
                elif event.key in _keys:
                    output=output+_keys[event.key]
                    question = question + _keys[event.key]
                elif event.key == K_BACKSPACE:
                    output=output[:len(output)-1]
                    question=question[:len(question)-1]
                elif event.key == K_RETURN:
                    return(output)
                    boucle=False
                elif event.key == K_ESCAPE:
                    raise Exception
        pygame.draw.rect(screen, (220, 220, 220), (x,y,size[0],size[1]))

def write_instructions(phrase):#affiche consignes, on va à la ligne avec \n
    police = pygame.font.SysFont("arial", W/30)
    screen.fill((255, 255, 255))
    affiche=''
    ligne = 0
    for i in range(len(phrase)):
        if i == (len(phrase)-1):
            affiche=affiche+phrase[i]
            surface=police.render(affiche, 1, (0, 0, 0))
            rectangle = surface.get_rect()
            rectangle.center = (W/2,(surface.get_height()/2)+(ligne*surface.get_height()))            
            screen.blit(surface, rectangle)
        elif phrase[i]=='\n':
            surface=police.render(affiche, 1, (0, 0, 0))
            rectangle = surface.get_rect()
            rectangle.center = (W/2,(surface.get_height()/2)+(ligne*surface.get_height()))            
            screen.blit(surface, rectangle)
            affiche=""
            ligne = ligne +1
        else:
            affiche=affiche+phrase[i]
            surface=police.render(affiche, 1, (0, 0, 0))
            rectangle = surface.get_rect()
            if phrase[i] == ' 'and surface.get_width()+W/4>W:
                rectangle.center = (W/2,(surface.get_height()/2)+(ligne*surface.get_height()))            
                screen.blit(surface, rectangle)
                affiche=""
                ligne = ligne +1
            else:
                pass
            
    boucle=True
    while boucle:    
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_SPACE:
                boucle=False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                raise Exception

def compte_a_rebours():
    rebours = ['3','2','1']
    boucle=True
    while boucle:
        ecrire(34*'#',"lucida console",W/14,(W/2,H/2),(0, 0, 0),(190, 190, 190))
        ecrire('Appuyez sur ESPACE pour commencer',"arial", W/30, (W/2,H/1.2),(0, 0, 0))
        lignes_rouges()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_SPACE:
                boucle=False
        
    for i in range (3):
        ecrire(34*'#',"lucida console", W/14, (W/2,H/2),(0, 0, 0),(190, 190, 190))
        ecrire(rebours[i],"arial", W/10, (W/2-30,H/6),(255, 0, 0))
        lignes_rouges()
        pygame.display.flip()
        pygame.time.wait(1000)
    

try:
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((0, 0), FULLSCREEN | DOUBLEBUF | HWSURFACE)
    W, H = screen.get_size()
    
    screen.fill((255, 255, 255))
    suj = text_input('Sujet n° : ',(50,H/9))
    init = text_input('Initiales : ',(50,H/9*2))
    sexe = text_input('Genre : ',(50,H/9*3))
    age = text_input('Âge : ',(50,H/9*4))
    lateralisation = text_input('Latéralisation : ',(50,H/9*5))

    data = open('suj'+suj+init+'.csv','w')
    print>>data, 'Sujet'+';'+ 'Initiales'+';'+'Sexe'+';'+ 'Age'+';'+ 'Lateralisation'+';'+'Partie'+';'+'Référence'+';'+'Distracteurs'+';'+'Lettre'+';'+ 'Reponse'+';'+'TR'+';'+'rang'+';'+'ecart_dernier_b'
    
    write_instructions(consignes)
    compte_a_rebours()
    barrage(reference_entrainement, distracteurs_entrainement, nombre_essais_entrainement)
    write_instructions(consignes)
    compte_a_rebours()
    barrage(reference_parties, distracteurs_partie1, nombre_essais_parties)
    write_instructions(consignes)
    compte_a_rebours()
    barrage(reference_parties, distracteurs_partie2,nombre_essais_parties)

                      

finally:
    try: data.close()
    except: pass
    pygame.quit()
