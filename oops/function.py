 // program 1:
def oops(a,b): // by passing parameter in method  
    c=a + b
    print("sum of two number",c) 
a = int(input("enter the nuber"))
b = int(input("enter the nuber"))
oops(a,b)



// program 2:
    def oops(a):
   if(a%2==0):
       print("it is even number")
   else:
       print("odd numer")

a= int(input("enter the a value"))
oops(a)
    
  //program 3:
   def myfun(j):
   print(j)
first="sandy"
get="kumar"
myfun(first)
myfun(get)

   //program 4:
  //args-//kwargs
    def fun( *arg):
        print(arg)
fun("arun","guna","balaji")

// progran indentation
def fun( *arg):
    for i in arg:
        print("he name was ",i)

fun("arun","guna","balaji")

// program 
