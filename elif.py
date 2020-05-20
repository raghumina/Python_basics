# We are now use the elif conditions 

# example 1 
print("Where are you from ,# please write in upper cases ")
print("""the available countries in our list are 
India,
England,
France,
Germany""")
country = input()
if country == "India":
    print("Namste")
elif country.upper() == "England":
    print("hello")
elif country.upper() == "France":
    print("Bonjour")   
elif country.upper() == "Germany":
    print("Guten Tag")      
else:
    print("Where are you from")