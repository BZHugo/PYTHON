""" 
tp1-22/09/2023
hugo prigent

"""

""" exercice1: """

def biss(x):
    C1=False
    if x%400==0:
        C1=True
    return(C1)

def ndays(x):
    L30=[4,6,9,11]
    L31=[1,3,5,7,8,10,12]
    if x in L30:
        return(30)
    else:
        return(31)

def valid(jour,mois,annee): #format d'entre de la date
    
    if biss(annee):         #cas des annee biss 
        if mois==2 and jour>29:
            return False
    if not biss(annee):
        if mois==2 and jour>28:
            return False


    if mois>12:             #mois impossible
        return False
    if jour>31:             #jour impossible
        return False
    if jour>ndays(mois):    #jour d'un mois impossible
        return False 
    
    else:
        return True
    

""" exercice 2"""

def mesImpots(revenu):
    
    
    #on rentre les paramètres pour les calculs:
    T2=[10226,26070]
    T3=[26071,74545]
    T4=[74546,160336]
    T5=160336
    tx2=0.11
    tx3=0.3
    tx4=0.41
    tx5=0.45
    if revenu <=10225 :return (0)
    if revenu <=T2[1] :return round ((revenu-T2[0])*tx2,1)
    if revenu <=T3[1] :return round((revenu-T3[0])*tx3 +(T2[1]-T2[0])*tx2,1)
    if revenu <=T4[1] :return round ((revenu -T4[0])*tx4 +(T3[1]-T3[0])*tx3 +(T2[1]-T2[0])*tx2,1 ) 
    if revenu <=T5    :return round ((revenu-T5)*tx5 + (T4[1]-revenu)*tx4 +(T3[1]-T3[0])*tx3 +(T2[1]-T2[0])*tx2,1 )





