#B"This is a Pyth program!"#
print"This is a Python program!"

-----
Explanation (Pyth):
  First line:
    #             Start infinite while loop (on error, cancels it and breaks)
      B           Break
    "..."         Print string
    #             Start infinite while loop (on error, cancels it and breaks)
  Second line:
    print"..."    Invalid Pyth code. Causes the infinite while loop to cancel the error and break.
Explanation (Python):
  #B"..."#        Python comment
  print"..."      Print string
