student = {
    "name" : "Parthiv",
    "subject" : {
            "math" : 98,
            "english" : 99,
            "gujrati": 99

    }
}

# print(list(student.keys()))

# print(list(student.values()))

# pairs = (list(student.items()))
# print (pairs[0])



# print(student.get("name2"))
# print(student["name2"])

student.update({"city" : "ahmdabad"})
print (student)


