import static_info

def check_cash(flavour):
    
    print("please insert coins:")
    quarters = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    nickles = float(input("Nickles: "))
    pennies = float(input("Pennies: "))

    change = 0
    cash_given = quarters*static_info.QUARTER + dimes*static_info.DIME + nickles*static_info.NICKLE + pennies*static_info.PENNY
    cash_required = static_info.MENU[f"{flavour}"]["price"]

    if cash_given >= cash_required:
        static_info.CASH += cash_required
        change = cash_given - cash_required
        return change
    else:
        print("not enough money no coffee for you")
        return None

def check_ingredients(flavour):
    if static_info.WATER >= static_info.MENU[f"{flavour}"]["ingredients"]["Water"] and static_info.MILK >= static_info.MENU[f"{flavour}"]["ingredients"]["Milk"] and static_info.COFFEE >= static_info.MENU[f"{flavour}"]["ingredients"]["Coffee"]:
        return True
    else:
        print("Not enough ingredients")

def make_coffee(flavour):
    static_info.WATER -= static_info.MENU[f"{flavour}"]["ingredients"]["Water"]
    static_info.COFFEE -= static_info.MENU[f"{flavour}"]["ingredients"]["Coffee"]
    static_info.MILK -= static_info.MENU[f"{flavour}"]["ingredients"]["Milk"]
    print("Here is your coffee☕")
           
def generate_report():
    print("\n--- Report ---")
    print(f"Water: {static_info.WATER}ml")
    print(f"Milk: {static_info.MILK}ml")
    print(f"Coffee: {static_info.COFFEE}g")
    print(f"Cash: ${static_info.CASH:.2f}")
    print("--------------\n")

def main():
    change = 0
    print("Welcome to the coffee shop")
    while True:
        option = input("What flavour of coffee you want(espresso/latte/cappucino\nYour Choice): ")
        if option == "off":
            break
        elif option != "report":
            flavour = option
            change = check_cash(flavour)
            if change is not None:
                if check_ingredients(flavour):
                    make_coffee(flavour)
                    if change > 0:
                        print(f"Here is your change ${change:.2f}")
                else:
                    print("not enough ingredients")        
        elif option == "report":    
            generate_report()

if __name__ == "__main__":
    main()