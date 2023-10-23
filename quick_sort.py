import streamlit as st

def quick_sort(arr):
    """
    Fungsi ini menerapkan algoritma Quick Sort untuk mengurutkan list 'arr'.

    Args:
    arr (list): List yang akan diurutkan.

    Returns:
    list: List yang telah diurutkan.
    """
    if len(arr) <= 1:
        return arr
    
    # Memilih pivot sebagai elemen tengah dari array.
    pivot = arr[len(arr) // 2]
    
    # Membagi elemen-elemen ke dalam kelompok 'kiri', 'tengah', dan 'kanan' tergantung pada hubungannya dengan pivot.
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Menggabungkan hasil dari pengurutan rekursif pada bagian-bagian kiri dan kanan dengan elemen tengah.
    return quick_sort(left) + middle + quick_sort(right)

def main():
    st.title("Quick Sort Program")
    
    # Meminta pengguna untuk memasukkan daftar angka yang akan diurutkan.
    user_input = st.text_input("Masukkan daftar angka yang akan diurutkan (pisahkan dengan spasi):")
    # Tombol untuk memulai program
    st.button("Mulai")
    
    if user_input:
        try:
            # Mengonversi input pengguna menjadi list of integers.
            user_list = list(map(int, user_input.split()))
            
            # Mengurutkan list menggunakan fungsi quick_sort.
            sorted_list = quick_sort(user_list)
            
            # Menampilkan hasil pengurutan.
            st.write(f"Hasil pengurutan: {sorted_list}")
        except ValueError:
            st.write("Masukkan hanya angka yang dipisahkan dengan spasi.")

# Menjalankan program jika file ini dijalankan sebagai script utama.
if __name__ == "__main__":
    main()
