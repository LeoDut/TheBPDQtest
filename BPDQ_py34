# -*- coding: cp1252 -*-

import pygame
from pygame.locals import *
import random
import os
import csv   
import sys     
import shutil
import tempfile
import zipfile
import time
import statistics


#-----------------------------------|
#-----------------------------------|
#         The BPDQ test             |
#-----------------------------------|
#-----------------------------------|




#------------------------------------------
# INITIALISATION
#------------------------------------------

fichiercsv = csv.reader(open("BPDQtest.csv","rb"))






#------------------------------------------
#INFORMATIONS
#------------------------------------------
EXPERIMENT = "BPDQ"
DATE = (time.strftime("%d/%m/%Y"))

initials = input("Quelles sont vos initiales?\n")
print()
print()

numerosujet = input("Quel est votre numéro de sujet?\n")
print()
print()

age = input("Quel est votre âge?\n")
print()
print()

sex = input("Quel est votre sexe? H ou F?\n")
print()
print()


input("Appuyez sur ENTREE pour continuer...\n")
print("Start Time : ", time.strftime("%H:%M:%S"))




#------------------------------------------
# DEMARRAGE
#------------------------------------------

run = True
pret = False
training = False
pret2 = False
part1 = False
pret3 = False
part2 = False



try:

    pygame.init()
    myfont = pygame.font.SysFont("Times New Roman", 50)
    myletter = pygame.font.SysFont("Lucida Sans Typewriter", 100)
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((0, 0), FULLSCREEN | DOUBLEBUF | HWSURFACE)
    pygame.display.set_caption("The BPDQ test")
    Clock = pygame.time.Clock()
    Clock.tick(60)
    screeninfo = pygame.display.Info() #to get the size of the screen



    while run:

#-----------------------------
# PRET
#-----------------------------
        pret = True
        

        screen.fill((255, 255, 255))
        label = myfont.render("Etes-vous prêt?", 10, (0,0,0))
        screen.blit(label, (0.75 * screeninfo.current_w / 2, 0.9 * screeninfo.current_h / 2))

        while pret: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("User asked to quit.", time.strftime("%H:%M:%S"))
                    pret = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        print("User asked to quit.", time.strftime("%H:%M:%S"))
                        pret = False
                        run = False
                    if event.key == K_SPACE:
                        pret = False
                    if event.key == K_b:
                        screen.fill((255, 255, 255))
                        label = myfont.render("Attendez, ceci n'est pas encore un b", 10, (0,0,0))
                        screen.blit(label, (0.5 * screeninfo.current_w / 2, 0.9 * screeninfo.current_h / 2))
                    if event.key == K_n:
                        screen.fill((255, 255, 255))
                        label = myfont.render("Attendez, ceci pourrait être un b", 10, (0,0,0))
                        screen.blit(label, (0.5 * screeninfo.current_w / 2, 0.9 * screeninfo.current_h / 2))
            pygame.display.flip()

        
#-----------------------------
# TRAINING
#-----------------------------
        training = True
        trial = 1

   #initialisation
        traininglist_weightedchoices = [("x", 15), ("b", 5)]
        traininglist = [val for val, cnt in traininglist_weightedchoices for i in range(cnt)]
        
   # C'est parti
        
        
        dispcroix = myletter.render("+", 10, (0,0,0))
        letter = random.choice(traininglist)
        screen.fill((255, 255, 255))
        displetter = myletter.render(letter, 10, (0,0,0))   
        screen.blit(displetter, (0.95 * screeninfo.current_w / 2, 0.85 * screeninfo.current_h / 2))
        Clock.tick()
        
        while training:

            

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("User asked to quit.", time.strftime("%H:%M:%S"))
                    training = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        print("User asked to quit.", time.strftime("%H:%M:%S"))
                        training = False
                        run = False
                        
                    if event.key == K_b and letter == "b":
                        timetrial = Clock.get_rawtime()
                        print("essai", trial, " : NB,", timetrial)                 
                        #tempvalue = [EXPERIMENT, DATE, time.strftime("%H:%M:%S"), numerosujet, initials, age, sex, "Training", trial, letter, "b", "NB", timetrial]
                        #tempvalue = training + str(trial)
                        trial = trial +1
                        
                        screen.fill((255, 255, 255))
                        #screen.blit(dispcroix, (0.95 * screeninfo.current_w / 2, 0.85 * screeninfo.current_h / 2))
                        pygame.time.wait(500)
                        
                        screen.fill((255, 255, 255))
                        letter = random.choice(traininglist)
                        displetter = myletter.render(letter, 10, (0,0,0))
                        Clock.tick()
                        screen.blit(displetter, (0.95 * screeninfo.current_w / 2, 0.85 * screeninfo.current_h / 2))
                        traininglist.remove("b")
                        
                    if event.key == K_b and letter == "x":
                        timetrial = Clock.get_rawtime() 
                        print("essai", trial, " : NA,", timetrial)
                        #training + int(trial) = [EXPERIMENT, DATE, time.strftime("%H:%M:%S"), numerosujet, initials, age, sex, "Training", trial, letter, "b", "NA", timetrial]
                        trial = trial +1

                        
                        letter = random.choice(traininglist)
                        screen.fill((255, 255, 255))
                        #screen.blit(dispcroix, (0.95 * screeninfo.current_w / 2, 0.85 * screeninfo.current_h / 2))
                        pygame.time.wait(500)

                        Clock.tick()
                        screen.fill((255, 255, 255))
                        displetter = myletter.render(letter, 10, (0,0,0))
                        screen.blit(displetter, (0.95 * screeninfo.current_w / 2, 0.85 * screeninfo.current_h / 2))
                        traininglist.remove("x")
                        
                    if event.key == K_n and letter == "b":
                        timetrial = Clock.get_rawtime() 
                        print("essai", trial, " : NO,", timetrial)
                        #training + int(trial) = [EXPERIMENT, DATE, time.strftime("%H:%M:%S"), numerosujet, initials, age, sex, "Training", trial, letter, "x", "NO", timetrial]
                        trial = trial +1
                        
                        
                        letter = random.choice(traininglist)
                        screen.fill((255, 255, 255))
                        #screen.blit(dispcroix, (0.95 * screeninfo.current_w / 2, 0.85 * screeninfo.current_h / 2))
                        pygame.time.wait(500)

                        Clock.tick()
                        screen.fill((255, 255, 255))
                        displetter = myletter.render(letter, 10, (0,0,0))
                        screen.blit(displetter, (0.95 * screeninfo.current_w / 2, 0.85 * screeninfo.current_h / 2))
                        traininglist.remove("b")
                        
                    if event.key == K_n and letter == "x":
                        timetrial = Clock.get_rawtime() 
                        print("essai", trial, " : NX,", timetrial)
                        #training + int(trial) = [EXPERIMENT, DATE, time.strftime("%H:%M:%S"), numerosujet, initials, age, sex, "Training", trial, letter, "x", "NX", timetrial]
                        trial = trial +1
                        
                        
                        letter = random.choice(traininglist)
                        screen.fill((255, 255, 255))
                        #screen.blit(dispcroix, (0.95 * screeninfo.current_w / 2, 0.85 * screeninfo.current_h / 2))
                        pygame.time.wait(500)

                        Clock.tick()
                        screen.fill((255, 255, 255))
                        displetter = myletter.render(letter, 10, (0,0,0))
                        screen.blit(displetter, (0.95 * screeninfo.current_w / 2, 0.85 * screeninfo.current_h / 2))
                        traininglist.remove("x")

                    if len(traininglist) < 1:
                        screen.fill((255, 255, 255))
                        screen.blit(dispcroix, (0.95 * screeninfo.current_w / 2, 0.85 * screeninfo.current_h / 2))
                        pygame.time.wait(500)
                        
                        screen.fill((255, 255, 255))
                        label = myfont.render("Fin de l'entrainement.", 10, (0,0,0))
                        screen.blit(label, (0.4 * screeninfo.current_w / 2, 0.9 * screeninfo.current_h / 2))
                        training = False



            pygame.display.flip()

    
        run = False



#-----------------------------
# PRET2
#-----------------------------
        pret2 = True
        

        screen.fill((255, 255, 255))
        label = myfont.render("Etes-vous prêt?", 10, (0,0,0))
        screen.blit(label, (0.75 * screeninfo.current_w / 2, 0.9 * screeninfo.current_h / 2))

        while pret2: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("User asked to quit.", time.strftime("%H:%M:%S"))
                    pret2 = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        print("User asked to quit.", time.strftime("%H:%M:%S"))
                        pret2 = False
                        run = False
                    if event.key == K_SPACE:
                        pret2 = False
            pygame.display.flip()








#------------------------------------------
# ENREGISTREMENT DU FICHIER
#------------------------------------------
        
    filename = numerosujet + initials + '.csv'

    with open(filename, 'w', newline='') as csvfile:
        f = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        f.writerow(["Experiment","Date", "Time", 'Numero','Initials',"Age","sex","Part", "Trial", "Letter","Answer", "Type", "Time"])
        f.writerow(["Experiment","Date", "Time", 'Numero','Initials',"Age","sex","Part", "Trial", "tasoeur","tasoeur", "tasoeur", "tasoeur"])
        f.writerow(parttraining1)







#-----------------------------
# ENDING
#-----------------------------
finally:



    
    
    pygame.quit()
