# put your python code here
input_1 = int(input()) * 3600  # Hour
input_2 = int(input()) * 60    # Min
input_3 = int(input())         # Second
input_4 = int(input()) * 3600  # Hour
input_5 = int(input()) * 60    # Min
input_6 = int(input())         # Second

time1 = input_1 + input_2 + input_3
time2 = input_4 + input_5 + input_6

answer = time2 - time1
print(answer)