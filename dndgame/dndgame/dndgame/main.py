'''
Created on May 12, 2013

@author: Brad
'''

hp = 50 #Base Health for All Chars
mana = 25 #Base Mana for all Chars
stamina = 25 #Base Stamina for Chars
stre = 5
agl = 5
inte = 5
cour = 5
dex = 5
conc = 5
item = 5
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
print hp,',',mana,',',stamina,',',stre,',',agl,',',inte,',',cour,',',dex,',',conc,'.',