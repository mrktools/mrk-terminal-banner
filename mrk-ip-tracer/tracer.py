import os
import time
import random
import phonenumbers
from phonenumbers import geocoder, carrier

os.system('clear')
print("\033[1;32m")
os.system('figlet -f slant "MRK TRACER" | lolcat')
print("\033[1;36m-------------------------------------------")
print("  Tool: Advanced Tracer | Developer: MRK")
print("-------------------------------------------\033[0m")

target = input("\n[+] Enter Target Number: ")

# নামের একটি লিস্ট (সিমুলেশনের জন্য)
names = ["Mijanur Rahman", "Kamal Hossain", "Abir Ahmed", "Sumon Ali", "Sakil Khan", "Unknown User"]

try:
    print(f"\n\033[1;34m[*] Accessing Global Database...\033[0m")
    time.sleep(2)
    print(f"\033[1;34m[*] Bypassing Firewall...\033[0m")
    time.sleep(2)
    
    # নম্বরটি প্রসেস করা
    if not target.startswith('+'):
        p_num = "+88" + target if target.startswith('0') else "+" + target
    else:
        p_num = target

    parsed_number = phonenumbers.parse(p_num)
    location = geocoder.description_for_number(parsed_number, "en")
    service_provider = carrier.name_for_number(parsed_number, "en")

    print(f"\n\033[1;32m[✔] Target Found!")
    print(f"\033[1;33m[•] Name        : \033[1;37m{random.choice(names)}") # সিমুলেটেড নাম
    print(f"\033[1;33m[•] Country     : \033[1;37m{location}")
    print(f"\033[1;33m[•] Operator    : \033[1;37m{service_provider}")
    
    # কল হিস্ট্রি সেকশন
    print("\n\033[1;34m[*] Fetching Call Logs...\033[0m")
    time.sleep(2)
    print("\033[1;32m[!] Recent Activity:")
    print("    - Incoming: 0171XXXXXXX (2m 10s)")
    print("    - Outgoing: 0192XXXXXXX (5m 45s)")

except:
    print("\n\033[1;31m[!] Error: System Timed Out!")

print("\n\033[1;36m-------------------------------------------\033[0m")
