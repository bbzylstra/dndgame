import random
attacker = '?'
defender = '?'
atkdmgtype = 1
atkdmgmod = 1
defdmgtype = 1
defdmgmod = 1
randmult = random.randint(2,4)
randmult = int(randmult)
attacker = raw_input('The name of the offensive combatant: ')
defender = raw_input('\nThe name of the defensive combatant: ')
f=open(attacker,'r')
atkname = f.readline()
atkrace = f.readline()
atkclass = f.readline()
atkhp = f.readline()
atkmana = f.readline()
atkstamina = f.readline()
atkstre = f.readline()
atkagl = f.readline()
atkinte = f.readline()
atkcour = f.readline()
atkdex = f.readline()
atkconc = f.readline()
f.close()
f=open(defender,'r')
defname = f.readline()
defrace = f.readline()
defclass = f.readline()
defhp = f.readline()
defmana = f.readline()
defstamina = f.readline()
defstre = f.readline()
defagl = f.readline()
definte = f.readline()
defcour = f.readline()
defdex = f.readline()
defconc = f.readline()
f.close()
atkstre = int(atkstre)
atkagl = int(atkagl)
atkinte = int(atkinte)
atkcour = int(atkcour)
atkdex = int(atkdex)
atkconc = int(atkconc)
defhp = int(defhp)
defstre = int(defstre)
defagl = int(defagl)
definte = int(definte)
defcour = int(defcour)
defdex = int(defdex)
defconc = int(defconc)

while True:
    if atkclass == 'scout' or 'knight' or 'berserker' or 'swordsman':
        atkdmgtype = 'melee'
        break
    elif atkclass == 'skirmisher' or 'ranger' or 'hunter':
        atkdmgtype = 'ranged'
        break
    elif atkclass == 'mage' or 'sorcerer' or 'priest':
        atkdmgtype = 'magic'
        break

while True:
    if atkdmgtype == 'melee':
        atkdmgmod = atkstre
        break
    elif atkdmgtype == 'ranged':
        atkdmgmod = atkagl
        break
    elif atkdmgtype == 'magic':
        atkdmgmod = atkinte
        break

while True:
    if defclass == 'scout' or 'knight' or 'berserker' or 'swordsman':
        defdmgtype = 'melee'
        break
    elif defclass == 'skirmisher' or 'ranger' or 'hunter':
        defdmgtype = 'ranged'
        break
    elif defclass == 'sorcerer' or 'mage' or 'priest':
        defdmgtype = 'magic'
        break
while True:
    if defdmgtype == 'melee':
        defdmgmod = defstre
        break
    elif defdmgtype == 'ranged':
        defdmgmod = defagl
        break
    elif defdmgtype == 'magic':
        defdmgmod = definte
        break

while True:
    dodge = random.randrange(0,51,1)
    if defagl >= dodge:
        print '\nThe defending', defclass, 'dodged completely!\n'
        break
    elif 3 * defagl >= dodge:
        atkdmg = (atkdmgmod * randmult)/2
        print '\nThe defending', defclass, 'partially dodged, and only suffered', atkdmg,'damage!\n'
        break
    else:
        atkdmg = atkdmgmod * randmult
        defhpleft = defhp - atkdmg
        print '\nThe defending', defclass, 'was hit for', atkdmg, 'damage, and has', defhpleft, 'health left!'
        break
print atkdmgmod, '= attack damage modifier'
print '\n'
print randmult, '= random attack multiplier'
print atkinte, '= attacker intelligence'
print atkstre, '= attacker strength'
