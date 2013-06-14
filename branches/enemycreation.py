import os
class enemycreation(object):
    def __init__(self,name,race,cclass):
        object.__init__()
        self.name=name
        self.race=race
        self.cclass=cclass
        self.name = 'unknown' #Variable for Player Name
        self.race = 'u' #Variable for Race of Player
        self.cclass = 'u' #Variable for the Class of Player Character
        self.hp = 50 #Base Health for all Chars
        self.mana = 25 #Base Mana for all Chars
        self.stamina = 25 #Base Stamina for all Chars
        self.stre = 5 #Base Strength for all Chars
        self.agl = 5 #Base Agility for all Chars
        self.inte = 5 #Base Intelligence for all Chars
        self.cour = 5 #Base Courage for all Chars
        self.dex = 5 #Base Dexterity for all Chars
        self.conc = 5 #Base Concentration for all Chars
        self.item = 'u' #Player's Weapon of Choice
        self.profblades = False
        self.profblunt = False
        self.profsmall = False
        self.profsmshields = False
        self.prof2handed = False
        self.dualwield = False
        self.profkiteshield = False
        self.smalldualwield = False
        self.profbows = False
        self.profsshields = False
        self.profspears = False
        self.profjavelins = False
        self.profthrowables = False
        self.profstaff = False
        self.profhealing = False
        self.profdarkmajyyks = False
        def create(self):
            while True:
                if race == 'human':
                    self.hp = self.hp + 5
                    self.mana = self.mana + 5
                    self.stamina = self.stamina + 15
                    self.stre = self.stre + 1
                    self.agl = self.agl
                    self.inte = self.inte
                    self.cour = self.cour + 1
                    self.dex = self.dex
                    self.conc = self.conc
                    break
                elif race == 'elf':
                    self.hp = self.hp - 5
                    self.mana = self.mana + 10
                    self.stamina = self.stamina
                    self.stre = self.stre - 1
                    self.agl = self.agl + 1
                    self.inte = self.inte + 2
                    self.cour = self.cour - 1
                    self.dex = self.dex + 2
                    self.conc = self.conc + 1
                    break
                elif race == 'drow':
                    self.hp = self.hp - 5
                    self.mana = self.mana + 10
                    self.stamina = self.stamina
                    self.stre = self.stre - 1
                    self.agl = self.agl + 2
                    self.inte = self.inte + 1
                    self.cour = self.cour
                    self.dex = self.dex + 1
                    self.conc = self.conc + 1
                    break
                elif race == 'dwarf':
                    self.hp = self.hp + 10
                    self.mana = self.mana - 5
                    self.stamina = self.stamina + 10
                    self.stre = self.stre + 2
                    self.agl = self.agl
                    self.inte = self.inte - 1
                    self.cour = self.cour + 1
                    self.dex = self.dex
                    self.conc = self.conc
                    self.profaxes = True
                    break
                elif race == 'halfling':
                    self.hp = self.hp - 10
                    self.mana = self.mana
                    self.stamina = self.stamina
                    self.stre = self.stre - 1
                    self.agl = self.agl + 1
                    self.inte = self.inte
                    self.cour = self.cour - 1
                    self.dex = self.dex + 1
                    self.conc = self.conc
                    break
                elif race == 'draconian':
                    self.hp = self.hp + 15
                    self.mana = self.mana - 10
                    self.stamina = self.stamina -5
                    self.stre = self.stre + 1
                    self.agl = self.agl
                    self.inte = self.inte - 1
                    self.cour = self.cour
                    self.dex = self.dex - 1
                    self.conc = self.conc + 1
                    break
                elif race == 'demon':
                    self.hp = self.hp + 50
                    self.mana = self.mana + 20
                    self.stamina = self.stamina + 10
                    self.stre = self.stre + 4
                    self.agl = self.agl - 1
                    self.inte = self.inte - 1
                    self.cour = self.cour
                    self.dex = self.dex - 1
                    self.conc = self.conc + 4
                    break
                elif race == 'dragon':
                    self.hp = self.hp + 450
                    self.mana = self.mana + 75
                    self.stamina = self.stamina + 75
                    self.stre = self.stre + 8
                    self.agl = self.agl + 2
                    self.inte = self.inte + 3
                    self.cour = self.cour + 10
                    self.dex = self.dex
                    self.conc = self.conc
                    break
                elif race == 'orc':
                    self.hp = self.hp
                    self.mana = self.mana - 10
                    self.stamina = self.stamina + 15
                    self.stre = self.stre + 2
                    self.agl = self.agl - 1
                    self.inte = self.inte - 3
                    self.cour = self.cour + 2
                    self.dex = self.dex - 3
                    self.conc = self.conc - 1
                    break
                elif race == 'goblin':
                    self.hp = self.hp - 20
                    self.mana = self.mana - 15
                    self.stamina = self.stamina - 5
                    self.stre = self.stre - 1
                    self.agl = self.agl
                    self.inte = self.inte - 1
                    self.cour = self.cour - 2
                    self.dex = self.dex - 1
                    self.conc = self.conc - 1
                    break
                else:
                    print "Not understood, please try again: "


            while True:
                if race in ['dragon','demon']:
                    break
                if cclass == 'swordsman':
                    self.hp = self.hp + 20
                    self.mana = self.mana - 10
                    self.stamina = self.stamina + 5
                    self.stre = self.stre + 2
                    self.agl = self.agl + 1
                    self.inte = self.inte - 1
                    self.cour = self.cour + 1
                    self.dex = self.dex
                    self.conc = self.conc - 1
                    self.profblades = True
                    self.profblunt = True
                    self.profsmall = True
                    self.profsmshields = True
                    break
                elif cclass == 'berserker':
                    self.hp = self.hp + 10
                    self.mana = self.mana - 10
                    self.stamina = self.stamina + 10
                    self.stre = self.stre + 3
                    self.agl = self.agl + 2
                    self.inte = self.inte - 2
                    self.cour = self.cour + 2
                    self.dex = self.dex - 1
                    self.conc = self.conc - 1
                    self.profblades = True
                    self.profblunt = True
                    self.prof2handed = True
                    self.dualwield = True
                    break
                elif cclass == 'knight':
                    self.hp = self.hp + 30
                    self.mana =self.mana
                    self.stamina = self.stamina
                    self.stre = self.stre + 4
                    self.agl = self.agl - 1
                    self.inte = self.inte
                    self.cour = self.cour + 2
                    self.dex = self.dex - 2
                    self.conc = self.conc - 1
                    self.profblades = True
                    self.profblunt = True
                    self.prof2handed = True
                    self.profkiteshield = True
                    break
                elif cclass == 'scout':
                    self.hp = self.hp
                    self.mana = self.mana
                    self.stamina = self.stamina + 10
                    self.stre = self.stre + 3
                    self.agl = self.agl + 2
                    self.inte = self.inte + 1
                    self.cour = self.cour - 1
                    self.dex = self.dex + 1
                    self.conc = self.conc - 1
                    self.profsmall = True
                    self.smalldualwield = True
                    break
                elif cclass == 'hunter':
                    self.hp = self.hp
                    self.mana = self.mana
                    self.stamina = self.stamina + 20
                    self.stre = self.stre - 1
                    self.agl = self.agl + 2
                    self.inte = self.inte
                    self.cour = self.cour - 1
                    self.dex = self.dex + 2
                    self.conc = self.conc
                    self.profbows = True
                    self.profblades = True
                    self.profblunt = True
                    break
                elif cclass == 'ranger':
                    self.hp = self.hp - 10
                    self.mana = self.mana
                    self.stamina = self.stamina + 30
                    self.stre = self.stre + 1
                    self.agl = self.agl + 2
                    self.inte = self.inte
                    self.cour = self.self.cour - 1
                    self.dex = self.dex + 2
                    self.conc = self.conc + 1
                    self.profsmall = True
                    self.profbows = True
                    break
                elif cclass == 'skirmisher':
                    self.hp = self.hp + 5
                    self.mana = self.mana
                    self.stamina = self.stamina + 15
                    self.stre = self.stre
                    self.agl = self.agl + 2
                    self.inte = self.inte
                    self.cour = self.cour - 1
                    self.dex = self.dex + 1
                    self.conc = self.conc
                    self.profsshields = True
                    self.profblades = True
                    self.profblunt = True
                    self.profspears = True
                    self.profjavelins = True
                    self.profthrowables = True
                    break
                elif cclass == 'priest':
                    self.hp = self.hp - 5
                    self.mana = self.mana + 20
                    self.stamina = self.stamina - 5
                    self.stre = self.stre - 2
                    self.agl = self.agl - 1
                    self.inte = self.inte + 3
                    self.cour = self.cour - 1
                    self.dex = self.dex - 1
                    self.conc = self.conc + 2
                    self.profstaff = True
                    self.profhealing = True
                    break
                elif cclass == 'sorcerer':
                    self.hp = self.hp
                    self.mana = self.mana + 30
                    self.stamina = self.stamina - 10
                    self.stre = self.stre - 3
                    self.agl = self.agl - 2
                    self.inte = self.inte + 4
                    self.cour = self.cour - 1
                    self.dex = self.dex + 1
                    self.conc = self.conc + 3
                    self.profstaff = True
                    self.profsmall = True
                    self.profdarkmajyyks = True
                    break
                elif cclass == 'mage':
                    self.hp = self.hp + 5
                    self.mana = self.mana + 30
                    self.stamina = self.stamina
                    self.stre = self.stre - 1
                    self.agl = self.agl - 2
                    self.inte = self.inte + 3
                    self.cour = self.cour
                    self.dex = self.dex
                    self.conc = self.conc + 2
                    self.profstaff = True
                    break
                else:
                    print "Not understood, please try again "

        print 'name =',self.name
        print '\nhp =',self.hp
        print '\nmana =',self.mana
        print '\nstamina =',self.stamina
        print '\nstrength =',self.stre
        print '\nagility =',self.agl
        print '\nintelligence =',self.inte
        print '\ncourage =',self.cour
        print '\ndexterity =',self.dex
        print '\nconcentration =',self.conc
        pathname = os.path.abspath(os.getcwd()+"/ai/%s/" % name)
        if not os.path.exists(pathname):
            os.makedirs(pathname)
        f=open(pathname+"/stats.wagh",'w')
        f.write(self.name)
        f.write('\n')
        f.write(self.race)
        f.write('\n')
        f.write(self.cclass)
        f.write('\n')
        f.write(str(self.hp))
        f.write('\n')
        f.write(str(self.mana))
        f.write('\n')
        f.write(str(self.stamina))
        f.write('\n')
        f.write(str(self.stre))
        f.write('\n')
        f.write(str(self.agl))
        f.write('\n')
        f.write(str(self.inte))
        f.write('\n')
        f.write(str(self.cour))
        f.write('\n')
        f.write(str(self.dex))
        f.write('\n')
        f.write(str(self.conc))
        f.close()