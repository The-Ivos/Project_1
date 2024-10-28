from random import randint

# CREATING THE FIRST NUMBER WHICH CANNOT BE 0
first_num = str(randint(1,9))
pre_nums = []
trash_nums = []

# CREATING THE REST (3) UNIQUE NUMBERS
while len(pre_nums) != 3:
    a = randint(0,9)
    print(first_num)
    print(pre_nums)
    print(trash_nums)
    print(a)
    print(len(pre_nums))
    wait = input("wait...")
    if str(a) in pre_nums or str(a) == str(first_num):
        trash_nums.append(a) 
    else:
        pre_nums.append(str(a))
print("====")
print(first_num)
print(pre_nums)
print(trash_nums)