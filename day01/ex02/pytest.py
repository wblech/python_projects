from vector import Vector


vetor = Vector([2.0, 3.0, 6.0])
vetor2 = Vector([3.0, 4.0, 5.0])
print(vetor)
print(vetor.size)
print("Vetor2", vetor2)
print("")
print("SUM:")
sum = vetor + 5
print("vetor + 5 = ", sum)
sum = vetor + vetor2
print("vetor + vetor2", sum)
print("")
print("SUB:")
sum = 5 - vetor
print("5 - vetor", sum)
sub = vetor - 5
print("vetor - 5 = ", sub)
sub = vetor - vetor2
print("vetor - vetor2", sub)
print("")
print("DIV:")
sum = 5 / vetor
print("5 / vetor", sum)
sub = vetor / 5
print("vetor / 5 = ", sub)
print("")
print("MUL:")
mul = vetor * vetor2
print("vetor * vetor2",mul)
mul = vetor * 5
print("vetor * 5", mul)
mul = 5 * vetor
print("5 * vetor", mul)
