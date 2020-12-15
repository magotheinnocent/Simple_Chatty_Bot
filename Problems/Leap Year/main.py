# put your python code here
def check_leap(year):
    if year / 4 and year / 400:
        return print("Leap")
    else:
        return print("Ordinary")