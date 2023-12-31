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
di dalam `views.py` import `Redirect`, `UserCreationForm`, dan `Messages`. Membuat sebuah fungsi `Register` seperti berikut:

```py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
Setelah membuat fungsi, buat file baru `register.html` di `main\templates` untuk mendapatkan data dari web. Membuat fungsi routing di dalam `urls.py`
2. Membuat form dan fungsi login, lalu tambahkan tanggal Last Login
di dalam `views.py` import `authenticate` dan `login`. Membuat fungsi `login_user` yang memuat tanggal last login dan menambahkan cookie sepert berikut:
```py
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
Setelah membuat fungsi, buat file baru `login.html` di `main\templates` untuk login user. saya menambahkan `'last_login': request.COOKIES['last_login'],` di dalam `context` untuk menampilkan data last login pada `main.html`. Membuat fungsi routing di dalam `urls.py`

3. Membuat form dan fungsi logout, juga Menghapus Last login dari Cookie
di dalam `views.py` import `logout`. Membuat fungsi `logout_user` yang memuat delete last login dari coockie seperti berikut:
```py
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Membuat fungsi routing di dalam `urls.py`. Menambahkan sebuah `logout` button di dalam `main.html` untuk logout user
4. Membatasi Akses ke Halaman Utama Jika Pengguna Belum Masuk (Login)
di dalam `views.py` import `login_required` lalu tambahkan `@login_required(login_url='/login')` diatas fungsi `show_main`

5. Menghubungkan `item` Model dengan `User` Model
di dalam `models.py` import user, lalu tambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE)` di dalam model item. modifikasi `create_item` seperti berikut:
```py
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
     item = form.save(commit=False)
     item.user = request.user
     item.save()
     return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```
di dalam `show_main` tambahkan fungsi `'name': request.user.username` di dalam context. Lalu save
![jsonid](https://github.com/MuhRafliD/essential-ease/blob/main/assets/cookies.png?raw=true)

7. Membuat 2 user dengan 3 item per user
#### Dummy 1
![jsonid](https://github.com/MuhRafliD/essential-ease/blob/main/assets/dummy1.png?raw=true)


#### Dummy 2
![jsonid](https://github.com/MuhRafliD/essential-ease/blob/main/assets/dummy2.png?raw=true)


   
7. Membuat Tombol Peningkatan dan Pengurangan untuk Jumlah serta Tombol Hapus untuk Menghapus Item


# Tugas 5
## Nomor 1
Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

1. Selector Elemen
Tujuannya adalah untuk Memilih semua elemen HTML dari jenis tertentu. Kami menggunakan selektor ini ketika kami ingin menerapkan gaya pada semua instansi elemen HTML tertentu di seluruh situs web kami. Contoh: selektor p menargetkan semua elemen "<p>"(paragraf).

2. Selektor Kelas
Tujuannya adalah untuk Memilih elemen dengan nilai atribut kelas tertentu. Kami menggunakan selektor ini ketika kami ingin menerapkan gaya pada satu atau lebih elemen dengan kelas tertentu. Kelas dapat digunakan kembali pada beberapa elemen. Contoh: selektor .btn menargetkan semua elemen dengan kelas="btn".

3. Selektor ID
Tujuannya adalah untuk Memilih satu elemen dengan nilai atribut id tertentu. Kami menggunakan selektor ini ketika kami ingin menargetkan elemen unik dengan id tertentu. Contoh: selektor #header menargetkan elemen dengan id="header".

## Nomor 2
Jelaskan HTML5 Tag yang kamu ketahui.

1. `<header>` - digunakan untuk menandai elemen bagian teratas dari sebuah laman web atau elemen teratas dari sebuah sektor pada laman web.
2. `<nav>` - digunakan untuk menunjukkan bagian navigasi pada sebuah laman web.
3. `<section>` - digunakan untuk menandai sebuah sektor pada sebuah laman web.
4. `<article>` - digunakan untuk menunjukkan sebuah tulisan atau artikel pada sebuah laman web.
5. `<aside>` - digunakan untuk menunjukkan sebuah elemen yang berkaitan dengan isi utama pada sebuah laman web.
6. `<footer>` - digunakan untuk menandai elemen bagian bawah dari sebuah laman web atau elemen bagian bawah dari sebuah sektor pada laman web.

## Nomor 3
Jelaskan perbedaan antara margin dan padding.

Padding menggambarkan jumlah ruang dalam yang dimiliki oleh suatu elemen, sementara margin adalah ruang putih yang tersedia di sekitar suatu elemen.

## Nomor 4
Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Tailwind adalah sebuah framework CSS yang menawarkan fleksibilitas dan kebebasan yang luas. Ia menawarkan banyak pilihan penyesuaian tetapi memiliki kurva pembelajaran yang lebih tinggi. Bootstrap menyediakan pengalaman pengembangan yang lebih bermutu dan terstruktur dengan beragam komponen pra-dibangun. Bootstrap tidak sefleksibel Tailwind, tetapi lebih mudah untuk dipahami. Kita sebaiknya menggunakan Bootstrap ketika ingin membuat situs web sederhana yang tidak memerlukan banyak penyesuaian pada CSS-nya. Kita sebaiknya menggunakan Tailwind jika ingin membuat situs web yang lebih ekstensif dengan banyak penyesuaian pada CSS-nya.

## Nomor 5
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Mengedit file `base.html` dengan menyisipkan kode berikut untuk menerapkan Bootstrap.
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
        {% endblock meta %}
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
2. Kustomisasi main.html
```
{% extends 'base.html' %}

{% block content %}
<div class="container">
    <h1>Essential Ease</h1>

    <div class="user-info">
        <h5>Name:</h5>
        <p>{{name}}</p>

        <h5>Class:</h5>
        <p>{{class}}</p>

        <h5>Persediaan</h5>
        <p>Di Essential Ease terdapat {{item_count}} item</p>
    </div>

    <div class="item-card-container">
        {% for item in items %}
        <div class="item-card">
            <h2>{{ item.name }}</h2>
            <p><strong>Category:</strong> {{ item.category }}</p>
            <p><strong>Description:</strong> {{ item.description }}</p>
            <p><strong>Price:</strong> {{ item.price }}</p>
            <p><strong>Amount:</strong> {{ item.amount }}</p>
            <div class="item-actions">
                <form method="post">
                    {% csrf_token %}
                    <button type="submit" name="increment" value="{{ item.id }}" class="increment-btn">
                        + Amount
                    </button>
                    <button type="submit" name="decrement" value="{{ item.id }}" class="decrement-btn">
                        - Amount
                    </button>
                    <button type="submit" name="delete" value="{{ item.id }}" class="delete-btn">
                        Delete
                    </button>
                </form>
                <a href="{% url 'main:edit_item' item.pk %}" class="edit-link">
                    Edit
                </a>
            </div>
        </div>
        {% endfor %}
    </div>

    <div class="page-actions">
        <a href="{% url 'main:create_item' %}" class="add-item-link">
            Add New Item
        </a>
        <a href="{% url 'main:logout' %}" class="logout-link">
            Logout
        </a>
        
    </div>

    <div>
        <h1></h1>
        <h2></h2>
        <h5>Sesi terakhir login: {{ last_login }}</h5>
    </div>
</div>

<style>
    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }

    .user-info {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
    }

    .item-card-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }

    .item-card {
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 20px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        text-align: left;
        margin-bottom: 20px;
    }

    .item-card h2 {
        color: #333;
        margin-top: 0;
    }

    .item-actions {
        margin-top: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .increment-btn,
    .decrement-btn,
    .delete-btn {
        background-color: #007BFF;
        color: #fff;
        border: none;
        padding: 5px 10px;
        border-radius: 3px;
        cursor: pointer;
    }

    .edit-link {
        color: #007BFF;
        text-decoration: none;
        font-weight: bold;
    }

    .add-item-link,
    .logout-link {
        background-color: #28a745;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 3px;
        text-decoration: none;
        margin-right: 10px;
        cursor: pointer;
    }
</style>
{% endblock %}
```
![jsonid](https://github.com/MuhRafliD/essential-ease/blob/main/assets/mainee.png?raw=true)

3. Kustomisasi Login
```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login-container">
    <div class="login-form">
        <h1>Login</h1>
        <form method="POST" action="">
            {% csrf_token %}
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" name="username" id="username" placeholder="Username" class="form-control">
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" name="password" id="password" placeholder="Password" class="form-control">
            </div>
            <div class="form-group">
                <button class="btn login-btn" type="submit">Login</button>
            </div>
        </form>
        {% if messages %}
            <ul class="error-messages">
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
        <p>Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a></p>
    </div>
</div>

<style>
    .login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .login-form {
        background-color: #fff;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    }

    .form-group {
        margin-bottom: 15px;
    }

    label {
        font-weight: bold;
    }

    .form-control {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 3px;
    }

    .login-btn {
        background-color: #007BFF;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 3px;
        cursor: pointer;
    }

    .error-messages {
        color: red;
        list-style-type: none;
        padding: 0;
    }

    .login-image {
        margin-left: 20px;
    }

    /* Add any additional styles as needed */
</style>
{% endblock content %}
```
![jsonid](https://github.com/MuhRafliD/essential-ease/blob/main/assets/loginee.png?raw=true)

4. Kustomisasi Register
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}
<div class="register-container">
    <div class="register-form">
        <h1>Register</h1>
        <form method="POST">
            {% csrf_token %}
            <div class="form-group">
                {{ form.username.label_tag }}
                {{ form.username }}
            </div>
            <div class="form-group">
                {{ form.email.label_tag }}
                {{ form.email }}
            </div>
            <div class="form-group">
                {{ form.password1.label_tag }}
                {{ form.password1 }}
            </div>
            <div class="form-group">
                {{ form.password2.label_tag }}
                {{ form.password2 }}
            </div>
            <div class="form-group">
                <button class="btn register-btn" type="submit">Register</button>
            </div>
        </form>
        {% if messages %}
            <ul class="error-messages">
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
        <p>Already have an account? <a href="{% url 'main:login' %}">Login</a></p>
    </div>
</div>

<style>
    .register-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .register-form {
        background-color: #fff;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    }

    .form-group {
        margin-bottom: 15px;
    }

    label {
        font-weight: bold;
    }

    .form-control {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 3px;
    }

    .register-btn {
        background-color: #28a745;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 3px;
        cursor: pointer;
    }

    .error-messages {
        color: red;
        list-style-type: none;
        padding: 0;
    }

    .register-image {
        margin-left: 20px;
    }

    /* Add any additional styles as needed */
</style>
{% endblock content %}
```
![jsonid](https://github.com/MuhRafliD/essential-ease/blob/main/assets/registeree.png?raw=true)

5. Kustomisasi add item
```
{% extends 'base.html' %}

{% block content %}
<div class="container">
    <div class="add-item-container">
        <h1>Add New Item</h1>
        <form method="POST">
            {% csrf_token %}
            <div class="form-group">
                {{ form.as_p }}
            </div>
            <div class="form-group">
                <input class="add-item-btn" type="submit" value="Add Item"/>
            </div>
        </form>
    </div>
</div>

<style>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .add-item-container {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        text-align: left;
        max-width: 400px;
        width: 100%;
    }

    h1 {
        color: #333;
        margin-top: 0;
    }

    .form-group {
        margin-bottom: 20px;
    }

    .add-item-btn {
        background-color: #007BFF;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 3px;
        cursor: pointer;
        font-size: 16px;
    }
</style>

{% endblock %}
```
![jsonid](https://github.com/MuhRafliD/essential-ease/blob/main/assets/addee.png?raw=true)

6. Kustomisasi edit item
```
{% extends 'base.html' %}

{% block content %}
<div class="container">
    <div class="edit-item-container">
        <h1>Edit Item</h1>
        <form method="POST">
            {% csrf_token %}
            <div class="form-group">
                {{ form.as_p }}
            </div>
            <div class="form-group">
                <input class="edit-item-btn" type="submit" value="Edit Item"/>
            </div>
        </form>
    </div>
</div>

<style>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .edit-item-container {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        text-align: left;
        max-width: 400px;
        width: 100%;
    }

    h1 {
        color: #333;
        margin-top: 0;
    }

    .form-group {
        margin-bottom: 20px;
    }

    .edit-item-btn {
        background-color: #28a745;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 3px;
        cursor: pointer;
        font-size: 16px;
    }
</style>

{% endblock %}
```
![jsonid](https://github.com/MuhRafliD/essential-ease/blob/main/assets/editee.png?raw=true)

# Tugas 6
## Nomor 1
Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Synchronous programming adalah metode pemrograman di mana operasi atau tugas-tugas dieksekusi secara berurutan. Dalam metode ini, jika ada operasi yang memerlukan durasi panjang, seluruh program akan menunggu dan tidak dapat melaksanakan operasi lain hingga operasi tersebut berakhir.

Asynchronous programming adalah metode pemrograman yang memungkinkan operasi untuk berjalan di latar belakang dan tidak menghalangi (blocking) eksekusi operasi lainnya. Dalam metode ini, tugas yang membutuhkan waktu yang lama dapat dijalankan secara bersamaan dengan tugas lainnya, sehingga program dapat terus berjalan tanpa terhenti.

Dalam pemrograman Asynchronous programming, program memanfaatkan fungsi callback atau promise untuk mengatasi hasil dari operasi yang sedang dijalankan. Fungsi callback akan diaktifkan saat operasi selesai, sementara promise memberikan nilai setelah operasi rampung. Sebaliknya, dalam Synchronous programming , program akan menanti hingga sebuah operasi selesai sebelum bergerak ke operasi selanjutnya, jadi tidak diperlukan fungsi callback atau promise.

## Nomor 2
Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

aradigma event-driven programming adalah paradigma pemrograman di mana program merespons peristiwa atau event yang terjadi, seperti klik tombol atau masukan dari pengguna. Dalam paradigma ini, program tidak dieksekusi secara berurutan, melainkan menunggu peristiwa atau event yang terjadi untuk memberikan respons. Saat event terjadi, program akan menjalankan fungsi atau kode yang telah ditentukan sebelumnya untuk menangani event tersebut. Paradigma ini terbukti sangat bermanfaat dalam pengembangan aplikasi web interaktif, karena memungkinkan program untuk dengan cepat dan efisien merespons masukan pengguna.

## Nomor 3
Jelaskan penerapan asynchronous programming pada AJAX.

Pada AJAX, asynchronous programming digunakan untuk mengambil data dari server tanpa harus memuat ulang halaman web. Dalam asynchronous programming, program akan mengirim permintaan ke server dan melanjutkan eksekusi program tanpa harus menunggu respon dari server. Ketika respon dari server diterima, program akan menjalankan fungsi atau kode yang telah ditentukan sebelumnya untuk menangani respon tersebut. Dalam AJAX, asynchronous programming memungkinkan program untuk mengambil data dari server secara efisien dan responsif, tanpa harus memuat ulang halaman web secara keseluruhan. Hal ini membuat pengalaman pengguna menjadi lebih baik dan meningkatkan kinerja aplikasi web secara keseluruhan.

## Nomor 4
Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

Sejak munculnya AJAX, library jQuery telah menjadi instrumen utama dalam implementasinya, menawarkan cara sederhana untuk melakukan permintaan asinkron. Keunggulan dari AJAX melalui jQuery terletak pada kompatibilitas lintas browser-nya, memastikan fungsionalitas bahkan pada browser yang lebih tua yang belum mendukung teknologi web terkini. Namun, seiring berjalannya waktu, browser modern telah menawarkan Fetch API yang merupakan fitur bawaan browser modern, memungkinkan permintaan asinkron tanpa kebutuhan library tambahan. Fetch API menyediakan fleksibilitas lebih dalam mengelola permintaan dan respons, dan mendukung teknologi terbaru seperti promises dan async/await. Mengingat Fetch API adalah standar web modern, dukungan lintas browser sudah luas, dan ini menghilangkan kebutuhan library tambahan.
Untuk sekarang, Fetch API sering kali dipilih karena kode yang lebih efisien, tidak adanya ketergantungan, dan kapabilitas aslinya. Meskipun demikian, untuk aplikasi yang fokus pada kompatibilitas atau telah mengadopsi jQuery sepenuhnya, AJAX melalui jQuery masih memiliki tempatnya.


## Nomor 
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).




