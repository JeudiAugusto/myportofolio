# Jeudi Augusto Asadullah — Personal Portfolio

Personal portfolio website yang dikembangkan sebagai bagian dari
pembelajaran Pemrograman Berbasis Platform (PBP) Gasal 2026/2027.

Website ini menampilkan profil, keterampilan, project, dan informasi
kontak dalam sebuah halaman portfolio yang responsif.

---

## Identity

- **Nama:** Jeudi Augusto Asadullah
- **NPM:** 2506656822
- **Kelas:** PBP B
- **Program:** S1 Sistem Informasi
- **Universitas:** Universitas Indonesia

---

## About The Project

Project ini merupakan personal portfolio website yang dibangun
menggunakan Django dan dikembangkan secara bertahap mengikuti
materi PBP.

Selain memenuhi kebutuhan dasar Tutorial 01, website ini juga
dikembangkan dengan beberapa peningkatan UI/UX agar memiliki
identitas visual dan interaksi yang lebih baik.

---

## Features

### Core Features

- Personal profile section
- About Me section
- Skills section
- Projects section
- Contact section
- Social media links
- Responsive layout
- Semantic HTML5 structure

### UI/UX Enhancements

- Sticky navigation
- Smooth scrolling
- Hover interaction pada navigation
- Interactive skill cards
- Skill proficiency indicators
- Project technology tags
- Project case-study preview
- Animated profile image
- "Currently Learning" status indicator
- Responsive desktop/tablet/mobile layout
- Keyboard focus states
- Reduced-motion support

---

## Projects

### 1. Personal Portfolio

Personal portfolio website yang dibangun menggunakan:

- Python
- Django
- HTML5
- CSS3

Repository:

https://github.com/JeudiAugusto/myportofolio

---

### 2. Cashie

Cashie adalah aplikasi web pengelola keuangan yang dikembangkan
sebagai project Pemrograman Web secara kolaboratif.

Project ini memiliki fitur seperti:

- Login
- Register
- Dashboard
- Pengelolaan data keuangan
- CRUD
- AJAX
- Database

Teknologi yang digunakan antara lain:

- PHP
- JavaScript
- SQL
- PHPMyAdmin

Repository:

https://github.com/fzdhl/cashie

---

## Tech Stack

### Backend

- Python
- Django

### Frontend

- HTML5
- CSS3

### Development Tools

- Git
- GitHub
- Visual Studio Code

---

## Project Structure

```text
myportofolio/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── portofolio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── img/
        └── profile.jpg

## Reflection

### Tugas 1

1. Pada Tutorial dan Tugas 1, saya menggunakan elemen semantik HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, dan `<footer>`. Elemen-elemen tersebut membantu saya membagi halaman berdasarkan fungsi dan struktur konten, bukan hanya berdasarkan tampilan visual. Misalnya, `<section>` saya gunakan untuk memisahkan About, Skills, Projects, dan Contact, sedangkan `<article>` digunakan untuk item yang berdiri sendiri seperti skill dan project. Penggunaan elemen semantik membuat struktur HTML lebih mudah dipahami, lebih terorganisir, dan lebih sesuai dengan tujuan masing-masing bagian halaman.

2. Tantangan utama saat membuat responsive CSS adalah mempertahankan hierarchy dan keterbacaan layout ketika ukuran layar berubah. Pada desktop, hero saya menggunakan CSS Grid dengan foto di sebelah kanan dan informasi utama di sebelah kiri. Pada layar yang lebih kecil, susunan tersebut harus diubah menjadi satu kolom agar teks tidak terlalu sempit dan gambar tidak keluar dari layar. Saya mengevaluasinya dengan menguji halaman pada ukuran desktop dan mobile, kemudian menggunakan breakpoint untuk mengubah jumlah kolom, ukuran typography, jarak antar elemen, serta susunan navigation. Dari proses tersebut saya belajar bahwa responsive design bukan sekadar mengecilkan ukuran elemen, tetapi menentukan kembali prioritas dan hubungan antar elemen pada layar yang berbeda.

3. Karena website ini masih merupakan static web murni, informasi di dalamnya harus ditulis langsung pada template sehingga perubahan konten masih membutuhkan perubahan source code. Keterbatasan lain adalah project dan skill belum dapat dikelola secara dinamis berdasarkan data pengguna atau database. Pada iterasi berikutnya, fungsionalitas yang paling ingin saya tambahkan adalah integrasi backend Django dengan database sehingga data seperti project, skill, dan informasi portfolio dapat dikelola melalui model dan halaman admin tanpa harus mengubah HTML secara manual.