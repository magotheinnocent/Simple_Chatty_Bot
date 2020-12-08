deposit = int(input())
years = 0
rate = 1.071
while 50000 < deposit < 700000:
    deposit = deposit * rate
    years += 1

print(years)
