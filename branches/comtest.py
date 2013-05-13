import random
attacker = '?'
defender = '?'
atkdmgtype = 1
atkdmgmod = 1
defdmgtype = 1
defdmgmod = 1
randmult = random.randint(3,6)
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
if atkclass == 'swordsman':
    atkdmgtype = 'melee'
elif atkclass == 'berserker':
    atkdmgtype = 'melee'
elif atkclass == 'knight':
    atkdmgtype = 'melee'
elif atkclass == 'scout':
    atkdmgtype = 'melee'
elif atkclass == 'hunter':
    atkdmgtype = 'ranged'
elif atkclass == 'ranger':
    atkdmgtype = 'ranged'
elif atkclass == 'skirmisher':
    atkdmgtype = 'ranged'
elif atkclass == 'priest':
    atkdmgtype = 'magic'
elif atkclass == 'sorcerer':
    atkdmgtype = 'magic'
elif atkclass == 'mage':
    atkdmgtype = 'magic'
if atkdmgtype == 'melee':
    atkdmgmod = atkstre
elif atkdmgtype == 'ranged':
    atkdmgmod = atkagl
elif atkdmgtype == 'magic':
    atkdmgmod = atkinte
if defclass == 'swordsman':
    defdmgtype = 'melee'
elif defclass == 'berserker':
    defdmgtype = 'melee'
elif defclass == 'knight':
    defdmgtype = 'melee'
elif defclass == 'scout':
    defdmgtype = 'melee'
elif defclass == 'hunter':
    defdmgtype = 'ranged'
elif defclass == 'ranger':
    defdmgtype = 'ranged'
elif defclass == 'skirmisher':
    defdmgtype = 'ranged'
elif defclass == 'priest':
    defdmgtype = 'magic'
elif defclass == 'sorcerer':
    defdmgtype = 'magic'
elif defclass == 'mage':
    defdmgtype = 'magic'
    #Now set dmg type(int)
if defdmgtype == 'melee':
    defdmgmod = defstre
elif defdmgtype == 'ranged':
    defdmgmod = defagl
elif defdmgtype == 'magic':
    defdmgmod = definte
while True:
    dodge = random.randrange(0,51,1)
    if defagl >= dodge:
        print '\nThe defending', defclass, 'dodged completely!\n'
        break
    elif 3 * defagl >= dodge:
        atkdmg = atkdmgmod * randmult
        print '\nThe defending', defclass, 'partially dodged, and only suffered', atkdmg,'damage!\n'
        break
    else:
        atkdmg = atkdmgmod * randmult
        defhpleft = defhp - atkdmg
        print '\nThe defending', defclass, 'was hit for', atkdmg, 'damage, and has', defhpleft, 'health left!'
        break
