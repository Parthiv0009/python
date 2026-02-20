# movies = []
# mov = input("Enter Movie 1:")
# movies.append(mov)
# mov = input("Enter Movie 2:")
# movies.append(mov)
# mov = input("Enter Movie 3:")
# movies.append(mov)


# print (movies)

 
 
list1 = [1,2,1,2]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print ("palindrom")
else:
    print ("not a palindrom")


    

grade  = ("C", "D", "A", "A", "B", "B", "A")
print (grade.count("A"))



grade  = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print (grade)
