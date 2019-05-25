''' Set is like list only
    Only differences are:
        it doesn't contain duplicates
        it doesn't support indexing
        it doesn't maintain order of elements
    List can be converted to set and vice versa
'''

setObj = {1,2,3,4,5}
print(type(setObj))
print(setObj)

setObj = set(["abc", "deg", "hjs", "abc"])
print(type(setObj))
print(setObj)

listObj = list(setObj)
print(type(listObj))
print(listObj)

setObj = {56,21,7,20}
print(setObj)
setObj.add(70)
print(setObj)
setObj.remove(7)
print(setObj)

''' doesn't crash program unlike remove, if value is not found in set '''
setObj.discard(100)
print(setObj)
