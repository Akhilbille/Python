#method 1

def purchase_mobile(price,brand):
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100

    print("Total price of Mobile is "+str(total_price))

def purchase_shoe(price,material):
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price = price + price * tax / 100

    print("Total price of Shoe is "+str(total_price))

purchase_mobile(20000,"Apple")
purchase_shoe(200,"leather")




# Method 2  
def purchase_mobile(price,brand=None):
    if brand=="Apple":
        total_price = price-price*0.1
        return total_price
    else:
        total_price =  price-price*0.05
        return total_price
        
    
def purchase_shoe(price,material=None):
    if material == "leather":
        total_price = price+price*0.05
        return total_price
    else:
        total_price = price+price*0.02
        return total_price
        
    
print('Total price of Mobile is {}'. format(purchase_mobile(20000,"Apple")))
print('Total price of shoe is %d'%( purchase_shoe(500,"leather")))