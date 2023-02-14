from Budget_management import *
from os import system

temp = 'y'

while temp in ('y', 'yes', 'yeah'):
     {     
     "code-runner.ignoreSelection": True
     }
     try:
          print("Budget Management".center(200, " "))
          print("-------------------".center(200, " "))
          operation = input("Type '\help' to get Help\n>>").lower()
          operation = operation.split(' ')
          
     #removes blank spaces
          while '' in operation:                   
               for n in operation:
                    if n == '':
                         operation.remove(n)
          if operation[0]in('transf', 'tranf', 'transfer') and len(operation)==6:
               if category_exist(operation[3]):                                                                         #Checks for transferable expense name in spendable expense.
                    if spending[operation[3]]>= int(operation[1]):                                                      #Checks if transferable amount is less or equal than in spendable.
                         UpdateBudget('less', operation[3], int(operation[1])).update_budget()                          #Withdraws the amount depositer.
                         UpdateBudget('add', operation[5], int(operation[1])).update_budget()                           #Deposits the amount in reciver spendable, if no such receiver exist, it creates one.
                         print(f"Amount {operation[1]} transferred from {operation[3]} to operation {operation[-1]}")
                    else:
                         print("Insufficient Balnce to transfer.")
               else:
                    print("No such expense exist.")
                    
          elif operation[0] == 'budget_limit':  #In progress
               budget_limit = operation[1]
     #Performs the operation deposit and withdrwal..
          elif operation[0] in ('add', 'withdraw', 'less', 'update'):
               item = AddCategory( operation[0], operation[1], int(operation[2])).add_category()
     #removes the Spendable expense from the bucket expenses
          elif operation[0] in ('remove', 'del'):
               item = remove_item(operation[1])
     #Generates a tables showing expenses and amount left.
          elif operation[0] == 'report':
               a = Docs(operation).report()
               print(a)
     #Shows the history of operations performed with date and Time-stamp.
          elif operation[0] == 'log':
               print(Docs(operation).log_all())
     #Generates Dacument to view expenses.
          elif operation[0] == 'save':
               Docs(operation).save_doc()
     #Help Menu.
          elif operation[0] == '\help':
               help()

          temp = input("\ncontinue... ").lower()
          system("cls")
     except:
          print("Error: Invalid Syntax.")