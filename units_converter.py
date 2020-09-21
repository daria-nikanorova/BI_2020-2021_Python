# This is a converter from magical (from Harry Potter`s Universe) to non-magical money and backwards.
# Firstly I`ve created a dictionary that contains exchange course of 7 currencies. This step prevents from using too many cycles

exchange_course = {
    'dollar': {'dollar': 1.0, 'euro': 0.84, 'pound': 0.77, 'ruble': 75.03, 'galleon': 0.14, 'sickle': 2.3,
               'knut': 50},
    'euro': {'dollar': 1.19, 'euro': 1.0, 'pound': 0.91, 'ruble': 88.96, 'galleon': 0.17, 'sickle': 2.9,
             'knut': 100},
    'pound': {'dollar': 1.29, 'euro': 1.1, 'pound': 1.0, 'ruble': 97.44, 'galleon': 0.2, 'sickle': 3.45, 'knut': 66.7},
    'ruble': {'dollar': 0.013, 'euro': 0.011, 'pound': 0.01, 'ruble': 1.0, 'galleon': 0.004, 'sickle': 0.074,
              'knut': 2.12},
    'galleon': {'dollar': 7.35, 'euro': 5.9, 'pound': 4.93, 'ruble': 229.8, 'galleon': 1.00, 'sickle': 17,
                'knut': 493},
    'sickle': {'dollar': 0.43, 'euro': 0.34, 'pound': 0.29, 'ruble': 13.52, 'galleon': 5.9, 'sickle': 0.34,
               'knut': 0.01},
    'knut': {'dollar': 0.02, 'euro': 0.01, 'pound': 0.015, 'ruble': 0.47, 'galleon': 4.93, 'sickle': 0.29,
             'knut': 0.015}
}
while True:
    input_currency = str(input(
        'Hello! It`s a unique tool that helps Wizards to convert money from Magical to Non-magical and backwards! \n'
        'So, which type of money do yo want to convert? Please, choose from the list below: '
        'dollar, euro, pound, ruble, galleon, sickle or knut \n'
        'Your choice: ')).lower()
    if input_currency not in exchange_course:
        input_currency = str(input(
            'Please, try again and choose ONLY from the list below: dollar, euro, pound, ruble, galleon, sickle or knut \n'
            'Your choice: ')).lower()
        if input_currency not in exchange_course:
            print('Sorry, we should start from the beginning...')
            continue
    # Try and except allow us to find ValueError if user enters characters instead of numbers

    try:
        amount_of_money = float(input("Ok! What amount of money do you want to convert? \n"
                                      'Your amount: '))
    except ValueError:
        print("WRONG VALUE! We will start again and please enter a number!")
        continue
    if amount_of_money < 0:
        amount_of_money = - amount_of_money
        print("MONEY CAN BE ONLY POSITIVE! Your amount of money has been automatically reversed to a positive number.")
    output_currency = str(input('Ok! Now choose the output currency. Please, choose from the list below: '
                                'dollar, euro, pound, ruble, galleon, sickle or knut \n'
                                'Your choice: ')).lower()
    if output_currency not in exchange_course:
        output_currency = str(input(
            'Oh, Merlin`s beard! PLEASE, CHOOSE ONLY FROM THE LIST: dollar, euro, pound, ruble, galleon, sickle or knut! \n'
            'Your choice: ')).lower()
        if output_currency not in exchange_course:
            print('Sorry, we should start from the beginning...')
            continue
    result = round(exchange_course[input_currency][output_currency] * amount_of_money, 3)
    print(f"There are {result} {output_currency}s in {amount_of_money} {input_currency}s")
    continue_or_exit = input('Do you want to continue? Yes/No ')
    if continue_or_exit == "Yes":
        continue
    else:
        print('Bye!')
        break
