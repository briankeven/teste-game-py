import pygame
import random
import sys

pygame.init()
window = pygame.display.set_mode([800, 580])

quadX= 100
quadY= 175
speedX= 0
speedY= 0

clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        speedX = -5
      if event.key == pygame.K_RIGHT:
        speedX = 5
      if event.key == pygame.K_UP:
        speedY = -5
      if event.key == pygame.K_DOWN:
        speedY = 5
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        speedX = 0
      if event.key == pygame.K_RIGHT:
        speedX = 0
      if event.key == pygame.K_UP:
        speedY = 0
      if event.key == pygame.K_DOWN:
        speedY = 0
  window.fill((150,200,180))
  pygame.draw.rect(
    window, (0,0,0), [0,150, 600, 100]
  )
  pygame.draw.rect(
    window, (0,0,0),[500,250, 100, 330]
  )
  pygame.draw.rect(
    window, (255,255,255), [quadX,quadY,50,50]
  )
  quadX+=speedX
  quadY+=speedY

  if quadY < 150 or quadY > 200 or quadX < 0  or quadX > 550:
    if quadX < 500 or quadX > 550 or quadY < 150:
      font=pygame.font.Font('freesansbold.ttf',150)
      text=font.render('PERDEU',True,(255,0,0))
      window.blit(text,[100,50])
      pygame.display.update()
      pygame.time.wait(2000)
      sys.exit()

  if quadY > 530:
    font=pygame.font.Font('freesansbold.ttf',150)
    text=font.render('GANHOU',True,(50,200,50))
    window.blit(text,[50,50])
    pygame.display.update()
    pygame.time.wait(2000)
    sys.exit()
 
  pygame.display.update()
  clock.tick(30)