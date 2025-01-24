#!/usr/bin/python3
import re
import subprocess
import optparse

def search_mac_address(mac_address):
    """
    Searches for a valid MAC address pattern in the provided string.
    """
    match = re.search(r'(([a-fA-F0-9]{2}[:\-]){5}[a-fA-F0-9]{2})', mac_address)
    return match.group(0) if match else None

def get_arguments():
    """
    Parses command-line arguments for interface and new MAC address.
    """
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, _) = parser.parse_args()

    if not options.interface:
        parser.error("Please specify an interface. Use --help for more information.")
    if not options.new_mac:
        parser.error("Please specify a new MAC address. Use --help for more information.")

    return options

def set_new_mac_address(interface, new_mac):
    """
    Sets a new MAC address for the given interface.
    """
    print(f"Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_mac_address(interface):
    """
    Retrieves the current MAC address of the specified interface.
    """
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
        return search_mac_address(ifconfig_result)
    except subprocess.CalledProcessError:
        print(f"Error: Could not read MAC address for interface {interface}")
        return None

# Main logic
options = get_arguments()
current_mac = get_mac_address(options.interface)
if current_mac:
    print(f"Current MAC address for interface {options.interface}: {current_mac}")
else:
    print("Could not retrieve current MAC address.")

set_new_mac_address(options.interface, options.new_mac)
new_mac = get_mac_address(options.interface)

if new_mac == options.new_mac:
    print(f"MAC address was successfully changed to {new_mac}.")
else:
    print("Error: MAC address did not get changed.")
