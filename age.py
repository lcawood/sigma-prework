from datetime import date
 
 # function input should have form date(YYYY, M, D)
def age_calculator(DoB):
    today = date.today()
    age = today.year - DoB.year - ((today.month, today.day) < (DoB.month, DoB.day))
    return str(age) + " years"


print(age_calculator(date(2001, 4, 19)))