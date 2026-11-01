# SIMUTEH — Studi Praproses Citra Daun Teh

## 1. Identitas Proyek

- **Nama:** Farhan Fadila
- **NIM:** 2330511014
- **Proyek:** SIMUTEH
- **SEED Dataset:** 1014
- **Topik:** Praproses Citra Daun Teh

## 2. Deskripsi Proyek

SIMUTEH merupakan proyek studi praproses citra daun teh menggunakan Python dan OpenCV. Proyek ini berfokus pada pengolahan citra untuk membantu memperbaiki kualitas visual daun teh sebelum dilakukan analisis lebih lanjut.

Tahapan yang dipelajari meliputi pengenalan lingkungan pengembangan, pengolahan kanal warna, analisis histogram, perbaikan pencahayaan, penapisan derau, serta penerapan rangkaian praproses citra.

Eksperimen disusun dalam lima notebook, yaitu B1 sampai B5. Setiap notebook membahas tahapan pengujian dan evaluasi yang berbeda.

**Catatan:** Dataset yang digunakan merupakan dataset sintetis yang dibuat secara terprogram, bukan kumpulan foto hasil pemotretan langsung di perkebunan.

## 3. Dataset

Dataset sintetis dibuat menggunakan SEED 1014 dan terdiri dari 60 citra dengan pembagian:

| Kelas | Jumlah Citra |
|---|---:|
| Sehat | 20 |
| Ringan | 20 |
| Berat | 20 |
| **Total** | **60** |

Dataset memiliki variasi kondisi pencahayaan dan derau untuk mendukung eksperimen pengolahan citra.

Struktur dataset:

```text
data/
└── sintetis/
    ├── citra/
    ├── bersih/
    ├── mask_daun/
    ├── mask_bercak/
    └── label.csv
```

Keterangan:
- `citra/`: citra dengan variasi pencahayaan dan derau.
- `bersih/`: citra acuan sebelum pemberian gangguan.
- `mask_daun/`: mask area daun.
- `mask_bercak/`: mask area bercak.
- `label.csv`: informasi nama file, kelas, kondisi pencahayaan, dan persentase bercak.

## 4. Struktur Folder Proyek

```text
simuteh-2330511014_Farhan_Fadila/
│
├── data/
│   └── sintetis/
│       ├── citra/
│       ├── bersih/
│       ├── mask_daun/
│       ├── mask_bercak/
│       └── label.csv
│
├── hasil/
│   ├── *.csv
│   ├── *.json
│   └── *.png
│
├── notebook/
│   ├── B1_lingkungan.ipynb
│   ├── B2_citra_warna.ipynb
│   ├── B3_histogram.ipynb
│   ├── B4_penapisan.ipynb
│   └── B5_praproses.ipynb
│
├── src/
│   ├── buat_dataset_sintetis.py
│   ├── praproses.py
│   └── utils_cv.py
│
├── Laporan/
│   ├── Laporan_EvalP1-2330511014_Farhan_Fadila.pdf
│   └── Slide_EvalP1-4_2330511014_Farhan_Fadila.pptx
│
├── requirements.txt
├── README.md

```

Folder `hasil/` menyimpan keluaran eksperimen berupa tabel, grafik, konfigurasi parameter, dan visualisasi hasil pengolahan citra.

## 5. Lingkungan Pengembangan

Proyek dikembangkan menggunakan Python dan pustaka pengolahan citra serta analisis data.

Versi perangkat lunak yang tercatat pada lingkungan Python yang diperiksa:

| Perangkat Lunak | Versi |
|---|---|
| Python | 3.11.9 |
| OpenCV | 4.10.0.84 |
| NumPy | 2.4.6 |
| scikit-image | 0.24.0 |
| Matplotlib | 3.11.2 |
| Pandas | 2.2.3 |
| Pillow | 13.0.0 |
| ipykernel | 7.4.0 |

Daftar dependensi utama tersedia pada file `requirements.txt`.

## 6. Instalasi dan Persiapan

Pastikan Python sudah terpasang pada komputer.

Buka terminal atau PowerShell pada folder utama proyek, kemudian jalankan:

```powershell
py --version
```

Pasang seluruh dependensi yang tercantum pada `requirements.txt` dengan perintah:

```powershell
py -m pip install -r requirements.txt
```

Setelah instalasi selesai, buka proyek menggunakan Visual Studio Code atau JupyterLab dan pilih kernel Python yang sesuai dengan lingkungan tempat dependensi dipasang.

## 7. Menjalankan Eksperimen

Notebook dikerjakan secara berurutan sebagai berikut:

| Notebook | Pembahasan |
|---|---|
| B1 | Lingkungan pengembangan dan alur kerja |
| B2 | Pengolahan citra warna |
| B3 | Histogram dan perbaikan pencahayaan |
| B4 | Penapisan dan pengurangan derau |
| B5 | Rangkaian praproses dan evaluasi |

Langkah menjalankan:

1. Buka folder utama proyek.
2. Buka folder `notebook/`.
3. Jalankan notebook B1 sampai B5 secara berurutan.
4. Pastikan kernel menggunakan Python yang telah dipasangi dependensi.
5. Perhatikan hasil pengujian yang tersimpan pada folder `hasil/`.

Gunakan direktori kerja yang sesuai dengan path relatif pada masing-masing notebook agar file dataset dan keluaran dapat ditemukan.

## 8. Pembuatan Dataset Sintetis

Dataset yang digunakan dalam eksperimen telah disertakan pada folder `data/sintetis/`.

Jika ingin membangkitkan ulang dataset, jalankan skrip berikut dari folder utama proyek:

```powershell
py src/buat_dataset_sintetis.py
```

Skrip menggunakan SEED 1014 dan menghasilkan 60 citra yang dibagi ke dalam tiga kelas, yaitu sehat, ringan, dan berat.

**Perhatian:** menjalankan ulang skrip akan menghasilkan ulang isi dataset sintetis. Jika ingin mempertahankan dataset yang sudah digunakan dalam eksperimen, jangan menjalankan skrip tersebut tanpa membuat salinan cadangan terlebih dahulu.

## 9. Modul Praproses

Modul utama praproses terdapat pada:

```text
src/praproses.py
```

Fungsi utama yang tersedia adalah:

```python
praproses(img_bgr, p=None)
```

Rangkaian operasi praproses meliputi:

1. Pengubahan ukuran citra dengan lebar target.
2. Koreksi gamma.
3. Peningkatan kontras menggunakan CLAHE pada kanal kecerahan V dalam ruang warna HSV apabila diaktifkan.
4. Pengurangan derau menggunakan penapis rerata, Gaussian, median, atau tanpa penapisan.
5. Penajaman citra menggunakan unsharp masking apabila diaktifkan.

Parameter bawaan disimpan pada variabel `PARAM_BAWAAN`.

Konfigurasi parameter pipeline yang digunakan pada file `hasil/param_praproses.json` mencatat:
- Lebar citra: 640 piksel.
- Gamma: 1.0.
- CLAHE: nonaktif.
- Penapis: median.
- Kernel: 3.
- Sigma: 1.0.
- Penajaman: nonaktif.

Modul pendukung lainnya adalah `src/utils_cv.py`, yang berisi fungsi bantu untuk pengolahan dan evaluasi citra.

## 10. Hasil dan Dokumentasi

Hasil eksperimen disimpan pada folder `hasil/` dalam beberapa format, antara lain:

- CSV untuk tabel hasil pengujian dan evaluasi.
- PNG untuk grafik, diagram pipeline, dan visualisasi citra.
- JSON untuk penyimpanan konfigurasi parameter praproses.

Dokumentasi lengkap mengenai metode, proses pengujian, hasil, dan pembahasan tersedia dalam folder `Laporan/`.

## 11. Repositori GitHub

Repositori proyek:

[SIMUTEH — GitHub](https://github.com/FarhanF22/simuteh-2330511014_Farhan_Fadila)

Versi proyek yang diberi tag:

```text
v0.1-praproses
```

Tag tersebut menandai versi proyek praproses yang telah disimpan pada repository Git.

## 12. Penutup

Proyek SIMUTEH merupakan studi pengolahan dan praproses citra daun teh menggunakan dataset sintetis. Melalui lima tahapan notebook, proyek ini mengevaluasi pengaruh pengolahan warna, histogram, pencahayaan, dan penapisan terhadap kualitas citra.

Seluruh hasil eksperimen, kode program, konfigurasi, serta dokumentasi disertakan dalam repository proyek agar proses pengujian dapat ditelusuri dan dijalankan kembali.
