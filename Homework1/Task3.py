# 1.3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# Примеры/Тесты:
# 385916 >>> yes
# 123456 >>> no

number_tiket = int(input("Введите номер билета: "))
number1 = number_tiket//100000
number2 = number_tiket//10000%10
number3 = number_tiket//1000%10
number4 = number_tiket//100%10
number5 = number_tiket//10%10
number6 = number_tiket%10
if number1+number2+number3 == number4+number5+number6:
    print(f"{number_tiket} >>> Yes")
else:
    print(f"{number_tiket} >>> No")
