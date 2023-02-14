#TODO : Need to add a trandiction history feature, to show all past transictions with time stamp as string in a list.
#<date>     <Time>    <operation>    <Item>          <amount>
#14-08-2022  13:05        add      Misclellaneous      5000
#14-08-2022  13:08        less     savings             8900
#Done
#Need to learn stacking features.
#TODO : Want to add print report/log feature.
#
from datetime import datetime
from load import loading
sum = 0
spending = {}
budget_limit = 0
log = []
item_logs = []
#Checks if the item exists in the 'spending' dictonary varaiable.
def category_exist(item_name):
    if item_name in spending:
        return True
    else:
        return False
    
#The following class adds the expenses into spending list(dictonary)
#if the expense already exists in the spending, it automatically add-on to the following expenditure.
class AddCategory:
	
     def __init__(self,operation, item_name, item_amt: int):
          self.item_name = item_name
          self.item_budget =  item_amt
          self.op = operation

     def add_category(self): 
        if not category_exist(self.item_name):
            if self.op == 'add' or self.op == 'deposit':
               spending[self.item_name] = self.item_budget
               return log_(date_time(), 'new_itm', self.item_name, self.item_budget)
        else:
            UpdateBudget(self.op, self.item_name, self.item_budget).update_budget()

#The following class perform the deposit and withdraw operation.
class UpdateBudget:
	def __init__(self, operation: str, item_name, item_amt:int):
		self.operation, self.budget_name, self.budget = operation, item_name, item_amt

	def update_budget(self):
    #Adds amount to the respective expense
		def deposit():
			spending[self.budget_name] += self.budget
			log_(date_time(), 'deposit', self.budget_name, self.budget)
   
    #Withdraws a certain amount certain from the alloted expense amount.
		def withdraw():
			if spending[self.budget_name] > 0 and spending[self.budget_name] >= self.budget:
				spending[self.budget_name] -= self.budget
				return log_(date_time(), ' less  ', self.budget_name, self.budget)

			else:
				return False and print("Insufficient balance.")
    #perform deposit and withdraw operation to the expense bucket
		if category_exist(self.budget_name):
			if self.operation == 'update':
				spending[self.budget_name] = self.budget
			elif self.operation in ('deposit', 'add'):
				deposit()
			elif self.operation in ('withdraw', 'less'):
				withdraw()
			
		else:
			new = AddCategory(self.budget_name, self.budget)
			new.add_category()

#Removes the expense from the spending
#Or show 'No such entry exists' if no such entry exists.
def remove_item(item):
    if category_exist(item):
        log_(date_time(), 'Deleted', item, '   ')
        del spending[item]
    else:
        print("No such entry exist.")

class BudgetExtra:
	def __init__(self):
		global budget_limit
		self.total_ = 0

	def total(self):
		for x in spending:
			self.total_ = (self.total_ + spending[x] )
		return self.total_

	def limit_budget(self , num : int):
		if self.total + num <= budget_limit:
			return True
		else:
			return False
#Docs class Prepare operation Log
class Docs:
     def __init__(self, opr:list):
          self.opr = opr
          self.doc = ""
     
     def log_all(self):
          particular = self.opr[1] if len(self.opr) > 1 else ''
          self.doc = f"{particular}".center(108, '-') + "\n"
          self.doc += "        Date      |       Time       |    Operation    |          Particular            |      Amount      |\n"
          self.doc += "------------------+------------------+-----------------+--------------------------------+------------------+"
          if len(self.opr) > 1 and category_exist(self.opr[1]):
               item_log(self.opr[1])
               for part in item_logs:
                    self.doc += f"\n    {part[0]}      |    {part[1]}      |" + f"{part[2]}".center(32)+ '|' + f"{part[3]}".center(18) + '|'
                    self.doc += ("\n------------------+------------------+-----------------+--------------------------------+------------------+")

          else:
               for part in log:
                    self.doc += f"\n    {part[0]}      |    {part[1]}      |" + f"{part[2]}".center(32)+ '|' + f"{part[3]}".center(18) + '|'
                    self.doc += "\n------------------+------------------+-----------------+--------------------------------+------------------+"
                    
                    
          print('\n\n')
          item_logs.clear()
          return self.doc
     
     def report(self):
          self.doc = "Report".center(94, '-')
          list = spending
          for item in list:
               self.doc += f"\n{item}\t:\t{spending[item]}"
          self.doc += ("\n-------------------------")
          self.doc += f"\nTotal\t:\t{BudgetExtra().total()}\n"
          self.doc += ''.center(94, '-')
          return self.doc

#def save_doc generate txt file of log and report.
     def save_doc(self):
          self.opr.remove('save')
          path_name = 'D:/python/test/'
          file_name = self.opr[-1]+'.txt'
          self.opr.remove(self.opr[-1])
          if self.opr[0] == 'log':
               self.log_all()
          elif self.opr[0] == 'report':
               self.report()
          path_name += file_name
          with open(path_name, 'w') as file:
               loading()
               file.write(self.doc)
               print(self.doc)
               print(f"\nFile created at <{path_name}>")

def item_log(item):
    for itm in log:
        if itm[2] == item:
               item_logs.append(itm)
    item_logs.reverse()

def date_time():
	dt = datetime.now()
	return dt.strftime("%d-%m-%Y    |    %H:%M:%S")

def log_(dt, operation, item, amount):
    log.append((dt, operation, item, amount))
    return True

def help():
    print("Help".center(60, '-'))
    print("""
Item naming convention:
    -> Do not leave any space in between of Item name.
    -> Use underscore ( _ ) to show gap between names. 

To add a new item :
	syntax-> add <item-name> <amount>


To withdraw amount from a existing item:
   syntax-> (less/withdraw) <item-name> <amount>


To add/deposit amount in an existing item:
    syntax-> (add/deposit) <item-name> <amount>


To update amount in an existing item:
    syntax-> update <item-name> <amount>


To delete an item:
    syntax-> del <item-name>


To save the report or log as document:
    syntax-> save <report/log/log (item_name)> <document_name>
    
    
To transfer spendings from Spendable amount to an existing/new expense:
    syntax-> (transfer/tranf/transf) <amount> from <exp_acc.> to <new/existing account>
		""")
{     
"code-runner.ignoreSelection": True
}