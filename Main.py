# Brute-force attack estimation Phase 1
#Baseline assumptions
import ipaddress


password_length = 8
charset = 26
speed = 10
max_hours = 24

# Calculate the number of combinations and time needed

combinations = charset ** password_length
seconds = combinations / speed
hours = seconds / 3600
worth_it = hours <= max_hours

#Brute-force attack estimation Phase 2 (Define the target)
#Known target Information
target_ip = input("Enter the target IP address: ")
service= input("Enter the service to attack (e.g., SSH, FTP): ")
port:int = int(input("Enter the port number: "))
username:str = str(input("Enter the username: "))

#Phase 3: Active network checking


#Final output of the brute-force attack estimation
print(f"Target IP: {target_ip}")
print(f"Service: {service}")
print(f"Port: {port}")  
print(f"Username: {username}")
print(f"combinations: {combinations}")
print(f"Hours needed: {hours:.2f}") 

print(f"Is it worth it? {'Yes' if worth_it else 'No'}")