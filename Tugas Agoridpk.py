var = ["Arsel","Avivah","Dava",["Wahyu","Wibi"]]
def jumpSearch(arr, x):
    n = len(arr)

    # Menentukan ukuran jump
    step = int(n ** 0.5)

    # Menentukan indeks awal dan akhir
    left = 0
    right = 0

    while right < n and arr[right] <= x:
        left = right
        right += step 

    # Melakukan pencarian linear
    for i in range(left, min(right, n)):
        if arr[i] == x:
            return i

    # Jika tidak ditemukan
    return -1

# Mencari data pada list
print("1. Arsel di Index", jumpSearch(var, "Arsel"))
print("   Avivah di Index", jumpSearch(var, "Avivah"))
print("   Daiva di Index", jumpSearch(var, "Daiva"))
print("2. Wahyu di Index", jumpSearch(var[3], "Wahyu"), ("pada kolom 0"))
print("3. Wibi di Index", jumpSearch(var[3], "Wibi"), ("pada kolom 1"))