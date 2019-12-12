from weather_scraper import weekly_periods, weekly_descs, weekly_temps
# Import lists from WebScraper

def days_of_week_left():

    days_of_week_left.days_left = []  # Initialize empty days_left list
    days_of_week_left.all_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    for day in days_of_week_left.all_days and weekly_periods:
        if day in days_of_week_left.all_days and weekly_periods:
            days_of_week_left.days_left.append(day)

    return days_of_week_left.days_left

def weather_greeting():

    days_of_week_left()
    print('Hello! What would you like to know about the weather in La Jolla this week? (Enter a letter)')

    user_option = input('A. Give me the current forecast for today \nB. Give me the forecast for another day\n')
    valid_inputs = ['A', 'B']

    while True:
        if user_option not in valid_inputs:
            user_option = input('Oops! Enter another option: ')
            continue

        elif user_option == 'A':

            if 'High' in weekly_temps[0]:
                high_or_low = 'high'
            else:
                high_or_low = 'low'

            print('The current forecast for ' + weekly_periods[0] + ' is ' + weekly_descs[0] + '. Current ' + high_or_low + ' for today: ' + weekly_temps[0])
            break

        elif user_option == 'B':
            print('Which day would you like to display? (Enter a day)')
            day_option = input()

            while True:
                if day_option not in days_of_week_left.days_left:
                    day_option = input('Oops! Enter another day left in the week: ')
                    continue

                else:
                    print('The forecast for ' + day_option + ' is: ' + weekly_temps[weekly_periods.index(day_option)])
                    break
        break

        return True

def clothing():
    print('Do you want suggestions on what to wear on a certain day? (Yes or No)')
    clothing_option = input()

    valid_inputs = ['Yes', 'No']

    while True:
        if clothing_option not in valid_inputs:
            clothing_option = input('Oops! Enter Yes or No: ')
            continue

        elif clothing_option == 'Yes':
            print('Which day would you like to know about? (Enter a day)')
            clothing_day = input()

            while True:
                if clothing_day not in days_of_week_left.days_left:
                    clothing_day = input('Oops! Enter another day left in the week: ')
                    continue

                elif clothing_day in days_of_week_left.days_left:

                    temp_index = weekly_temps[weekly_periods.index(clothing_day)]
                    temp = temp_index[6:8]

                    if int(temp) >= 75:
                        print('It will be warm on ' + clothing_day + ' (' + temp + 'F), try to dress lightly')
                        break

                    elif int(temp) >= 65 and int(temp) < 75:
                        print('It will be cool on ' + clothing_day + ' (' + temp + 'F), bring a jacket')
                        break

                    else:
                        print('It will be chilly on ' + clothing_day + ' (' + temp + 'F), try to dress warmly')
                        break

        elif clothing_option == 'No':
            print('Have a nice day!')
            break

        break

        return True

weather_greeting()
clothing()
