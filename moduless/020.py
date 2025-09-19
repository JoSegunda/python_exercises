#Programa que abre e reproduz um áudio mp3
import pygame

pygame.init()
pygame.mixer.music.load("/home/joel-pereira/Documents/Skills/Python/Beginning/exercises/yhea.mp3")

pygame.mixer.music.play()
input("Pressione Enter para sair...")