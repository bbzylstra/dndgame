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
name = raw_input("Enter your character's name:\n")
race = raw_input('Enter race.\n(Choose any of the following: Human, Elf, Drow, Dwarf, Halfling or Draconian)\n')
cclass = raw_input('Enter class.\n(Choose any of the following: Swordsman, Berserker, Knight, Scout, Hunter, Ranger, Skirmisher, Priest, Sorcerer, or Mage)\n')
race.lower()
cclass.lower()
if race == 'human':
    hp = hp + 5
    mana = mana
    stamina = stamina + 15
    stre = stre + 1
    agl = agl
    inte = inte
    cour = cour + 1
    dex = dex
    conc = conc
if race == 'elf':
    hp = hp - 5
    mana = mana + 10
    stamina = stamina
    stre = stre - 1
    agl = agl + 1
    inte = inte + 2
    cour = cour - 1
    dex = dex + 2
    conc = conc + 1
if race == 'drow':
    hp = hp - 5
    mana = mana + 10
    stamina = stamina
    stre = stre - 1
    agl = agl + 2
    inte = inte + 1
    cour = cour
    dex = dex + 1
    conc = conc + 1
if race == 'dwarf':
    hp = hp + 10
    mana = mana - 5
    stamina = stamina + 10
    stre = stre + 2
    agl = agl
    inte = inte - 1
    cour = cour + 1
    dex = dex
    conc = conc
if race == 'halfling':
    hp = hp - 10
    mana = mana
    stamina = stamina
    stre = stre - 1
    agl = agl + 1
    inte = inte
    cour = cour - 1
    dex = dex + 1
    conc = conc
if race == 'draconian':
    hp = hp + 15
    mana = mana - 10
    stamina = stamina -5
    stre = stre + 1
    agl = agl
    inte = inte - 1
    cour = cour
    dex = dex - 1
    conc = conc + 1
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
if cclass == 'berserker':
    hp = hp + 10
    mana = mana - 10
    stamina = stamina + 10
    stre = stre + 3
    agl = agl + 2
    inte = inte - 2
    cour = cour + 2
    dex = dex - 1
    conc = conc - 1
if cclass == 'knight':
    hp = hp + 30
    mana = mana
    stamina = stamina
    stre = stre + 3
    agl = agl - 1
    inte = inte
    cour = cour + 2
    dex = dex - 2
    conc = conc - 1
if cclass == 'scout':
    hp = hp
    mana = mana
    stamina = stamina + 10
    stre = stre + 3
    agl = agl
    inte = inte - 1
    cour = cour
    dex = dex + 1
    conc = conc - 1
if cclass == 'hunter':
    hp = hp
    mana = mana
    stamina = stamina + 20
    stre = stre - 1
    agl = agl + 2
    inte = inte
    cour = cour - 1
    dex = dex + 2
    conc = conc
if cclass == 'ranger':
    hp = hp - 15
    mana = mana
    stamina = stamina + 30
    stre = stre + 1
    agl = agl + 2
    inte = inte
    cour = cour - 1
    dex = dex + 2
    conc = conc + 1
if cclass == 'skirmisher':
    hp = hp + 5
    mana = mana
    stamina = stamina + 15
    stre = stre 
    agl = agl + 1
    inte = inte
    cour = cour - 1
    dex = dex + 1
    conc = conc
if cclass == 'priest':
    hp = hp - 5
    mana = mana + 20
    stamina = stamina - 5
    stre = stre - 2
    agl = agl - 1
    inte = inte + 3
    cour = cour - 1
    dex = dex - 1
    conc = conc + 2
if cclass == 'sorcerer':
    hp = hp + 5
    mana = mana + 30
    stamina = stamina - 10
    stre = stre - 3
    agl = agl - 2
    inte = inte + 4
    cour = cour - 1
    dex = dex + 1
    conc = conc + 3
if cclass == 'mage':
    hp = hp 
    mana = mana + 30
    stamina = stamina
    stre = stre - 1
    agl = agl - 2
    inte = inte + 3
    cour = cour
    dex = dex
    conc = conc + 2
print 'hp =',hp, '\n mana =',mana, '\n stamina =',stamina, '\n  strength =',stre, '\n agility =',agl, '\n intelligence =',inte, '\n courage =',cour, '\n dexterity =',dex, '\n concentration =',conc,
