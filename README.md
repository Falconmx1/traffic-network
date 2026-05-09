🚀 Instalación
Windows (PowerShell como Administrador)
git clone https://github.com/Falconmx1/traffic-network.git
cd traffic-network
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

Linux (Ubuntu/Debian)
sudo apt update && sudo apt install python3 python3-pip tcpdump -y
git clone https://github.com/Falconmx1/traffic-network.git
cd traffic-network
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

Termux (Android)
pkg update && pkg upgrade
pkg install python git tsu
git clone https://github.com/Falconmx1/traffic-network.git
cd traffic-network
pip install -r requirements.txt
# Para acceso root en Termux (opcional)
tsu python3 main.py

🎯 Uso básico
bash

python main.py

Menú principal
    ╔══════════════════════════════════════════╗
    ║        🔥 TRAFFIC-NETWORK v1.0 🔥       ║
    ║    Herramienta ética para análisis de red║
    ╚══════════════════════════════════════════╝
    
    [1] 📡 Monitoreo de tráfico (sniffer)
    [2] ⚡ Test de ancho de banda
    [3] 🎮 Generador de tráfico controlado
    [4] 📊 Analizador de red
    [5] 📈 Reportes y estadísticas
    [6] ⚙️ Configuración de interfaz
    [0] 🚪 Salir

    📋 Requisitos

    Python 3.8 o superior

    Permisos de administrador/root (para captura de paquetes)

    scapy, psutil, speedtest-cli, colorama

⚠️ Aviso legal

    Esta herramienta es SOLO para fines educativos y pruebas en redes propias o con autorización explícita.
    El uso no autorizado para espiar tráfico ajeno o interferir con redes sin permiso es ilegal en casi todas las jurisdicciones. El autor no se hace responsable del mal uso de esta herramienta.
