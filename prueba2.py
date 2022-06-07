import re

j = "100 mg/4 ml solucion inyectable"

f = re.search("\d+.?\d*\s*", j).group()
print(f)