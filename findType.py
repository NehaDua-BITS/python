def getType(param):
    paramType = type(param)
    if (paramType == int):
        return "Int"
    elif (paramType == str):
        return "String"
    elif (paramType == float):
        return "Float"

print(getType(10.45))
print(getType(5))
print(getType("neha"))
