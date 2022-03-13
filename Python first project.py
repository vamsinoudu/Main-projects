print("Welcome to Bistro")
print("This is our Ala cart menu.")

# menu_1 = input("Would you like to have Vegetarian:")
# menu_2 = input("Would you like to have NON-Vegetarian:")
# a = "veg_biryani"
veg_biryani = "Allergen info are , contains Gluten,contains soybeans ,contains dairy , Traces of Tree-nuts."
veg_biryani_cost = 150
# b = "veg_sandwich"
veg_sandwich = "Allergen info are ,contains Gluten,Traces of soybeans , contains dairy . "
veg_sandwich_cost = 120
# c = "veg_ball_platter"
veg_ball_platter = "Allergen info are ,contains Gluten , Traces of Egg."
veg_ball_platter_cost = 200
# d = "cinnamon_bun"
cinnamon_bun = "Allergen info are ,contains Gluten ,contains soybeans , contains dairy , Traces of Tree-nuts ," \
               "Traces of " \
               "Egg, Traces of Sulphite. "
cinnamon_bun_cost = 60
# e = "pizza_puff"
pizza_puff = "Allergen info are ,contains Gluten,contains soybeans , contains dairy , Traces of Tree-nuts ,Traces of " \
             "Egg ,Traces of Sulphite."
pizza_puff_cost = 80
# f = "salmon_fillet "
salmon_fillet = "Allergen info are,contains Seafood."
salmon_fillet_cost = 650
# g = "chicken_nuggets"
chicken_nuggets = "Allergen info are,contains Gluten+contains Dairy,contains soybeans."
chicken_nuggets_cost_1 = 170
chicken_nuggets_cost_2 = 250
# h = "chicken_meatballs"
chicken_meatballs = "Allergen info are,Traces of Gluten,Traces of Egg+contains soybeans+contains Dairy."
chicken_meatballs_cost = 250
# i = "Biryani_salmon_fillet"
Biryani_salmon_fillet = "Allergen info are,contains seafood ,Traces of Tree-nuts."
Biryani_salmon_fillet_cost = 850
# j = "coffee"
coffee_cost = 60
# k = "sparkling_waters_cost"
sparkling_waters_cost = 60

order = {"1": "Veg biryani",
         "2": "veg sandwich",
         "3": "veg_ball platter",
         "4": "Cinnamon bun",
         "5": "Pizza puff",
         "6": "Salmon fillet",
         "7": "Chicken Nuggets",
         "8": "Chicken Meatballs",
         "9": "Salmon Biryani",
         "10": "Filter coffee",
         "11": "Sparkling water ",
         "12": "Total bill"
         }
print(order)

option = int(input("Enter your option :"))
totalBillAmount = 0
while option != 0:

    if option == 1:
        print("veg Biryani", ':$', veg_biryani_cost)
        print(veg_biryani)
        Quantity = int(input("Enter how much quantity you want: "))
        bill1 = Quantity * veg_biryani_cost
        totalBillAmount += bill1
        print('Bill Amount is $', bill1)
        print("If you want order more please continue,or if you want pay the total bill the press 12.")
        if option == 12:
            print("total bill amount is ", totalBillAmount)
            break


    elif option == 2:
        print("Veg sandwich ", ':$', veg_sandwich_cost)
        print(veg_sandwich)
        Quantity = int(input("Enter how much quantity you want: "))
        bill2 = Quantity * veg_sandwich_cost
        totalBillAmount += bill2
        print('Bill Amount is $', bill2)
        print("If you want order more please continue,or if you want pay the total bill the press 12.")
        if option == 12:
            print("total bill amount is ", totalBillAmount)
            break

    elif option == 3:
        print("veg_ball platter ", ':$', veg_ball_platter_cost)
        print(veg_ball_platter)
        Quantity = int(input("Enter how much quantity you want: "))
        bill3 = Quantity * veg_ball_platter_cost
        totalBillAmount += bill3
        print('Bill Amount is $', bill3)
        print("If you want order more please continue,or if you want pay the total bill the press 12.")
        if option == 12:
            print("total bill amount is ", totalBillAmount)
            break

    elif option == 4:
        print("Cinnamon bun", ': $', cinnamon_bun_cost)
        print(cinnamon_bun)
        Quantity = int(input("Enter how much quantity you want: "))
        bill4 = Quantity * cinnamon_bun_cost
        totalBillAmount += bill4
        print('Bill Amount is $', bill4)
        print("If you want order more please continue,or if you want pay the total bill the press 12.")
        if option == 12:
            print("total bill amount is ", totalBillAmount)
            break

    elif option == 5:
        print("Pizza puff ", ':$', pizza_puff_cost)
        print(pizza_puff)
        Quantity = int(input("Enter how much quantity you want: "))
        bill5 = Quantity * pizza_puff_cost
        totalBillAmount += bill5
        print('Bill Amount is $', bill5)
        print("If you want order more please continue,or if you want pay the total bill the press 12.")
        if option == 12:
            print("total bill amount is ", totalBillAmount)
            break

    elif option == 6:
        print("Salmon fillet", ':$', salmon_fillet_cost)
        print(salmon_fillet)
        Quantity = int(input("Enter how much quantity you want: "))
        bill6 = Quantity * salmon_fillet_cost
        totalBillAmount += bill6
        print('Bill Amount is $', bill6)
        print("If you want order more please continue,or if you want pay the total bill the press 12.")
        if option == 12:
            print("total bill amount is ", totalBillAmount)
            break

    elif option == 7:
        print("If you want 12 pieces press 12")
        print("If you want 18 pieces press 18 ")
        Quantity = int(input("Enter how much quantity you want: "))
        if Quantity == 12:
            print("Chicken Nuggets", '12 pieces', ':$', chicken_nuggets_cost_1)
            bill7 = chicken_nuggets_cost_1
            totalBillAmount += bill7
            print('Bill Amount is $', bill7)
            print("If you want order more please continue,or if you want pay the total bill the press 12.")
            if option == 12:
                print("total bill amount is ", totalBillAmount)
                break

        elif Quantity == 18:
            print("Chicken Nuggets ", '18 pieces', ':$', chicken_nuggets_cost_2)
            bill8 = chicken_nuggets_cost_2
            totalBillAmount += bill8
            print('Bill Amount is $', bill8)
        print(chicken_nuggets)
        print("If you want order more please continue,or if you want pay the total bill the press 12.")
        if option == 12:
            print("total bill amount is ", totalBillAmount)
            break

    elif option == 8:
        print("Chicken meatball ", ':$', chicken_meatballs_cost)
        print(chicken_meatballs)
        Quantity = int(input("Enter how much quantity you want: "))
        bill8 = Quantity * chicken_meatballs_cost
        totalBillAmount += bill8
        print('Bill Amount is $', bill8)
        print("If you want order more please continue,or if you want pay the total bill the press 12.")
        if option == 12:
            print("total bill amount is ", totalBillAmount)
            break

    elif option == 9:
        print("Salmon Biryani", ':$', Biryani_salmon_fillet_cost)
        print(Biryani_salmon_fillet)
        Quantity = int(input("Enter how much quantity you want: "))
        bill9 = Quantity * Biryani_salmon_fillet_cost
        totalBillAmount += bill9
        print('Bill Amount is $', bill9)
        print("If you want order more please continue,or if you want pay the total bill the press 12.")
        if option == 12:
            print("total bill amount is ", totalBillAmount)
            break

    elif option == 10:
        print("Filter coffee", ':$', coffee_cost)
        Quantity = int(input("Enter how much quantity you want: "))
        bill10 = Quantity * coffee_cost
        totalBillAmount += bill10
        print('Bill Amount is $', bill10)
        print("If you want order more please continue,or if you want pay the total bill the press 12.")
        if option == 12:
            print("total bill amount is ", totalBillAmount)
            break

    elif option == 11:
        print("Sparkling waters ", ':$', sparkling_waters_cost)
        Quantity = int(input("Enter how much quantity you want: "))
        bill11 = Quantity * sparkling_waters_cost
        totalBillAmount += bill11
        print('Bill Amount is $', bill11)
        print("If you want order more please continue,or if you want pay the total bill the press 12.")
        if option == 12:
            print("total bill amount is ", totalBillAmount)
            break

    else:

        print("Total amount of order is ", totalBillAmount)
        print("your food is on the way , Enjoy your meal!")

        break
    option = int(input("Enter your option :"))
feedback = int(input("please rate us from 1 to 5 : "))
while feedback != 0:
    print("Thank you for providing feedback\n", "Its will help us to serve better.")
    break
