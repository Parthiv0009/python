# dict = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", "list of fact and figures "]
# }
# print (dict)


# room = { "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
# print (type(room) , room)
# print (len(room))

data = {}

x = (input("Enter Your Math Marks:"))
data.update({"math" : x })

y = (input("Enter Your Gujrati Marks:"))
data.update({"gujrati" : y })

z = (input("Enter Your English Marks:"))
data.update({"english" : z })

print (data)
 