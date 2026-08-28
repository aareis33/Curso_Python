## Tocando um áudio

import pygame

pygame.init()

pygame.mixer.music.load('exercicio21.wav')
pygame.mixer.music.play()

clock = pygame.time.Clock()
while pygame.mixer.music.get_busy():
	clock.tick(10)
