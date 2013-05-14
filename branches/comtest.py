import random
attacker = ''
defender = ''
atkdmgmod = 1
defdmgmod = 1
randmult = random.randint(2,4)
randmult = int(randmult)
attacker = raw_input('The name of the offensive combatant: ')
defender = raw_input('\nThe name of the defensive combatant: ')
distance = raw_input('\nThe distance from which the combatants are fighting (1 for melee): ')
attack=[]
defend=[]
f = open(attacker)
attack = f.readlines()
f.close()
f = open(defender)
defend = f.readlines()
f.close()
#array[0]=name
#array[1]=race
#array[2]=cclass
#array[3]=hp
#array[4]=mana
#array[5]=stamina
#array[6]=stre
#array[7]=agl
#array[8]=inte
#array[9]=cour
#array[10]=dex
#array[11]=conc

if attack[2] in ['swordsman'+'\n','berserker'+'\n','knight'+'\n','scout'+'\n']:
    atkdmgmod = int(attack[6])
    atkdmgtype = 'melee'
elif attack[2] in ['hunter'+'\n','ranger'+'\n','skirmisher'+'\n']:
    atkdmgmod = int(attack[7])
    atkdmgtype = 'ranged'
elif attack[2] in ['priest'+'\n','sorcerer'+'\n','mage'+'\n']:
    atkdmgmod = int(attack[8])
    atkdmgtype = 'magic'

#Determining the defender's armor type [will be determined by equipment later]
if defend[2] in ['knight'+'\n']:
    armor = 'heavy'
elif defend[2] in ['swordsman'+'\n','berserker'+'\n']:
    armor = 'medium'
elif defend[2] in ['hunter'+'\n','ranger'+'\n','skirmisher'+'\n','priest'+'\n','sorcerer'+'\n','mage'+'\n','scout'+'\n']:
    armor = 'light'

#Determining defence stats to use and the defender's attack type
if defend[2] in ['swordsman\n','berserker\n','knight\n','scout\n']:
    defdmgmod = int(defend[7])
    defdmgtype = 'melee'
elif defend[2] in ['hunter\n','ranger\n','skirmisher\n']:
    defdmgmod = int(defend[10])
    defdmgtype = 'ranged'
elif defend[2] in ['priest\n','sorcerer\n','mage\n']:
    defdmgmod = int(defend[11])
    defdmgtype = 'magic'

#Mages defend against mages, a battle of wills muahaha
if atkdmgtype == 'magic' and defdmgtype == 'magic':
    atkdmgmod = int(attack[8]) - int(defend[8])

#Mages can reduce damage based on their concentration... just a little bit though.
if atkdmgtype == 'melee' and defdmgtype == 'magic':
    atkdmgmod = int(attack[6]) - (int(defend[11]) / 3 )

#Same as before.
if atkdmgtype == 'ranged' and defdmgtype == 'magic':
    atkdmgmod = int(attack[7]) - (int(defend[11]) / 3 )

#Damage reduction for generic medium armor at the moment (only does 80%)
if armor == 'medium':
    atkdmgmod = atkdmgmod * .8

#Defending ranged units use their dexterity to reduce the damage they take from projectiles.
if atkdmgtype == 'ranged' and defdmgtype == 'ranged':
    atkdmgmod = atkdmgmod - ( defdmgmod / 3 )

#Heavy armor reduces melee damage by about 30%
if atkdmgtype == 'melee' and armor == 'heavy':
    atkdmgmod = atkdmgmod / 1.4

#Heavy armor reduces ranged damage by 50%
if atkdmgtype == 'ranged' and armor == 'heavy':
    atkdmgmod = atkdmgmod / 2

#Heavy armor conducts magic, doubling damage >:D
if armor == 'heavy' and atkdmgtype == 'magic':
    atkdmgmod = atkdmgmod * 2

#Damage calculations, watch out.
dodge = random.randrange(0,100,1)
crit = random.randrange(0,100,1)
if atkdmgtype == 'melee' and int(distance) >= 2:#lol theyre out of range
    atkdmg = 0
    defhpleft = int(defend[3]) - int(atkdmg)
    print '\nThe defending', defend[2], 'was out of range, you noob!'#lmoa nubs
else:
    while True:
        if atkdmgtype == 'ranged':
            if int(distance) <= int(attack[6]):
                atkdmg = atkdmg * (1 + (int(attack[6])) / (int(distance)))
                if int(defend[8]) >= (dodge / 1.5):
                    defhpleft = int(defend[3]) - int(atkdmg)
                    print '\nThe defending', str(defend[2]), 'dodged completely, and still has ',defhpleft,' left!\n'
                    break

                elif 1.5 * int(defend[8]) >= dodge:
                    atkdmg = (atkdmgmod * randmult)/2
                    defhpleft = int(defend[3]) - int(atkdmg)
                    print '\nThe defending', str(defend[2]), 'partially dodged, and only suffered', atkdmg,'damage, and has ',defhpleft,' left!\n'
                    break

                else:
                    if int(attack[10] >= crit:
                        atkdmg = atkdmgmod * randmult * 2
                        defhpleft = int(defend[3]) - int(atkdmg)
                        print '\nThe defending', str(defend[2]), 'suffered a crit for', atkdmg, 'damage, and has', defhpleft, 'health left!'
                        break

                    else:
                        atkdmg = atkdmgmod * randmult
                        defhpleft = int(defend[3]) - int(atkdmg)
                        print '\nThe defending', str(defend[2]), 'was hit for', atkdmg, 'damage, and has', defhpleft, 'health left!'
                        break

            else:
                atkdmg = 0
                defhpleft = int(defend[3]) - int(atkdmg)
                print '\nThe defending', defend[2], 'was out of range, you noob!'#lmoa nubs
                break

        elif atkdmgtype == 'melee':
            if int(defend[8]) >= dodge:
                defhpleft = int(defend[3]) - int(atkdmg)
                print '\nThe defending', defend[2], 'dodged completely, and still has ',defhpleft,' left!\n'
                break

            elif 3 * int(defend[8]) >= dodge:
                atkdmg = (atkdmgmod * randmult)/2
                defhpleft = int(defend[3]) - int(atkdmg)
                print '\nThe defending', str(defend[2]), 'partially dodged, and only suffered', atkdmg,'damage, and has ',defhpleft,' left!\n'
                break

            else:
                if int(attack[10] >= crit:
                    atkdmg = atkdmgmod * randmult * 2
                    defhpleft = int(defend[3]) - int(atkdmg)
                    print '\nThe defending', str(defend[2]), 'suffered a crit for', atkdmg, 'damage, and has', defhpleft, 'health left!'
                    break

                else:
                    atkdmg = atkdmgmod * randmult
                    defhpleft = int(defend[3]) - int(atkdmg)
                    print '\nThe defending', str(defend[2]), 'was hit for', atkdmg, 'damage, and has', defhpleft, 'health left!'
                    break

        if atkdmgtype == 'magic':
            if int(distance) <= 8:
                if int(defend[8]) >= dodge:
                    defhpleft = int(defend[3]) - int(atkdmg)
                    print '\nThe defending', str(defend[2]), 'dodged completely, and still has ',defhpleft,' left!\n'
                    break
                
                elif int(defend[8]) >= dodge:
                    atkdmg = (atkdmgmod * randmult)/2
                    defhpleft = int(defend[3]) - int(atkdmg)
                    print '\nThe defending', str(defend[2]), 'partially dodged, and only suffered', atkdmg,'damage, and has ',defhpleft,' left!\n'
                    break

                else:
                    if int(attack[10] >= crit:
                        atkdmg = atkdmgmod * randmult * 2
                        defhpleft = int(defend[3]) - int(atkdmg)
                        print '\nThe defending', str(defend[2]), 'suffered a crit for', atkdmg, 'damage, and has', defhpleft, 'health left!'
                        break

                    else:
                        atkdmg = atkdmgmod * randmult
                        defhpleft = int(defend[3]) - int(atkdmg)
                        print '\nThe defending', str(defend[2]), 'was hit for', atkdmg, 'damage, and has', defhpleft, 'health left!'
                        break
            else:
                atkdmg = 0
                defhpleft = int(defend[3]) - int(atkdmg)
                print '\nThe defending', defend[2], 'was out of range, you noob!'#lmoa nubs
                break

