#!/usr/bin/env python3
from colorama import Fore, Style
import psutil
import socket

def network_analyzer():
    print(f"{Fore.CYAN}[+] Analizador de Red{Style.RESET_ALL}")
    
    # Estadísticas de red
    stats = psutil.net_io_counters()
    print(f"\n{Fore.GREEN}📊 Estadísticas de red:{Style.RESET_ALL}")
    print(f"  📥 Bytes recibidos: {stats.bytes_recv / 1_000_000:.2f} MB")
    print(f"  📤 Bytes enviados: {stats.bytes_sent / 1_000_000:.2f} MB")
    print(f"  📦 Paquetes recibidos: {stats.packets_recv}")
    print(f"  📦 Paquetes enviados: {stats.packets_sent}")
    
    # Conexiones activas
    print(f"\n{Fore.GREEN}🔌 Conexiones activas:{Style.RESET_ALL}")
    connections = psutil.net_connections(kind='inet')
    for conn in connections[:10]:  # Mostrar solo 10
        if conn.raddr:
            print(f"  {conn.laddr.ip}:{conn.laddr.port} → {conn.raddr.ip}:{conn.raddr.port} [{conn.status}]")
    
    # Interfaces de red
    print(f"\n{Fore.GREEN}🌐 Interfaces de red:{Style.RESET_ALL}")
    for iface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                print(f"  {iface}: {addr.address}")
    
    input("\nPresiona Enter para continuar...")
