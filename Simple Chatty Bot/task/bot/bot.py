print("Hello! My name is Aid.")
print("I was created in 2020.")
print("Please, remind me your name.")
name = str(input())
print(f"What a great name you have, {name}!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7")
remainder1 = int(input())
remainder2 = int(input())
remainder3 = int(input())
age = (remainder1 * 70
        + remainder2 * 21
        + remainder3 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want")
number=int(input())
i = 0
while i < number:
    print(f"{i}!")
    i += 1
print("Completed, have a nice day!")