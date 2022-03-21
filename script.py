import pandas as pd   #type: ignore

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
# Columns are times of each step in the funnel above "step"_time

visits_cart = pd.merge(visits, cart, how = "left")
#print(visits_cart)

# How many total visitors did the website recieve?

total_visits = len(visits_cart)
print(total_visits) # There are 2000 datapoints in the visits_cart dataframe

# How many visitors did not add an item to their cart?

visit_no_cart = visits_cart['cart_time'].isna().sum()
print(visit_no_cart) # 1652 visitors did not add an item to their cart

# What percentage of visitors did not add an item to their cart?

print(float(visit_no_cart) / total_visits) # 82.6 percent of visitors did not add an item to their cart

# What is the total percentage of visitors who add items to their cart but did not proceed to checkout?

cart_checkout = pd.merge(cart, checkout, how = "left")
#print(cart_checkout)

total_carts = len(cart_checkout)
print(total_carts)
cart_no_checkout = cart_checkout['checkout_time'].isna().sum()
print(cart_no_checkout)

checkout_percent = float(cart_no_checkout) / total_carts
print(checkout_percent) # 25.3 percent of visitors that add an item to their cart do not proceed to checkout

# What percentage of visitors proceeded to checkout but did not make a purchase?

checkout_purchase = pd.merge(checkout, purchase, how = "left")
#print(checkout_purchase)

total_checkouts = len(checkout_purchase)
print(total_checkouts)
checkout_no_purchase = checkout_purchase['purchase_time'].isna().sum()
print(checkout_no_purchase)

no_purchase_percent = float(checkout_no_purchase) / total_checkouts
print(no_purchase_percent) # 16.9 percent of visitors who proceed to checkout do not make a purchase

# The step in the funnel in which the lowest percentage of visitors complete is the cart step. The company may consider looking into ways to better advertise their items and make it easier for customers to add the items they like to a cart.

# Merge all the steps of the funnel into one data frame called 'all_data'

all_data = visits\
                .merge(cart, how = "left")\
                .merge(checkout, how = "left")\
                .merge(purchase, how = "left")
print(all_data.head())

# What's the average time from intial vist to final purchase for the website?
all_data['total_time'] = all_data.purchase_time - all_data.visit_time
print(all_data.total_time.mean()) # The average time to purchase is 43 minutes and 53.4 seconds / 00:43:53.36
