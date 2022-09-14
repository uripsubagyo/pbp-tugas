
# Link Heroku

Anda dapat mengakses code ini pada [link](https://pbp-tugas-urip.herokuapp.com/katalog/) ini.


## Penjelasan Bagan

![Logo](https://drive.google.com/uc?export=view&id=1shOuCmVnHddrDRwPoG2etfNKjjyI4B7N)

Penjelasan berdasarkan urutan bagan:

1. Pada tahap pertama user mengakses path yang telah kita buat. request itu dilanjutkan melalui intet untuk dicari path tersebut.
2. Pada tahap kedua, path yang sudah melalui jaringan internet diterima dan dicari path yang terdaftar pada url.py. Ketika terdapat path yang telah didaftarkan, maka view.py masuk tahap ketiga.
3. Pada tahap ketiga view.py melakukan pengerjaan dengan memanggil fungsi yang telah didaftarkan sebelumnya. Fungsi tersebut berisikan pengerjaan yang akan dilakuakn pada tahap 4, 5, dan 6.
4. Pada tahap keempat view.py melakuakan pendefinisian sumber yang akan diambil pada local database.
5. Pada tahap kelima model.py mendefinisikan setiap isi yang berada pada data local database.
6. Pada tahap 6 model.py mengembalikan data yang siap digunakan pada view.
7. Pada tahap ketujuh view.py melakukan render data html dengan menggunakan data atau tidak yang telah diperoleh dari model.py.
8. Pada tahp ketujuh html format yang telah jadi dikirimkan melalui internet sebagai response yang sesuai pada request yang diminta user.
9. Pada tahap kesembilan internet menampilkan hasil response pada laptop user


## Mengapa virtual environment?

Virtual enviroment dapat dikatan sebagai sebuah lingkup yang terisolasi dengan yang lain. Dalam hal ini suatu tempat untuk menjalankan program django yang dapat tidak mengganggu sistem utama komputer atau luar virtual enviroment. Sehingga setiap projek dapat dijalankan secara bersamaan dengan spesifikasi dan versi yang berbeda dan tidak bisa diakses dari luar lingkup itu sendiri.

Virtual enviroment digunakan untuk memudahkan kita sebagai programer untuk customize setiap aplikasi yang sedang dikembangkan. Dalam artian aplikasi 1 membutuhkan versi x dan app 2 membutuhkan versi y. Dengan adanya virtuan enviroment kita tidak merubah ubah secara terus terusan ketika sedang develop 2 app sekaligus


Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Jawabannya bisa, tetapi perlu digaris bawahi akibat dari penggunaan tidak menggunakan virtual enviroment dapat mengganggu aplikasi yang telah kita buat. Hal tersebut karena pengguanaan modulnya yaitu modul gelobal. Dengan begitu ketika kita mengubah modul untuk aplikasi x maka ketika balik mengerjakan aplikasi y harus mengubahnya dulu lagi.

## Cara Implementasi

Implementasi point 1 adalah membuat fungsi yang digunakan untuk mengambil data yang telah dibuat untuk dapat dikelola dan disalurkan datanya ke html. Cara implementasinya dapat membuat fungsi di views.py pada project kita atau katalog. Ketika sudah membuat fungsi tidak lupa untuk import model sebagai bentuk pemanggilan

Contoh fungsi :

```bash
  def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()    --> bentuk pemanggilan model
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Urip'
    'id' : '2106'
    }
    return render(request, "wishlist.html", context)
```
Proses pemanggilan untuk nama dan id yaitu:
```bash
    <h5>Nama: </h5>
    <b>{{nama}}</b> -> ini untuk pemanggilan nama dan id
```
Proses pemanggilan untuk pada context yaitu:
```bash
{% for barang in list_barang %}
    <tr>
        <th>{{barang.nama_barang}}</th>
        <th>{{barang.harga_barang}}</th>
        <th>{{barang.deskripsi}}</th>
    </tr>
{% endfor %}
## Perlu diperhatikan barang.nama_barang, nama_barang disesuaikan berdasarkan 
model dan nama pada database.
```

Implemntasi point 2 yaitu dengan melakukan proses routing yang akan digunakan untuk diakses diperlukan pada bagian ini. Pada proses ini kita harus mengimplementasikannya dengan menambahkan path pada urlpattern di url.py pada folder projectDjanggo dan aplikasi kita (katalog). Path yang ditambahkan pada url.py di project djanggo berisikan alamat serta alamat url dari katalog. sedangkan isi dari url.py pada applikasi kita adalah yang akan path dan apa yang akan ditamplikan.

Untuk penulisan path pada project_django:

```bash
    path('wishlist/', include('wishlist.urls')),
```

Untuk penulisan path pada projek kita atau katalog:

```bash
from django.urls import path
from wishlist.views import show_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),     -> penambahan ini yang perlu diperhatikan
]
```


Implementasi dari point 3 yaitu memetakan data pada html adalah dengan mengola data dari render yang telah ada pada fungsi views.py. Setelah itu kita mengambil data yang ada di view digunakan sebagai variabel yang dapat diimplementasikan pada kebutuhan di html sebagai fill text atau yang lainnya. bentuk omplementasi pemanggilan dapat dilihat pada implementasi point 1 terkait pemanggilan.

Implementasi dari point 4 yaitu proses deploy yang dapat melalui setting dari github atau connect dari website heroku yang dapat di connect dengan repo yang telah dibuat. Cara tersebut merupakan salah satu cara implemtasi deploy ke heroku paling mudah. Setelah berhasil maka dapat dilihat oleh teman-teman.

Sebelum melakukan proses deploy perlu diperhatikan untuk melakukan konfigurasi sebagai berikut: 

- Membuat file bernama Procfile dengan isi sebagai berikut
```bash
web: gunicorn aplikasi_django.wsgi --log-file -

```
- Membuat berkas dpl.yml di .github/workflows dengan isi sebagai berikut 
```bash
name: Deploy

on:
  push:
    branches-ignore:
      - template
  pull_request:
    branches-ignore:
      - template

jobs:
  Deployment:
    runs-on: ubuntu-latest
    env:
      HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
      HEROKU_APP_NAME: ${{ secrets.HEROKU_APP_NAME }}
    steps:
    - uses: actions/checkout@v2
    - name: Set up Ruby 2.7
      uses: actions/setup-ruby@v1
      with:
        ruby-version: 2.7
    - name: Install dpl
      run: gem install dpl
    - name: Install Heroku CLI
      run: wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
    - name: Deploy to Heroku
      run: dpl --provider=heroku --app=$HEROKU_APP_NAME --api-key=$HEROKU_API_KEY
    - name: Run migrations on Heroku
      run: heroku run --app $HEROKU_APP_NAME migrate
    - uses: chrnorm/deployment-action@releases/v1
      name: Create GitHub deployment
      with:
        initial_status: success
        token: ${{ github.token }}
        target_url: https://${{ secrets.HEROKU_APP_NAME }}.herokuapp.com
        environment: production
```
- Membuat berkas .gitinore dengan isi yang boleh dan tidak boleh masuk deploy
- Menambahkan root pada setting.py di project_django sebagai berikut:
```bash
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
```
- Menambahkan * didalam ALLOWED_HOSTS pada setting.py di project_django sebagai berikut:

```bash
ALLOWED_HOSTS = ["*"]
```
- Terakhir menambahkan middleware kedalam MIDDLEWARE di settings.py. Jika sudah ada tidak perlu ditambahkan. 

```bash
    'whitenoise.middleware.WhiteNoiseMiddleware',
```
