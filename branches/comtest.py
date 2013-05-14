import random
attacker = ''
defender = ''
atkdmgtype = 1
atkdmgmod = 1
defdmgtype = 1
defdmgmod = 1
randmult = random.randint(2,4)
randmult = int(randmult)
atkstre = 1
atkagl = 1
atkinte = 1
atkcour = 1
atkdex = 1
atkconc = 1
defhp = 1
defstre = 1
defagl = 1
definte = 1
defcour = 1
defdex = 1
defconc = 1
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


if atkclass == ('swordsman\n' or 'berserker\n' or 'knight\n' or 'scout\n') :
    atkdmgmod = atkstre
elif atkclass == ('hunter\n' or 'ranger\n' or 'skirmisher\n'):
    atkdmgmod = atkagl
elif atkclass == ('priest\n' or 'sorcerer\n' or 'mage\n'):
    atkdmgmod = atkinte

if defclass == ('swordsman\n' or 'berserker\n' or 'knight\n' or 'scout\n'):
    defdmgmod = defstre
elif defclass == ('hunter\n' or 'ranger\n' or 'skirmisher\n'):
    defdmgmod = defagl
elif defclass == ('priest\n' or 'sorcerer\n' or 'mage\n'):
    defdmgmod = definte


dodge = random.randrange(0,100,1)
if defagl >= dodge:
    print '\nThe defending', defclass, 'dodged completely!\n'

elif 3 * defagl >= dodge:
    atkdmg = (atkdmgmod * randmult)/2
    print '\nThe defending', defclass, 'partially dodged, and only suffered', atkdmg,'damage!\n'

else:
    atkdmg = atkdmgmod * randmult
    defhpleft = defhp - atkdmg
    print '\nThe defending', defclass, 'was hit for', atkdmg, 'damage, and has', defhpleft, 'health left!'


print randmult, '= random attack multiplier'
print atkinte, '= attacker intelligence'
print atkstre, '= attacker strength'
print atkdmgmod, '= atkdmgmod'
print atkclass, ' = Class'
print atkdmg,'= total damage'
