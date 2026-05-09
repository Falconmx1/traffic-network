#!/usr/bin/env python3
from colorama import Fore, Style
import socket
import time
import threading

def traffic_generator():
    print(f"{Fore.CYAN}[+] Generador de Tráfico Controlado{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[!] Solo para pruebas en localhost (127.0.0.1){Style.RESET_ALL}")
    
    print(f"\n{Fore.GREEN}Selecciona tipo de tráfico:{Style.RESET_ALL}")
    print("  [1] TCP Flood (controlado)")
    print("  [2] UDP Flood (controlado)")
    print("  [3] ICMP Ping Flood")
    print("  [4] HTTP Request Test")
    
    opt = input(f"{Fore.CYAN}➤ Opción: {Style.RESET_ALL}")
    
    if opt == '1':
        target = input("IP objetivo (localhost: 127.0.0.1): ")
        port = int(input("Puerto: "))
        packets = int(input("Número de paquetes: "))
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for i in range(packets):
            try:
                sock.connect((target, port))
                sock.send(b"TRAFFIC-TEST-PACKET")
                sock.close()
                print(f"{Fore.GREEN}[✓] Packet {i+1}/{packets} enviado{Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}[✗] Error en packet {i+1}{Style.RESET_ALL}")
            time.sleep(0.01)
    
    elif opt == '2':
        target = input("IP objetivo (localhost): ")
        port = int(input("Puerto: "))
        packets = int(input("Número de paquetes: "))
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for i in range(packets):
            sock.sendto(b"UDP-TEST", (target, port))
            print(f"{Fore.GREEN}[✓] UDP Packet {i+1}/{packets}{Style.RESET_ALL}")
            time.sleep(0.01)
    
    elif opt == '3':
        packets = int(input("Número de pings: "))
        import subprocess
        for i in range(packets):
            subprocess.run(["ping", "-c", "1", "127.0.0.1"], capture_output=True)
            print(f"{Fore.GREEN}[✓] Ping {i+1}/{packets}{Style.RESET_ALL}")
            time.sleep(0.1)
    
    elif opt == '4':
        import requests
        url = input("URL (ej: http://localhost:8000): ")
        requests_count = int(input("Número de requests: "))
        for i in range(requests_count):
            try:
                r = requests.get(url)
                print(f"{Fore.GREEN}[✓] Request {i+1} - Status: {r.status_code}{Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}[✗] Error en request {i+1}{Style.RESET_ALL}")
    
    input("\nPresiona Enter para continuar...")
