import datetime
global now
import re
import os, sys
from os import system,name





def createacc():
     global usn
     usn=input("enter username:\n")
     f=open("usn.txt",'a')
     f.close()
     f=open("usn.txt",'r')
     if usn not in (f.read().splitlines()):
        f.close()
        f1=open("usn.txt",'a')
        f1.write("%s\n"% usn)
        f1.close()
     else:
        print('User exists, enter different user name')
        createacc()
             
     passwrd()
     with open("psw.txt",'a') as f:
        f.write("%s\n"% psw)   
     print("Your account was successfully created!!\n")
     opt2=int(input("If you want to deposit money to your account,press 1 else press 2:\n"))
     if opt2==1:
        print("The minimim deposit should be 2000\n")
        dep=int(input("Rs."))
        if dep<2000:
             dep=input("Your entered amount is less than 2000,please deposit more than RS.2000:\n")
        with open("bal_%s.txt"% usn,'a') as f:
          f.write("%s"% dep)
        print("your amount was successfully added!! \n")
        print("You have logged out. To continue, please login again\n")
        now = datetime.datetime.now()
        f5=open("trans_%s.txt"% usn,'a')
        f5.write("\n%s--------------------(CREDIT)\nRs.%s added through direct deposit\nUpdated balance is %s\n"% (now,dep,dep))
        f5.close()
     elif opt2==2:
          with open("bal_%s.txt"% usn,'a') as f:
            f.write('0')
     opt=int(input("if you want to login to your account, press 1 OR\nTo exit, press 2:\n"))
     if opt==1:
            clear()
            loginacc()
     elif opt==2:
        exit()
             
     


def passwrd():
 password=input("Enter a password...Your password should contain:\n1)Atleast 6 characters\n2)Atleast 1 upper and lowercase\n2)Atleast 1 number for security:\n")
 flag = 0
 while True:   
    if (len(password)<6): 
        flag = -1
        break
    elif not re.search("[a-z]", password): 
        flag = -1
        break
    elif not re.search("[A-Z]", password): 
        flag = -1
        break
    elif not re.search("[0-9]", password): 
        flag = -1
        break        
    else: 
        flag = 0
        print("Valid Password")
        global psw
        psw=password
        break  
 if flag ==-1: 
    print("Not a Valid Password")
    passwrd()
              


def loginacc():
     global usn
     global psw
     usn=input("please enter username:\n")
     f1=open("usn.txt",'r')
     lst1=f1.read().splitlines()
     f2=open("psw.txt",'r')
     lst2=f2.read().splitlines()
     for i in range(0,len(lst1)):
            if lst1[i]==usn:
                 psw=input("please enter password: \n")
                 if psw==lst2[i]:
                    print("password correct")
                    loggedin()
                 else:
                         print("password incorrect, please enter again...")
                         loginacc()
     if usn not in lst1:
         print("The username does not exist")
         opt3=int(input("If you want to create a new account, press 1.... To try and login to your account, press 2:\n"))
         if(opt3==1):
              createacc()
         elif(opt3==2):
              loginacc()


def loggedin():
    f=open("bal_%s.txt"% usn,'r')
    print("Your current balance is Rs.",f.read())
    print("\nAll your previous transactions are: ")
    prntpassbook()
    opt1=int(input("If you want to send money to another user, press 1 OR\nIf you want to add money to your account, press 2 OR\nIf you want to delelete your account,press 3 OR\nIf you want to logout,press 4:\n"))
    if opt1==1:
        transactions()
    elif opt1==2:
        addmoney()
    elif opt1==3:
          delacc()
    else:
        print("you are logged out")
        exit()


def transactions():
     global rec
     global amt
     global updated_bal
     global updated_recbal
     rec=input("enter the username of the reciever of the money: \n")
     if rec==usn:
          rec=input("The reciever username should be other than your own...,so please enter a different username: ")
     f1=open("usn.txt",'r')
     lst1=f1.read().splitlines()
     f1.close()
     if rec not in lst1:
          print("This user does not exist(The reciever should have an account)....Try again")
          transactions()     
     for i in range(0,len(lst1)):
            if lst1[i]==rec:
                 amt=int(input("enter amount to send"))
                 f=open("bal_%s.txt"% usn,'r')
                 bal=int(f.read())
                 f.close()
                 if(bal>=amt):
                      updated_bal=bal-amt
                      f1=open("bal_%s.txt"% usn,'w')
                      f1.write("%s"% updated_bal)
                      f2=open("bal_%s.txt"% rec,'r') 
                      rec_bal=int(f2.read())
                      updated_recbal=rec_bal+amt
                      f3=open("bal_%s.txt"% rec,'w')
                      f3.write("%s"% updated_recbal)
                      f1.close()
                      f2.close()
                      f3.close()
                      print("Your transaction was successfully processed, your updated balance is: Rs.",updated_bal)
                      passbook()
                 else:
                       print("you do not have sufficient balance to conduct this transaction....")
                       opt=int(input("Enter 1 if you want to add money now and send it, else press 2:\n"))
                       if opt==1:
                            addmoney()
                            transactions()
                       elif opt==2:
                            loggedin() 
            
            


def addmoney():
        print("You have chosen to add money\n")
        dep=int(input("The minimim deposit should be 2000:\n"))
        while dep<2000:
             dep=input("Your entered amount is less than 2000, please deposit more than RS.2000:\n")
        f=open("bal_%s.txt"% usn,'r')
        f1=int(f.read())
        f.close()
        bal=dep+f1
        with open("bal_%s.txt"% usn,'w') as f2:
          f2.write("%s"% bal)
          f2.close()
        print("your amount was successfully added!! \n")
        now = datetime.datetime.now()
        f5=open("trans_%s.txt"% usn,'a')
        f5.write("\n%s--------------------(CREDIT)\nRs.%s added through direct deposit\nUpdated balance is %s\n"% (now,dep,bal))
        f5.close()
        menu()



     

def passbook():
        f=open("trans_%s.txt"% usn,'a')
        f1=open("trans_%s.txt"% rec,'a')
        now=datetime.datetime.now()
        f.write("\n%s--------------------(DEBIT)\nRs.%s sent to %s\nUpdated balance is Rs.%s\n"% (now,amt,rec,updated_bal))
        now1=datetime.datetime.now()
        f1.write("\n%s--------------------(CREDIT)\nRs.%s received from %s\nUpdated balance is Rs.%s\n"% (now1,amt,usn,updated_recbal))
        f.close()
        f1.close()
        menu()



def delacc():
         f1=open("usn.txt",'r')
         lst1=f1.read().splitlines()
         f1.close()
         lst1.remove("%s"% usn)
         f2=open("usn.txt",'w')
         f2.writelines(["%s\n"% item  for item in lst1])
         f2.close()
         f3=open("psw.txt",'r')
         lst2=f3.read().splitlines()
         f3.close()
         lst2.remove("%s"% psw)
         f4=open("psw.txt",'w')
         f4.writelines(["%s\n"% item  for item in lst2])
         f4.close()
         
         
         
         
         
       
        
def menu():
      opt5=int(input("If you want to go to the main menu, press 1 OR\nPress 2 to logout:\n"))
      if opt5==1:
                 loggedin()
      elif opt5==2:
        print("you have logged out")           
        exit()
     

def prntpassbook():
    try:
        f=open("trans_%s.txt"% usn,'r')
        print(f.read())
    except IOError:
        print ("No Transactions")


def clear(): 
  
    _ = system('cls') 
 
    print("------------------------------PESU BANK------------------------------")
    print("----------------------(Always here, for you)-----------------------")
   
     
def main():
  print("------------------------WELCOME TO PESU BANK-------------------------")
  print("----------------------(Always here, for you)-----------------------")
  option1=int(input("To create account , press 1\nTo login to your account, press 2:\n"))
  if(option1==1):
    createacc()
  elif(option1==2):
     loginacc()
        


                            
            
main()
