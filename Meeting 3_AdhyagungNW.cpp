#include <iostream>
#include <map>
#include <string>

int main() {
    std::map<int, std::string> data_map;
    
    // Menambahkan data ke dalam map
    data_map[1] = "Nilai 1";
    data_map[2] = "Nilai 2";
    data_map[3] = "Nilai 3";
    
    // Mengakses data dalam map
    std::cout << "Data dengan kunci 2: " << data_map[2] << std::endl;
    
    // Menggunakan iterator untuk mengakses semua data dalam map
    std::cout << "Semua data dalam map:" << std::endl;
    for (const auto& pair : data_map) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    
    return 0;
}

#include <iostream>
#include <string>

// Mendefinisikan struct
struct Mahasiswa {
    std::string nama;
    int usia;
    
    // Method untuk menampilkan informasi mahasiswa
    void tampilkanInfo() {
        std::cout << "Nama: " << nama << ", Usia: " << usia << " tahun" << std::endl;
    }
};

int main() {
    // Membuat objek-objek struct
    Mahasiswa mahasiswa1;
    mahasiswa1.nama = "John";
    mahasiswa1.usia = 20;
    
    Mahasiswa mahasiswa2;
    mahasiswa2.nama = "Jane";
    mahasiswa2.usia = 22;
    
    // Memanggil method dari struct
    mahasiswa1.tampilkanInfo();
    mahasiswa2.tampilkanInfo();
    
    return 0;
}

#include <iostream>
#include <string>

// Mendefinisikan struct
struct Mahasiswa {
    std::string nama;
    int usia;
    
    // Method untuk menampilkan informasi mahasiswa
    void tampilkanInfo() {
        std::cout << "Nama: " << nama << ", Usia: " << usia << " tahun" << std::endl;
    }
};

int main() {
    // Membuat objek struct
    Mahasiswa mahasiswa;
    mahasiswa.nama = "John";
    mahasiswa.usia = 20;
    
    // Menampilkan informasi awal
    std::cout << "Informasi awal mahasiswa:" << std::endl;
    mahasiswa.tampilkanInfo();
    
    // Menggunakan pointer untuk manipulasi data dalam struct
    Mahasiswa* pointer_mahasiswa = &mahasiswa;
    pointer_mahasiswa->nama = "Jane";
    pointer_mahasiswa->usia = 22;
    
    // Menampilkan informasi setelah manipulasi
    std::cout << "Informasi setelah manipulasi:" << std::endl;
    mahasiswa.tampilkanInfo();
    
    return 0;
}
