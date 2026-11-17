import os
import subprocess
from datetime import datetime
from tabulate import tabulate

"""
RecipenManager: Build a console-based recipe manager. Users should be able to add recipes, view recipes, search for recipes by ingredients, and perform other recipe-related operations

"""

recipe = []

def recipe_Task():
  """
  Tasks to perform

  """
  print("Action: TASKS TO PERFORM...")
  print("1. Add a recipe")
  print("2. View all recipes")
  print("3. Search for a recipe by ingredients")
  print("4. Delete a single recipe")
  print("5. Delete all recipes")
  print("6. Update a single recipe")
  print("7. Exit")


def clear_Console():
  """
  Clear a console
shell=True means to run the code inside shell environment
  """
os.system("cls" if os.name == "nt" else "clear")


def add_a_recipe():
  """
  Add a recipe to the list

  """
  food_type = input("Enter food type: ").strip().lower()
  if check_food_exist(food_type):
    print(f"{food_type} recipe already exist")
  elif len(food_type) < 3:
    print("Recipe should be descriptive")
  else:
    add_food = {}
    add_food["name"] = food_type
    add_food["ingredients"] = input("Enter ingredients separated by a comma: ").strip().split(",")
    add_food["cooking_step"] = input("Enter steps in cooking the food separated by a comma: ").strip().split(",")
    add_food["date"] = datetime.today().strftime("%Y-%m-%d")

      
    recipe.append(add_food)
    print("Recipe Added Successfully")
    return recipe


def check_food_exist(name):
  for add_food in recipe:
    if add_food["name"] == name:
      return True
  return False


def view_all_recipes():
  """
  View all recipes in the recipe 

  list in tabular form
  """
  try:
    #check if recipe exists
    if recipe:

      #create an empty array to store recipe list items with index
      table = []

      #loop through the recipe
      for num, item in enumerate(recipe, 1):
        #num here is the serial number of the recipe items
        #item here is the actual recipe items itself
        table.append([
          num,
          item["name"],
          item["ingredients"],
          item["cooking_step"],
          item["date"]
        ])
        print(
          tabulate(
            table,
            headers=[
            "S/N",
            "FOOD_TYPE",
            "INGREDIENTS_USED",
            "COOKING_STEP",
            "DATE"
          ],
          tablefmt="grid"
        )
      )

    else:
      print("No recipe is found in the list")
  except TypeError:
    print("Error: Date object is not iterable")



def search_for_a_recipe_ingredients():
  """
  Ingredients used to cook the recipe, are used to
  search for a recipe type. Make sure you remember
  the ingredients used. View all recipes incase you
  have forgotten.
  """
  ingredient = input("Enter ingredients used: ").strip().split(",")
  for item in recipe:
    if item["ingredients"] == ingredient:
      print("Recipe Type Found is: ",item["name"])
      break
  else:
    print("No recipe found in the list")




def Delete_a_single_recipe():
  """
  Delete a single recipe using recipe serial number
  """
  try:
    #find the item to remove using its index number
      recipe_num = int(input("Enter recipe num to delete: "))
      for num,item in enumerate(recipe, 1):
        if num == recipe_num:
          recipe.remove(item)
          print(f"{item['name']} deleted succssfully")
          break # Stops the loop immediately after finding and deleting the recipe
      else:
        print("Item number not found")
  except ValueError:
    print("Input must be an integer")



def Delete_all_recipes():
  """
  Delete all items in the recipe list
  """
  if recipe:
    recipe.clear()
    print("Items cleared successfully")
  else:
    print("Items not found")



def Update_a_single_recipe_type():
  """
  Change a single recipe type
  """
  try:
    food_type_index_num = int(input("Enter recipe type index number to replace existing recipe: "))
    for num, item in enumerate(recipe, 1):
      if num == food_type_index_num:
        item["name"] = input("Enter new recipe: ").strip().lower()
        item["ingredients"] = input("Enter new ingredients: ").strip().split(",")
        item["cooking_step"] = input("Enter new cooking step: ").strip().split(",")
        item["date"] = datetime.today().strftime("%Y-%m-%d")

        print("Recipe updated successfully")
        break
    else:
      print("No such index number found in the recipe list of items")
  except ValueError:
    print("Input must be an integer not a string")


def exit_action():
  """
  Action for exiting the task
  """
  print("Task has finished...")




def main():
  """
  The execution guard
  """
  while True:
    clear_Console()
    recipe_Task()
    num = input("Enter a number to perform an action: ")

    if num == "1":
      add_a_recipe()
      clear_Console()
      input("Press enter to continue...")

    elif num == "2":
      view_all_recipes()
      clear_Console()
      input("Press enter to continue...")

    elif num == "3":
      search_for_a_recipe_ingredients()
      clear_Console()
      input("Press enter to continue...")

    elif num == "4":
      Delete_a_single_recipe()
      clear_Console()
      input("Press enter to continue...")

    elif num == "5":
      Delete_all_recipes()
      clear_Console()
      input("Press enter to continue...")

    elif num == "6":
      Update_a_single_recipe_type()
      clear_Console()
      input("Press enter to continue...")

    elif num == "7":
      exit_action()
      clear_Console()
      input("Please Enter a num greater than 7 to terminate tasks...")

    else:
      print("Task terminating....")
      print("Thanks for a job well done!!!")
      print("Please come back later to perform another tasks......")
      break
      

#The Execution Guard
if __name__ == "__main__":
  main()