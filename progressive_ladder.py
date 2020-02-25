(lambda f: lambda m, n: f(f, m, n))(lambda g, a, b: [[print('*' * (a+1)), g(g, a+1, b)] if a < b else ''])(0, int(input()))

# It's a single line instruction that writes:
#
#*
#**
#***
#****
#*****
#******
#...
