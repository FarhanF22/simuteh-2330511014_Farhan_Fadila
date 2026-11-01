# SIMUTEH — Studi Praproses Citra Daun Teh

## Identitas

- Nama: Farhan Fadila
- NIM: 2330511014
- Seed dataset: 1014
- Proyek: SIMUTEH

## Tentang proyek

Proyek ini mengeksplorasi praproses citra daun teh menggunakan Python, OpenCV, dan Jupyter Notebook. Rangkaian notebook B1–B5 membahas lingkungan dan alur kerja, kanal warna, histogram dan perbaikan pencahayaan, penapisan spasial, serta evaluasi rangkaian praproses.

Dataset yang disertakan adalah dataset **sintetis**. Dataset berisi 60 citra (20 citra untuk masing-masing kelas `sehat`, `ringan`, dan `berat`), dengan variasi kondisi cahaya dan derau. Dataset ini dibuat untuk eksperimen notebook, bukan kumpulan foto lapangan.

## Struktur proyek

```text
data/sintetis/
  citra/       Citra dengan variasi pencahayaan dan derau
  bersih/      Citra acuan sebelum gangguan pencahayaan dan derau
  mask_daun/   Mask area daun
  mask_bercak/ Mask area bercak
  label.csv    Label kelas, kondisi cahaya, dan persentase bercak
hasil/         Tabel CSV, konfigurasi JSON, grafik, dan citra hasil
notebook/      Eksperimen B1 sampai B5
src/           Fungsi praproses, utilitas, dan pembangkit dataset
Laporan/       Laporan PDF dan presentasi
requirements.txt
```

## Persiapan

Jalankan perintah berikut dari folder utama proyek untuk memasang dependensi ke instalasi Python yang sedang digunakan:

```bash
python -m pip install -r requirements.txt
```

Dependensi yang tercantum meliputi OpenCV, NumPy, scikit-image, Matplotlib, pandas, dan ipykernel.

## Menjalankan eksperimen

1. Buka folder utama proyek di VS Code atau JupyterLab.
2. Pilih kernel Jupyter yang menggunakan instalasi Python tempat dependensi di atas dipasang.
3. Jalankan notebook di `notebook/` secara berurutan: `B1_lingkungan.ipynb`, `B2_citra_warna.ipynb`, `B3_histogram.ipynb`, `B4_penapisan.ipynb`, lalu `B5_praproses.ipynb`.
4. Notebook menggunakan path relatif seperti `../data/sintetis/` dan `../hasil/`; jalankan notebook dengan folder kerja `notebook/` agar path tersebut ditemukan.
5. Hasil tabel dan visualisasi disimpan di `hasil/`.

Dataset sintetis yang digunakan sudah disertakan. Jika ingin membuat ulang dataset dari folder utama proyek, jalankan:

```bash
python src/buat_dataset_sintetis.py
```

Skrip ini memakai seed 1014 (empat digit terakhir NIM pada konfigurasi saat ini) dan menulis dataset ke `data/sintetis/`.

## Fungsi praproses

`src/praproses.py` menyediakan `praproses(img_bgr, p=None)`. Urutan operasinya adalah:

1. Ubah ukuran citra dengan lebar target.
2. Koreksi gamma.
3. Terapkan CLAHE pada kanal kecerahan V di ruang warna HSV, jika diaktifkan.
4. Redam derau dengan penapis rerata, Gaussian, median, atau tanpa penapisan.
5. Pertajam dengan unsharp masking, jika diaktifkan.

Parameter bawaan saat ini tersedia di `PARAM_BAWAAN` pada modul tersebut. Konfigurasi hasil eksperimen yang disimpan pada `hasil/param_praproses.json` memakai lebar 640 piksel, gamma 1.0, CLAHE nonaktif, median kernel 3, dan penajaman nonaktif. Notebook dapat menguji konfigurasi lain; JSON itu mencatat parameter pipeline, bukan rangkuman seluruh eksperimen.

`src/utils_cv.py` berisi fungsi bantu untuk membaca dan menampilkan citra serta menghitung statistik dan kontras bercak.

## Artefak

Folder `hasil/` berisi keluaran eksperimen B1–B5 dalam format CSV, JSON, dan PNG, termasuk tabel evaluasi, grafik, panel perbandingan, dan diagram pipeline. Dokumen laporan dan presentasi tersedia di `Laporan/`.

## Repositori

[GitHub — simuteh-2330511014_Farhan_Fadila](https://github.com/FarhanF22/simuteh-2330511014_Farhan_Fadila)
