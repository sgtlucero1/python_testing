import random

def main():
    # Predefined meal options
    meal_options = {
        'chicken': ['Chicken Parmesan', 'Chicken Curry', 'Grilled Chicken','BBQ Chicken', 'Fried Chicken', 'Chicken Pot Pie', 'Sweet Chili Chicken', 'Chicken Strips' ],
        'beef': ['Beef Stroganoff', 'Tacos', 'Beef and Broccoli', 'Beef Stir Fry', 'Burgers', 'Steak Sandwiches', 'Shepards Pie', 'BBQ Short Ribs', 'Galbi', 'Chicken Fried Steak'],
        'pork': ['Pulled Pork', 'Pork Chops', 'Baked Pork Tenderloin', 'Pork Fried Rice', 'BBQ Ribs', 'Fried Tenderloin Sandwiches', ],
        'fish': ['Grilled Salmon', 'Fish Tacos', 'Baked Cod', 'Fish and Chips'],
        'pasta': ['Spaghetti', 'Pasta Bake', 'Lasagna', 'Chicken Alfredo', 'Stuffed Shells'],
        'none': ['Brinner', 'Ramen', 'Grilled Cheese and Tomato Soup']
    }
    
    takeout_options = {
        'pizza': ['Dominos', 'Pizza Hut', 'IMOs', 'Mellow Mushroom'],
        'asian': ['88 China', 'New China', 'Happy China', 'Thai Kitchen'],
        'fastfood': ['McDonalds', 'Wendys', 'Rallys', 'Five Guys', 'Lions Choice', 'Popeyes', 'Burger King', 'Taco Bell', 'Sonic', 'Jack in the Box' ],
        'american': ['Applebees', 'Outback', 'B Dubs', 'Red Robin' ],
        'mexican': ['Jose Penos', 'Las Margaritas' ]
        
    }

    # Get user input for meal type
    meal_type = input('Do you want to cook or get takeout? (Enter "cook" or "takeout"): ').lower()

    # Check if the meal type is valid
    if meal_type == 'cook':
        # Get user input for primary food
        food = input('Enter a food type(chicken, beef, pork, fish, pasta or none): ').lower()

        # Check if the food is valid and available in the meal options
        if food in meal_options:
            # Select a random meal
            random_meal = random.choice(meal_options[food])
            print(f'Suggested meal: {random_meal}')
        else:
            print('Invalid input. Enter a food type(chicken, beef, pork, fish, pasta or none).')
    elif meal_type == 'takeout':
        # Get user input for takeout food
        food = input('Enter a primary food type (pizza, burgers, asian, etc): ').lower()

        # Check if the food is valid and available in the takeout options
        if food in takeout_options:
            # Random takeout options
            random_meal = random.choice(takeout_options[food])
            print(f'Suggested meal: {random_meal}')
        else:
            print('Invalid input. Please enter a food type')
    else:
        print('Invalid input. Please enter "cook" or "takeout".')

if __name__ == '__main__':
    main()
