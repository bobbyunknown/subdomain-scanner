#!/usr/bin/env python3

# Script dari BobbyUnknown
# Gunakan dengan bijak dan bertanggung jawab
#
# Script ini digunakan untuk memeriksa status HTTP dari subdomain yang ditemukan
# Pastikan Anda memiliki izin untuk memindai domain target
# Penggunaan skrip ini mungkin dibatasi oleh kebijakan penggunaan yang adil dari layanan yang digunakan
# 
# Harap diingat bahwa penggunaan alat pemindaian tanpa izin dapat melanggar hukum
# Gunakan hanya untuk tujuan yang sah dan etis
# Penulis tidak bertanggung jawab atas penyalahgunaan script ini

import sys
import yaml
import requests
from termcolor import colored
import os

def read_config(filename):
    print(f"Membaca file: {filename}")
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)
    print(f"Isi file: {data}")
    return data

def get_status_code(url):
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        return response.status_code
    except requests.RequestException as e:
        print(f"Error saat mengakses {url}: {e}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Penggunaan: ./check_status.py <yaml_file>")
        sys.exit(1)

    yaml_file = sys.argv[1]
    domain = os.path.splitext(os.path.basename(yaml_file))[0].replace('_result', '')
    config = read_config(yaml_file)

    if 'sites' not in config:
        print("Error: File YAML tidak memiliki kunci 'sites'")
        sys.exit(1)

    ok_count = 0
    total_count = len(config['sites'])
    ok_domains = []

    print(colored("Memeriksa status 200 OK...", "yellow"))
    for site in config['sites']:
        print(f"Memeriksa: {site}")
        code = get_status_code(site)
        if code == 200:
            ok_count += 1
            ok_domains.append(site)
            print(colored(f"{site} memiliki status 200 OK", "green"))
        else:
            print(colored(f"{site} memiliki status {code}", "red"))

    print(colored(f"\nHasil:", "cyan"))
    print(colored(f"{ok_count} dari {total_count} situs memiliki status 200 OK", "cyan"))

    output_file = f'{domain}_status_200_ok.txt'
    with open(output_file, 'w') as f:
        f.write(f"{ok_count} dari {total_count} situs memiliki status 200 OK\n")
        f.write(f"Persentase: {(ok_count/total_count)*100:.2f}%\n\n")
        f.write("Daftar domain dengan status 200 OK:\n")
        for domain in ok_domains:
            clean_domain = domain.replace("https://", "")
            f.write(f"{clean_domain}\n")

    print(colored(f"\nDomain dengan status 200 OK:", "cyan"))
    for domain in ok_domains:
        clean_domain = domain.replace("https://", "")
        print(colored(f"- {clean_domain}", "cyan"))

    print(colored(f"\nHasil telah disimpan ke {output_file}", "green"))

if __name__ == "__main__":
    main()