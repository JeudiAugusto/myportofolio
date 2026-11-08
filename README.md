# Jeudi Augusto Asadullah - Personal Portfolio

Personal portfolio website yang dikembangkan sebagai bagian dari pembelajaran mata kuliah **Pemrograman Berbasis Platform (PBP) Gasal 2026/2027** di Fakultas Ilmu Komputer, Universitas Indonesia.

Website ini menampilkan profil pribadi, keterampilan, project yang pernah saya kerjakan, serta informasi kontak dalam sebuah halaman portfolio yang responsif.

---

## Identity

- **Nama:** Jeudi Augusto Asadullah
- **NPM:** 2506656822
- **Kelas:** PBP C
- **Program Studi:** S1 Sistem Informasi
- **Universitas:** Universitas Indonesia

---

## About the Project

Project ini merupakan website portfolio pribadi yang dikembangkan secara bertahap mengikuti materi PBP.

Pada **Tutorial 01 dan Tugas Individu 1**, fokus utama pengembangan berada pada struktur halaman menggunakan semantic HTML5 dan styling menggunakan CSS3. Django digunakan sebagai struktur project dan untuk menyajikan template, sedangkan tampilan halaman pada Tugas Individu 1 tetap dibangun menggunakan HTML5 dan CSS3 tanpa database maupun pengelolaan data dinamis.

Selain memenuhi kebutuhan dasar tugas, website dikembangkan dengan beberapa peningkatan UI/UX agar memiliki identitas visual yang lebih kuat, tetap mudah digunakan, dan nyaman dilihat pada berbagai ukuran layar.

---

## Features

### Core Features

- Personal profile / hero section
- About Me section
- Skills section
- Projects section
- Contact section
- Social media links
- Responsive layout
- Semantic HTML5 structure

### UI/UX Enhancements

Beberapa pengembangan tambahan yang diterapkan di luar kebutuhan minimum tugas:

- Sticky navigation
- Smooth scrolling
- Navigation hover interaction
- Interactive skill cards
- Skill proficiency indicators
- Project technology tags
- Project case-study preview
- Animated profile image
- "Currently Learning" status indicator
- Responsive desktop, tablet, dan mobile layout
- Keyboard focus states
- `prefers-reduced-motion` support untuk meningkatkan accessibility

---

## Projects

### 1. Personal Portfolio

Website portfolio pribadi yang dikembangkan sebagai bagian dari mata kuliah Pemrograman Berbasis Platform.

**Teknologi:**

- Python
- Django
- HTML5
- CSS3

**Repository:**
https://github.com/JeudiAugusto/myportofolio

### 2. Cashie

Cashie merupakan aplikasi web pengelola keuangan yang dikembangkan secara kolaboratif pada project Pemrograman Web.

Beberapa fitur yang tersedia:

- Login
- Register
- Dashboard
- Pengelolaan data keuangan
- CRUD
- AJAX
- Database integration

**Teknologi:**

- PHP
- JavaScript
- SQL
- phpMyAdmin

**Repository:**
https://github.com/fzdhl/cashie

---

## Tech Stack

### Backend / Project Environment

- Python
- Django

### Frontend

- HTML5
- CSS3

### Deployment

- PWS Fasilkom UI
- Gunicorn
- WhiteNoise

### Development Tools

- Git
- GitHub
- Visual Studio Code
- PowerShell

---

## Project Structure

```text
myportofolio/
|-- manage.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- portofolio/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- views.py
|   |-- asgi.py
|   `-- wsgi.py
|-- templates/
|   `-- index.html
`-- static/
    |-- css/
    |   `-- style.css
    `-- img/
        `-- profile.jpg
```

---

## Running the Project Locally

### Prerequisites

Pastikan perangkat sudah memiliki:

- Python
- Git
- `pip`

### 1. Clone repository

```bash
git clone https://github.com/JeudiAugusto/myportofolio.git
cd myportofolio
```

### 2. Create virtual environment

Pada Windows:

```powershell
py -m venv env
```

Aktifkan virtual environment:

```powershell
.\env\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Run Django development server

```powershell
python manage.py runserver
```

Apabila command `python` tidak dikenali pada Windows, gunakan:

```powershell
py manage.py runserver
```

### 5. Open the website

Buka browser dan akses:

```text
http://127.0.0.1:8000/
```

---

## Deployment

Versi deployment project dapat diakses melalui PWS Fasilkom UI:

https://jeudi-augusto-jeudiaugustoasadullah.pws.cs.ui.ac.id/

Konfigurasi production memanfaatkan environment variable agar konfigurasi development dan production dapat dibedakan. Static files ditangani menggunakan WhiteNoise dan aplikasi dijalankan dengan Gunicorn pada environment deployment.

Informasi sensitif seperti `SECRET_KEY` tidak disimpan di repository, dan file environment production dimasukkan ke `.gitignore`.

---

## Development Progress

### Week 1 - Tutorial 0

Tahap awal project berfokus pada:

- Konfigurasi Git
- Membuat repository GitHub
- Mempelajari workflow commit dan push
- Membuat serta menggabungkan branch
- Membuat virtual environment
- Membuat initial Django project
- Menyiapkan dependency project
- Melakukan konfigurasi deployment awal

Pada tahap ini saya juga berlatih menggunakan branch terpisah dan Pull Request sebelum perubahan digabungkan kembali ke branch utama.

### Week 2 - Tutorial 1 dan Individual Assignment 1

Tahap ini berfokus pada:

- Menyiapkan Django view
- Menghubungkan URL dengan view
- Menghubungkan view dengan HTML template
- Membuat halaman portfolio
- Menggunakan semantic HTML5
- Menggunakan external CSS
- Membuat responsive layout
- Menampilkan data pribadi pada halaman About Me
- Menambahkan Skills section
- Menambahkan Projects section
- Menambahkan Contact section
- Menambahkan hover interaction
- Menambahkan skill proficiency indicator
- Menambahkan technology tags pada project
- Menambahkan project case-study preview
- Menambahkan animasi pada profile image
- Menambahkan "Currently Learning" status
- Menambahkan keyboard focus state
- Menambahkan `prefers-reduced-motion`
- Melakukan deployment dan final documentation

Saya tidak hanya berusaha memenuhi checklist minimum tugas, tetapi juga mempertimbangkan hierarchy, konsistensi visual, responsiveness, accessibility, dan maintainability dari struktur HTML/CSS.

---

## Git Workflow

Project dikembangkan menggunakan Git secara bertahap.

Beberapa jenis commit yang digunakan antara lain:

```text
feat: ...
fix: ...
chore: ...
docs: ...
```

Saya menggunakan commit terpisah untuk merekam perubahan sesuai tujuan masing-masing, seperti pembuatan fitur portfolio, konfigurasi production, perbaikan kompatibilitas deployment, dan pembaruan dokumentasi.

Pada latihan Git sebelumnya saya juga menggunakan feature branch dan Pull Request untuk memahami workflow pengembangan yang lebih terstruktur.

---

## AI Disclosure

Dalam pengerjaan project ini saya menggunakan **ChatGPT** sebagai alat bantu pembelajaran, evaluasi, dan debugging.

AI tidak digunakan hanya untuk menghasilkan source code secara langsung, tetapi terutama untuk membantu memahami langkah pengerjaan, menjelaskan alasan di balik konfigurasi, mengevaluasi kemungkinan error, dan memberikan alternatif solusi ketika terjadi masalah.

### Bagian yang Dibantu AI

1. **Git workflow**
   - Menjelaskan repository initialization, branch, commit, push, Pull Request, dan sinkronisasi remote.
   - Membantu memahami perbedaan branch GitHub dengan branch yang digunakan untuk deployment.

2. **Django project configuration**
   - Menjelaskan struktur Django project.
   - Membantu menghubungkan URL, view, template, dan static files.
   - Membantu mengevaluasi konfigurasi development dan production.

3. **HTML5 dan CSS3**
   - Memberikan masukan mengenai semantic HTML.
   - Membantu mengevaluasi responsive layout.
   - Memberikan ide enhancement UI/UX seperti skill indicator, project preview, focus state, dan reduced-motion support.

4. **Deployment debugging**
   - Membantu membaca dan menganalisis build log dari PWS.
   - Membantu mengidentifikasi masalah compatibility dependency.
   - Membantu mengevaluasi konfigurasi HTTPS dan reverse proxy pada deployment.

5. **Documentation**
   - Membantu mengevaluasi struktur README agar informasi project, setup, progres pengerjaan, AI disclosure, dan refleksi disampaikan dengan lebih terstruktur.

### Prompting Strategy

Saya menggunakan AI secara iteratif, bukan hanya memberikan satu prompt besar untuk menghasilkan seluruh project.

Strategi yang saya gunakan:

- Menjelaskan konteks tutorial atau tugas yang sedang dikerjakan.
- Memberikan requirement tugas agar solusi tetap sesuai materi.
- Mengirimkan error message atau build log ketika terjadi masalah.
- Meminta penjelasan langkah demi langkah, bukan hanya meminta hasil akhir.
- Menjalankan solusi pada komputer saya sendiri.
- Memberikan kembali output terminal kepada AI untuk dianalisis.
- Membandingkan saran AI dengan requirement resmi tugas.
- Melakukan pengecekan manual pada source code dan hasil website.

Alur prompting yang digunakan:

```text
Context dan requirement tugas
        |
        v
Meminta penjelasan dan langkah implementasi
        |
        v
Implementasi secara lokal
        |
        v
Menjalankan program atau deployment
        |
        v
Mengirim output atau error
        |
        v
Menganalisis dan memperbaiki solusi
        |
        v
Verifikasi manual
```

### Limitations of AI and Manual Improvements

Selama pengerjaan, saya menemukan bahwa saran AI tidak selalu dapat langsung digunakan tanpa verifikasi.

Salah satu contoh penting terjadi pada dependency Django. Environment lokal saya dapat menggunakan versi Python yang lebih baru, sedangkan environment deployment PWS menggunakan versi Python yang berbeda. Build PWS menunjukkan bahwa versi Django yang sebelumnya digunakan tidak kompatibel dengan Python pada server.

Saya membaca kembali build log dan menyesuaikan dependency menjadi versi Django yang kompatibel dengan environment PWS. Setelah perubahan tersebut, project diuji kembali secara lokal dan melalui deployment.

Hal serupa terjadi ketika mengatur HTTPS pada production. Mengaktifkan HTTPS redirect saja dapat menghasilkan redirect loop ketika aplikasi berjalan di belakang reverse proxy. Konfigurasi kemudian diperbaiki dengan memperhatikan header proxy dari environment deployment dan diuji kembali melalui website PWS.

Untuk HTML dan CSS, ide dari AI juga tidak langsung dianggap sebagai hasil final. Saya tetap melakukan penyesuaian terhadap:

- Konten pribadi yang ditampilkan
- Hierarchy halaman
- Project yang ingin ditampilkan
- Responsive behavior
- Ukuran dan spacing elemen
- Konsistensi visual
- Deployment configuration

Dari proses tersebut saya memahami bahwa AI lebih tepat digunakan sebagai alat bantu analisis dan pembelajaran. Keputusan akhir tetap membutuhkan pemahaman terhadap requirement, pengujian langsung, pemeriksaan dokumentasi atau error log, dan evaluasi manual terhadap hasil implementasi.

---

## Reflection

### Tugas 1

1. **Penggunaan semantic HTML5**

   Pada Tutorial 01 dan Tugas Individu 1, saya menggunakan elemen semantic HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, dan `<footer>`.

   Saya memilih semantic HTML karena setiap elemen dapat menggambarkan peran konten, bukan sekadar menjadi container visual. Sebagai contoh, `<section>` saya gunakan untuk memisahkan bagian About, Skills, Projects, dan Contact, sedangkan `<article>` saya gunakan untuk konten yang secara konseptual dapat berdiri sendiri seperti setiap skill atau project.

   Dibandingkan menggunakan `<div>` untuk hampir seluruh bagian halaman, struktur semantik membuat hubungan antarbagian lebih mudah dipahami ketika source code dibaca kembali. Hal ini juga membantu ketika membuat CSS karena struktur halaman memiliki pembagian tanggung jawab yang lebih jelas.

   Walaupun website pada tahap ini masih static, penggunaan semantic HTML tetap penting karena membuat kode lebih maintainable dan mempersiapkan struktur yang lebih baik ketika website berkembang menjadi lebih kompleks. Semantic element juga memberikan struktur dokumen yang lebih bermakna untuk browser dan teknologi accessibility dibandingkan container generik.

2. **Tantangan responsive CSS**

   Tantangan utama ketika membuat responsive CSS bukan hanya membuat seluruh elemen menjadi lebih kecil, tetapi mempertahankan hierarchy informasi ketika ruang layar berkurang.

   Pada desktop, beberapa bagian dapat menggunakan lebih dari satu kolom karena tersedia ruang horizontal yang cukup. Contohnya, hero section dapat menempatkan informasi utama dan foto secara berdampingan. Ketika layout tersebut dipertahankan pada layar mobile, ruang untuk teks menjadi terlalu sempit dan komposisi halaman menjadi kurang nyaman dibaca.

   Karena itu, saya mengevaluasi responsiveness berdasarkan prioritas konten. Informasi utama seperti nama, deskripsi singkat, dan navigasi harus tetap mudah ditemukan, sedangkan layout visual dapat berubah selama tidak mengurangi makna konten. Pada ukuran layar yang lebih kecil saya mengubah beberapa grid menjadi satu kolom, menyesuaikan typography, spacing, ukuran gambar, dan susunan navigation.

   Saya juga menggunakan lebih dari satu breakpoint agar perubahan antara desktop, tablet, dan mobile tidak terlalu mendadak. Dari proses tersebut saya memahami bahwa responsive design lebih tepat dipandang sebagai proses mengatur ulang hubungan dan prioritas antarelemen daripada sekadar melakukan scaling terhadap layout desktop.

3. **Keterbatasan static web dan rencana pengembangan dinamis**

   Keterbatasan utama yang saya rasakan dari static web adalah hubungan antara konten dengan source code masih terlalu erat. Informasi seperti skills dan projects saat ini ditulis langsung di template HTML. Artinya, setiap kali saya ingin menambah atau mengubah sebuah project, saya harus melakukan perubahan pada source code lalu melakukan deployment ulang.

   Pendekatan tersebut masih cukup untuk portfolio sederhana, tetapi akan semakin sulit dikelola ketika jumlah konten bertambah. Website juga belum dapat menerima, menyimpan, atau memproses input pengguna karena belum terdapat database dan mekanisme pengelolaan data dinamis.

   Pada iterasi berikutnya, fungsi yang paling ingin saya tambahkan adalah penyimpanan data menggunakan model dan database Django. Data seperti projects dan skills nantinya dapat disimpan sebagai objek dan ditampilkan secara dinamis melalui template. Dengan begitu, struktur presentasi tidak perlu berisi seluruh data secara hard-coded.

   Saya juga ingin memanfaatkan Django Admin atau form khusus agar perubahan konten dapat dilakukan melalui interface pengelolaan data. Menurut saya, pengembangan tersebut merupakan langkah yang logis dari static portfolio saat ini karena HTML dan CSS yang sudah dibuat dapat tetap berfungsi sebagai presentation layer, sementara Django dan database nantinya menangani data serta logic aplikasi.

---

## References

- PBP Fasilkom UI - Tutorial 01
- PBP Fasilkom UI - Individual Assignment 1
- Django Documentation
- MDN Web Docs
- Git Documentation

Official PBP course website:

https://pbp.cs.ui.ac.id/

---

## Author

**Jeudi Augusto Asadullah**
S1 Sistem Informasi - Universitas Indonesia
PBP C - Gasal 2026/2027


---

### Tugas 2

1. **Jelaskan bagaimana alur request dari pengguna hingga data model dapat ditampilkan pada halaman melalui MVT.**

   Ketika pengguna membuka halaman `/projects/`, request pertama kali masuk ke `portofolio/urls.py`. Dari sana request diteruskan ke `main/urls.py` menggunakan `include()`.

   Pada `main/urls.py`, path `projects/` diarahkan ke view `show_projects`. View tersebut mengambil data dari model `Project` menggunakan Django ORM dengan `Project.objects.all().order_by("-year", "title")`.

   Hasil query dimasukkan ke context dengan nama `project_list`, kemudian dikirim ke `projects.html` menggunakan fungsi `render()`.

   Pada template, data ditampilkan dengan Django Template Language melalui loop `{% for project in project_list %}`. Jadi alurnya adalah browser -> project URL -> app URL -> view -> model dan database -> context -> template -> HTML response.

   Menurut saya pembagian MVT membuat fungsi setiap bagian lebih jelas. URL menentukan request diarahkan ke mana, view menangani logic dan pengambilan data, model merepresentasikan data di database, sedangkan template bertugas menampilkan hasilnya.

2. **Mengapa data lebih baik disimpan pada model dibandingkan ditulis secara hard-coded pada template?**

   Pada Tugas 1, data Personal Portfolio dan Cashie masih saya tulis langsung di `index.html`. Cara tersebut masih cukup ketika jumlah project sedikit, tetapi setiap ingin mengubah atau menambah project saya harus mengedit HTML secara langsung.

   Pada Tugas 2, data tersebut saya pindahkan ke model `Project`. Dengan begitu data dan tampilan menjadi terpisah. Template hanya menentukan bentuk tampilan project, sedangkan isi seperti title, description, year, role, focus, technologies, dan repository URL disimpan pada database.

   Satu template juga dapat digunakan untuk menampilkan banyak object menggunakan loop. Data dapat diurutkan menggunakan `Project.objects.all().order_by("-year", "title")`, sehingga urutan project tidak perlu diatur secara manual di HTML.

   Menurut saya struktur ini lebih mudah dikembangkan. Ke depannya data Project dapat dikelola melalui Django Admin atau form tanpa perlu mengubah template setiap kali ada project baru.

3. **Apa perbedaan `makemigrations` dan `migrate`? Berikan contoh berdasarkan perubahan model pada project.**

   `makemigrations` digunakan untuk membaca perubahan pada model Django kemudian membuat file migration yang berisi instruksi perubahan struktur database.

   Ketika saya menambahkan model `Project`, saya menjalankan `python manage.py makemigrations`. Django kemudian menghasilkan file `main/migrations/0004_project.py`.

   Pada tahap tersebut perubahan belum diterapkan ke database. Setelah itu saya menjalankan `python manage.py migrate`. Migration `0004_project` kemudian diterapkan sehingga struktur tabel untuk Project dibuat pada database.

   Jadi yang saya pahami, `makemigrations` membuat catatan atau instruksi perubahan schema berdasarkan model Django, sedangkan `migrate` menerapkan instruksi tersebut ke database.


### Tugas 3

1. **Mengapa menggunakan `ModelForm` dibandingkan membuat form HTML secara manual? Mengapa perlu `{% csrf_token %}`?**

   Saya menggunakan `ModelForm` karena form dapat dibuat langsung berdasarkan model Django yang sudah ada. Dengan begitu, saya tidak perlu mendefinisikan ulang setiap field dan validasinya secara manual di HTML. Pada tugas ini, saya membuat `ExperienceForm` berdasarkan model `Experience`, sehingga field seperti `title`, `description`, `category`, dan `thumbnail` dapat langsung digunakan untuk proses create maupun update. Penggunaan `ModelForm` juga membuat kode lebih konsisten karena validasi form mengikuti aturan yang sudah didefinisikan pada model.

   `{% csrf_token %}` digunakan untuk melindungi form yang mengirim request `POST` dari serangan Cross-Site Request Forgery (CSRF). Token tersebut memastikan bahwa request yang diterima server berasal dari form pada aplikasi Django yang sah. Pada fitur create, update, dan delete Experience, token CSRF disertakan agar Django dapat memverifikasi request sebelum data di database diubah.

2. **Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?**

   JSON lebih sering digunakan karena struktur datanya lebih ringkas dan mudah dibaca. Penulisannya tidak membutuhkan tag pembuka dan penutup seperti XML sehingga ukuran data yang dikirim juga cenderung lebih kecil. JSON juga sangat mudah digunakan bersama JavaScript karena format object dan array pada JSON mirip dengan struktur data yang digunakan di JavaScript. Hal ini membuat proses pertukaran data antara backend dan frontend menjadi lebih sederhana.

   XML tetap memiliki kegunaan tertentu, tetapi untuk kebutuhan web modern seperti REST API dan komunikasi client-server, JSON biasanya lebih praktis karena parsing-nya sederhana dan formatnya tidak terlalu verbose.

3. **Bagaimana alur view ketika mengembalikan data portofolio dalam format JSON? Mengapa model Django perlu diserialisasi?**

   Pada tugas ini, fungsi `get_experiences_json` mengambil data dari model `Experience` menggunakan Django ORM. Hasil query tersebut masih berupa QuerySet yang berisi object model Django. Object tersebut belum dapat langsung dikirim sebagai response JSON karena JSON hanya dapat merepresentasikan tipe data tertentu seperti string, angka, boolean, array, object, dan null.

   Karena itu, saya menggunakan `serializers.serialize("json", experiences)` untuk mengubah QuerySet menjadi representasi JSON. Hasil serialization kemudian dikembalikan melalui `HttpResponse` dengan `content_type="application/json"`.

   Untuk menampilkan Experience pada halaman web, fungsi `show_experience` mengambil response JSON tersebut lalu melakukan `serializers.deserialize()`. Hasil deserialization diubah kembali menjadi object `Experience` sehingga atribut dan method model, seperti `get_category_display` dan `is_ongoing`, tetap dapat digunakan oleh template `experience.html`.

#### Progress Tugas 3

Pada Tugas 3 saya memilih bagian **Experience** sebagai objek penerapan Form & Data Delivery. Fitur yang saya implementasikan meliputi:

- Create Experience menggunakan `ExperienceForm`.
- Update Experience berdasarkan UUID.
- Delete Experience menggunakan request `POST`.
- Endpoint JSON pada `/api/experiences/`.
- Serialization dan deserialization data Experience.
- Halaman create dan update yang menggunakan template inheritance.
- Tombol Add, Update, dan Delete pada halaman Experience.
- Success message setelah proses create, update, dan delete.
- Automated testing untuk fitur Experience dan fitur Tutorial 03 yang sudah ada.

#### AI Disclosure

Dalam pengerjaan Tugas 3, saya menggunakan **ChatGPT** sebagai alat bantu untuk berdiskusi mengenai implementasi Django, menyusun langkah pengembangan secara bertahap, melakukan review struktur kode, dan membantu menyusun skenario automated testing. Prompt yang saya gunakan umumnya meminta penjelasan langkah demi langkah berdasarkan struktur project yang sudah saya buat, kemudian setiap perubahan saya jalankan dan uji sendiri pada environment lokal.

Bagian yang dibantu AI terutama meliputi struktur `ModelForm`, pola view create/update/delete, serialization dan deserialization JSON, penataan UI form, serta penyusunan test case. Saya tidak langsung menganggap setiap output AI benar. Setiap perubahan diperiksa menggunakan `python manage.py check`, diuji melalui browser, dicek langsung pada database melalui Django shell, dan akhirnya diuji menggunakan `python manage.py test`.

Salah satu keterbatasan AI yang saya temukan adalah AI dapat memberikan asumsi mengenai requirement atau struktur project apabila konteks yang diberikan belum lengkap. Karena itu, saya melakukan cross-check terhadap instruksi resmi PBP dan menyesuaikan kode dengan model serta template yang sudah ada. Contohnya, field yang berhubungan dengan timestamp tidak saya masukkan ke dalam `ExperienceForm` karena field tersebut tidak termasuk data yang perlu diisi melalui form. Saya juga melakukan pengujian manual terhadap alur Create → Update → Delete untuk memastikan jumlah object di database berubah sesuai yang diharapkan.
---

### Tugas 4

Pada Tugas 4, saya melanjutkan fitur Experience dari Tugas 3 dengan menerapkan autentikasi, otorisasi berbasis role, dan fitur Star.

#### Progress Tugas 4

Hak akses dibagi menjadi empat role:

- Guest dapat melihat Experience dan tombol Star, tetapi ketika melakukan aksi Star akan diarahkan ke halaman login. Guest tidak dapat melakukan create, update, atau delete.
- User biasa dapat melihat Experience serta melakukan Star dan Unstar, tetapi tidak dapat melakukan create, update, atau delete.
- Editor memiliki hak seperti user biasa dan dapat melakukan update Experience, tetapi tidak dapat melakukan create atau delete.
- Superuser dapat melakukan Star, Unstar, create, update, dan delete Experience.

Pembatasan akses tidak hanya dilakukan melalui tampilan template, tetapi juga diperiksa pada sisi server. User yang belum login diarahkan ke halaman login, sedangkan user yang sudah login tetapi tidak memiliki izin akan menerima HTTP 403 Forbidden.

Role Editor menggunakan Django Group bernama `Editor`. Group tersebut dibuat melalui data migration sehingga tersedia ketika project dijalankan pada database baru.

Model Experience memiliki relasi `ManyToManyField` bernama `starred_by` untuk menyimpan user yang memberikan Star pada suatu Experience.

Fitur Star menggunakan request POST dan CSRF token. Jika user sudah memberikan Star, relasi akan dihapus. Jika belum, user akan ditambahkan ke `starred_by`.

Endpoint JSON `/api/experiences/` menggunakan `use_natural_foreign_keys=True` agar relasi user tidak menggunakan ID internal database dan tidak mengekspos data sensitif seperti password.

Automated testing mencakup akses Guest, User biasa, Editor, Superuser, Star/Unstar, role-based UI, dan keamanan endpoint JSON.

Hasil akhir pengujian lokal:

    Found 42 test(s).
    ..........................................
    Ran 42 tests in ...
    OK

#### AI Disclosure Tugas 4

Dalam pengerjaan Tugas 4 saya menggunakan ChatGPT sebagai alat bantu pembelajaran, debugging, review requirement, dan penyusunan automated test.

Pengerjaan dilakukan secara bertahap. Setiap perubahan diverifikasi menggunakan `python manage.py check`, migration, Django shell, dan `python manage.py test`.

AI membantu dalam memahami pembagian role, server-side authorization, relasi ManyToMany untuk fitur Star, pengujian JSON, serta penyusunan test untuk setiap role.

Saya tetap melakukan verifikasi terhadap setiap saran. Contohnya, error `UNIQUE constraint failed: auth_group.name` terjadi karena Group Editor sudah dibuat oleh migration tetapi test mencoba membuat Group yang sama kembali. Setup test kemudian diperbaiki menggunakan `get_or_create()`.

Automated test juga membantu menemukan bahwa tombol Star untuk Guest masih tersembunyi. Template kemudian diperbaiki agar tombol tetap terlihat, sedangkan keamanan tetap dijaga menggunakan `@login_required` pada view.

Dari proses ini saya memahami bahwa penggunaan AI tetap harus disertai pengecekan requirement, source code, dan pengujian langsung.

### Tugas 5
1. **Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!**
   Debouncing adalah teknik pemrograman yang menunda eksekusi sebuah fungsi sampai jeda waktu tertentu (misal 300ms) berlalu sejak interaksi terakhir. Pada pencarian AJAX, ini penting agar aplikasi tidak menembakkan request ke server pada setiap ketikan huruf. Tanpa debouncing, server berisiko overload dan antarmuka pengguna menjadi lag.

2. **Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?**
   wait digunakan untuk menjeda eksekusi baris kode berikutnya sampai *Promise* dari fungsi asynchronous (seperti etch()) berstatus *resolved* atau selesai mengembalikan data. Jika tidak menggunakan wait, kode di bawahnya akan langsung dieksekusi saat data belum tiba, menyebabkan variabel berisi objek *Promise* menggantung dan berujung pada error saat mencoba merender data tersebut ke HTML.

3. **Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini?**
   XSS adalah serangan yang dilakukan dengan cara menginjeksi skrip berbahaya (seperti tag <script>) ke dalam input data, yang kemudian terender di halaman pengguna lain. Data yang disisipkan melalui AJAX menggunakan manipulasi DOM (seperti .innerHTML) sangat rentan karena browser akan mengeksekusi *string* HTML secara mentah. Hal ini berbeda dengan sistem *template* Django yang secara default melakukan *auto-escaping* untuk mengubah karakter tag HTML menjadi entitas yang aman.


### Tutorial 7 ? Django REST Framework

Implementasi mengikuti [Tutorial 07 PBP](https://pbp.cs.ui.ac.id/tutorial/tutorial-7.html) pada proyek dan database yang sama. Halaman Projects memakai API DRF untuk pencarian, tambah, star/unstar, dan hapus tanpa reload. Pola tersebut juga diterapkan pada Experience, termasuk create/update melalui AJAX dan hak akses Editor.

#### Penyesuaian model

Model Project yang sudah ada dipertahankan: `technologies` merupakan padanan `tech_stack`, sedangkan `repository_url` merupakan padanan `project_url`. Field tambahan `year`, `role`, dan `focus` tetap wajib. Model ini tidak memiliki `project_image_url`, sehingga field gambar contoh tutorial tidak ditambahkan. Template yang digunakan adalah `templates/projects.html` dan `templates/experience.html`; template Experience di folder app bukan template aktif karena direktori template proyek didahulukan.

#### Endpoint dan izin

| Endpoint | Method | Akses |
| --- | --- | --- |
| `/api/v1/projects/` | GET, HEAD | Publik; pencarian `?title=...` |
| `/api/v1/projects/` | POST | Superuser |
| `/api/v1/projects/<uuid>/` | GET, HEAD | Publik |
| `/api/v1/projects/<uuid>/` | PUT, PATCH, DELETE | Superuser |
| `/api/v1/projects/<uuid>/star/` | POST | Akun login |
| `/api/v1/experiences/` | GET, HEAD | Publik; pencarian `?title=...` |
| `/api/v1/experiences/` | POST | Superuser |
| `/api/v1/experiences/<uuid>/` | GET, HEAD | Publik |
| `/api/v1/experiences/<uuid>/` | PUT, PATCH | Superuser atau anggota Group Editor |
| `/api/v1/experiences/<uuid>/` | DELETE | Superuser |
| `/api/v1/experiences/<uuid>/star/` | POST | Akun login |

Browsable API tersedia pada endpoint tersebut; login API tersedia di `/api-auth/login/`. Gunakan `?format=json` atau header `Accept: application/json` untuk JSON. Endpoint lama tetap tersedia untuk kompatibilitas.

Serializer menghasilkan objek datar (`id`, `title`, dan seterusnya), bukan bentuk `pk`/`fields`. ID dan informasi star hanya bisa dibaca. Validasi menolak judul kosong/tag saja, URL tidak valid, serta kategori Experience yang tidak dikenal. Data teks tetap di-escape saat dirender; tautan repository hanya menggunakan HTTP/HTTPS. SessionAuthentication menggunakan login Django yang sudah ada, dengan token CSRF untuk operasi tulis.

POST sukses menghasilkan 201, GET/update/star menghasilkan 200, DELETE menghasilkan 204 tanpa body. Input salah menghasilkan 400, izin/CSRF gagal 403, objek tidak ditemukan 404, dan method tidak didukung 405. Frontend menangani error DRF, debounce 300 ms, pembatalan pencarian lama, status loading/kosong/error, dan toast.

#### Menjalankan dan memeriksa

```powershell
.\env\Scripts\python.exe -m pip install -r requirements.txt
.\env\Scripts\python.exe manage.py check
.\env\Scripts\python.exe manage.py migrate
.\env\Scripts\python.exe manage.py test main.tests_api --verbosity 2
.\env\Scripts\python.exe manage.py test main
.\env\Scripts\python.exe manage.py runserver
```

`main/tests_api.py` mencakup 13 tes Projects dari tutorial yang disesuaikan dengan model, ditambah 8 tes Experience. Tes memakai database pengujian terpisah. Pengujian meliputi CRUD, pencarian, validasi, field read-only, star akun aktif, perbedaan role, dan session dengan/tanpa CSRF.

Untuk pemeriksaan manual, buka Projects sebagai guest, akun biasa, dan superuser. Coba pencarian kosong, tambah melalui modal, star/unstar, lalu hapus. Pada Experience, Editor dapat memperbarui data tetapi tidak dapat menambah/menghapus. Form tambah/update lama tetap dapat diakses dan kini memakai API melalui JavaScript, dengan fallback POST Django jika JavaScript tidak aktif.

Commit/push GitHub dan deployment PWS dilakukan terpisah oleh pemilik repositori. Sesudah deploy, periksa login dan operasi tulis di PWS. Submisi SCELE membutuhkan tautan **commit**, bukan hanya tautan repositori.

### Tugas 6

Implementasi mengacu pada [Individual Assignment 6 PBP](https://pbp.cs.ui.ac.id/assignments/individual/tugas-6.html). Bagian tugas individu adalah **Experience**, menggunakan model, UUID, data, dan relasi `starred_by` yang sudah ada. Projects tetap menjadi bagian Tutorial 07.

1. **REST, JSON, PUT, dan PATCH**

   REST adalah gaya arsitektur yang mengatur interaksi client dan server melalui resource dengan antarmuka yang konsisten, antara lain identifikasi resource melalui URI, semantik method HTTP, dan komunikasi stateless. JSON hanya format representasi data; endpoint yang mengembalikan JSON belum otomatis mengikuti prinsip REST. Contohnya, menghapus Experience melalui GET tetap salah meskipun responsnya JSON. Pada proyek ini resource berada di `/api/v1/experiences/` dan `/api/v1/experiences/<uuid>/`, dengan method serta status HTTP sesuai operasinya. Autentikasi menggunakan session Django sesuai panduan; karena masih memakai state sesi di server, implementasi ini tidak diklaim memenuhi seluruh batasan REST secara ketat.

   PUT digunakan untuk mengirim representasi lengkap field yang dapat ditulis: misalnya mengganti judul, deskripsi, kategori, dan thumbnail Experience sekaligus. Field wajib yang hilang menyebabkan 400. PATCH digunakan untuk perubahan sebagian, misalnya hanya `{"title": "Research Assistant"}`; field yang tidak dikirim tetap dipertahankan. Form edit memakai PATCH. Dalam DRF, perlakuan field opsional yang tidak dikirim mengikuti konfigurasi serializer; PUT tidak berarti seluruh field opsional otomatis dikosongkan.

2. **Peran serializer**

   `ExperienceSerializer` mengubah instance model menjadi representasi yang dapat dirender sebagai JSON, memvalidasi input, serta membuat atau memperbarui instance melalui `.save()`. Daftar field eksplisit membatasi data yang keluar. `validate_title` dan `validate_description` menggunakan `strip_tags`, sedangkan field perhitungan seperti `star_count` dan `is_starred` bersifat read-only. Dibandingkan dictionary manual dan `JsonResponse`, validasi, pesan error per field, konversi tipe, serta create/update menjadi terpusat dan lebih mudah diuji. `strip_tags` tetap perlu disertai escaping saat teks dimasukkan ke HTML.

3. **Autentikasi dan otorisasi**

   Autentikasi menjawab siapa pengirim request; `SessionAuthentication` menggunakan sesi login Django untuk mengisi `request.user`. Otorisasi menentukan tindakan yang boleh dilakukan akun tersebut. `IsPortfolioOwnerOrEditorOrReadOnly` mengizinkan pembacaan publik, perubahan PUT/PATCH oleh Editor, dan seluruh operasi pengelolaan oleh superuser. Pengguna biasa hanya dapat membaca dan melakukan star melalui endpoint dengan `IsAuthenticated`. Menyembunyikan tombol hanya membantu antarmuka: pengguna tetap dapat mengirim request langsung. Karena itu, permission wajib diperiksa di server sebelum database diubah.

4. **CSRF dan pengujian autentikasi**

   Browser otomatis menyertakan cookie sesi pada request yang memenuhi aturan cookie. Tanpa pemeriksaan CSRF, situs lain dapat mencoba memicu perubahan dengan sesi korban. Request tulis memakai header `X-CSRFToken`, yang diperiksa terhadap token CSRF sesi/browser. Login saja tidak menggantikan pemeriksaan tersebut. `force_authenticate` memasukkan identitas uji secara langsung dan melewati alur autentikasi sesi, sehingga tidak membuktikan perlindungan CSRF. Tes memakai `APIClient(enforce_csrf_checks=True)` dan `.login()`: POST star serta PATCH Editor tanpa token menghasilkan 403 dan database tetap sama; dengan token dari halaman Experience, operasi berhasil.

#### Implementasi dan verifikasi

| Kebutuhan | Implementasi |
| --- | --- |
| Serializer dengan field eksplisit, validasi, dan star read-only | `main/serializers.py`, `ExperienceSerializer` |
| Izin guest, pengguna biasa, Editor, dan superuser | `main/permissions.py` |
| Function-based API, session, pencarian `?title=...` | `main/api_views.py` |
| List, detail, dan star di `/api/v1/experiences/` | `main/api_urls.py` |
| Daftar, pencarian, tambah, star, hapus tanpa reload | `templates/experience.html` |
| Edit melalui PATCH, error API melalui toast | `templates/components/experience_api_form.html` |
| Uji setiap role, database setelah penolakan, validasi, star, CSRF | `main/tests_api.py`, `ExperienceAPITest` |

Pengalaman tambahan yang sudah tersedia meliputi pembatalan request pencarian lama dengan `AbortController`, loading/empty/error state, konfirmasi hapus, dan tombol yang dinonaktifkan selama request berlangsung untuk mengurangi pengiriman ganda. Penyelesaian Tugas 6 memperkuat tes regresi untuk memastikan penolakan PUT/PATCH tidak mengubah data, identitas pemberi star tidak dapat dipalsukan melalui payload, dan login Editor tetap memerlukan CSRF.

Gunakan virtual environment dan dependency pada bagian setup, lalu jalankan:

```powershell
.\env\Scripts\python.exe manage.py migrate
.\env\Scripts\python.exe manage.py check
.\env\Scripts\python.exe manage.py test main
.\env\Scripts\python.exe manage.py makemigrations --check --dry-run
.\env\Scripts\python.exe manage.py runserver
```

Untuk pemeriksaan browser, buka `/experience/`, `/projects/`, dan `/api/v1/experiences/`. Coba pencarian, tambah, edit, star/unstar, dan hapus menggunakan role yang sesuai. Uji penolakan API melalui request langsung juga diperlukan, bukan hanya melihat tombol. Tes otomatis memakai database pengujian terpisah.

Hasil verifikasi lokal pada sesi 8 November 2026: **67 tes lulus**, `manage.py check` tanpa masalah, dan pemeriksaan migrasi menghasilkan `No changes detected`. Server lokal berhasil menyajikan `/experience/`, `/projects/`, serta Browsable API Experience dan Projects dengan HTTP 200. Pemeriksaan HTTP ini bukan pengujian interaksi browser secara menyeluruh.

#### Deklarasi Penggunaan AI Tugas 6

Format deklarasi mengikuti [deklarasi AI ValuWaste](https://github.com/TK-PBP-C-04-GASAL-2026-2027/valuwaste#deklarasi-penggunaan-ai): tabel kontribusi, ringkasan prompt dan jawaban, serta keterbatasan. Cakupan berikut khusus sesi penyelesaian Tugas 6; deklarasi tugas sebelumnya tetap berlaku.

Proyek dikembangkan dari basis portofolio saya yang sudah tersedia sebelum sesi ini. Pada commit `eaf00d5`, model Experience, serializer, permission, endpoint DRF, integrasi AJAX, dan tes awal sudah ada. Bantuan AI pada sesi ini melanjutkan basis tersebut melalui pemeriksaan kesesuaian panduan, penguatan pengujian, dan penyusunan dokumentasi. Pembedaan ini menunjukkan kontribusi proyek yang sudah tersedia tanpa mengklaim bahwa bantuan AI terbatas pada fitur di luar panduan: review persyaratan, tes wajib, dan refleksi juga dibantu AI.

| Alat AI | Dipakai untuk | Basis dan keputusan pemilik proyek |
| --- | --- | --- |
| Codex (OpenAI) | Memeriksa panduan resmi dan kode lokal, melengkapi tes regresi permission/CSRF/star, menjalankan pemeriksaan otomatis, dan menyusun bagian Tugas 6 README | Melanjutkan portofolio dan bagian Experience yang telah tersedia; meminta penyelesaian sesuai panduan dan format dokumentasi kelompok. Review pribadi serta submisi akhir tetap menjadi tanggung jawab pemilik proyek. |

##### Ringkasan prompt dan respons

**1. Review dan penyelesaian tugas**

**Prompt (ringkasan):** Selesaikan Tugas Individu 6 sesuai situs PBP pada proyek yang ada, termasuk tambahan yang relevan dan README.

**Jawaban/tindakan:** AI membaca panduan dan menemukan implementasi utama telah tersedia. Perubahan difokuskan pada pengujian isi database setelah penolakan, PUT untuk guest/pengguna biasa, login sesi nyata untuk CSRF, PATCH Editor dengan/tanpa token, serta payload star yang mencoba memakai identitas akun lain. AI juga menambahkan jawaban reflektif dan pemetaan persyaratan ke berkas implementasi.

**2. Format deklarasi**

**Prompt (ringkasan):** Ikuti format deklarasi AI repo ValuWaste dan jelaskan kontribusi dasar pemilik proyek.

**Jawaban/tindakan:** AI membaca README ValuWaste dan memakai struktur tabel, prompt/respons, serta keterbatasan. Basis kode sebelum sesi dibedakan dari perubahan dalam sesi ini. Tidak dibuat klaim bahwa pemilik telah melakukan review manual atau pengujian browser yang belum dikonfirmasi.

##### Keterbatasan yang ditemukan

1. Pembaca web AI sempat menerima 403 dari situs PBP; panduan kemudian diperoleh melalui request HTTP dari terminal. Requirement diperiksa dari halaman tugas, bukan ditebak dari nomor tutorial.
2. Keberadaan kode sebelum sesi tidak membuktikan seluruh riwayat penulisannya. Deklarasi ini membatasi klaim pada kondisi repository dan pekerjaan sesi yang dapat diperiksa.
3. Status HTTP saja belum membuktikan database aman. Tes diperkuat dengan pembacaan ulang objek dan jumlah record setelah request ditolak.
4. Tes API tidak membuktikan seluruh interaksi visual berjalan di semua browser. Pemeriksaan antarmuka dan hasil deployment perlu dibedakan dari hasil tes otomatis; tidak ada klaim deployment atau pengumpulan SCELE dalam sesi ini.
