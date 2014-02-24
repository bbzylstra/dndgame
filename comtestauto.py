import random,pickle
attacker = ''
defender = ''
atkdmgmod = 1
defdmgmod = 1
randmult = random.randint(2,4)
randmult = int(randmult)
defhpleft=0
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
a = open(attacker)
attack = a.readlines()
d = open(defender)
defend = d.readlines()
a.close()
d.close()
defhpleft=0
while dead==False:

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
        if defhpleft !=0:
            defhpleft = int(defend[12])
        else:
            defhpleft = int(defend[3])
        print '\nThe defending', defend[2], 'dodged completely!\n'

    elif 3 * int(defend[8]) >= dodge:
        atkdmg = (atkdmgmod * randmult)/2
        if defhpleft !=0:
            defhpleft = int(defend[12]) - int(atkdmg)
        else:
            defhpleft = int(defend[3]) - int(atkdmg)
        print '\nThe defending', str(defend[2]), 'partially dodged, and only suffered', atkdmg,'damage and has', defhpleft, 'health left!'

    else:
        atkdmg = atkdmgmod * randmult
        if defhpleft !=0:
            defhpleft = int(defend[12]) - int(atkdmg)
        else:
            defhpleft = int(defend[3]) - int(atkdmg)
        defend[12]=str(defhpleft)
        #for item in defend:
           #d.write("%s" % item)
        d = open(defender,'w')
        d.writelines(defend)
        d.close()
        print '\nThe defending', defend[2], 'was hit for', atkdmg, 'damage, and has', defhpleft, 'health left!'
    if defhpleft<=0:
        print "The attacker ",attack[0].replace('\n',''),' killed the defender ',defend[0].replace('\n',''),
        dead=True
        attack[12]=attack[3]
        defend[12]=defend[3]
        a = open(attacker,'w')
        a.writelines(attack)
        d = open(defender,'w')
        d.writelines(defend)
        a.close()
        d.close()
    else:
        holder=defend
        defend=attack
        attack=holder
        attacker,defender=defender,attacker