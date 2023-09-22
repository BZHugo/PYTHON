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
    ldate=liste(date)
    day=str(ldate[0])+str(ldate[1])
    month=stre(ldate[3])+str(ldate[4])
    return (day != nday(month))

