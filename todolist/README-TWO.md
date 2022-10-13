
# Tugas 6

Anda dapat mengakses tugas 6 PBP I Made Urip Subagyo  pada [link](https://pbp-tugas-urip.herokuapp.com/todolist/) berikut.

## Perbedaan antara asynchronous dengan synchronous programming

Asynchronus Programing  adalah  kode yang dideklarasi akan dijalankan sesuai dengan deklarasi urutan, tetapi urutan tersebut bisa dijalankan secara bersamaan. Sebagai contoh pelayan restoran sedang menanyakan Pelanggan A, ketika pelanggan A sedang memilih makanan, pelayan bisa melayani pelanggan B sambari menunggu. Intinya ia dapat melaukan suatu pekerjaan berdasarkan waktunya.


Synchronous progaming adalah setiap kode yang dideklarasi akan dijalankan atau dieksekusi satu persatu hingga selesai setiap kodenya.

Secara keseluruhan yang membedakan adalah cara ia melakukan pengerjaan.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Paradigma Event-Driven Programing adalah alur yang dilakukan oleh kode karena efek action button atau yang lainnya. Dengan begitu ia akan melakukan suatu action akibat kegiatan

Sebagai contoh jika melihat action button pada submit modal untuk form. Ketika sudah submit maka ia Event-Driven Programing akan melakukan action untuk menambahkan task 

event-Driven lainnya sebagai berikut:

    1. Event
    2. trigger
    3. event-Handler
    4. Event Loop


## Jelaskan penerapan asynchronous programming pada AJAX.

Salah satu penerapan asynchronous programing pada ajax yaitu fetch. fetch adalah proses pengambilan data. Mengapa fetch asyncrous karna pada proses pengambilan data memerlukan waktu yang berbeda setiap pengambilan bergantung pada kecepatan internet pengguna. Dengan begitu proses ini dibarengi dengan fetch agar fungsi asyncs dapat tetap berjalan hingga selesai proses pengambilan data dan tidak melakukan selanjutnya ketika kode sudah selesai tetapi data belum terambil sepenuhnya.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

    1. Membuat view baru untuk mengambil data json
    2. kemudian membuat path untuk data json
    3. Membuat button dan Modal Bootstrap sebgaai tempat mengisi tambah task
    4. membuat  path add sebagai handle dari button submit di modal
    5. Melakuakn integrasi path dengan ajax
    6. Menambahkan event pada setiap klik agar tanpa refresh akan memunculkan daftar task