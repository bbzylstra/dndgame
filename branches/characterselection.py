__author__ = 'Ian'
def characterSelect(screen):
   import os,pygame,GraphicInput, ctypes, charactercreation
   user32 = ctypes.windll.user32
   screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
   screen.fill((0,0,0))
   
   name = None
   race = None
   cclass = None
   hp = None
   mana = None
   stamina = None
   stre = None 
   agl = None 
   inte = None 
   cour = None 
   dex = None 
   conc = None
   item = None
   try:
       current_directory=os.getcwd()
       saves_path=current_directory+'/saves/'
       fileNames=os.listdir(saves_path)
       selectedSave=GraphicInput.ask(screen,'CharName: ',(300,300))
       GraphicInput.display_message(screen, "names"+str(fileNames), (600, 600))
   except:
        charactercreation.characterCreate(screen)
       
   while True:
        #write graphical front end here to display the names in fileNames
        #please store the selected file name in a variable called selectedSave, please delete line 24 when done.
        #Screensize is stored in the screensize tuple. Get x from screensize[0] and y from screensize[1]
        
        f=open(saves_path+selectedSave+"\stats.wagh",'r')
        name = f.readline()
        race = f.readline()
        cclass = f.readline()
        hp = int(f.readline())
        mana = int(f.readline())
        stamina = int(f.readline())
        stre = int(f.readline())
        agl = int(f.readline()) 
        inte = int(f.readline()) 
        cour = int(f.readline())
        dex = int(f.readline()) 
        conc = int(f.readline())
        
        #Write front end to display the stats read from the file
        
        event=pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or pygame.K_RETURN:
                return name, race, cclass, hp, mana, stamina, stre, agl, inte, cour, dex, conc
        
        
