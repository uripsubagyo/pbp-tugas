
# TUGAS 3

Anda dapat mengakses tugas 3 PBP I Made Urip Subagyo  pada [link](https://pbp-tugas-urip.herokuapp.com/mywatchlist/) berikut.




## Akses URL 
Berikut hasil status akses melalui postman:

- Akses pada URL  http:/localhost:8000/mywatchlist/html pada format HTML
    ![Logo](https://drive.google.com/uc?export=view&id=11KA9mldFtvrE3uTLLXqdRTSqRfvI83oB)


- Akses pada URL  http:/localhost:8000/mywatchlist/json pada format JSON
    ![Logo](https://drive.google.com/uc?export=view&id=1sBqlg0cHy5SmboXKzEJjUZ7NMo93zUz8)


- Akses pada URL  http:/localhost:8000/mywatchlist/xml pada format XML
    ![Logo](https://drive.google.com/uc?export=view&id=152cIFe295EnQDXwvOWdmeIDgS4dqow6c)


## Perbedaan JSON, XML, dan HTML

- Perbedaan Arti:
    
    JSON atau Javascript object notation merupakan format yang digunakan untuk menyimpan dan mentransfer data.
	Struktur yang digunakan JSON lebih sederhana dan musah dipahami oleh manusia.
	Struktur tersebut berisikan key dan value yang berurutan menjadi array.
    Penulisan format file dari json diakhiri dengan ektensi .json .
    Secara elemen yang digunakan JOSN lebih terstruktur dan efisien dibandingkan XML

	XML atau extensible Markub Language merupakan bahasa yang digunakan untuk menyederhanakan dan mentimpan data. 
    Bahasa ini dibuat oleh Word Wide Consortium (W3C). XML serupa seperti JSON, tetapi berbeda struktur dan efisiensinya. XML bersifat dinamis karena digunakan untuk transfer data.
    Penulisan format file dari XML diakhiri dengan ekstensi .xml . XML menyimpan elemennya dengan cara terstruktur, mudah dibaca oleh manusia dan mesin.

	HTML atau Hypertext Markup Language merupakan bahasa markup yang digunakan untuk menentukan tata letak elemen di dalam halaman.
	Fungsi dari HTML hanya dapat menampilkan data. Penulisan format file dari html diakhiri dengan ekstensi .html


    b. Secara elemen yang digunakan JOSN lebih sterstruktur dan efisien dibandingkan XML dan 
	   XML menyimpan elemennya dengan cara terstruktur, mudah dibaca oleh manusia dan mesin.
		
- Perbedaan Struktur :

    - JSON  
        Syarat dari penyusunan format json sebagai berikut:
        -   Terdiri atas struktur key dan value
        - Data dipisahkan dengan koma
        - Tanda kurung kurawal menahan object --> object berisikan data berisi key dan value
        - Tanda kurung sikut untuk menahan array --> array berisikan atas object
        ```bash
        [  
            {
            key : value,
            key : value,
            },
            {
            name : "XY"
            id : 112
            }
        ]
        ```
    
    - XML
        XML terdiri atas struktur sebagai berikut :
        - Deklarasi
        - Atribut
        - Elemen

        Penulisan penamaan atribut dan elemen dapa disesuaikan dan tidak harus dengan contoh dibawah. Sebagai syarat jika diawalin dengan tag tidak lupa diakhiri juga.


        ```bash
        <?xml version="1.0"? >                                              --> Deklarasi
        <object model="mywatchlist.mylist" pk="1">                          --> Atribut
            <field name="watched" type="CharField">Belum ditonton</field>   --> Element
            <field name="title" type="TextField">Mumun</field>
            <field name="rating" type="IntegerField">1</field>
        </object>

        CONTOH LAIN 
        [contoh berikut diambil dari website dewa web]

        <?xml version="1.0"? >
        <breakfast_menu title: "Breakfast Menu Restauran A>
            <name>Belgiian Waffles</name>
            <price>Rp35.0000</price>
            <description>Two of our famous Belgian Waffles with plenty of real maple syrup</description>
            <calories>650</calories>
        </breakfast_menu>
        ```
    
    - HTML  
        Setiap html harus diawali dengan tag dan diakhiri dengan tag
        ```bash
        STRUKTUR HTML 
        <!DOCTYPE HTM>
        <html>                                      -> awal tag
            <head>                                  -> awal tag
                <title>Judul Halaman</title>
            </head>                                 -> akhir tag
            <body>                                  -> akhir tag
                <h1>Judul Paragraf</h1>
                <p>Paragraf Pertama</p>
                ..
                ..
                ..
            </body>                                 -> akhir tag

            <script>
        </html>                                     ->> akhir tag
        ``` 

                

    
## Alasan Memerlukan Data Delivery

Kita mengunakan data delivery sebagai salah satu cara dalam mengintegrasikan data pada setiap platform. Sebagai contoh kita ingin membuat sebuah platform tetapi membutuhkan data yang sama. Oleh karena itu penggunaan data delivery dibutuhkan dalam mengirimkan data sekaligus dengan format yang mudah diterima.


## Cara Implementasi

Saya mengimplementasikan setiap checklist dengan mengikutin cara pada sesi tutorial yang telah diberikan. 

Berikut cara implementasi setiap checklist:

- Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas pekan lalu

    Pada bagian ini saya mengimplementasikan code berikut pada terminal pada folder tugas saya.

    ```bash
        python manage.py startapp mywatchlist
    ```


- Menambahkan path mywatchlist sehingga pengguna dapat mengakses http:/localhost:8000/mywatchlist
    Mendaftarkan aplikasi mywatchlist di dalam urls.py yang berada di poject_django sebagai berikut

    ```bash
        path('mywatchlist/', include('mywatchlist.urls')),

    ```
    dan membuat urls.py pada folder mywatchlist dengan isi sebagai berikut:
    ```bash
        from django.urls import path
        from mywatchlist.views import show_mywatchlist

        app_name = 'mywatchlist'

        urlpatterns = [
            path('', show_mywatchlist, name='show_mywatchlist'),
        ]
    ```
    Untuk mengecek apakah sudah berhasil yaitu menjalankan kode berikut pada terminal

    ```bash
        python manage.py runserver
    ```
- Membuat sebuah model MyWatchList dengan memiliki atribut
    Maka dari itu saya menambahkan isi models.py yang ada pada folder mywatchlist sebagai berikut:
    ```bash
        from django.db import models

        class MyList(models.Model): 
            watched = models.CharField(max_length=50)
            title = models.TextField()
            rating = models.IntegerField()
            release_date = models.TextField()
            review = models.TextField()
    ```
    setelah itu melakukan perintah pada terminal yaitu 
    ```bash
        python manage.py makemigrations

        dan

        python manage.py migrate
    ```

- Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas
    Menambahkan folder fixture dengan isi file json dan menambahkan struktur sebagai contoh dibawah ini
    ```bash
    [
        {
        "model": "mywatchlist.mylist",
        "pk": 1,
        "fields": {
            "watched": ....,
            "title": ....,
            "rating": ...,
            "release_date": .....,
            "review": ....
        }
    ]
    ```
    Kemudian menjalankan perintah python manage.py nama_file_json_anda.json diterminal

-  Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format:
    Menambahkan import HttpResponse dan Serializer pada views.py pada 
    ```bash
        from django.http import HttpResponse
        from django.core import serializers 
    ```

    kemudian membuat fungsi pada views.py folder mywatchlist
    ```bash
        from mywatchlist.models import MyList

        # Untuk format json
        def show_json_mywatchlist(request):
            data_watchlist = MyList.objects.all()
            return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")
        
        # Untuk format XML
        def show_xml_mywatchlist(request):
            data_watchlist = MyList.objects.all()
            return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")
    
        # Untuk format html
        def show_html_mywatchlist(request):
            data_watchlist = MyList.objects.all()
            context = {
                'list_watch' : data_watchlist,
            }
            return render(request, "mylist.html", context)   --> html menyesuaikan template yang telah kita buat
    ```

- Membuat routing sehingga data di atas dapat diakses melalui URL:
    Menambahkan path url dalam urlpatterns
    ```bash
        path('html', show_html_mywatchlist, name='show_html_mywatchlist'),
        path('json/', show_json_mywatchlist, name='show_json_mywatchlist'),
        path('xml/', show_xml_mywatchlist, name='show_xml_mywatchlist'),

    ```

- Membuat routing sehingga data di atas dapat diakses melalui URL:
    Cara implementasinya saya buat seperti yang saya jelaskan pada jawaban katalog di file README.md
    