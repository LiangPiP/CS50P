camel_name=input("camelCase: ")
snake_name=""
for c in camel_name:
    if c.isupper():
        snake_name+="_"+c.lower()
    else:
        snake_name+=c
print("snake_case",snake_name)