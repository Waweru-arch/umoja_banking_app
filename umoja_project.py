def open_account():
   accounts = []
   if choice == 1:
      print('Open an account')
      number_of_clients = int(input('How many clients do you want to add? '))   
      
      for i in range(number_of_clients):                                    
         account_type = input('What is your account type ? (current/saving) ')
         account_type = account_type.lower()
      
         if account_type == 'current' or account_type == 'saving' :
            name = input('What is your full names ? ' )
            id_number = int(input('What is your identificstion number ? ' ))
      
            print(f'Account type : {account_type}')
            print(f'Name : {name}')
            print(f'Id number : {id_number}')
            accounts.append(name)
            print(accounts)
         else:
            print('Invalid option')         
   

def freeze_account():
   account_status = input('What is your account status : ')
   if account_status.upper() == 'FROZEN' :
      print('Your account is frozen already')
      
   elif account_status.upper() == 'UNFROZEN' :
         print('Your account has been frozen succesfully')
      
   else:
      print('Your input is invalid')   

def unfreeze_account():
   account_status = input('Enter account status (Frozen/Unfrozen) : ')
   if account_status.upper() == 'UNFROZEN' :
      print('Your account is not frozen')
      
   elif account_status.upper() == 'FROZEN' :
      print('Account unfrozen successfully. Welcome back')
      
   else:
      print(f"You entered the wrong account status '{account_status}' ")
      
   
def close_account():
   is_closed = False
   if is_closed:
      print('Account is allready closed')
   else:
      confirm = input("Enter ('Yes') to confirm : ")
      if confirm.lower() == ('Yes') or confirm.lower().startswith('y') :
         print('Account closed successfully')
      else:
         print('Account closure cancelled')
      

def withdraw():
   account_balance = int(input('Enter account balance : ' ))
   amount_to_withdraw = int(input('Enter amount to withdraw : ' ))
   if amount_to_withdraw > account_balance :
      print( 'Insufficient funds' )
   else :
      print ( 'Withdrawal successful' )   
   
def cancel_withdraw():
   account_balance = int(input('Enter account balance : '))   
   amount_to_withdraw = int(input('Enter amount to withdraw : '))
   if amount_to_withdraw > account_balance :
      print('Insufficent funds')
   else:
      confirm = input('Enter "cancel" to cancel or "Accept" to accept : ' )
      if confirm.lower() == 'cancel' or confirm.lower().startswith('c'):
         print(f'Withdrawal cancelled. Current balance is {account_balance}')
      else:
         account_balance -= amount_to_withdraw
         print('Withdrawal successful')
         print(f'Current balance : Ksh. {account_balance}')
      
   

welcome_message = """

+---------------------------------------------+
|            UMOJA BANK MENU                  |
+---------------------------------------------+
"""
print(welcome_message)

bank_menu = """
+---------------------------------------------+
|            UMOJA BANK MENU                  |
+---------------------------------------------+
| 1. Open an account                          |
| 2. Freeze account                           |
| 3. Unfreeze account                         |
| 4. Close account                            |
| 5. Withdraw                                 |
| 6. Cancel withdrawal                        |
| 7. Deposit                                  |
| 8. Request a loan                           |
| 9. Grant a loan                             |
| 10. Make installment                        |
| 0. Exit                                     |
|                                             |
+---------------------------------------------+
"""
while True  :
   print( bank_menu )
   
   choice = int(input('What option do you wish to proceed with : ' ))
   
   if choice == 1:
      open_account()
            
   elif choice == 2:
      freeze_account()
      
   elif choice == 3:
      unfreeze_account()
      
   elif choice == 4:
      close_account()
     
   elif choice == 5:
      withdraw()
         
   elif choice == 6:
      cancel_withdraw()
      
   elif choice == 7:
      print('Deposit successful')
   
   elif choice == 8:
      print('Loan requested')
   
   elif choice == 9:
      print('Loan granted')
   
   elif choice == 10:
      print('Installment made')
   
   elif choice == 0:
      print('Thank you for using Umoja Bank. Goodbye!')
      
      exit()
      
      
   else:
         print('Invalid option')
   
      
    
       
                   
       
       
   
   
     
    
