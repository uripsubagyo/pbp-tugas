
# TUGAS 4

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


# TUGAS 5

Anda dapat mengakses tugas 5 PBP I Made Urip Subagyo  pada [link](https://pbp-tugas-urip.herokuapp.com/todolist/) berikut.




## Perbedaan dari Inline, Internal, dan External CSS
- Inline:
    
    Perbedaan inline css adalah css yang dibuat berada pada dalam tag html sehingga css itu hanya berlaku pada tag dan bagian itu saja.
	
    Kelebihan:

	    - Perubahan yang dilakukan pada css hanya akan berlaku pada 1 tag saja.
		- Karena perubahan hanyak berlaku pada 1 div, maka perbaikan cenderung lebih cepat.
	Kekurangan:

		- Penulisan kode jadi tidak efisien karena setiap tag html hanya berlaku pada satu tempat, jika ingin berlaku juga ditempat lain maka harus juga dilakukan penulisan inline ditempat lain secara berulang.

- Internal:
		
    Perbedaaan intenal css dengan yang lainnya adalah css berada dalam dokumen yang sama dengan dokumen html tetapi berada dalam tag.
		
    Kelebihan :
		
        - Setiap perubahan pada internal css hanya berlaku pada 1 halaman
		- Tidak perlu mengimport css dari dokumen lain.
	
    Kekurangan: 
			
        - Tidak efisien jika css yang digunakan sama dengan css pada dokumen lain sehingga dokumen satu dengan lainnya ditulis kembali

- External:

	Perbedaan external css dengan yang lainnya adalah css dibuat dengan dokumen yang berbeda dengan dokumen html serta dokumen css dipanggil melalui dokumen html.
		
    - Kelebihan :
		
        Penulisan kode menjadi lebih rapi dan kode css tidak dicampur pada struktur html.
		Loading website jadi lebih cepat dari pada inline dan internal css.
	- Kekurangan:
			
        Ketika kode css atau file css tidak dapat dipanggil, maka html atau website akan berantakan.

## HTML5 yang kamu ketahui.
    1. <h1> hingga <h6> -> digunakan untuk membuat heading.
    2. <p> -> digunakan untuk membuat teks.
    3. <a> -> digunakan untuk membuat hyper link
    4. <nav> -> digunakan untuk membuat navigasi link atau navbar.
    5. <ul> -> digunakan untuk membuat list item
    6. <ol> -> digunakan untuk membuat list itemnya dengan nomor
    7. <li> -> digunakan untuk membuat list itemnya dengan selain nomor
    8. <div> -> untuk membuat bagian sesuatu pada dokumen atau untuk mengelompokkan suatu bagian
    9. <footer> -> digunakan untuk membuat catatan kaki pada dokumen website


## Tipe-tipe CSS selector yang kamu ketahui.
- Selector tag
		
    selector tag yaitu pembuatan css dengan memanggil tag html pada dokument html.
- Selector class

	selector tag yaitu pembuatan css dengan memanggil nama class yang di define pada tag html
- Selector id

	selector id yaitu pembuatan css dengan memanggil nama id yang di define pada tag html
- Selector atribut

	Selector atribut yaitu pembuatan css dengan memanggil berdasarkan atributnya
- Selector universal

	selector universal yaitu pembuatan css dengan mencakup untuk semua dokument yang memanggilnya, sehingga akan berlaku pada keseluruhan
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat static root pada setting.py agar file css yang akan di deklarasi di static dapat terbaca.
- Kemudian, import link bootstrap pada base.html agar framework bootstrap dapat digunakan pada website kita dan tidak lupa juga import dile static yang udah dibuat agar terbaca oleh website.
- Setelah semua terinstall, kemudian lakuakan styling css dengan tag pemanggilan tag, class, id, atribut, ataupun universal. 
- Dengan begitu style css akan terlihat di broser internet.