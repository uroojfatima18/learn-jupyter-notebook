name:str ="urooJ faTima"

#object.method()
#object.attribute

print(name .capitalize())
print(name .casefold())
print(name .center (25,  '*'))
print(name .upper())
print(name .lower())
print(name .title())



print([i for i in dir(name) if not i.startswith('_')])
