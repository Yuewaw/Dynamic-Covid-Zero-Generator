# to JavaScript format
f = open("sentence")
text = f.read().split("\n")
f.close()
f = open("json","a")
for i in text:
    f.write("\"%s\",\n"%i)
f.close()