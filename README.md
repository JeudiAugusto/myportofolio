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
