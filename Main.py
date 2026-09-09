# Brute-force attack estimation Phase 1
password_length = 8

charset = 26

speed = 500000

max_hours = 24

combinations = charset ** password_length

seconds = combinations / speed

hours = seconds / 3600

worth_it = hours <= max_hours

print(f"Number of combinations: {combinations}")
print(f"Seconds needed: {seconds:.2f}")
print(f"Hours needed: {hours:.2f}")
print(f"Is it worth it? {'Yes' if worth_it else 'No'}")

#Brute-force attack estimation Phase 2 (Dfine the target)

