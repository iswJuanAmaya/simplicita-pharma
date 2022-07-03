import re

info = '3 viales con 0.2 gramos'

print( re.search("\d+\.?\d*\s*(mg|gramos)", info).group() )