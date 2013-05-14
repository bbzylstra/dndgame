import random
attacker = ''
defender = ''
atkdmgmod = 1
defdmgmod = 1
randmult = random.randint(2,4)
randmult = int(randmult)
attacker = raw_input('The name of the offensive combatant: ')
defender = raw_input('\nThe name of the defensive combatant: ')
attack=[]
defend=[]
f = open(attacker)
attack = f.readlines()
f.close()
f = open(defender)
defend = f.readlines()
f.close()

if attack[2] == ('swordsman\n' or 'berserker\n' or 'knight\n' or 'scout\n') :
    atkdmgmod = int(attack[6])
elif attack[2] == ('hunter\n' or 'ranger\n' or 'skirmisher\n'):
    atkdmgmod = int(attack[7])
elif attack[2] == ('priest\n' or 'sorcerer\n' or 'mage\n'):
    atkdmgmod = int(attack[8])

if defend[2] == ('swordsman\n' or 'berserker\n' or 'knight\n' or 'scout\n'):
    defdmgmod = int(defend[6])
elif defend[2] == ('hunter\n' or 'ranger\n' or 'skirmisher\n'):
    defdmgmod = int(defend[7])
elif defend[2] == ('priest\n' or 'sorcerer\n' or 'mage\n'):
    defdmgmod = int(defend[8])

dodge = random.randrange(0,100,1)
if int(defend[8]) >= dodge:
    print '\nThe defending', defend[2], 'dodged completely!\n'

elif 3 * int(defend[8]) >= dodge:
    atkdmg = (atkdmgmod * randmult)/2
    print '\nThe defending', str(defend[2]), 'partially dodged, and only suffered', atkdmg,'damage!\n'

else:
    atkdmg = atkdmgmod * randmult
    defhpleft = int(defend[3]) - int(atkdmg)
    print '\nThe defending', defend[2], 'was hit for', atkdmg, 'damage, and has', defhpleft, 'health left!'

