from lfg import LaggedFibonacciGenerator
from lcg import LinearCongruentialGenerator
from millerRabbin import millerRabbin
from fermat import fermat

lfg = LaggedFibonacciGenerator(bits=1024)
lcg = LinearCongruentialGenerator()
number = lcg.next()


while(millerRabbin(number, 10) != True):
  number = lfg.next()
  print(number)
  print(millerRabbin(number, 10))
  print(fermat(number))


