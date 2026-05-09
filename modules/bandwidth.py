#!/usr/bin/env python3
from colorama import Fore, Style
import speedtest
import threading

def test_bandwidth():
    print(f"{Fore.CYAN}[+] Iniciando Test de Ancho de Banda...{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[!] Esto puede tomar unos segundos...{Style.RESET_ALL}")
    
    def show_progress():
        chars = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
        i = 0
        while not done:
            print(f"\r{Fore.CYAN}Medición en curso {chars[i % len(chars)]}{Style.RESET_ALL}", end="")
            i += 1
            import time
            time.sleep(0.1)
    
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        
        global done
        done = False
        thread = threading.Thread(target=show_progress)
        thread.start()
        
        download = st.download() / 1_000_000  # Mbps
        upload = st.upload() / 1_000_000
        ping = st.results.ping
        
        done = True
        thread.join()
        
        print(f"\n\n{Fore.GREEN}📊 RESULTADOS:{Style.RESET_ALL}")
        print(f"  📥 Descarga: {Fore.CYAN}{download:.2f} Mbps{Style.RESET_ALL}")
        print(f"  📤 Subida:   {Fore.CYAN}{upload:.2f} Mbps{Style.RESET_ALL}")
        print(f"  🏓 Ping:     {Fore.CYAN}{ping:.1f} ms{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")
    
    input("\nPresiona Enter para continuar...")
