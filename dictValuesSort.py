dict1 = {}

while True:
    key = input("enter keys: ")
    if key == 'q':
        break
    value = input("enter values: ")
    dict1[key] = value

print(dict1)

values = dict1.values()
sorted_values = sorted(values)
print(sorted_values)