import streamlit as st

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Bagi array menjadi dua bagian
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Rekursif untuk mengurutkan kedua bagian
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Gabungkan kembali bagian yang sudah diurutkan
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # Gabungkan elemen dari left dan right
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Sisakan elemen yang belum digabungkan
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def main():
    st.title("Merge Sort Program")
    # Meminta pengguna untuk memasukkan daftar angka yang akan diurutkan.
    user_input = st.text_input("Masukkan daftar angka yang akan diurutkan (pisahkan dengan spasi):")
    # Tombol untuk memulai program
    st.button("Mulai")
    if user_input:
        try:
            user_list = list(map(int, user_input.split()))
            sorted_list = merge_sort(user_list)
            # Menampilkan hasil pengurutan.
            st.write(f"Hasil pengurutan: {sorted_list}")
        except ValueError:
            st.write("Masukkan hanya angka yang dipisahkan dengan spasi.")
        
# Menjalankan program jika file ini dijalankan sebagai script utama.        
if __name__ == "__main__":
    main()
