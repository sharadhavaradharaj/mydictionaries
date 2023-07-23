person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# print out the name of the second child
print(person['children'] [1])
print(person["pets"]["cat"])

# print out the name of the cat


# use a loop to print out the names of each child
#here child is the index
for child in person["children"]:
    print(child)




# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido
# here i and j are the items of pet

mydict = person["pets"]
print(mydict)
for i,j in person.items():
    print(i)
    print(j)
    print(f"the type of the pet is: {i} and the name of he pet is:{j}")

#or 
for i,j in person["pet"].items():
    print(f"the type of the pet is: {i} and the name of he pet is:{j}")