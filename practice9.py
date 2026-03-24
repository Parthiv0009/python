with open("sample1.txt","r") as f:
    data = f.read()

new_data = data.replace("python","java")
print(new_data)

with open("sample1.txt","w") as f:
  f.write(new_data)



word = "learning"
with open("sample1.txt","r") as f:
    data = f.read()   
    if(data.find(word) != -1):
       print("found")
    else:
       print("not found")