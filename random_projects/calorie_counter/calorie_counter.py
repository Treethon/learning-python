import data
from datetime import date

'''
Keep a dictionary of items I consume, whether they are home cooked, bought or otherwise.  If the item is not in the dictionary, add it.
caloric_items dictionary has a key/value in the format of: {home_cheeseburger: 200} or {mcd_cheeseburger: 400}
Keep a dictionary of calories eaten per day
daily_calories dictionary has a key/value in the format of: {1/25: 2300} or {1/26: 2500}
'''

def add_to_daily_calories(caloric_item):
    # Pass a string for an item.  use caloric_item_check function to see for if the item already exists. 
    # If it does, add to your daily calories. 
    caloric_item_check(caloric_item)
    today = date.today()
    return caloric_item

def caloric_item_check(item):
    # Check the caloric_item dictionary to see if the item already exists.
    # If the item exists, return the value (calories).
    # If it does not, add the item and calories.
    if item in data.caloric_items:
        return data.caloric_items.item.calories
    else:
        ## Prompt for # of calories, return amount of calories after entering into caloric_items.
        calorie_input = input('Please enter the calories of ' + item + ': ')
        data.caloric_items['item'] = item
        data.caloric_items['calories'] = int(calorie_input)
        return data.caloric_items.item.calories

def print_daily_calories(day):
    # Pass a day paramater such as 2026-01-23.  Return the calories on that day.
    if day in data.daily_calories:
        print(data.daily_calories.calories)
    else:
        print('Error!  No caloric intake for this day.')