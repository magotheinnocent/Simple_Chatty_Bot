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
while i <= number:
    print(f"{i}!")
    i += 1
print("Let's test your programming knowledge.")
print("Why do we use methods?")
answer_1 = list("1. To repeat a statement multiple times.")
answer_2 = list("2. To decompose a program into several small subroutines.")
answer_3 = list("3. To determine the execution time of a program.")
answer_4 = list("4. To interrupt the execution of a program.")
answer = input()
while answer != "2":
        print('Please, try again.')
        answer = input()
if answer == "2":
    print("Completed, have a nice day!")
print("Congratulations, have a nice day!")
