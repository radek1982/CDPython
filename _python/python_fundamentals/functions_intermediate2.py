
#1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x[1][0] =15;
print(x)    

students[0]["last_name"] = "Bryant"

print(students)

sports_directory["soccer"][0] = "Andres"

print(sports_directory)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

 #2   
def iterateDictionary(students): 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
  
    for d in students:
        first = d["first_name"]
        last = d["last_name"]
        print(f"first_name - {first}, last_name - {last}")
iterateDictionary(students)


#3 

def iterateDictionary2(key_name, students): 

    for d in students: 
        print(d[key_name])

iterateDictionary2("first_name", students)

iterateDictionary2("last_name", students)

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dictOfLists): 
    
    for k in dictOfLists.keys():

        l = len(dictOfLists[k])
        print(f"{l} {k.upper()}")

        for i in dictOfLists[k]: 
            print(i)

printInfo(dojo)