import math

num1 = 12
num2 = 18

hcf = math.gcd(num1, num2)
lcm = abs(num1 * num2) // hcf

print("Number 1:", num1)
print("Number 2:", num2)
print("HCF:", hcf)
print("LCM:", lcm)