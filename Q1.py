dict1 = eval(input("Enter first dictionary: "))
dict2 = eval(input("Enter second dictionary: "))
dict3 = eval(input("Enter third dictionary: "))

dict4 = {}
dict4.update(dict1)
dict4.update(dict2)
dict4.update(dict3)

print("Concatenated dictionary:", dict4)
