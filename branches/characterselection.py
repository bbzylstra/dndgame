__author__ = 'Ian'
def characterSelect(screen):
   import os,pygame,GraphicInput, ctypes
   user32 = ctypes.windll.user32
   screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
   screen.fill((0,0,0))
   running=True
   current_directory=os.getcwd()
   saves_path=current_directory+'/saves/'
   fileNames=os.listdir(saves_path)
   GraphicInput.display_message(screen, "names"+str(fileNames), (600, 600))
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
