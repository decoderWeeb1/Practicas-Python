def square(x):
  return x * x

def test(func, x):
 print(func(x))

 

test(square,42)

def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)

def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))

#List Comprehensions
cubes = [i**3 for i in range(5)]
print(cubes)

def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()


#Switch Budget function
def zero():
    return "zero"
 
def one():
    return "one"
 
def two():
    return "two"
 
switch = {
  0: zero,
  1: one,
  2: two
}
 
 
def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switch.get(argument, "nothing")
    # Execute the function
    return func()

print(numbers_to_strings(1))