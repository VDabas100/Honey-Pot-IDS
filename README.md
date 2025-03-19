# Honeypot Intrusion Detection System (IDS)

A Python-based Honeypot IDS designed to simulate a fake system for detecting and logging incoming attack attempts while providing decoy responses. This project serves as a tool for simulating attack scenarios and testing the effectiveness of intrusion detection mechanisms in a controlled environment.

# Key Features:

•Port Simulation: Simulates multiple service ports (e.g., FTP, SSH, HTTP) to mimic real-world network services.        

•Attack Detection & Logging: Detects and logs attack attempts, capturing detailed information such as attacker IPs and accessed ports.                                                                                       


•Fake Responses: Responds with decoy messages to mislead and confuse intruders.    

•Real-Time Monitoring: Provides visual feedback with dynamic progress bars and status updates during attack simulations.

•Security Testing Tool: Helps in testing intrusion detection strategies and understanding attacker behavior in a controlled setting.

# Technologies Used:

•Programming Language: Python 3.x

•Libraries:

   •pyfiglet for ASCII banner displays

   •termcolor for terminal output with color coding
   
   •tqdm for real-time progress bars

•Network Programming: Socket programming for simulating network services and monitoring ports.

•Logging: Tracks attack events with detailed logs, enabling post-incident analysis.

# Usage:

•The honeypot listens on predefined service ports and simulates responses when an attack is detected.

•Attack attempts, such as port scans or unauthorized access, are logged to the honeypot.log file for further analysis.

•Key details recorded include the attacker's IP, timestamp, and the targeted service port.