__author__ = 'Brad'
import enemycreation,os
def enemycreateGroup(numberOfEnemies,typeOfEnemy):
    #Type of Enemy is Name_Race_Type ex. Ian_Human_Swordsman
    aiDict={}
    for i in (0,numberOfEnemies):
        aiDict[1]=enemycreation.enemycreation(str(i),'orc','swordsman')
        return aiDict