""" What eval() does?

This function executes a string of python code that is passed as a parameter.  """

var = "print(5+8)"
eval(var)

""" Repr prints with strings including the quotes  """

print(repr('With repr the quotes'))

var = "print('var = ', repr(var), 'eval(var)')"
eval(var)

""" Creating the new line """ 

var = "print('var = ', repr(var), '\\neval(var)')"
eval(var)


""" Quine """

q='q=%r;print (q%%q)';print (q%q)

print(open(__file__).read())