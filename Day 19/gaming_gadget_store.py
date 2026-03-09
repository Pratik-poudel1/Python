# Project Task: Gaming Gadget Store Billing System
# Description:
# You are asked to create a console-based billing system for a Gadget Gaming Store where customers can purchase one or more items. 
# The store also provides:
# 1.Membership discounts
# 2.Different delivery options
# 3.Gift wrapping
# 4.Loyalty points based on the final amount

from datetime import datetime
import os

# Ensure required directories and files exist
if not os.path.exists('users'):
    os.makedirs('users')
if not os.path.exists('users/shopdata.txt'):
    open('users/shopdata.txt', 'w').close()
if not os.path.exists('users/atmdata.txt'):
    open('users/atmdata.txt', 'w').close()
if not os.path.exists('users/record.txt'):
    open('users/record.txt', 'w').close()

# --- USER AUTH ---
def register():
    username = input('Enter username: ')
    with open("users/shopdata.txt", "r") as file:
        users = file.read()
        if f'Username : {username} ,' in users:
            print('Username already exists. Please try again.')
            exit()

    password = input('Enter Password: ')
    c_password = input('Confirm Password: ')
    if password != c_password:
        print('Passwords do not match. Try again.')
        exit()

    while True:
        pin = input('Set your 4-digit PIN: ')
        if pin.isdigit() and len(pin) == 4:
            break
        else:
            print('PIN must be exactly 4 digits.')

    with open('users/shopdata.txt', 'a') as file:
        file.write(f'Username : {username} , Password : {password} , PIN : {pin}\n')

    print('Registration Successful.')
    return username

def login():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        username = input('Enter username: ')
        password = input('Enter password: ')

        with open('users/shopdata.txt', 'r') as file:
            users = file.readlines()
            for user in users:
                if f'Username : {username} , Password : {password}' in user:
                    print(f'Welcome {username}')
                    return username

        print('Invalid username or password.')
        attempts += 1

    print('Too many failed attempts. Exiting...')
    exit()

# --- PRODUCT DATA ---
gadgets = {
    '1': ('Gaming Mouse', 2500),
    '2': ('Mechanical Keyboard', 5000),
    '3': ('Gaming Headset', 3500),
    '4': ('Gaming Chair', 15000),
    '5': ('Gaming Card', 45000),
    '6': ('RGB Mousepad', 1500),
    '7': ('Gaming Monitor', 30000),
    '8': ('VR Headset', 40000),
    '9': ('Streaming Mic', 6000),
    '10': ('Gaming Desk', 20000),
    '11': ('Capture Card', 12000),
    '12': ('Gaming Controller', 7000),
    '13': ('Webcam', 5000),
    '14': ('Headphone Stand', 1200),
    '15': ('Cable Management Kit', 800)
}

# --- ORDER SYSTEM ---
print('\n\n\t\tGaming Gadget Store')
print('   Gadget                           Price')
for key, value in gadgets.items():
    print(f'{key}. {value[0]:30} Rs. {value[1]}')
print('============================================')

print('\n\nDo You want to place an order: ')
print('1.Yes                          2.No')
while True:
    y_n = input('Enter Your Choice (1/2): ')
    if y_n == '1':
        print('1. Login            2. Register              3.Exit')
        choice = input('\n\nEnter Your Choice (1/2/3): ')
        if choice == '1':
            username = login()
            break
        elif choice == '2':
            username = register()
            break
        else:
            exit()
    elif y_n == '2':
        print('Exiting.....')
        exit()
    else:
        print('Option Invalid!!!!!')
        again = input('Do you want to try again? (Y/N): ')
        if again.lower() != 'y':
            print('Exiting')
            exit()

cart = []
home_del = 0
gift_wrap = 0
tax_amt = 0
mem_amt = 0
discount_amt = 0
member_ship = ''

while True:
    order = input('\n\nPlace your order by number (1-15): ')
    if order in gadgets:
        while True:
            quantity = int(input(f"Enter quantity for {gadgets[order][0]}: "))
            if quantity > 0:
                item_total = gadgets[order][1] * quantity
                cart.append((gadgets[order][0], quantity, gadgets[order][1], item_total))
                break
            else:
                print('Invalid quantity! Must be at least 1.')
    else:
        print('Invalid Option! Choices are between 1 and 15.')

    more = input('Do you want to add more items? (Y/N): ')
    if more.lower() != 'y':
        break

# Delivery
print('\n\nDelivery Options:')
print('1.Home Delivery - Rs.200')
print('2.Store Pickup  - Free')
while True:
    opt = input('Enter your Choice (1/2): ')
    if opt == '1':
        home_del = 200
        break
    elif opt == '2':
        break
    else:
        again = input('Invalid! Try again? (Y/N): ')
        if again.lower() != 'y':
            exit()

# Gift Wrap
print('\n\nGift Wrap Options (Per Piece): ')
print('1. Basic Wrap  - Rs.100')
print('2. Premium Box - Rs.300')
print('3. No Wrap     - Rs.0')
total_items = sum(item[1] for item in cart)
while True:
    opt = input('Enter Your Choice (1/2/3): ')
    if opt == '1':
        gift_wrap = 100 * total_items
        break
    elif opt == '2':
        gift_wrap = 300 * total_items
        break
    elif opt == '3':
        break
    else:
        again = input('Invalid! Try again? (Y/N): ')
        if again.lower() != 'y':
            exit()

# Membership
total = sum(item[3] for item in cart)
while True:
    print('\n\nAre you a Member of our shop: ')
    print('1.YES')
    print('2.No')
    opt = input('Enter Your Choice (1/2): ')
    if opt == '1':
        print('\nWhich member are you ?')
        print('1.Platinum Member   - 25% Discount')
        print('2.Gold Member       - 15% Discount')
        print('3.Silver Member     - 10% Discount')
        choice = input('Enter your choice: ')
        if choice == '1':
            discount_amt = total * 0.25
            member_ship = 'Platinum'
        elif choice == '2':
            discount_amt = total * 0.15
            member_ship = 'Gold'
        elif choice == '3':
            discount_amt = total * 0.10
            member_ship = 'Silver'
        break
    elif opt == '2':
        print('Do you want to buy membership?\n1. YES\n2. NO')
        subopt = input('Enter your choice: ')
        if subopt == '1':
            print('1. Platinum - Rs.5000\n2. Gold - Rs.2500\n3. Silver - Rs.1000')
            option = input('Select membership: ')
            if option == '1':
                mem_amt = 5000
                discount_amt = total * 0.25
                member_ship = 'Platinum'
            elif option == '2':
                mem_amt = 2500
                discount_amt = total * 0.15
                member_ship = 'Gold'
            elif option == '3':
                mem_amt = 1000
                discount_amt = total * 0.10
                member_ship = 'Silver'
            break
        else:
            break
    else:
        continue

dis_total = total - discount_amt

# VAT
print('\n\nLocation:')
print('1. Inside Kathmandu  - 13% VAT')
print('2. Outside Kathmandu - 15% VAT')
while True:
    opt = input('Enter Your choice (1/2): ')
    if opt == '1':
        tax_amt = dis_total * 0.13
        break
    elif opt == '2':
        tax_amt = dis_total * 0.15
        break

grand_total = dis_total + tax_amt + gift_wrap + home_del + mem_amt
point = round(grand_total // 100)

# BILL
print('\n\n================ Gadget Gaming Store BILL ================')
print(f'Username : {username}')
print('\nItems Purchased:')
for name, qty, price, total_price in cart:
    print(f'- {name:25} Qty: {qty:2} x Rs.{price} = Rs.{total_price}')
print(f'\nTotal Price                   : Rs. {total}')
print(f'Membership Discount (Rs)     : Rs. {discount_amt}')
if mem_amt:
    print(f'Membership Type              : {member_ship} (Rs. {mem_amt})')
print(f'Tax Amount (VAT)             : Rs. {tax_amt}')
print(f'Gift Wrap Charges            : Rs. {gift_wrap}')
print(f'Delivery Charges             : Rs. {home_del}')
print('----------------------------------------------------------')
print(f'GRAND TOTAL                  : Rs. {grand_total}')
print(f'Loyalty Points Earned        : {point}')
print('==========================================================')

# Save to file
with open('users/record.txt', 'a') as handle:
    handle.write('\n\n================ Gadget Gaming Store BILL ================\n')
    handle.write(f'Username : {username}\n')
    for name, qty, price, total_price in cart:
        handle.write(f'- {name:25} Qty: {qty} x Rs.{price} = Rs.{total_price}\n')
    handle.write(f'Total Price: Rs. {total}\n')
    handle.write(f'Membership Discount: Rs. {discount_amt}\n')
    if mem_amt:
        handle.write(f'Membership Type: {member_ship}, Cost: Rs. {mem_amt}\n')
    handle.write(f'Tax: Rs. {tax_amt}\n')
    handle.write(f'Gift Wrap: Rs. {gift_wrap}\n')
    handle.write(f'Delivery: Rs. {home_del}\n')
    handle.write(f'GRAND TOTAL: Rs. {grand_total}\n')
    handle.write(f'Loyalty Points: {point}\n')
    handle.write('==========================================================\n')

# PAYMENT
print('\n\nDo you want to proceed with payment now? 1. YES 2. NO')
pay_opt = input('Enter Your Choice (1/2): ')
if pay_opt == '1':
    print('Choose Payment Method:\n1. Card\n2. Cash')
    choice = input('Enter your Choice (1/2): ')
    if choice == '1':
        print('Welcome to our ATM')
        attempts = 0
        while attempts < 3:
            atm_username = input('Enter ATM username: ')
            atm_password = input('Enter ATM password: ')
            atm_pin = input('Enter your 4-digit PIN: ')
            with open('users/shopdata.txt', 'r') as f:
                users = f.readlines()
            found = any(f'Username : {atm_username} , Password : {atm_password} , PIN : {atm_pin}' in line for line in users)
            if found:
                print('Payment Successful!')
                with open('users/atmdata.txt', 'a') as atmfile:
                    atmfile.write('\n================ ATM Payment Log ================\n')
                    atmfile.write(f'Username          : {atm_username}\n')
                    atmfile.write(f'Amount Paid (Rs)  : {grand_total}\n')
                    atmfile.write(f'Payment Status    : Successful\n')
                    atmfile.write(f'Time              : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
                    atmfile.write('=================================================\n')
                break
            else:
                print('Incorrect ATM credentials.')
                attempts += 1
        else:
            print('Too many failed attempts. Exiting payment.')
    elif choice == '2':
        print('Payment will be done via Cash on Delivery/Pickup.')
else:
    print('You chose not to pay now. Please pay on delivery or at store.')

print('\nThank you for shopping with us! Have a great day :)')
