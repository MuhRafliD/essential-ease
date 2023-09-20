# Muhammad Rafi Darmawan(2206828052) - PBP B

# Essential Ease
"EssentialEase" adalah aplikasi unggulan yang dirancang untuk membuat belanja kebutuhansehari-hari Anda menjadi pengalaman yang lebih mudah, efisien, dan menyenangkan. Aplikasi ini adalah solusi lengkap untuk semua kebutuhan rumah tangga Anda.

EssentialEase adalah sahabat Anda dalam menjalani kehidupan sehari-hari yang sibuk. Dengan kemudahan belanja, pengiriman cepat, dan beragam fitur yang memudahkan, Anda dapat fokus pada hal-hal yang benar-benar penting dalam hidup Anda. Jadi, nikmati hidup tanpa stres dengan EssentialEase!

![warehous](https://github.com/MuhRafliD/essential-ease/blob/main/assets/background-toko-online-8%20(1).jpg?raw=true)

[Klik disini untuk membuka apikasi](https://essential-ease.adaptable.app/)

# Tugas 2 
## Jawaban
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
## Jawaban
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
   
3. Membuat objek `create_item` di dalam file `view.py`
   
5. Mengedit fungsi `show_main` di dalam file `view.py`
   
7. Membuat URL routiing untuk `create_item`
   
9. Membuat file `create_item.html` di dalam folder `templates` yang berada di dalam folder `main`
10. Membuat objek `show_xml` dan membuat URL routingnya
    Objek Item yang Diambil dan Dikembalikan sebagai XML dengan Menggunakan
    ```py
    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    di `urls.py` di dalam `essential_ease` tambahkan `path('show_xml/', show_xml, name='show_xml'),`
12. Membuat objek `show_json` dan membuat URL routingnya
    Objek Item yang Diambil dan Dikembalikan sebagai JSON dengan Menggunakan
   ```py
    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

   ```
   di `urls.py` di dalam `essential_ease` tambahkan `path('show_json/', show_json, name='show_json'),`
14. Membuat objek `show_xml_by_id` dan membuat URL routingnya
15. Membuat objek `show_json_by_id` dan membuat URL routingnya

### Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![biasa](https://github.com/MuhRafliD/essential-ease/blob/main/assets/Screenshot%20(312).png?raw=true)

![xml](https://github.com/MuhRafliD/essential-ease/blob/main/assets/Screenshot%20(307).png?raw=true)

![json](https://github.com/MuhRafliD/essential-ease/blob/main/assets/Screenshot%20(308).png?raw=true)

![xmlid](https://github.com/MuhRafliD/essential-ease/blob/main/assets/Screenshot%20(310).png?raw=true)

![jsonid](https://github.com/MuhRafliD/essential-ease/blob/main/assets/Screenshot%20(311).png?raw=true)




