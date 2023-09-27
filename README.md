# Muhammad Rafi Darmawan(2206828052) - PBP B

# Essential Ease
"EssentialEase" adalah aplikasi unggulan yang dirancang untuk membuat belanja kebutuhansehari-hari Anda menjadi pengalaman yang lebih mudah, efisien, dan menyenangkan. Aplikasi ini adalah solusi lengkap untuk semua kebutuhan rumah tangga Anda.

EssentialEase adalah sahabat Anda dalam menjalani kehidupan sehari-hari yang sibuk. Dengan kemudahan belanja, pengiriman cepat, dan beragam fitur yang memudahkan, Anda dapat fokus pada hal-hal yang benar-benar penting dalam hidup Anda. Jadi, nikmati hidup tanpa stres dengan EssentialEase!

![warehous](https://github.com/MuhRafliD/essential-ease/blob/main/assets/background-toko-online-8%20(1).jpg?raw=true)

[Klik disini untuk membuka apikasi](https://essential-ease.adaptable.app/)

# Tugas 2 
### Nomor 1
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat sebuah proyek Django baru.
   untuk membuat proyek django baru, pretama yang perlu kita lakukan membuat sebuah virtual environment
    ```
    python -m venv env
    ```
    - lalu aktifkan virtual environment tersebut
    ```
    env\Scripts\activate
    ```
    - di dalam direktori yang sama buatlah file requirenments.txt dan tambahkan beberapa dependencies
    - kemudian jalankan perintah 'pip install -r requirenments.txt' untuk menginstall dependencies.
    - lalu mulailah proyek dengan perintah 'django-admin startproject essential_ease'.
    - untuk tujuan deploy nanti, tambahkan "*" di dalam  'ALLOWED_HOSTS' di 'settings.py'
    - tambahkan file '.gitignore'
      
2. Membuat aplikasi dengan nama main pada proyek tersebut.
   - jalankan perintah 'python manage.py startapp main' untuk membuat aplikasi 'main'.
   - membuat folder 'templates' di dalam 'main'.
   - membuat 'main.html' di dalam folder templates.
     
3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
   - di dalam 'urls.py' di dalam 'essential_ease' tambahkan 'path('main/', include('main.urls'))'
     
4. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
   - 'name'
   - 'amount'
   - 'description'
   - 'price'
   - 'category'

5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
   - di ' views.py' saya menambahkan fungsi 'show_main` dengan context _application name_, _my name_, _my class_. lalu saya render context tersebut ke 'main.html'
   - di 'main.html' saya memanggil setiap item dalam kontext dengan '{{name}}'  sebagai contoh.
     
7. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
   - di dalam 'main.py' buatlah 'urls.py' dan tambahkan  ` app_name = `main` `. Add `path('', show_main, name='show_main')` untuk melist variable dengan nama 'urlpatterns'
     
8. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
   - add, commit, push proyek ke repository dengan nama essential_ease
   - deploy di adaptable

### Nomor 2
Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![bagan](https://niagaspace.sgp1.digitaloceanspaces.com/blog/wp-content/uploads/2022/06/17132515/2-belajar-django-framework-mtv-1024x464.jpg)
referensi : https://niagaspace.sgp1.digitaloceanspaces.com/blog/wp-content/uploads/2022/06/17132515/2-belajar-django-framework-mtv-1024x464.jpg

### Nomor 3
Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Tujuan lingkungan virtual adalah mengisolasi dependensi dan perpustakaan yang diperlukan untuk proyek tertentu. Memungkinkan untuk membuat aplikasi web Django tanpa lingkungan virtual, tetapi dalam beberapa kasus, lebih baik menggunakan lingkungan virtual. Sebagai contoh, dalam proyek A, kami menggunakan Django versi 4.0 dan kami ingin membuat proyek B dengan Django versi 4.1. Jika kami menginstal Django tanpa lingkungan virtual, Django akan diperbarui ke versi 4.1 pada proyek A. Dalam situasi seperti itu, lingkungan virtual dapat sangat berguna untuk menjaga dependensi kedua proyek tersebut.

### Nomor 4
Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC adalah Model-View-Controller. Dalam MVC, Model menyimpan data dan logika aplikasi, View menampilkan data dari Model, dan Controller berfungsi sebagai perantara antara Model dan View. 
MVT adalah Model-View-Template. Dalam MVT, Model menyimpan data dan logika aplikasi, View menampilkan data dari Model dan menghubungkannya ke template, dan Template menentukan tampilan antarmuka pengguna. 
MVVM adalah Model-View-ViewModel. Dalam MVVM, Model menyimpan data dan logika aplikasi, View menampilkan data dari Model, dan ViewModel mengubah data dari Model menjadi format yang dapat dengan mudah ditampilkan dan diinteraksi oleh View. MVC dan MVT mirip, dengan perbedaan utama terletak pada terminologi yang digunakan dan detail implementasi yang khusus dalam kerangka kerja masing-masing. MVVM memperkenalkan pemisahan yang jelas antara View dan ViewModel, dengan penekanan pada data binding dan komunikasi dua arah antara keduanya.

# Tugas 3 
### Nomor 1
Apa perbedaan antara form POST dan form GET dalam Django?

Perbedaannya terletak pada penggunaannya. POST digunakan jika permintaan membuat perubahan dalam basis data atau dalam hal lain kita menggunakan POST untuk mengirim data ke basis data. GET hanya digunakan untuk permintaan yang tidak memengaruhi status sistem atau dalam hal lain kita menggunakan GET untuk mengambil data dari basis data tanpa mengubahnya.

### Nomor 2
Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

HTML adalah blok bangunan utama dalam pengembangan web dan digunakan untuk mendefinisikan struktur halaman. Sementara JSON dan XML digunakan untuk mengangkut data antara server, ada perbedaan antara keduanya. XML cocok untuk data yang terstruktur dan mandiri, sedangkan JSON lebih disukai untuk pertukaran data ringan dan integrasi dengan JavaScript.

### Nomor 3
Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

HTML adalah blok bangunan utama dalam pengembangan web dan digunakan untuk mendefinisikan struktur halaman. Sementara JSON dan XML digunakan untuk mengangkut data antara server, ada perbedaan antara keduanya. XML cocok untuk data yang terstruktur dan mandiri, sedangkan JSON lebih disukai untuk pertukaran data ringan dan integrasi dengan JavaScript.

### Nomor 4
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

1. Membuat `form.py` di dalam folder `main`.
   Di dalam file `forms.py` saya membuat clas `ItemForm` untuk formnya sendiri saya menggunakan `ModelForm` sebagai parameter. Di dalam class saya membuat class `META` yang mengandung `model = item` untuk mengarahkan model yang digunakan. Ini juga berisi `fields = ["name", "amount", "description", "price", "category"]` untuk memilih atribut-atribut dari model Item.
   
2. Membuat objek `create_item` di dalam file `view.py`
Di dalam file `views.py`, kita membuat fungsi `create_item` yang menerima parameter request. Di dalam `create_item`, kita membuat sebuah `ItemForm` baru yang diisi dengan input pengguna dalam `request.POST` sebagai `QueryDict`. Kemudian, kita memvalidasi kontennya dengan menggunakan `form.is_valid()` dan menyimpan kontennya dengan menggunakan `form.save()`. Jika kontennya berhasil disimpan, kembali ke halaman utama dengan menggunakan `return HttpResponseRedirect(reverse('main:show_main'))`. Fungsi ini akan merender `create_item.html`.
   
3. Mengedit fungsi `show_main` di dalam file `view.py`
Tambahkan perintah `item = Item.objects.all()` untuk mengambil semua objek item dari basis data aplikasi.
   
4. Membuat URL routiing untuk `create_item`\
   Di dalam `urls.py` di dalam `essential_ease` tambahkan `path('create_item', create_item, name='create_item'),`.

5. Membuat file `create_item.html` di dalam folder `templates` yang berada di dalam folder `main`
   Isi file HTML dengan kode yang sesuai untuk menampilkan form sebagai tabel, gunakan `{% csrf_token %}` sebagai keamanan, dan gunakan `<form method="POST">` untuk menandai formulir dengan metode `POST`.
   
6. Membuat objek `show_xml` dan membuat URL routingnya
    Objek Item yang Diambil dan Dikembalikan sebagai XML dengan Menggunakan
    ```py
    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    di `urls.py` di dalam `essential_ease` tambahkan `path('show_xml/', show_xml, name='show_xml'),`
   
 7. Membuat objek `show_json` dan membuat URL routingnya
    Objek Item yang Diambil dan Dikembalikan sebagai JSON dengan Menggunakan
   ```py
    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

   ```
   di `urls.py` di dalam `essential_ease` tambahkan `path('show_json/', show_json, name='show_json'),`
   
8. Membuat objek `show_xml_by_id` dan membuat URL routingnya
Objek Item yang Diambil dan Dikembalikan sebagai XML dengan Menggunakan
    ```py
        def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    di `urls.py` di dalam `essential_ease` tambahkan `path('show_xml_by_id/', show_xml_by_id, name='show_xml_by_id'),`
9. Membuat objek `show_json_by_id` dan membuat URL routingnya
    Objek Item yang Diambil dan Dikembalikan sebagai JSON dengan Menggunakan
   ```py
    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

   ```
   di `urls.py` di dalam `essential_ease` tambahkan `path('show_json_by_id/', show_json_by_id, name='show_json_by_id'),`
### Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![biasa](https://github.com/MuhRafliD/essential-ease/blob/main/assets/Screenshot%20(312).png?raw=true)

![xml](https://github.com/MuhRafliD/essential-ease/blob/main/assets/Screenshot%20(307).png?raw=true)

![json](https://github.com/MuhRafliD/essential-ease/blob/main/assets/Screenshot%20(308).png?raw=true)

![xmlid](https://github.com/MuhRafliD/essential-ease/blob/main/assets/Screenshot%20(310).png?raw=true)

![jsonid](https://github.com/MuhRafliD/essential-ease/blob/main/assets/Screenshot%20(311).png?raw=true)

# Tugas 4
### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
#### Dummy 1
![jsonid](https://github.com/MuhRafliD/essential-ease/blob/main/assets/dummy1.png?raw=true)


#### Dummy 2
![jsonid](https://github.com/MuhRafliD/essential-ease/blob/main/assets/dummy2.png?raw=true)


### Nomor 1
Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm digunakan untuk membuat pengguna baru yang dapat menggunakan aplikasi web kita. Formulir ini memiliki tiga bidang: username, password1, dan password2 (yang digunakan untuk konfirmasi kata sandi). Keuntungannya adalah sangat mudah digunakan dan memiliki template sendiri untuk formulir pendaftaran. Kelemahannya adalah memiliki bidang yang terbatas. Misalnya, jika kita ingin mengirimkan email verifikasi untuk memverifikasi pengguna, kita tidak dapat melakukannya karena tidak memiliki bidang email.

### Nomor 2
Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi memverifikasi bahwa seorang pengguna adalah apa yang mereka klaim menjadi, sedangkan otorisasi menentukan apa yang diizinkan oleh seorang pengguna yang telah diotentikasi untuk dilakukan. Autentikasi dan otorisasi adalah dua proses keamanan informasi yang sangat penting yang digunakan oleh administrator untuk melindungi sistem dan informasi. Autentikasi memverifikasi identitas seorang pengguna atau layanan, dan otorisasi menentukan hak akses mereka.

### Nomor 3
Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah berkas teks yang berisi potongan-potongan data kecil yang digunakan untuk mengidentifikasi komputer Anda saat Anda menggunakan jaringan. Django menggunakan sebuah cookie yang berisi ID sesi khusus untuk mengidentifikasi setiap peramban (browser) dan sesi yang terkait dengan situs tersebut. Data sesi sebenarnya disimpan dalam basis data situs secara default.

### Nomor 4
Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Cookies sendiri tidak secara inheren aman atau tidak aman; keamanannya bergantung pada bagaimana kuki tersebut digunakan dan diimplementasikan. Kuki adalah potongan-potongan kecil data yang disimpan oleh situs web pada perangkat pengguna untuk melacak informasi atau menjaga data sesi. Risiko potensialnya adalah bahwa pelaku kejahatan dunia maya dapat mencuri data sensitif dari kuki jika kuki tersebut tidak diamankan.

### Nomor 5
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat form dan fungsi Register
2. Membuat form dan fungsi login, lalu tambahkan tanggal Last Login


