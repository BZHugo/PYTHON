""" 
tp1-22/09/2023
hugo prigent

"""

#exercice1:

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
        if jour>28:
            return False


    if mois>12:             #mois impossible
        return False
    if jour>31:             #jour impossible
        return False
    if jour>ndays(mois):    #jour d'un mois impossible
        return False 
    
    

