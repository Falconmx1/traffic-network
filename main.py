#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from colorama import init, Fore, Style
import platform

init(autoreset=True)

BANNER = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════╗
{Fore.RED}║{Fore.YELLOW}          🔥 TRAFFIC-NETWORK v1.0 - Ethical Tool 🔥          {Fore.RED}║
{Fore.RED}║{Fore.CYAN}     Monitoreo | Test de Banda | Generador | Sniffer      {Fore.RED}║
{Fore.RED}╠══════════════════════════════════════════════════════════════╣
{Fore.RED}║{Fore.WHITE}  [1] 📡 Monitoreo de tráfico (Sniffer educativo)        {Fore.RED}║
{Fore.RED}║{Fore.WHITE}  [2] ⚡ Test de ancho de banda                          {Fore.RED}║
{Fore.RED}║{Fore.WHITE}  [3] 🎮 Generador de tráfico controlado                 {Fore.RED}║
{Fore.RED}║{Fore.WHITE}  [4] 📊 Analizador de red                               {Fore.RED}║
{Fore.RED}║{Fore.WHITE}  [5] 📈 Reportes y estadísticas                         {Fore.RED}║
{Fore.RED}║{Fore.WHITE}  [6] ⚙️  Configuración de interfaz                       {Fore.RED}║
{Fore.RED}║{Fore.WHITE}  [0] 🚪 Salir                                           {Fore.RED}║
{Fore.RED}╚══════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}"""

LEGAL_WARNING = f"""
{Fore.RED}[!] AVISO LEGAL [!]
{Fore.YELLOW}Esta herramienta es SOLO para fines educativos.
El uso en redes sin autorización es ILEGAL en la mayoría de países.
El usuario asume toda la responsabilidad legal.
{Style.RESET_ALL}
"""

def check_root():
    if os.name == 'nt':  # Windows
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    else:  # Linux/Termux
        return os.geteuid() == 0

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def show_menu():
    clear_screen()
    print(BANNER)
    print(LEGAL_WARNING)
    
    if not check_root():
        print(f"{Fore.RED}[⚠] Sin permisos de administrador/root. Algunas funciones no estarán disponibles.{Style.RESET_ALL}")
    
    option = input(f"\n{Fore.GREEN}➤ Selecciona una opción: {Style.RESET_ALL}")
    return option

def main():
    while True:
        option = show_menu()
        
        if option == '1':
            from modules.sniffer import start_sniffer
            start_sniffer()
        elif option == '2':
            from modules.bandwidth import test_bandwidth
            test_bandwidth()
        elif option == '3':
            from modules.traffic_gen import traffic_generator
            traffic_generator()
        elif option == '4':
            from modules.analyzer import network_analyzer
            network_analyzer()
        elif option == '5':
            print(f"{Fore.CYAN}[+] Generando reportes... (Próximamente){Style.RESET_ALL}")
            input("Presiona Enter para continuar...")
        elif option == '6':
            print(f"{Fore.CYAN}[+] Configuración de interfaz (Próximamente){Style.RESET_ALL}")
            input("Presiona Enter para continuar...")
        elif option == '0':
            print(f"{Fore.GREEN}[✓] Saliendo... ¡Ética siempre!{Style.RESET_ALL}")
            sys.exit(0)
        else:
            print(f"{Fore.RED}[✗] Opción inválida{Style.RESET_ALL}")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
