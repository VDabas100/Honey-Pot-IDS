import socket
import threading
import logging
import time
import random
import pyfiglet
from termcolor import colored
from tqdm import tqdm


logging.basicConfig(filename="honeypot.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Non-privileged ports to listen on (above 1024)
PORTS = [8080, 8443, 9090, 10000, 11000, 12000]

# Honeypot banner
def banner():
    print(colored(pyfiglet.figlet_format("Honeypot IDS"), "cyan"))
    print(colored("[+] Initializing Honeypot System...", "yellow"))
    for _ in tqdm(range(10), desc="Loading", bar_format="{l_bar}{bar} [ Time: {elapsed} ]"):
        time.sleep(0.2)
    print(colored("[+] Honeypot is Active! Listening for attacks...", "green"))

def handle_connection(client_socket, addr, port):
    logging.info(f"Connection attempt from {addr} on port {port}")
    print(colored(f"[!] Intruder detected from {addr} on port {port}", "red"))
    
    # Simulating fake vulnerabilities
    responses = [
        "220 Fake FTP Server Ready",
        "SSH-2.0-OpenSSH_7.4p1 Debian-10+deb9u7",
        "HTTP/1.1 200 OK\nServer: Apache/2.4.41 (Ubuntu)"
    ]
    response = random.choice(responses)
    client_socket.send(response.encode())
    time.sleep(2)
    client_socket.close()

def start_honeypot():
    threads = []
    for port in PORTS:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("0.0.0.0", port))  # Listen on all interfaces
        server.listen(5)
        print(colored(f"[*] Honeypot active on port {port}", "green"))

        def listen_for_connections():
            while True:
                client, addr = server.accept()
                thread = threading.Thread(target=handle_connection, args=(client, addr[0], port))
                thread.start()

        t = threading.Thread(target=listen_for_connections)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    banner()
    start_honeypot()
