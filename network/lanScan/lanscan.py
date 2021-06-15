import scapy.all as scapy
import re
import sys
# Basic user interface header
print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(r"""
    .-.    .--. .-..-. .--.  .--.  .--. .-..-.
    : :   : .; :: `: :: .--': .--': .; :: `: :
    : :   :    :: .` :`. `. : :   :    :: .` :
    : :__ : :: :: :. : _`, :: :__ : :: :: :. :
    :___.':_;:_;:_;:_;`.__.'`.__.':_;:_;:_;:_; """)
print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Regular Expression Pattern to recognise IPv4 addresses.
addr_range_re = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
# Get the address range to ARP
try:
    while True:
        print("[*] CTRL^C to quit the program.")
        addr_range = input("[+] Enter IPv4 address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
        if addr_range == "quit":
            sys.exit("Gracefully exiting the program...")

        if addr_range_re.search(addr_range):
            print(f"{addr_range} is a valid ip address range, initiating scan...\n")
            break
        else: 
            print(f"{addr_range} is NOT a valid ip address range, please try again.\n")
except KeyboardInterrupt:
    print('[*] Gracefully quitting...')
    sys.exit(0)
# Try ARPing the ip address range supplied by the user. 
# The arping() method in scapy creates a pakcet with an ARP message 
# and sends it to the broadcast mac address ff:ff:ff:ff:ff:ff.
# If a valid ip address range was supplied the program will return 
# the list of all results.
arp_res = scapy.arping(addr_range)
