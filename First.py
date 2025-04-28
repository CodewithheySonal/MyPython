vadapav = int(input('Enter the price of vadapav: '))
pavbhaji = int(input('Enter the price of pavbhaji: ')) 

print('\nwelcome to the food stall\n')

if vadapav <= 20 and pavbhaji <= 30:
    print('we have vadapav and pavbhaji available\n')
else:
    print('we do not have vadapav and pavbhaji available at this price\n')
