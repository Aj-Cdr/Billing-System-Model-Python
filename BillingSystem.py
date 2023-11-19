# Fake Billing System Python Script:

while True:
    total_customers = int(input('Enter How Many Customers Are In Line: '))
    Customer_Name = input('Customer Name: ')
    while True: 
        Quantity = int(input('Enter the quantity of items: '))
        Items = int(input('Enter # of items: '))

        Total = int(Quantity)*int(Items)
        repeat = input('Do you want to add more items (y/Y/n/N): ')

        if repeat=='n' or repeat=='N':
            break

        print('_'*50)
        print('Name: ', Customer_Name)
        print('Total Cost: ', Total)
        print()
        print('*****Thank you shopping with us*****')
        print('_'*50)

        New_Customer=input('Go to the next person (y/Y/n/N): ')

        if New_Customer=='n' or New_Customer=='N':
            break