import comtest, pygame,characterselection, ctypes, sys
def openScreen(screen):
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    game_font = pygame.font.Font("freesansbold.ttf",16)
    LEFT=True
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            print "You released the left mouse button at (%d, %d)" % event.pos
            if (event.pos[0] >=screensize[0]*.4033 and event.pos[0] <=screensize[0]*.63) and (event.pos[1] >=screensize[1]*.02 and event.pos[1] <=screensize[1]*.16) :
                return
                pygame.quit()
            elif(event.pos[0] >=screensize[0]*.1244 and event.pos[0] <=screensize[0]*.63) and (event.pos[1] >=screensize[1]*.02 and event.pos[1] <=screensize[1]*.15625) :
                charactercreation.characterCreate(screen)
            elif (event.pos[0] >=screensize[0]*.0073 and event.pos[0] <=screensize[0]*.106149) and (event.pos[1] >=screensize[1]*.8905 and event.pos[1] <=screensize[1]*.990885) :
                sys.exit()
            elif (event.pos[0] >=370 and event.pos[0] <=590) and (event.pos[1] >=330 and event.pos[1] <=380) :
                comtest.combatsim(screen)
            elif(event.pos[0] >=screensize[0]*.3184480234 and event.pos[0] <=screensize[0]*.4595592972) and (event.pos[1] >=screensize[1]*.6184895833 and event.pos[1] <=screensize[1]*.7161458333) :
                characterselection.characterSelect(screen)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
                pygame.quit()
        screen.fill((0, 0, 0))
        pygame.draw.polygon(screen, (255, 0, 0), [(screensize[0]*.4033,screensize[1]*.02),(screensize[0]*.63,screensize[1]*.02),(screensize[0]*.63,screensize[1]*.16),(screensize[0]*.4033,screensize[1]*.16)],1)
        game = game_font.render("Launch A Game", True, (255,0, 0), (0, 0, 0))
        screen.blit(game,(screensize[0]*.46658,screensize[1]*.0799))
        pygame.draw.polygon(screen, (255, 0, 0), [(screensize[0]*.1244,screensize[1]*.02),(screensize[0]*.35139,screensize[1]*.02),(screensize[0]*.35139,screensize[1]*.15625),(screensize[0]*.1244,screensize[1]*.15625)],1)
        game = game_font.render("Create A New Character", True, (255,0, 0), (0, 0, 0))
        screen.blit(game,(screensize[0]*.16065,screensize[1]*.0799))
        pygame.draw.polygon(screen, (255, 0, 0), [(370, 380),(370,330), (590, 330),(590,380)],1)
        game = game_font.render("1v1 Combat Simulator", True, (255,0, 0), (0, 0, 0))
        screen.blit(game, (375,350) )
        pygame.draw.polygon(screen, (255, 0, 0), [(screensize[0]*.0073,screensize[1]*0.9375),(screensize[0]*.106149,screensize[1]*0.9375), (screensize[0]*.106149,screensize[1]*.990885),(screensize[0]*.0073,screensize[1]*.990885)],1)
        game = game_font.render("Exit", True, (255,0, 0), (0, 0, 0))
        screen.blit(game, (screensize[0]*.034407,screensize[1]*0.96484375))
        pygame.draw.polygon(screen, (255, 0, 0), [(screensize[0]*.3184480234,screensize[1]*.6184895833),(screensize[0]*.4595592972,screensize[1]*.6184895833),(screensize[0]*.4595592972,screensize[1]*.7161458333),(screensize[0]*.3184480234,screensize[1]*.7161458333)],1)
        game = game_font.render("Character Selection", True, (255,0, 0), (0, 0, 0))
        screen.blit(game,(screensize[0]*.336749634,screensize[1]*.6590416667))
        pygame.display.flip()
