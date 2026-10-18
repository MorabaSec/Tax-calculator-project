#income = float(input("Enter the annual income: "))


#if income < 1000000:
#	tax = income * 0.18 - 556.02
#else:
#	tax = (income - 1000000) * 0.32 + 14839.02

#if tax < 0.0:
#	tax = 0.0
                       
#tax = round(tax, 0)
#print("The tax is: R", tax, "tax deduction)# 

# calculate tax.................................................................

#income = float(input("enter your annual income: "))

#if income < 100000:
 #   tax = income * 0.18 - 556.02
#else:
  #  tax =  (income - 100000) * 0.32 + 14839.02
    
#if tax < 0.0:
 #   tax = 0.0
    
#tax = round(tax, 0)
#print("your tax is: R" ,tax, "tax deduction")












# calulations,.......................................

#income = float(input("enter your annual tax amount"))

#if income < 150000:
 #   tax = income * 150000 - 556.02
#else:
  #  tax = (income - 150000) * 0.32 + 14839.02
    
#if tax < 0.0:
   # tax = 0.0
    
#tax = round(tax, 0)
#print("your tax is: R", tax, "deduction ") 













# tax calculator

income = float(input("enter your annual income: "))

if income < 80000:
    tax = income * 0.18 - 556.02
else:
    tax = (income - 80000) * 0.32 + 14839.02
    
if tax < 0.0:
    tax = 0.0
    
    tax = round(tax, 0)
    print("your tax is: R", tax, "deduction")
