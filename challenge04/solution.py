# 5 digits
i = 1

list_numbers = []

# Ascending order
def check_ascend(n):
    n = str(n)
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True

for number in range(10000, 99999):
    # Number 3 appears 2 times min
    if str(number).count("5") < 2:
        continue
    if not check_ascend(number):
        continue
    list_numbers.append(number)
    i += 1

print("Solution:", str(len(list_numbers)) + "-" + str(list_numbers[55]))