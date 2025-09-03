t = input("")
index = t.index("@")
index_sp = t.index(" ", index)
print(t[index+1:index_sp])