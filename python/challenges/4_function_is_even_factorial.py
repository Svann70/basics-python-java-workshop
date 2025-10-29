# TODO: Fungsi untuk memeriksa apakah sebuah bilangan genap
num = (4,7)
def is_even(num):
    if num %2 == 0 :
        print ('Bilangan Genap')
    else :
        print ('Bukan Genap')
    

# Tes fungsi
is_even(4)   # True
is_even(7)  # False

# TODO: Fungsi untuk menghitung faktorial
n = (0,5)

def factorial(n):
    if n == 0:
        print ('Faktorial : 1')
    elif n <= 0:
        print ('Faktorial tidak bisa bilangan negatif')
    else:
        a = 1
        factorial = 1
        while a <= n :
            factorial *= a
            a += 1
            print (f'faktorial : {factorial}')

# Tes fungsi
factorial(5) # 120
factorial(0) # 1
