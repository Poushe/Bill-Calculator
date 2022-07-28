print('welcome to the bill calculator')
total_bill=input('what was the total bill? ')
percen=input('what percentage tip whould you like to give? 10, 12 or 15? ')
total_people=input('How many people to split the bill? ')
res=float(total_bill)/int(total_people);
per_res=res*(float(percen)/100)
res1=round(res+per_res,2)
print(res1)
