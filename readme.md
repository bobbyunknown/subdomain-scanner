# Subdomain Scanner dan Cloudflare Detector

Proyek ini terdiri dari skrip Python untuk memindai subdomain dari sebuah domain, mendeteksi penggunaan Cloudflare, dan memeriksa status subdomain.

## Fitur

- Memindai subdomain menggunakan Sublist3r
- Mendeteksi penggunaan Cloudflare pada subdomain yang ditemukan
- Menyimpan hasil pemindaian dalam format YAML
- Menyimpan daftar subdomain yang menggunakan Cloudflare dalam file teks terpisah
- Memeriksa status HTTP dari subdomain yang ditemukan

## Instalasi

### Instalasi Python3 dan pip

Jika Anda belum memiliki Python3 dan pip, Anda dapat menginstalnya dengan perintah berikut:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Instalasi Dependensi

Proyek ini membutuhkan beberapa library Python tambahan. Anda dapat menginstalnya dengan perintah berikut:

```bash
pip3 install sublist3r requests termcolor PyYAML
```

Atau, Anda dapat menggunakan file `requirements.txt`:

```bash
pip3 install -r requirements.txt
```

## Penggunaan

1. Clone repositori ini:
   ```bash
   git clone https://github.com/bobbyun/subdomain-scanner.git
   cd subdomain-scanner
   ```

2. Jalankan skrip pemindaian subdomain dengan menentukan domain target:
   ```bash
   python3 scan_sub.py example.com
   ```
   Ganti `example.com` dengan domain yang ingin Anda pindai.

3. Hasil pemindaian akan disimpan dalam file YAML (`example.com_result.yaml`) dan daftar subdomain yang menggunakan Cloudflare akan disimpan dalam file teks terpisah (`example.com_cloudflare.txt`).

4. Untuk memeriksa status HTTP dari subdomain yang ditemukan, gunakan skrip `check_status.py`:
   ```bash
   python3 check_status.py example.com_result.yaml
   ```
   Ganti `example.com_result.yaml` dengan nama file hasil pemindaian yang dihasilkan oleh `scan_sub.py`.

5. Hasil pemeriksaan status akan disimpan dalam file `example.com_status_200_ok.txt`.

## Catatan

- Pastikan Anda memiliki izin untuk memindai domain target.
- Penggunaan skrip ini mungkin dibatasi oleh kebijakan penggunaan yang adil dari layanan yang digunakan.
- Gunakan dengan bijak dan bertanggung jawab.

## Lisensi

[MIT License](LICENSE)

## Kontribusi

Kontribusi selalu diterima. Silakan buka issue atau pull request jika Anda ingin berkontribusi pada proyek ini.

<hr>

<details>
<summary>Informasi Tambahan</summary>

### Penjelasan Skrip

- `scan_sub.py`: Memindai subdomain menggunakan Sublist3r, memeriksa penggunaan Cloudflare, dan menyimpan hasil dalam format YAML dan teks.
- `check_status.py`: Membaca file YAML hasil pemindaian dan memeriksa status HTTP dari setiap subdomain.

Untuk informasi lebih lanjut tentang cara kerja skrip, silakan lihat komentar dalam kode sumber.

</details>


