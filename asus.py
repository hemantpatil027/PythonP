duplicateElement=set()
count=0
unique=[]
duplicate=[]
sampleList =  [['e2806894200050299705499e', '30361F8B380783174876F5AA', 1, False],

              ['e2806894200040289df3717d', '30361F8B380783174876F5AB', 1, False],

              ['e2806894200050299703fd3e', '30361F8B380783174876F5AC', 1, False],

              ['e2806894200050289df5ece4', '30361F8B380783174876F5AD', 1, False],

              ['e280689420005028a323d4e0', '30361F8B380783174876F5AE', 1, False],

              ['e2806894200050299a079572', '30361F8B380783174876F5AF', 1, False],

              ['e280689420004028441518f6', '30361F8B380783174876F5B0', 1, False],

              ['e2806894200040299a067ca8', '30361F8B380783174876F5B1', 1, False],

              ['e280689420005028a266bd51', '30361F8B380783174876F5B2', 1, False],

              ['e2806894200040299a07f97f', '30361F8B380783174876F5B3', 1, False],

              ['e280689420004028a25485cf', '30361F8B380783174876F5B4', 1, False],

              ['e280689420005028a1a6386c', '30361F8B380783174876F5B5', 1, False],

              ['e2806894200050289df37933', '30361F8B380783174876F5B6', 1, False],

              ['e280689420005028a1a5bd76', '30361F8B380783174876F5BC', 1, False],

              ['e28068942000402104b03d1d', '30361F8B380783174876F5B8', 2, False],

              ['e280689420004029970565ab', '30361F8B380783174876F5B8', 2, False],

              ['e280689420005028a269513f', '30361F8B380783174876F5BA', 2, False],

              ['e2806894200050299703c0b1', '30361F8B380783174876F5BC', 3, False],

              ['e2806894200040289df390e1', '30361F8B380783174876F5BC', 3, False],

              ['e2806894200040289e0415d1', '30361F8B380783174876F5BD', 3, False]

              ]


for x in sampleList:
    count=count + 1
    for i in sampleList[:count-1]:
        if x[1]==i[1]:
            duplicateElement.add(x[1])
    for i in sampleList[count:]:
        if x[1]==i[1]:
            duplicateElement.add(x[1])
for x in sampleList:
     if x[1] in duplicateElement:
         duplicate.append(x)
     else:
         unique.append(x)
print(unique)       
print(duplicate)

print('Duplicates found:')
print(duplicate)
print('unique list:')
print(unique)
print('number of unique :')
print(len(unique))
print('duplicate list:')
print(duplicate)
print('number of duplicate :')
print(len(duplicate))