# This program utilizes the psutil library to obtain the MAC address of the network interface
# of the device running it. If the MAC address is an approved MAC address it can "access the network"
# If the MAC address isn't approved, the program will display "Access Denied"
import psutil

def get_mac():
    # Get all network interfaces
    interfaces = psutil.net_if_addrs() 
    # psutil.net_if_addrs() returns a dictionary with keys of adapter names and values 
    # of MAC addresses and ip addresses associated with the interface
    interface_name = input('Enter the name of your network interface: ')
    # User must enter the name of their network interface
    for interface, addrs in interfaces.items():
        # Check for specified interface (My wireless adapter's name is "Wi-Fi")
        if interface_name in interface:
            for addr in addrs:
                if addr.family == psutil.AF_LINK:  # Check for MAC address family
                    # addr.family refers to the family attribute associated with the
                    # addresses of the interface (such as MAC, IPv4, and IPv6)
                    # psutil.AF_LINK refers to link layer addresses (MAC addresses)
                    return addr.address #returns MAC address
    return None

print('Welcome to the program!')
choice = ''
while choice.lower() not in ['y', 'n']:
    choice = input('Would you like to access the network (Y/n): ')
    if choice.lower() not in ['y', 'n']:
        print('Invalid input')

if choice.lower() == 'y':
    # Obtain MAC address of adapter
    mac_address = get_mac()
    if mac_address:
        print(f'MAC address is: {mac_address}')
    else:
        print('Adapter not found.')
    # Grant access if MAC address is in the list of approved MAC addresses
    with open('MAC Addresses.txt', 'r') as file:
        contents = file.read() 
    if mac_address in contents:
        print('Access Granted')
    else:
        print('Access Denied')
