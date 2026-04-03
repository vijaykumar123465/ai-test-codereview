# Test code with multiple issues

def calculate_average(total, count)
    result = total / count   # possible division by zero
    return result

name == "Vijay"   # wrong assignment operator

age = "20"
print("Age: " + age + 5)   # type error

if age > 18:
print("Eligible")   # indentation error