#sum of (0 to 10)
taken_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = taken_values[-1]
c=(a * (a + 1) / 2)
print(c)

#5 fruits revers
fruits = ("Dragon fruit,Cherry,Mango,Banana,Water melon")  
print("The original tuple is: ", fruits)  
#using slicing  
reversed_fruits = fruits[::-1]  
print("The reversed_fruits is: ", fruits)

# Student Grades
Student_Grades ={"sai":88,"Ganesh":72,"dk":77}
print(Student_Grades)
Student_Grades["chinni"]=92
print(Student_Grades)
Student_Grades["dk"]=90
print(Student_Grades)

# Unique Element
values = [1,4,4,5,8,7,9,1,0,6,2,3,9,8,2,5,8]
print("Original list:", values)
values_duplicate = set(values)
print("Set (no duplicates):", values_duplicate)

#List Comprehensio
squares = [x**2 for x in range(1, 11)]
print(squares)

#Unpacking Tuples
persons=("Sai",25,"NewYork")
name,age,city=persons
print(name)
print(age)
print(city)

#Merge two dictionaries
grades={
    "ravi":9.5,
    "dk":9.0,
    "ram":8.8
}
age={
    "ravi":25,
    "dk":23,
    "ram":24
}
merged_dict = {name: {"Grade": grades[name], "Age": age[name]} for name in grades}
print("Merged dictionary with both grades and age:", merged_dict)

#Set Intersection and Union
set1={1,4,7,9,6,3}
set2={9,5,3,2,0,8}
intersection = set1.intersection(set2)
union = set1.union(set2)
print("value of intersection",intersection)
print("value of union",union)

#List to Dictionary Conversion
students_list = [("ram", 8.8), ("dk", 9.0), ("ravi", 9.2), ("nehal", 9.8)]
students_dict = dict(students_list)
print("list of students",students_dict)

# Nested Dictionaries
myclass = {
    "student1" : {
        "name": "DK",
        "age" :'20'
        },
    "student2" :{
        "name" :"Ravi",
        "age":'22'
        }
    }
print(myclass)
