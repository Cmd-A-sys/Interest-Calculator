
def type():
    try:
        investment_type = (input("What type of interest do you want to invest with (1-2):\n1.Compound\n2.Simple\n"))
        if investment_type == '1':
            return 'compound'
        elif investment_type == '2':
            return 'simple'
    except ValueError:
        print("Please enter only 1 or 2")
        type()
def amount():
    try:
        return float(input("Please enter the initial investment amount: "))
    except ValueError:
        print("Sorry. Invalid input")
        amount()
def percent():
    try:
        return float(input("Please enter the percentage amount here: "))
    except ValueError:
        print("Sorry invalid input")
        percent()
def currencies():
    currency = (input("Please enter the currency to be used (Type only short forms; INR, USD, GBP, EUR, JPY): "))
    if currency.upper() == 'INR':
        currency = '₹'
    elif currency.upper() == 'USD':
        currency = '$'
    elif currency.upper() == 'GBP':
        currency = '£'
    elif currency.upper() == 'EUR':
        currency = '€'
    elif currency.upper() == 'JPY':
        currency = '¥'
    else:
        print('Sorry, that currency is currently unsupported')
        currencies()
    return currency
am = amount()
cu = currencies()
ty = type()
pe = percent()
def compound(pe,am,cu):
    i = 0
    multiplier = 1+(pe/100)
    years = float(input("How many years do you plan on keeping this investment: "))
    year_mult = multiplier ** years
    value_final = am * year_mult
    print("Your investment will be worth {:.2f}{} at the end of the term".format(value_final,cu))
    restart = (input("Click 'm' to restart or Enter to quit\n"))
    if restart == 'm':
        restarting()
    elif restart == "":
        print("Finished")
        quit()
    restart = (input("Click 'm' to restart or Enter to quit\n"))
    if restart == 'm':
        restarting()
    elif restart == "":
        print("Finished")
        quit()
def simple(pe,am,cu):
    years = float(input("How many years do you plan on keeping this investment: "))
    multiplier = pe / 100
    total = am + (am*years*multiplier)
    print("Your investment will be worth {:.2f}{} at the end of the term".format(total, cu))
    restart = (input("Click 'm' to restart or Enter to quit\n"))
    if restart == 'm':
        restarting()
    elif restart == "":
        print("Finished")
        quit()
    if restart == 'm':
        restarting()
    elif restart == "":
        print("Finished")
        quit()
def restarting():
    am = amount()
    cu = currencies()
    ty = type()
    pe = percent()
    conf = confirmation(am,cu,ty,pe)
    while conf != 1:
        if conf == 2:
            am = amount()
            conf = confirmation(am,cu,ty,pe)
        elif conf == 3:
            cu = currencies()
            conf = confirmation(am,cu,ty,pe)
        elif conf == 4:
            ty = type()
            conf = confirmation(am,cu,ty,pe)
        elif conf == 5:
            pe = percent()
            conf = confirmation(am,cu,ty,pe)
        else:
            print("Invalid input. Enter numbers 1-5.")
            confirmation()
    if conf == 1:
        if ty == 'compound':
            compound(am, cu, pe)
        elif ty == 'simple':
            simple(am, cu, pe)
def confirmation(am,cu,ty,pe):
    try:
        confirm = int(input("You have invested {:,}{}, using {} interest at {}%. Would you like to (1-5)\n"
                    "1.Confirm this amount\n"
                    "2.Change the Amount\n"
                    "3.Change the currency\n"
                    "4.Change type of interest\n"
                    "5.Change the percentage rate of interest\n".format(am,cu,ty,pe)))
        return confirm
    except ValueError:
        print("Enter numbers 1 through 5")
        confirmation(am,cu,ty,pe)

conf = confirmation(am,cu,ty,pe)

while conf != 1:
    if conf == 2:
        am = amount()
        conf = confirmation(am,cu,ty,pe)
    elif conf == 3:
        cu = currencies()
        conf = confirmation(am,cu,ty,pe)
    elif conf == 4:
        ty = type()
        conf = confirmation(am,cu,ty,pe)
    elif conf == 5:
        pe = percent()
        conf = confirmation(am,cu,ty,pe)
    else:
        print("Invalid input. Enter numbers 1-5.")
        confirmation(am,cu,ty,pe)
if conf == 1:
    if ty == 'compound':
        compound(am,cu,pe)
    elif ty == 'simple':
        simple(am,cu,pe)