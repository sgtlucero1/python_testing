import random
import tkinter as tk
from tkinter import ttk

def suggest_meal():
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
    
    meal_type = meal_type_var.get()
    food = food_var.get().lower()
    
    if meal_type == 'cook' and food in meal_options:
        random_meal = random.choice(meal_options[food])
        result_label.config(text=f'Suggested meal: {random_meal}')
    elif meal_type == 'takeout' and food in takeout_options:
        random_meal = random.choice(takeout_options[food])
        result_label.config(text=f'Suggested meal: {random_meal}')
    else:
        result_label.config(text='Invalid input. Check your options.')

def main():
    global meal_type_var, food_var, result_label

    # Create the main window
    root = tk.Tk()
    root.title('Meal Planner')
    root.geometry('400x300')

    # Create the user interface
    ttk.Label(root, text='Do you want to cook or get takeout?').pack(pady=10)
    meal_type_var = tk.StringVar()
    ttk.Radiobutton(root, text='Cook', variable=meal_type_var, value='cook').pack()
    ttk.Radiobutton(root, text='Takeout', variable=meal_type_var, value='takeout').pack(pady=10)

    ttk.Label(root, text='Enter a food type:').pack()
    food_var = tk.StringVar()
    ttk.Entry(root, textvariable=food_var).pack(pady=10)

    ttk.Button(root, text='Suggest Meal', command=suggest_meal).pack(pady=10)

    result_label = ttk.Label(root, text='')
    result_label.pack(pady=10)

    # Start the main event loop
    root.mainloop()

if __name__ == '__main__':
    main()