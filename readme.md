### Requirement :
- Python >= 3
- Numpy
- Opencv >= 3
<br><br>

### How to install?
1. Pastikan sudah menginstall `python` pada komputer masing - masing.

2. Python dapat diperiksa dengan menjalankan perintah `python` pada command prompt (cmd).

3. Jika tidak terdapat error, maka python interpreter sudah terinstal.

4. Jika python belum terinstal, maka ikuti langkah no 5. Jika sudah, maka dapat skip ke langkah no 7.

5. Bagi komputer yang belum terinstal python, download python pada laman resminya `https://www.python.org/downloads/` atau dapat menggunakan anaconda.

6. Setelah terinstal, setup python pada environment variable dengan langkah berikut: 
    -  Ketik `python.exe` pada start menu dan pilih `open file location`
    <br>
    <img src="imgs/1.png">
    <br><br>

    - Maka anda akan diarahkan ke folder tempat python terinstal.
    <br>
    <img src="imgs/2.png">
    <br><br>

    - Setelah itu kembali ke start menu dan ketik environment variable dan pilih Edit System Environment seperti pada gambar berikut:
    <br>
    <img src="imgs/3.png">
    <br><br>

    - Kemudian akan muncul popup seperti berikut. Click kotak berwarna merah.
    <br>
    <img src="imgs/4.png">
    <br><br>

    - Selanjutkan akan muncul popup lagi seperti berikut. Pilih `Path` dan click `Edit`.
    <br>
    <img src="imgs/5.png">
    <br><br>

    - Jika muncul popup yang berisi daftar path environment variable yang ada pada komputer, maka abaikan dulu. Kita kembali ke folder pada tempat python terinstal.

    - Copy path folder tersebut.
    <br>
    <img src="imgs/6.png">
    <br><br>

    - Kembali pada popup daftar path environment variable. Klik `new` dan paste path folder python pada baris paling bawah.
    <br>
    <img src="imgs/7.png">
    <br><br>

    - Kembali ke folder python terinstal. Cari folder dengan nama `Scripts` kemudian copy path folder tersebut dan paste ke popup daftar path environment variable (lakukan seperti langkah sebelumnya).
    <br>
    <img src="imgs/8.png">
    <br><br>

7. Jika langkah sebelumnya sudah dilakukan dan tidak terdapat error, maka `python` sudah berhasil terinstal pada komputer anda. Anda dapat memastikannya dengan membuka command prompt kemudian ketik `python`. Seharusnya akan tampil seperti berikut:
<br>
<img src="imgs/9.png">
<br><br>

8. Copy citra yang akan dideteksi ke folder `datatest` dan model yang sudah dilatih ke folder `models`.
<br>
<img src="imgs/10.png">
<br><br>

9. Buka cmd dan arahkan ke folder project ini. Anda dapat langsung membuka cmd pada folder root dengan cara klik address bar, ketik cmd, dan tekan enter.
<br>
<img src="imgs/11.png">
<br><br>

10. Setelah cmd terbuka pada folder project, install semua package (library) yang dibutuhkan dengan cara ketik `pip install -r requirements.txt`. Maka python akan menginstall semua library yang dibutuhkan.
<br>
<img src="imgs/12.png">
<br><br>

11. Jika semua library sudah terinstal dan tidak terdapat error, anda dapat menjalankan program dengan perintah `python nama_program.py` atau `python image.py`. Pastikan anda telah membukan program dan mengganti nama citra serta model yang akan digunakan.

12. Program akan menampilkan hasil deteksi sebagai berikut.
<br>
<img src="imgs/13.png">