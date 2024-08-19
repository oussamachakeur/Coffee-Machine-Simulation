# TODO : 1. SETUP ALL THE COFFEE MACHINE FEATURES :

coffe_types= { "espresso":{"ingredient":{ "water" : 50 , 'milk': 000 , 'coffee': 18},"price" : 1.5} ,
               "latte":{"ingredient":{ "water" : 100 , 'milk': 80 , 'coffee': 24},"price" : 2.5} ,
               "capuccino":{"ingredient":{ "water" : 150 , 'milk': 120 , 'coffee': 24},"price" : 3}}
report = {"water":1000 , "milk":1000 , "coffee": 1000 , "Money : RM ": 0}

# TODO : 2. ASKING USER FOR WHAT HE NEEDS

def choice(user_need):
        if user_need == 1:
            type = coffe_types["espresso"]["price"]
            water = coffe_types["espresso"]["ingredient"]["water"]
            milk = coffe_types["espresso"]["ingredient"]["milk"]
            coffee = coffe_types["espresso"]["ingredient"]["coffee"]
            print("great , u chose expresso ")
        elif user_need ==2:
            type = coffe_types["latte"]["price"]
            water = coffe_types["latte"]["ingredient"]["water"]
            milk = coffe_types["latte"]["ingredient"]["milk"]
            coffee = coffe_types["latte"]["ingredient"]["coffee"]
            print("great , u chose latte ")
        elif user_need == 3:
            type = coffe_types["capuccino"]["price"]
            water = coffe_types["capuccino"]["ingredient"]["water"]
            milk = coffe_types["capuccino"]["ingredient"]["milk"]
            coffee = coffe_types["capuccino"]["ingredient"]["coffee"]
            print("great , u chose capuccino ")
        print("please enter ur coins ")
        one_cent = int(input("how many 1 cents(RM 0.01) you inserts:  "))
        five_cent = int(input("how many 5 cents(RM 0.05) you inserts:  "))
        ten_cent = int(input("how many 10 cents(RM 0.1) you inserts:  "))
        fifty_cent = int(input("how many 50 cents you(RM 0.5) inserts:  "))
        total_money = (one_cent/100) + (five_cent/20) + (ten_cent/10) + (fifty_cent / 2)
        if total_money == type:
            print("here is ur coffee , no change left . THANKS ")
            report["Money "] = report["Money "] + type
            report['water'] = report['water'] - water
            report['milk'] = report['milk'] - milk
            report['coffee'] = report['coffee'] - coffee
        elif total_money > type:
            change = float(total_money) - float(type)
            print("here is ur coffee , ur change is: RM" +str(change) + " THANKS")
            report["Money "] = report["Money "] + type
            report['water'] = report['water'] - water
            report['milk'] = report['milk'] - milk
            report['coffee'] = report['coffee'] - coffee
        elif total_money < type:
            print("sorry ur money is not enough")

# TODO : 3. USER INTERFACE
buy = True
while buy ==True:
    user_need = int(input("do u need : 1-espresso , 2- latte , 3-capuccino , 4-report (1/2/3/4): "))
    if user_need == 1 or user_need==2 or user_need ==3 :
        choice(user_need)
    elif user_need == 4:
        print(report)
    staying = int(input("do you wanna buy again or not (1 for stay , 2 for exit) : "))
    if staying == 1:
        continue
    elif staying == 2:
        buy = False


