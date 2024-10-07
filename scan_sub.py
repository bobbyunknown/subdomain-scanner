#!/usr/bin/env python3

# Script dari BobbyUnknown
# Gunakan dengan bijak dan bertanggung jawab
#
# Script ini digunakan untuk memindai subdomain dari sebuah domain
# Pastikan Anda memiliki izin untuk memindai domain target
# Penggunaan skrip ini mungkin dibatasi oleh kebijakan penggunaan yang adil dari layanan yang digunakan
# 
# Harap diingat bahwa penggunaan alat pemindaian tanpa izin dapat melanggar hukum
# Gunakan hanya untuk tujuan yang sah dan etis
# Penulis tidak bertanggung jawab atas penyalahgunaan script ini

import sys
import sublist3r
import requests
from termcolor import colored
import yaml
import signal
import socket

def scan_subdomains(domain):
    try:
        subdomains = sublist3r.main(domain, 40, savefile=None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)
        return subdomains or []
    except Exception as e:
        print(colored(f"Kesalahan saat memindai subdomain: {str(e)}", "red"))
        return []

def save_to_yaml(subdomains, filename):
    data = {'sites': [f'https://{subdomain}' for subdomain in subdomains]}
    with open(filename, 'w') as f:
        yaml.dump(data, f)

def check_cloudflare(subdomain):
    try:
        ip = socket.gethostbyname(subdomain)
        response = requests.get(f'https://{subdomain}', timeout=5, allow_redirects=False)
        server = response.headers.get('Server', '').lower()
        cf_ray = 'cf-ray' in response.headers
        is_cloudflare = 'cloudflare' in server or cf_ray
        return is_cloudflare, ip
    except:
        return False, None

def save_cloudflare_domains(domains, ips, filename, target_domain):
    with open(filename, 'w') as f:
        f.write(f"Hasil scan {target_domain} menggunakan Cloudflare\n\n")
        for domain, ip in zip(domains, ips):
            f.write(f"{domain} {ip}\n")

def signal_handler(sig, frame):
    print(colored("\nPemindaian dihentikan oleh pengguna.", "yellow"))
    if cloudflare_domains:
        cf_output_file = f"{domain}_cloudflare.txt"
        save_cloudflare_domains(cloudflare_domains, cloudflare_ips, cf_output_file, domain)
        print(colored(f"Domain yang menggunakan Cloudflare telah disimpan ke {cf_output_file}", "green"))
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    
    if len(sys.argv) != 2:
        print("Penggunaan: ./scan_sub.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    output_file = f"{domain}_result.yaml"

    print(colored(f"Memulai pemindaian untuk domain: {domain}", "yellow"))
    
    subdomains = scan_subdomains(domain)

    if not subdomains:
        print(colored("Tidak ada subdomain yang ditemukan atau terjadi kesalahan saat memindai.", "red"))
        sys.exit(1)

    save_to_yaml(subdomains, output_file)
    print(colored(f"Subdomain telah disimpan ke {output_file}", "green"))

    cloudflare_count = 0
    cloudflare_domains = []
    cloudflare_ips = []

    print(colored("Memeriksa status Cloudflare...", "yellow"))
    for subdomain in subdomains:
        is_cloudflare, ip = check_cloudflare(subdomain)
        status = "Menggunakan Cloudflare" if is_cloudflare else "Tidak menggunakan Cloudflare"
        color = "green" if is_cloudflare else "red"
        print(colored(f"{subdomain} {ip} {status}", color))
        if is_cloudflare:
            cloudflare_count += 1
            cloudflare_domains.append(subdomain)
            cloudflare_ips.append(ip)

    print(colored(f"\nHasil:", "cyan"))
    print(colored(f"{cloudflare_count} subdomain menggunakan Cloudflare", "cyan"))
    
    if cloudflare_domains:
        cf_output_file = f"{domain}_cloudflare.txt"
        save_cloudflare_domains(cloudflare_domains, cloudflare_ips, cf_output_file, domain)
        print(colored(f"\nDomain yang menggunakan Cloudflare telah disimpan ke {cf_output_file}", "green"))
        for domain, ip in zip(cloudflare_domains, cloudflare_ips):
            print(colored(f"- {domain} {ip}", "cyan"))
