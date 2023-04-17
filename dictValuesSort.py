dict1 = {}

while True:
    key = input("enter keys: ")

    if key == 'q':                 # used to break out of the while loop
        break
    value = input("enter values: ")
    dict1[key] = value

print(dict1)

print("----------------------------------------")

values = dict1.values()
sorted_values = sorted(values)
print(sorted_values)