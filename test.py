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

def valid(date):                #date format jj/mm/aaaa
    date=str(date[0])+str(date[1])
    month=str(date[3])+str(date[4])
    print(date,month)
        

