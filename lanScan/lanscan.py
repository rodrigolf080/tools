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
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

# Get the address range to ARP
while True:
    print("Type 'quit' to exit the program.")
    ip_add_range_entered = input("\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
    if ip_add_range_entered == "quit":
        sys.exit("Gracefully exiting the program...")

    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} is a valid ip address range, initiating scan...\n")
        break
    else: 
        print(f"{ip_add_range_entered} is NOT a valid ip address range, please try again.\n")


# Try ARPing the ip address range supplied by the user. 
# The arping() method in scapy creates a pakcet with an ARP message 
# and sends it to the broadcast mac address ff:ff:ff:ff:ff:ff.
# If a valid ip address range was supplied the program will return 
# the list of all results.
arp_result = scapy.arping(ip_add_range_entered)