def decorator_func(say_hello_func):
  
  def wrapper_func(*arg, **kwargs):
    return say_hello_func(*arg, **kwargs)
  
  return wrapper_func



@decorator_func
def say_hello(*arg, **kwargs):
  return  ("--".join(arg))

if __name__ == '__main__':
  print (say_hello('string_1','string_2','string_3'))