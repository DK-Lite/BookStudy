import re
r = re.compile("a+b*")
print(r.findall("aaaa, cc, bbbb, aabbb"))


r = re.compile("[A-Z]+")
print(r.findall("HOMEHome"))

r = re.compile("^a.......")
print(r.findall("abcdf, cba, dce"))