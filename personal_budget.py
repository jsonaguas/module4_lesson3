class BudgetCategory:
    def __init__ (self, category, amount):
        self.__category = category
        self.__amount = amount

    def get_category(self):
        return self.__category
    
    def get_amount(self):
        return self.__amount


    def set_amount(self, amount):
        self.__amount = amount
        if self.__amount < 100:
            print("Warning: You are running low on funds")

    
    

def add_category(budget):
    category = input("Enter the category: ").lower()
    amount = float(input("Enter the amount: "))
    budget[category] = BudgetCategory(category, amount)
    print (f"Category {category} added with ${amount}")
    return budget

def add_expense(budget):
    category = input("Enter the category: ").lower()
    if category in budget:
        expense = float(input("Enter the expense: "))
        if expense <= budget[category].get_amount():
            budget[category].set_amount(budget[category].get_amount() - expense)
            print(f"You have ${budget[category].get_amount()} left in this category")
        else:
            print(f"Expense exceeds the amount by ({expense} - {budget[category].get_amount()})")
    else:
        print("Category not found")
 

def display_category_summary(budget):
    for category in budget:
        print(f"For the category {budget[category].get_category()}, you have ${budget[category].get_amount()} left")
    if len(budget) == 0:
        print("No categories added yet")

def view_categories(budget):
    for category in budget:
        print(f"{category} - ${budget[category].get_amount()}")


def main():
    budget = {}
    while True:
        print('''
              1. Add a category
              2. Add an expense
              3. Display category summary
              4. Quit
              5. View categories
              ''')
        choice = input("Enter your choice: ")
        if choice == "1":
            add_category(budget)
        elif choice == "2":
            add_expense(budget)
        elif choice == "3":
            display_category_summary(budget)
        elif choice == "4":
            break
        elif choice == "5":
            view_categories(budget)
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()
