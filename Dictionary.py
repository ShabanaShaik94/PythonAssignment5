# Creating a dictionary and finding name found or not

Name =input("Enter the student's Name: ")
dictionary ={'Alice':'85','John':'90','Noori':'60'}

# Check if the name exists in the dictionary
if Name in dictionary:
    print(f"{Name}'s marks : {dictionary[Name]}")
else:
    print(f"Student not found.")