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
name = raw_input("Enter your character's name: ")

while True:
    race = raw_input('\nEnter race.\n(Choose any of the following: Human, Elf, Drow, Dwarf, Halfling or Draconian)\n: ')
    race = race.lower()

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
        print "Not understood, please try again: "


while True:
    cclass = raw_input('\nEnter class.\n(Choose any of the following: Swordsman, Berserker, Knight, Scout, Hunter, Ranger, Skirmisher, Priest, Sorcerer, or Mage)\n:')
    cclass = cclass.lower()
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
        profblades = True
        profblunt = True
        profsmall = True
        profsmshields = True
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
        profblades = True
        profblunt = True
        prof2handed = True
        dualwield = True
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
        profblades = True
        profblunt = True
        prof2handed = True
        profkiteshield = True
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
        profsmall = True
        smalldualwield = True
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
        profbows = True
        profblades = True
        profblunt = True
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
        profsmall = True
        profbows = True
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
        profsshields = True
        profblades = True
        profblunt = True
        profspears = True
        profjavelins = True
        profthrowables = True
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
        profstaff = True
        profhealing = True
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
        profstaff = True
        profsmall = True
        profdarkmajyyks = True
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
        profstaff = True
        break
    else:
        print "Not understood, please try again "

print 'name =',name
print '\nhp =',hp
print '\nmana =',mana
print '\nstamina =',stamina
print '\nstrength =',stre
print '\nagility =',agl
print '\nintelligence =',inte
print '\ncourage =',cour
print '\ndexterity =',dex
print '\nconcentration =',conc

f=open(name,'w')
f.write('name: ' + name)
f.write('\nrace: ' + race)
f.write('\ncclass: ' + cclass)
f.write('\nhp: ' + str(hp))
f.write('\nmana: ' + str(mana))
f.write('\nstamina: ' + str(stamina))
f.write('\nstre: ' + str(stre))
f.write('\nagl: ' + str(agl))
f.write('\ninte: ' + str(inte))
f.write('\ncour: ' + str(cour))
f.write('\ndex: ' + str(dex))
f.write('\nconc: ' + str(conc))
f.close()