products = ["Sankofa Foods","Jamestown Coffee","Bioko Chocolate","Blue Skies Ice Cream","Fair Afric Chocolate",\
            "Kawa Moka Coffee","Aphro Spirit","Mensado Bissap","Voltic"]
prices = [30,25,40,20,20,35,45,50,35]
last_week = [2,3,5,8,4,4,6,2,9]

# 1. Total average price
total_price_amount = 0
for price in prices:
    total_price_amount =  total_price_amount + price

average_price = round(total_price_amount/len(prices),2)
print(f"Total average price is ${average_price}")

#Create a new price list that reduces the old prices by $5
new_prices = []
for index, price in enumerate(prices,1):
    new_prices.append(price - 5)
print(new_prices)

#Total revenue generated from sales
total_revenue_gen = 0

for index,price in enumerate(prices):
    total_revenue_gen = total_revenue_gen + last_week[index] * price
print(total_revenue_gen)

# Average daily revenue generated from the products
ave_daily_revenue = round(total_revenue_gen/7,2)
print(f"Total average daily revenue ${ave_daily_revenue}")

#Based on the new prices, which products are less than $30
selected_products = []
for index,price in enumerate(new_prices):
    if price < 30:
        selected_products.append(products[index])
print(selected_products)