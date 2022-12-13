f = open("origin")
text = f.read()
f.close()
arr = set()
for i in text.split("\n"):
    for o in i.split("。"):
        arr.add(o+"。")

arr = list(arr)
# arr.sort(key=lambda i:len(i))
arr.sort()
f =open("sentence","a")
for i in arr:
    f.write("%s\n"%i)
f.close()