import math
print("""*_* This code solves quadratic equations *_*
*_* Only give me: a,b,c and the answer will appear *_*
""")
print("ax^2+bx+c=0")
try:
 A = float(input("a= "))
 while A == 0:
   print("If 'a' is Zero, then it can't be a quadratic equation; try again.")
   A = float(input("a= "))
 worked_1 = True
except ValueError:
 print("You must enter a number!")
 worked_1 = False
if worked_1:
 try:
  B = float(input("b= "))
  worked_2 = True
 except ValueError:
  print("You must enter a number!")
  worked_2 = False
 if worked_2:
    B_2 = B / A
    try:
      C = float(input("c= "))
      worked_3 = True
    except ValueError:
      print("You must enter a number!")
      worked_3 = False
    if worked_3:
      B_2 = B / A
      C_2 = C / A
      step_1 = B_2 / -2
      step_2 = step_1**2
      step_3 = step_2 - C_2
      try:
        step_4 = math.sqrt(step_3)
        worked4 = True
      except ValueError:
        print("The numbers you gave can't make a quadratic equation.")
        worked4 = False
      if worked4:
        step_5_1 = step_1 + step_4
        step_5_2 = step_1 - step_4
        #the code between the following 2 comments can be removed; it is just an explination
        #start
        step_5_1_2 = step_5_1 * -1
        step_5_2_2 = step_5_2 * -1
        if step_5_1 > 0 and step_5_2 > 0:
          if C < 0:
            print(f"your equation is: {A}x^2+{B}x{C}")
            print(f"Which can be factorized into: (x{step_5_1_2})( x{step_5_2_2})= 0")
          elif C == 0:
            print(f"your equation is: {A}x^2+{B}x")
          else:
            print(f"your equation is: {A}x^2+{B}x +{C}")
            print(f"Which can be factorized into: (x{step_5_1_2})( x{step_5_2_2})= 0")
        elif step_5_1 < 0 and step_5_2 > 0:
          if C < 0:
            print(f"your equation is: {A}x^2+{B}x{C}")
            print(f"Which can be factorized into: (x+{step_5_1_2})(x{step_5_2_2})= 0")
          elif C == 0:
            print(f"your equation is: {A}x^2+{B}x")
          else:
            print(f"your equation is: {A}x^2+{B}x +{C}")
            print(f"Which can be factorized into: (x+{step_5_1_2})(x{step_5_2_2})= 0")
        elif step_5_1 > 0 and step_5_2 < 0:
          if C < 0:
            print(f"your equation is: {A}x^2+{B}x{C}")
            print(f"Which can be factorized into: (x{step_5_1_2})(x+{step_5_2_2})= 0")
          elif C == 0:
            print(f"your equation is: {A}x^2+{B}x")
          else:
            print(f"your equation is: {A}x^2+{B}x +{C}")
            print(f"Which can be factorized into: (x{step_5_1_2})(x+{step_5_2_2})= 0")
        else:
          if C < 0:
            print(f"your equation is: {A}x^2+{B}x{C}")
            print(f"Which can be factorized into: (x+{step_5_1_2})(x+{step_5_2_2})= 0")
          elif C == 0:
            print(f"your equation is: {A}x^2+{B}x")
          else:
            print(f"your equation is: {A}x^2+{B}x +{C}")
            print(f"Which can be factorized into: (x+{step_5_1_2})(x+{step_5_2_2})= 0")
        print("which means that:")
        #end
        print(f"The first x = {step_5_1}    The second x = {step_5_2}")