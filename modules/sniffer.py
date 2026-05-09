#!/usr/bin/env python3
from colorama import Fore, Style
import sys

def start_sniffer():
    print(f"{Fore.CYAN}[+] Iniciando Sniffer Educativo...{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[!] Este sniffer SOLO captura headers, NO payload sensible.{Style.RESET_ALL}")
    
    try:
        from scapy.all import sniff, IP, TCP, UDP, ICMP
        
        def packet_callback(packet):
            if IP in packet:
                src = packet[IP].src
                dst = packet[IP].dst
                proto = "TCP" if TCP in packet else "UDP" if UDP in packet else "ICMP" if ICMP in packet else "IP"
                
                print(f"{Fore.GREEN}[{proto}]{Style.RESET_ALL} {src} → {dst}")
                
                # Ético: No mostrar payloads
                if TCP in packet and packet[TCP].payload:
                    print(f"{Fore.RED}    [Payload suprimido por privacidad]{Style.RESET_ALL}")
        
        print(f"{Fore.CYAN}[✓] Capturando 50 paquetes... (Ctrl+C para detener){Style.RESET_ALL}")
        sniff(prn=packet_callback, count=50, store=False)
        
    except ImportError:
        print(f"{Fore.RED}[✗] Scapy no instalado. Ejecuta: pip install scapy{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}[✗] Permisos insuficientes. Ejecuta con sudo/root.{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Sniffer detenido.{Style.RESET_ALL}")
    
    input("\nPresiona Enter para continuar...")
