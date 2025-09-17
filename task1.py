# #restaurnt bill
# bill=int(input("Enter the Bill"))

# if bill>=500:

#     og_bill=bill*5/100
#     curntbill=og_bill-bill
#     print("your Bill",curntbill)

# elif bill>=1000:
   
#     og_bill=bill*10/100
#     curntbill=og_bill-bill
#     print("your Bill",curntbill)

# else:
#     print("You Have No Discount")


# # buyticket

# age=int(input("Enter your age"))
# if age<=5:
#     print(age,"Enjoy Your Free Ticket")
# elif age<18:
#     print(age,"You must buy the Half Ticket")
# elif age>=18:
#     print(age,"You must buy full Ticket")
# else:
#     print("invalid Number")


# # electricity bill

# bill=int(input("enter your bill"))

# if bill<=100:
#     og_bill=bill*5
#     print(og_bill,"Your Bill")
# elif bill>=101 and bill<=300:
#     og_bill=bill*7
#     print(og_bill,"Your Bill")
# else:
    
#     print(bill*10,"your Bill")


# num=int(input("Enter the number"))
# sum_of_digit=0

# for i in range(2,num+1,2):
#     sum_of_digit+=i**2

# print("sum of squre of ",num,"is",sum_of_digit)


# #reverse
# num=int(input("ENter the number"))

# rev=0

# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10

# print("the reverse num is",rev)


# #salaryslip
# name=input("enter your name")
# bsalary=int(input("Enter your Salary"))

# hra=0.20*bsalary
# da=0.10*bsalary
# tax=0.5*bsalary

# net_salary=hra+da+bsalary-tax

# print("Your HRA",hra)
# print("Your DA",da)
# print("your tax",tax)
# print("net salary",net_salary)


for i in range(1,11):
    print("-"*25)
    for j in range(1,11):
        
        print(f"{j}*{i}={i*j}")

num=int(input("Enter the number")                                             )

 

