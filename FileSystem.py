import random

def staff_login():
            
    username = input('Enter username: ')
    password = input('Enter password: ')
    get_data = open('staff.txt', 'r').readlines()
    staff_data = []
    for staff in get_data:
        staff_data.append(staff.split())

    total_staff = len(staff_data)
    details = 0
    login_success = 0
    while details < total_staff:
        usernames = staff_data[details][2]
        passwords = staff_data[details][3]
        if username == usernames and password == passwords:
            login_success = 1
        details += 1

    while login_success == 1:
        action = input("Would you like to 'Create new bank Account' or 'Check Account Details' or Logout: ")
        create_acc = 'create new bank account'
        check_acc = 'check account details'
        logout = 'logout' 
        if action == create_acc:
            accountname = input('Account Name: ')
            openbalance = input('Opening Balance: ')
            accounttype = input('Account Type: ')
            accountemail = input('Account Email: ')
            accountnumber = str(random.randrange(0, 9999999999))   
            handle = open('customer.txt', 'a')
            handle.write(accountname)
            handle.write(' ')
            handle.write(openbalance)
            handle.write(' ')
            handle.write(accounttype)
            handle.write(' ')
            handle.write(accountemail)
            handle.write(' ')
            handle.write(accountnumber)
            handle.write('\n')
            handle.close()
            print(accountnumber)        
                        
        elif action == check_acc:
            accountnumber = input('Account Number: ')
            get_customerdata = open('customer.txt', 'r').readlines()
            customer_data = []
            for customer in get_customerdata:
                customer_data.append(customer.split())
            total_customer = len(customer_data)
            customer_details = 0
            while customer_details < total_customer:
                accountnumbers = customer_data[customer_details][4]
                if accountnumber == accountnumbers:
                    customer_details = 1
                    print(customer_data)
                                
        else: 
            action == logout
            print('Logging out')
            break 
                    
    else:
        print('invalid username & password') 

question = input('Enter one of the otpions: Staff login or Close App: ')
if question == 'staff login':
    staff_login()

else:
    question == 'close app'
    print('Goodbye')




