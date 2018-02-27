from Barista import Barista
from Custmer_test import Customer

boboke = Barista()
jungwoon = Customer()

print boboke.showMenu()
boboke.makeAndServe()
jungwoon.order("Ameriacano2", boboke)
jungwoon.order("Americano", boboke)
print boboke.totalSales
jungwoon.order("Caffe Latte", boboke)
print boboke.totalSales
