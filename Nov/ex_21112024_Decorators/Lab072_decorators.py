def add_extra_security(function):
  def wrapper():
      print("Before function is called")
      print("2 add helmet,knee guard,License, gloves")
      function()
      print("3 after the function")
      print("4 secure driving, leave all the items")


  return wrapper()

@add_extra_security

def Ola_scooty():
    print("i have Ola scooty ")
    
@add_extra_security
def drive_scooty():
   print("Normal function")
   print("im driving scooty")

