# Printing in Python
      # print("Hello Rohit")


# comments
      # singLine: '#'
      # multiline: """ Rohit """


# importing Functions from other file:
    #  file1.py:
         # def hello(name):
         # print("Hello"+name)

    #  file2.py:
          # from file1 import hello
          # hello("Rohit")



# Python Internal Working:
        # Python scripts -> coverts to Byte code => Python virtual Machine.
        

        # Bytecode(Lowlevel and platform independent binary/hexadecimals/macro instruction not totally understandable by CPU): 
            # Compiles to ByteCode:    
            #     1. Runs Faster than python scripts
            #     2. .pyc generated files are complied python(Bytecode) also known as Frozen Binaries.
            #     3. __pycache__ : 
                        #  i.  system folder of python Stores .pyc files
                        #  ii. Like whatever changes we make in our dependencies files, it keeps a track of it and only makes sure that the new changes are pushed to our .pyc file.
            #     4. Naming covension to Pyc files: Filename.pythonversion.pyc
        

            # Note: 
                # i.  .pyc files only are used for imported files, ByteCode is not Machine code.
                # ii. Frozen binaries are compiled executable files containing all necessary code and resources for independent execution on a specific platform 


        # Python Vitual Machine:
             # 1. RunTime Engine
             # 2. code loop to iterate bytecode also called as python interpretor














# Immutable and Mutable:
    # Immutable: i.  Datatypes that whose values cannot be changed (more pricesely the refrence created inside memory cannot be changed). 
    #            ii. Example: Integers,Float,Boolean,Strings, tuples,bytes  
   
    # Mutable: i.  Datatypes that whose values can be changed. 
    #          ii. Ex: List, set, dictionary, Array, ByteArray




# Note:
    #  i.   Remember in python memory references of value are created.
    #         Example: username = "Rohit"
    #                  username = "Rohan" // separate memory references are created for values "Rohit" and "Rohan".
    #  ii.  But, if we wanna change "Rohit" to "RoHiT", then it is immutable.
    #  iii. In python, datatype is assigned to memory references not the variables. So, variables have no datatypes but, memory referencess do have it.



# Object/Data Types: (Data are also called as Object in Python ) => High level disscussion
    # i.   Numbers: 1234, 3.14, decimal, fraction, etc
    # ii.  String: "Rohit"  
    # iii. List: [1,2,3,4,5]
    # iv.  Tuple: (1,2,3,4,5)
    # v.   Dictionary: {"name":"Rohit", "age":23}
    # vi.  set: {1,2,3,4,5}
    # vii. Files
    # viii.Boolean: True / False
    # ix.  None: empty values



# Further Internal working of Python:

        #    i.  Python does not keep memory have empty references, and this memory is removed by pythons garbage collector.
        #        For, Numbers and Strings garbage collection is done little late.

        #    ii. In python count of memory references of a memory is maintained inside refcount is not true.
        #           Exmaple:  import sys
        #                  sys.getrefcount(123) // results => 4294967295, which is a result of execution of compiler optimization loop, giving us the same number again and again. 
        
        #    iii. Example:
                        #   a=2 // memory of 2 created first and its reference assigned to a.
                        #   a=a+2 // value from memory reference of a is taken and after computation, the new values memory is created and its reference is assigned to a.

        #     iV. Mutable Datatypes(List):
                        # Example1:
                        #          L1 = [1,2,3]
                        #          L2 = L1
                        #          L1[0] = 100
                        #          print(L1)  # [100,2,3]
                        #          print(L2)  # [100,2,3]
               
                        # Example2:
                        #          L1 = [1,2,3]
                        #          L2 = L1
                        #          L1 = [1,2,3]
                        #          L1[0] = 100
                        #          print(L1)  # [100,2,3]
                        #          print(L2)  # [1,2,3]

                        # Example2:
                        #          L1 = [1,2,3]
                        #          L2 = L1[:]
                        #          L1[0] = 100
                        #          print(L1)  # [100,2,3]
                        #          print(L2)  # [1,2,3]



                #   In Example2, new memory is actually assigning to L1 as it is mutable,
                #   and changes are being made to the new memory instead of old one.
 
                #   In Example3, we are not using memory referce instead making a new copied memory 
                #   While using slicing we always create a new copied memory


        # v. 'is' operator checks the memory references or, the location of the memory.















# operator in Python:
#     1. Arithmetic Operator:
        #   i. Addition(+)
        #  ii. Substraction(-)
        # iii. Division(/) 
        #  iv. Multiply(*)
        #   v. Power(**)
        #  vi. Remainder(%)
 

#     2. Comparison Operators:
        #   i. (>)
        #  ii. (<)
        # iii. (>=) 
        #  iv. (<=)
        #   v. (==)
        #  vi. (!=)


#     3. Logical Operators:
        #   i. and: T+T => T, T+F =>F, F+T => F, F+F =>F
        #  ii. or: T+T => T, T+F =>T, F+T => T, F+F =>F
        # iii. not: T->F, F->T


#     4. Bitwise operators: 
        #   i. LeftShift (<<): multiply by 2 to the power n, from the number.
                            #    Example: a = 5
                            #             a<<2 => 20

        #  ii. RightShift (<<): divide by 2 to the power n, from the number.
                            #    Example: a = 20
                            #             a<<2 => 5

        # iii. Bitwise And (&): 1 zero means 0  
                                #  Example:
                                #    a = 10    # Binary: 1010
                                #    b = 6     # Binary: 0110
                                #    result = a & b  # Result: 2 (Binary: 0010)

        #  iv. Bitwise Or(|): 1 one means 1  
                                #  Example:
                                #    a = 10    # Binary: 1010
                                #    b = 6     # Binary: 0110
                                #    result = a | b  # Result: 14 (Binary: 0010)

        #  v. Bitwise Xor(^): Different bits results in 1 else 0. 
                              #  Example:
                                #    a = 10    # Binary: 1010
                                #    b = 6     # Binary: 0110
                                #    result = a | b  # Result: 12 (Binary: 1100)

        #  vi. Bitwise Not(~): reverse 0->1 and 1->0 bits
                              #  Example:
                                # a = 10    # Binary: 1010
                                # result = ~a  # Result: -11 (Binary: 0101, considering 2's complement representation)
    
        


# DataTypes in Python:

    #1. Number: 
           #  i. operands: Addition(+), Substraction(-), Division(/), Multiply(*), Power(**), Remainder(%)
           #       Example: a = 2
           #                b = 3
           #                print((a+b)*2)
 
           #  ii. operator overloading exists in python capability of operators to detect operands and calculte.
           #          Example: print('Rohit' + 'Pandey') // 'RohitPandey'


           #  iii. Math Library: import math
           #          a. closes bottom value: math.floor(3.5) =>3
           #          b. Towards 0 values: math.trunc(2.5) => 2
           #          c. square roots: math.sqrt(25) => 5
           #          d. power: math.pow(a,b) => a to the power b


           #   iv. Number conversion:
                    #   1. Integer: int(64) => 64
                    #   2. Decimal -> Integer:   int('64' ,8) => 52
                    #   3. HexaDecimal -> Integer:   int('64' ,16) => 100
                    #   4. Binary -> Integer:   int('10000' ,2) => 16

           # Note:
           #       i. Always use () where multiple operations are there.
           #      ii. Always do calculation of numbers of same types like int with int, float with float, etc.
           #     iii. If we return multiple numbers or anything together, they come together in tuple format.
           #      iv. Example:
                            #  repr('Rohit) => "'Rohit'" => Returns a string representation of the object, mainly used for debugging and development
                            #  str('Rohit') => 'Rohit => Returns a nicely printable string representation of the object, intended for presenting to end-users.	
                            #  print('Rohit') => Rohit => Displays the textual representation of an object on the console.

          

















# Random modules: import random
        # i.  random.random(): Generate random values from 0 to 1 range
        # ii. random.randint(start , last): Generate random values within a given range.
        # iii.random.choice([1,2,3,4,5]): Generate random values from the list of elemnts.
        # iv. random.shuffle([1,2,3,4,5]): Shuffles elements inside the list.

# Decimal and Fraction module: 
        # i. from decimal import Decimal
        #    Decimal('123.56)
        # ii. from fractions import Fraction
        #     Fraction(2,7)
        
        # Note: In python it is difficult to handle the decimals, so we use decimal module.


# Sets:  
#   A set is a collection which is unordered, unchangeable*, and unindex
        # i. Syntax: setone = {1,2,3,4,5}
        # ii. set Intersection:  setone & {1,3} => {1,3}
        # iii.set union: setone | {1,3,5} = >{1,2,3,4,5}
        # iv. set differences: setone - {1,2,3} => {4}
        #  v. Empty set: set()
        # vi. Adding elements: setone.add(element)
        # Note: Empty {} are dictionary by default.


# Boolean:
#      i.  True: 1
#      ii. False: 0 




# Strings:
#  Can be written using '', "", """ """.
#        i. Syntax:  name = "Rohit"
#       ii. Indexing: 0 to n-1, -1 to -n(backwards diraction)
#      iii. Get index value: name[index] 
#       iv. Slicing:  name[start : end : Indexjump] => start to end-1 elements are inclusive here, by hoping values according to the hoping number .
#        v. lowerCase: name.lower()
#       vi. Uppercase: name.upper()
#      vii. Remove extra spaces:  name.strip()
#     viii. Replace substring: name.replace(substring, newsubstring)
#       ix. String to List: 
#                     sentence = "Rohit is a good boy"
#                     print(sentence.split(" ")) => ['Rohit', 'is', 'a', 'good', 'boy'] => splitiing done based on spaces.
#        x. Find substring: 
#                         name.find(substring/character) // If not found returns -1.
#                         substaring in  name: => This just returns a boolean value after check
#       xi. Get count of substring/character:   name.count(substring/character)
#      xii. Placeholders: 
#                      name = "My name is {} and my age is {}"
#                      name.format('Rohit','23')
#     xiii. length of string: len(name)
#      xiv. List to string: 
#                         L1 = ['rohit','is','good']
#                         " ".join(l1) => rohit is good => joining of elements inside List are done with the specified character in "".
#       xv.  Printing characters in String: 
#                      for ch in name:
#                           print(ch)
#      xvi. To handle "" or / inside a string we use raw strings:
#                 Example: r"c:\user\pwd"



# Note: 
#      i. slicing:  selecting subsets of elemnet inside list/string/etc
#     ii. dicing:  silcing done in multi dimension or nested levels. 



# List / Array:
#             i. Syntax: L1 = [1,2,3,4,5]
#            ii. Indexing: Same as string
#           iii. To get a particular element present at a index: L1[index]
#            iv. Length: len(l1)
#             v. Slicing and dicing: same as string
#            vi. changing elements at a index: L1[index] = new value
#           vii. Looping List elements:
#                     for element in L1:
#                         print(element, end) //end means change line
#          viii. Add elements at end: L1.append(element)
#            ix. Remove elements from end: L1.pop()
#             x. remove elements by themselves: l1.remove(element)
#            xi. Inserting elements at a position: L1.insert(position, new element)
#           xii. Creating copy of memory: L1.copy() // same as L1[:]
#          xiii. List comprehension:  [x**2 for x in range(10)] => [0,1,4,9,16,25,36,49,64,81] 





















# Dictionary
          #    i. Syntax: student = { "name": "Rohit", "age": 50, "roll": 27 }
          #   ii. consists of key-value pairs. 
          #  iii. Get values: student[key] / student.get(key)
          #   iv. changeing values:  student[key] = new value  
          #    v. Iterate over dictionary :  
          #                              i. for keys in  student:
          #                                     print(student, student[keys]) 
          #                             ii. for keys,values in  student.items():
          #                                     print(keys, values) 
          #   vi. Length of dictionary: len(student) 
          # viii. Adding new elements: student[newkey] = new value
          #   ix. Remove of elements/items:  student.pop(key)
          #    x. Remove of items from end:  student.popitem()
          #   xi. deleting the memory reference in dictionary: del student[key]
          #  xii. Distionary comprehension:  {x:x**2  for x in range(10)} => {0:0 , 1:1 , 2:4 , 3:9 , 4:16 , 5:25 , 6:36 ,7:49, 8:64 , 9:81} 
          # xiii. Remove all dictionary items: student.clear()
          #  xiv. creating dictionary through keys:
          #                         keys = ["Rohit","Rohan","sham"]
          #                         default_value = 0
          #                         dict.fromkeys(keys,default_value) => {"Rohit": 0,"Rohan":0,"sham":0}



# Note: 
#      i. 'in' keyword checks the availability of an element inside the data types.  
#     ii. checking datatypes of element = type(variablename)


# Tuples
#    List is mutable but tuple is immutable.
          #    i. Syntax: name = ("Rohit","Rohan","Romit")
          #   ii. Indexing: 0-n-1, -1 to -n
          #  iii. Getting values at a particular index: name[0] => "Rohit"
          #   iv. Length: len(name)
          #    v. Tuple/List concat: (1,2,3) + (4,5) => (1,2,3,4,5)
          #   vi. To count number of a element present in tuple: name.count(element)
          # viii. destructuring data: 
          #                         name = ("Rohit","Rohan","Romit")  
          #                         (name1, name2, name3) = name =>  name1 = "Rohit" | name2 = "Rohan" |name3 = "Romit" 
          










# Taking users input:
#            i. String: input("Enter usersname: ")
#           ii. Int: int(input("Enter users age: "))


#  Conditional Statements:
#     Syntax:
        #    if(consdition):
        #         statement
        #    elif(condition):
        #         statement
        #    else:
        #         statement


# Tertiary operator:   min = a if a < b else b     // a is correct ans, b is a false value

#  Switch Statements:
#       Syntax:
                # lang = input("What's the programming language you want to learn? ")
                # match lang:
                #     case "JavaScript":
                #         print("You can become a web developer.")
                #         break
                #     case "Python":
                #         print("You can become a Data Scientist")
                #         break
                #     case "Java":
                #         print("You can become a mobile app developer")
                #         break
                #     case _:
                #         print("The language doesn't matter, what matters is solving problems.")
                #         break
  

# Note:
#     i. How to exit a program in python:  'exit()'
#    ii. Leap Year (concept): divisible by 400 or (divisible by 4 and not divisible by 100)




# Loops in Python:
        # L1 = [1,2,3,4,5]


        # 1. For Loop:
                # Syntax:
                #     for i in range(0,len(L1)):
                #         print(L1[i])
        #    Note: range(start,end,rangejump) => inclusive start to end-1, with range jump


        # 2. For Each loop:
                # Syntax:
                #      for element in L1:
                #         print(element)


        # 3. While Loop:
                # Syntax: 
                #        sum = 0
                #        index = len(L1) - 1
                #        while(index):
                #            print(l1[index])
                #            index-=1

        # 4. Do while Loop:  Python does not have a inbuilt do while,
        #                      but functionality can be acheive using while loop itself.


                # Example:
                        # secret_word = "python"
                        # counter = 0

                        # while True:
                        # word = input("Enter the secret word: ").lower()
                        # counter = counter + 1
                        # if word == secret_word:
                        #         break
                        # if word != secret_word and counter > 7: 
                        #         break


#  Break and continue:
        #  i. Break: Breaks the current statement and program execution moves to the other statement
        # ii. Continue: Skips the current statement/ iteration and program execution moves to next iteration
























# Time module:
        # Example: Implement an exponential backoff stratergy 
        #          that doubles the wait time between retries, 
        #          starting from 1 second but stops after 5 retries
        
                # Code:
                      # import time 
               
                      # wait_time = 1
                      # max_retries = 5
                      # attempts = 0

                      # while attempts < max_retries:
                              # print("Attempt",attempts+1,"-wait time",wait_time)
                              # time.sleep(wait_time)       
                              # attempts += 1
                              # wait_time *= 2
           


# # Loop Internal working:
#        i. Iteration tool: For,while,for each,comprehension etc
#       ii.  Iteration Objects: Provides us the first values memory address initially. List,File,set,etc
#      iii.  __next__/next() : until and unless __next__ is present, iteration tools calls iter() and iterates over iterable objects. 
#                              Else if the range of loop gets over, the stop iteraion exception gets raised and loop terminates.
#       iv. Example of itrating over list using iter() and __next__():
                      # L1 = [1,2,3]
                      # I = iter(L1)
                      # I.__next__() => 1      
                      # I.__next__() => 2
                      # I.__next__() => 3



# File handling in Python:
#          i. Open File: f = open('note.py')  / iter(f) // f.__iter__() // It is a iterable object in case of file, but in case of List and others it is just file memory reference of data 
#         ii. Reading line: f.readline()
#        iii. Reading lines throught __next__(): On using f.__next__() we can read the file line by line and when all lines are covered it throws an StopIteration exception.
#         iv. Example of iterating through File:
                # for line in open('note.py'):
                    # print(line)





















# Functions:
#     A set of instructions which can be used again and again.
        # syntax:
        #      def add(a,b=5): => a and b are variables
        #         return a+b  => return statement
        #      add(3,2) => function call

    # Note: here default value is given to b, as if no value is passed for b then this default value is used. 



# Taking multiple values in one parameter of function:
        # syntax:
        #      def add(*args): => args taking all values as a tuple of all values
        #         return sum(args) => sum() builtin function doing sum of args elements
        #      add(1,2,3,4,5) 




# Taking named parameters using **kwargs:
        # syntax:
        #      def add(*kwargs): => args taking all values as a tuple of all values
        #         for key,value in kwargs.items():
        #            print(f"{key}: {value}")
        #         return sum(args)
        #      add(num1=2,num2=5,num3=6)




# Returning values through yield:
#    Yield keeps the value of function and its state in memory.
        # Syntax:
        #       def even_generator(limit):
        #            for i in range(0,limit,2):
        #                yield i
        #       even_generator(100)
        
        #       for i in even_generator(100):
        #            print(i)



# Lambda function: 
#    A function with no name or defination, moreover it's a function just for one time usage generally.
#    Example:
#           add = lambda a,b: a+b
#           add(2,3) // 5




# Recursion:
#     A function repeatedly calling itself. Basically we solve bigger problems here
#     by solving the smaller problems of similar type.

#     Example:
#             def factorial(n):
#                 if(n==1 || n==0):  // base case: Avoids infinite recursion calls, thereby protecting memory overflow
#                     return 1
#                 return n* fact(n-1) // Recursive function
#             factorial(10)