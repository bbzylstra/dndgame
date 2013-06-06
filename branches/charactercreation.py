def characterCreate(screen):
    import os,pygame,GraphicInput
    screen.fill((0,0,0))
    name = 'unknown' #Variable for Player Name
    race = 'u' #Variable for Race of Player
    cclass = 'u' #Variable for the Class of Player Character
    hp = 50 #Base Health for all Chars
    mana = 25 #Base Mana for all Chars
    stamina = 25 #Base Stamina for all Chars
    stre = 5 #Base Strength for all Chars
    agl = 5 #Base Agility for all Chars
    inte = 5 #Base Intelligence for all Chars
    cour = 5 #Base Courage for all Chars
    dex = 5 #Base Dexterity for all Chars
    conc = 5 #Base Concentration for all Chars
    item = 'u' #Player's Weapon of Choice
    profs=[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    #profs[0] = blades
    #profs[1]= blunt
    #profs[2]= small
    #profs[3]= small/medium shields
    #profs[4]= two handed
    #profs[5]= dual wield
    #profs[6]= kiteshield
    #profs[7]= small dualwield
    #profs[8]= bow
    #profs[9]= small shields
    #profs[10]= spears
    #profs[11]= javelins
    #profs[12]= throwables
    #profs[13]= staffs
    #profs[14]= healing
    #profs[15]= dark majyyks
    dispBox=pygame.Surface((320,240))
    running=True
    name=GraphicInput.ask(screen,'Enter Name: ',(300,300))
    if name == 'FALSE':
        running=False
        return None
    else:
        pass
    pygame.display.update()
    screen.fill((0,0,0))
    while running:
        race=GraphicInput.ask(screen,'Choose any of the following: Human, Elf, Drow, Dwarf, Halfling or Draconian ',(300,300))
        pygame.display.update()
        race = race.lower()
        print race
        if race=='false':
            running=False
            return None
        if race == 'human':
            hp = hp + 5
            mana = mana + 5
            stamina = stamina + 15
            stre = stre + 1
            agl = agl
            inte = inte
            cour = cour + 1
            dex = dex
            conc = conc
            break
        elif race == 'elf':
            hp = hp - 5
            mana = mana + 10
            stamina = stamina
            stre = stre - 1
            agl = agl + 1
            inte = inte + 2
            cour = cour - 1
            dex = dex + 2
            conc = conc + 1
            break
        elif race == 'drow':
            hp = hp - 5
            mana = mana + 10
            stamina = stamina
            stre = stre - 1
            agl = agl + 2
            inte = inte + 1
            cour = cour
            dex = dex + 1
            conc = conc + 1
            break
        elif race == 'dwarf':
            hp = hp + 10
            mana = mana - 5
            stamina = stamina + 10
            stre = stre + 2
            agl = agl
            inte = inte - 1
            cour = cour + 1
            dex = dex
            conc = conc
            profaxes = True
            break
        elif race == 'halfling':
            hp = hp - 10
            mana = mana
            stamina = stamina
            stre = stre - 1
            agl = agl + 1
            inte = inte
            cour = cour - 1
            dex = dex + 1
            conc = conc
            break
        elif race == 'draconian':
            hp = hp + 15
            mana = mana - 10
            stamina = stamina -5
            stre = stre + 1
            agl = agl
            inte = inte - 1
            cour = cour
            dex = dex - 1
            conc = conc + 1
            break
        else:
            screen.fill((0,0,0))
    screen.fill((0,0,0))

    while running:
        cclass=GraphicInput.ask(screen,'Choose any of the following: Swordsman, Berserker, Knight, Scout, Hunter, Ranger, Skirmisher, Priest, Sorcerer, or Mage',(300,300))
        pygame.display.update()
        cclass = cclass.lower()
        if cclass=='false':
            running=False
            return None
            break
        if cclass == 'swordsman':
            hp = hp + 20
            mana = mana - 10
            stamina = stamina + 5
            stre = stre + 2
            agl = agl + 1
            inte = inte - 1
            cour = cour + 1
            dex = dex
            conc = conc - 1
            profs[0] = True
            profs[1]  = True
            profs[2] = True
            profs[3] = True
            break
        elif cclass == 'berserker':
            hp = hp + 10
            mana = mana - 10
            stamina = stamina + 10
            stre = stre + 3
            agl = agl + 2
            inte = inte - 2
            cour = cour + 2
            dex = dex - 1
            conc = conc - 1
            profs[0] = True
            profs[1] = True
            profs[4] = True
            profs[5] = True
            break
        elif cclass == 'knight':
            hp = hp + 30
            mana = mana
            stamina = stamina
            stre = stre + 4
            agl = agl - 1
            inte = inte
            cour = cour + 2
            dex = dex - 2
            conc = conc - 1
            profs[0] = True
            profs[1] = True
            profs[4] = True
            profs[6] = True
            break
        elif cclass == 'scout':
            hp = hp
            mana = mana
            stamina = stamina + 10
            stre = stre + 3
            agl = agl + 2
            inte = inte + 1
            cour = cour - 1
            dex = dex + 1
            conc = conc - 1
            profs[2] = True
            profs[7] = True
            break
        elif cclass == 'hunter':
            hp = hp
            mana = mana
            stamina = stamina + 20
            stre = stre - 1
            agl = agl + 2
            inte = inte
            cour = cour - 1
            dex = dex + 2
            conc = conc
            profs[8] = True
            profs[0] = True
            profs[1] = True
            break
        elif cclass == 'ranger':
            hp = hp - 10
            mana = mana
            stamina = stamina + 30
            stre = stre + 1
            agl = agl + 2
            inte = inte
            cour = cour - 1
            dex = dex + 2
            conc = conc + 1
            profs[2] = True
            profs[8] = True
            break
        elif cclass == 'skirmisher':
            hp = hp + 5
            mana = mana
            stamina = stamina + 15
            stre = stre
            agl = agl + 2
            inte = inte
            cour = cour - 1
            dex = dex + 1
            conc = conc
            profs[9] = True
            profs[0] = True
            profs[1] = True
            profs[10] = True
            profs[11] = True
            profs[12] = True
            break
        elif cclass == 'priest':
            hp = hp - 5
            mana = mana + 20
            stamina = stamina - 5
            stre = stre - 2
            agl = agl - 1
            inte = inte + 3
            cour = cour - 1
            dex = dex - 1
            conc = conc + 2
            profs[13] = True
            profs[14] = True
            break
        elif cclass == 'sorcerer':
            hp = hp
            mana = mana + 30
            stamina = stamina - 10
            stre = stre - 3
            agl = agl - 2
            inte = inte + 4
            cour = cour - 1
            dex = dex + 1
            conc = conc + 3
            profs[13] = True
            profs[2] = True
            profs[15] = True
            break
        elif cclass == 'mage':
            hp = hp + 5
            mana = mana + 30
            stamina = stamina
            stre = stre - 1
            agl = agl - 2
            inte = inte + 3
            cour = cour
            dex = dex
            conc = conc + 2
            profs[13] = True
            break
        else:
            screen.fill((0,0,0))
    screen.fill((0,0,0))
    while running:
        xi,yi=screen.get_size()
        event=pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or pygame.K_RETURN:
                break
        z=(yi/6)-(yi/7)
        GraphicInput.display_message(screen,'name = '+name+'\n\n',(0,0))
        GraphicInput.display_message(screen,'hp = '+str(hp)+'\n\n',(0,(z)*1))
        GraphicInput.display_message(screen,'mana = '+str(mana)+'\n\n',(0,((z)*2)))
        GraphicInput.display_message(screen,'stamina = '+str(stamina)+'\n\n',(0,((z)*3)))
        GraphicInput.display_message(screen,'strength = '+str(stre)+'\n\n',(0,((z)*4)))
        GraphicInput.display_message(screen,'agility = '+str(agl)+'\n\n',(0,((z))*5))
        GraphicInput.display_message(screen,'intelligence = '+str(inte)+'\n\n',(0,(z)*6))
        GraphicInput.display_message(screen,'courage = '+str(cour)+'\n\n',(0,((z)*7)))
        GraphicInput.display_message(screen,'dexterity = '+str(dex)+'\n\n',(0,((z)*8)))
        GraphicInput.display_message(screen,'concentration = '+str(conc)+'\n\n',(0,(z)*9))
        GraphicInput.display_message(screen,'race = '+race+'\n\n',(0,(z)*10))
        GraphicInput.display_message(screen,'class = '+cclass+'\n\n',(0,(z)*11))
    pathname = os.path.abspath(os.getcwd()+"/%s/" % name)
    if not os.path.exists(pathname):
        os.makedirs(pathname)
    f=open(pathname+"\stats.wagh",'w')
    f.write(name)
    f.write('\n')
    f.write(race)
    f.write('\n')
    f.write(cclass)
    f.write('\n')
    f.write(str(hp))
    f.write('\n')
    f.write(str(mana))
    f.write('\n')
    f.write(str(stamina))
    f.write('\n')
    f.write(str(stre))
    f.write('\n')
    f.write(str(agl))
    f.write('\n')
    f.write(str(inte))
    f.write('\n')
    f.write(str(cour))
    f.write('\n')
    f.write(str(dex))
    f.write('\n')
    f.write(str(conc))
    f.close()
    f=open(pathname+"/profs.wagh",'w')
    profstr=['']*16
    counter=0
    for x in profs:
        profstr[counter]=str(x)+'\n'
        counter+=1
    f.writelines(profstr)
    f.write("\n"+'profs[0] = blades'+'\n'+'profs[1]= blunt'+'\n'+'profs[2]= small'+'\n'+'profs[3]= small/medium shields'+'\n'+'profs[4]= two handed'+'\n'+'profs[5]= dual wield'+'\n'+
    'profs[6]= kiteshield'+'\n'+'profs[7]= small dualwield'+'\n'+'profs[8]= bow'+'\n'+'profs[9]= small shields'+'\n'+'profs[10]= spears'+'\n'+'profs[11]= javelins'+'\n'+ 'profs[12]= throwables'+
    '\n'+'profs[13]= staffs'+'\n'+'profs[14]= healing'+'\n'+'profs[15]= dark majyyks'+'\n'+'more blood for the blood god')
    f.close()
