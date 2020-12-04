# put your python code here
days = int(input())
food_cost_daily = int(input()) * days
flight_return = int(input()) * 2
hotel_cost_nightly = int(input()) * (days - 1)

total_cost = food_cost_daily + flight_return + hotel_cost_nightly
print(total_cost)