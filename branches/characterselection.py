__author__ = 'Ian'
def characterSelect(screen):
   import os,pygame,GraphicInput
   screen.fill((0,0,0))
   running=True
   name=GraphicInput.ask(screen,'Enter Name of Character to Select', (300,300))
   if name == 'FALSE':
       running=False
       return None
   else:
       pass
   pygame.display.update()
   screen.fill((0, 0, 0))
   while running:
        xi,yi=screen.get_size()
        event=pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or pygame.K_RETURN:
                break
