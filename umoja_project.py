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
print( bank_menu )

choice = int(input('What option do you wish to proceed with : ' ))

accounts = []

if choice == 1:
   print('Open an account')
   
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
elif choice == 2:
   account_status = input('What is your account status : ')
   if account_status.upper() == 'FROZEN' :
      print('Your account is frozen already')
      
   elif account_status.upper() == 'UNFROZEN' :
         print('Your account has been frozen succesfully')
      
   else:
      print('Your input is invalid')
      
   
elif choice == 3:
   print('Account has been unfrozen')

elif choice == 4:
   print('Account has been closed')

elif choice == 5:
   print('Withdrawal successful')

elif choice == 6:
   print('Withdrawal cancelled')

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
   
else:
      print('Invalid option')

   
 
    
                
    
    


  
 
