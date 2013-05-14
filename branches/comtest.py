import random
attacker = ''
defender = ''
atkdmgmod = 1
defdmgmod = 1
randmult = random.randint(2,4)
randmult = int(randmult)
attacker = raw_input('The name of the offensive combatant: ')
defender = raw_input('\nThe name of the defensive combatant: ')
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
#array[12]=hpleft
dead=False
attack=[]
defend=[]
while dead==False:
    attack=[]
    defend=[]
    a = open(attacker)
    attack = a.readlines()
    d = open(defender)
    defend = d.readlines()

    dead=False
    
    if attack[2] in ['swordsman'+'\n','berserker'+'\n','knight'+'\n','scout'+'\n']:
        atkdmgmod = int(attack[6])
    elif attack[2] in ['hunter'+'\n','ranger'+'\n','skirmisher'+'\n']:
        atkdmgmod = int(attack[7])
    elif attack[2] in ['priest'+'\n','sorcerer'+'\n','mage'+'\n']:
        atkdmgmod = int(attack[8])
    

    if defend[2] in ['swordsman\n','berserker\n','knight\n','scout\n']:
        defdmgmod = int(defend[6])
    elif defend[2] in ['hunter\n','ranger\n','skirmisher\n']:
        defdmgmod = int(defend[7])
    elif defend[2] in ['priest\n','sorcerer\n','mage\n']:
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
        defend[12]=defhpleft
        d.writelines(defend[0],defend[1],defend[2],defend[3],defend[4],defend[5],defend[6],defend[7],defend[8],defend[9],defend[10],defend[11],defend[12],)
        d.close
        a.close
        
        print '\nThe defending', defend[2], 'was hit for', atkdmg, 'damage, and has', defhpleft, 'health left!'
    if defhpleft<=0:
        print "The attacker ",attack[0]-'\n',' killed the defender ',defend[0]-'\n',
        dead=True
    else:
        attack,defend=defend,attack
