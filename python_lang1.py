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

           # iii. Note:
           #       i. Always use () where multiple operations are there.
           #      ii. Always do calculation of numbers of same types like int with int, float with float, etc.
           #     iii. If we return multiple numbers or anything together, they come together in tuple format.
           #      iv. Example:
                            #  repr('Rohit) => "'Rohit'" => Returns a string representation of the object, mainly used for debugging and development
                            #  str('Rohit') => 'Rohit => Returns a nicely printable string representation of the object, intended for presenting to end-users.	
                            #  print('Rohit') => Rohit => Displays the textual representation of an object on the console.

          