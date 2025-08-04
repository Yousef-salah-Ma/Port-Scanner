import socket
import threading

# خريطة لبعض البورتات المعروفة
common_ports = {
    21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
    80: 'HTTP', 110: 'POP3', 143: 'IMAP', 443: 'HTTPS',
    3306: 'MySQL', 3389: 'RDP'
}

def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        if result == 0:
            service = common_ports.get(port, 'Unknown')
            print(f"✅ Port {port} OPEN [{service}]", end='')

            try:
                banner = s.recv(1024).decode().strip()
                if banner:
                    print(f" --> Banner: {banner}")
                else:
                    print(" --> (No banner)")
            except:
                print(" --> (No banner read)")
        s.close()
    except:
        pass

try:
    ip = input("📍 Enter IP to scan: ")
    start_port = int(input("🔢 Start port: "))
    end_port = int(input("🔢 End port: "))
    print(f"\n🔎 Scanning {ip} from {start_port} to {end_port}...\n")

    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

except KeyboardInterrupt:
    print("\n⛔ Scan stopped by user.")
except ValueError:
    print("🚫 Please enter valid port numbers.")
except Exception as e:
    print(f"🚨 Error: {e}")
