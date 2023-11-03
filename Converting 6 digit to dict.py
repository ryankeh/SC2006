dict = {}
typeString = 100101
types = ['Micro-USB','Lightning','USB-C cable','USB-C port','USB port','Lockable']
for type in types:
    dict[type] = int(typeString%10)
    typeString = typeString/10
print(dict)

types = ['Lockable','USB port','USB-C port','USB-C cable','Lightning','Micro-USB']
finalValue = 0
for type in types:
    value = int(dict.pop(type))
    finalValue = finalValue*10 + value
print(finalValue)
