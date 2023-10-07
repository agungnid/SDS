def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        terjadi_perubahan = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                terjadi_perubahan = True
        if not terjadi_perubahan:
            break

# Contoh penggunaan:
bilangan = [64, 25, 12, 22, 11]
bubble_sort(bilangan)
print("Bilangan yang sudah diurutkan dari terbesar ke terkecil:", bilangan)

# Inisialisasi slice dengan 5 data awal
my_slice = [1, 2, 3, 4, 5]

# Menambahkan 3 data ke dalam slice
data_baru = [6, 7, 8]
my_slice += data_baru

# Hasil slice dengan 8 data (5 data awal + 3 data baru)
print("Slice dengan 8 data:", my_slice)

Slice dengan 8 data: [1, 2, 3, 4, 5, 6, 7, 8]
