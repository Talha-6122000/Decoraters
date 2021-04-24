# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.
def my_decoraters(fun):
  def wrap_function():
    print("*************")
    fun()
    print("*************\n")
  return wrap_function
@my_decoraters
def helllo():
  print("Helloooo")
helllo()
@my_decoraters
def bye():
  print("Byeee")
bye()
def my_dec2(fun):
  def wrap_function1(x):
    print("++++++++++")
    fun(x)
    print("+++++++++\n")
  return wrap_function1
@my_dec2
def display(x):
  print(x)
display("Hiiiiiiiiiii")