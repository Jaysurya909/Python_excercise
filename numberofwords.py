str = "This is a boy, this is a girl, this is a dog"

str.lower()

l = str.split(" ")
d = {}
for i in l:
    if i not in d:
        d[i] = l.count(i)
        
sorted_by_value_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_value_desc)
