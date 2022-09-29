
# TUGAS 3

Anda dapat mengakses tugas 4 PBP I Made Urip Subagyo  pada [link](https://pbp-tugas-urip.herokuapp.com/todolist/) berikut.




## kegunaan {% csrf_token %}
Kegunaan csrf_token adalah untuk menghidari serangan pada website dan csrf_token menghasilkan token untuk memproteksi user. Kegunaan lain adalah agar request yang dilakuakan oleh user 1 tidak dilakukan pada user 2.
## Apakah kita dapat membuat elemen <form> secara manual
Bisa. Jika melihat kembali dari pada add_task.html terdapat method POST yang dapat digunakan sebagai parameter pada views.py.
Setelah itu views.py menerima parameter POST. Dari sini views.py tetap bisa menjalankan fungsinya pada template yang telah disediaan.
Setelah itu ia melakukan pekerjaan manipulasi data atau menambahkan dan mengurangi data pada database sesuai paremeter tambahan pada fungsinya.

Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

1. Dapat menyebarkan malware
2. Dapat mengubah dan memperbarui data dengan satu kali permintaan request. Dengan begitu, penyerang website dapat mengambil dan mengubah data user.
3. Kerentanan pengguna keluar otomatis
## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form

Pada button di from.html, view akan bekerja dengan membaca parameter request dari client. Dari view tersebut view akan melakukan pengambilan action post kemudian membuat object baru dengan parameter value yang diambil dari parameter. Object tersebut akan tersimpan pada database. Kemudian mengembalikan pada halaman utama user. Object yang telah dibuat akan muncul pada list.
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Buat aplikasi todolist dengan command python manage.py startapp todolist.
- Mendaftarkan aplikasi yang telah dibuat pada setting.py pada folder project_django.
- Menambahkan routing pada urls.py pada aplikasi yang dibuat dan urls.py pada project_django.
- Membuat Models.py.
- Melakukan migrasi models.py.
- Melakuakan implementasi fungsi login, registrasi, logout, create-task pada views.py.
- menambahkan templates.html untuk setiap implemntasi fungsi.
- Melakukan routing atas fungsi yang baru.
- Melakuakan add, commit, dan melakukan push pada repo yang terhubung pada heroku.