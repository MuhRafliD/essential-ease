# Tugas 2 PBP
Muhammad Rafi Darmawan(2206828052) - PBP B

# Essential Ease
"EssentialEase" adalah aplikasi unggulan yang dirancang untuk membuat belanja kebutuhansehari-hari Anda menjadi pengalaman yang lebih mudah, efisien, dan menyenangkan. Aplikasi ini adalah solusi lengkap untuk semua kebutuhan rumah tangga Anda.

EssentialEase adalah sahabat Anda dalam menjalani kehidupan sehari-hari yang sibuk. Dengan kemudahan belanja, pengiriman cepat, dan beragam fitur yang memudahkan, Anda dapat fokus pada hal-hal yang benar-benar penting dalam hidup Anda. Jadi, nikmati hidup tanpa stres dengan EssentialEase!

![warehous](https://github.com/MuhRafliD/essential-ease/blob/main/assets/jual%20beli.jpg?raw=true)

[Klik disini untuk membuka apikasi](https://essential-ease.adaptable.app/)

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
