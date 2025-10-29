# TODO: Program untuk mencetak bilangan ganjil dari 1 hingga 15
odd_numbers = [1,3,5,7,9,11,13,15]
for i in odd_numbers:
    print(odd_numbers)

# TODO: Program menghitung jumlah huruf vokal
word = input("Masukkan kata: ").lower()

vowels = "aiueo"
count = 0
for char in word :
    if char in vowels:
        count += 1
        
print("Jumlah huruf vokal:", count)
