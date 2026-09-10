#1 Target Information
import socket

target_ip = input("Enter the target IP address: ")
port = int(input("Enter the port number: "))

#2. Active Network Check
print(f"[*] Testting connection to {target_ip}:{port}...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3.0)

result = s.connect_ex((target_ip, port))
s.close()

if result == 0:
    print("[+] SUCCESS : port is OPEN and target ia reachable!")
else:
    print("[-] FALIED : Target unreachble or port is closed")

#3 Mode selecations : Wordlist vs Pure Brute-Force
wordlist_path = input("Enter the path to the wordlist file (or press enter to skip): ").strip().strip('"\'')

speed= 30
max_hours = 72

if wordlist_path:
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as f:
            compinations = sum(1 for _ in f)
            attack_type = "Wordlist Attack"
    except Exception as e :
        print(f"[-] File erroe: {e}. Defaulting to Brute-Force.")
        wordlist_path = None

if not wordlist_path:
    attack_type = "Pure Brute-Force"
    password_length = 8  #Based on Min Password Pollicy Mostly The min is 8
    charset = 26 # number of letters in English
    compinations = charset ** password_length

#4 Calculations
seconds = compinations / speed
hours = seconds / 3600
worth_it = hours <= max_hours


#5 Output
print("\n--- Feasbility Report ---")
print(f"Target: {target_ip}:{port}")
print(f"Mode: {attack_type }")
print(f"Total Tries: {compinations}")
print(f"Hours needed: {hours:.2f} hrs ({hours/24:.2f} days)")
print(f"Feasible: {'Yes' if worth_it else 'No'}")
