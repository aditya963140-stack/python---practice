name = input("Enter your name: ")
math = int(input("Enter the math marks: "))
python = int(input("Enter the python marks: "))
english = int(input("Enter the english marks: "))
total_marks = math + python + english
percentage = (total_marks / 300) * 100
if math >=33 and python >=33 and english >=33:
    print("pass")
else:
    print("fail")
print("name: ", name)
print("math marks: ", math)
print("python marks: ", python)
print("english marks: ", english)
print("total marks: ", total_marks)
print("percentage: ", percentage) 
    