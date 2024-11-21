print(help('math'))
# print(help('modules'))
import math
import module_import

import module_import as module #aliasing module_import

from module_import import area_square #importing a specific requirement instead of all

from module_import import area_square as area #aliasing area_square

print(math.factorial(10))
print(math.gcd(10,100,34,67))
print(math.sqrt(144))

print(module_import.area_square(12))
module_import.calculator(20,10)
print(module_import.num)

print(module.area_square(67))

print(area(90))