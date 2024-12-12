import scapy.all as scapy
import argparse
import re


def get_arguments():
    parser = argparse.ArgumentParser(
        description='Tool for changing the MAC address.')
    parser.add_argument('-i', '--ip', dest='ip_address',
                        help='IP address or range to scan. For example: 192.168.1.1/24')
    args = parser.parse_args()
    return args


def validate_ip(ip):
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?:/[0-9]{1,2})?$")
    if not ip_pattern.match(ip):
        return False
    return True


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = arp_broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


args = get_arguments()
ip_address = args.ip_address

if not ip_address or not validate_ip(ip_address):
    print('[-] Invalid IP address. Please use the script as follows:')
    print('python network_scanner.py -i <IP_ADDRESS_RANGE>')
    print('For example: python network_scanner.py -i 192.168.1.1/24')
else:
    scan_results = scan(ip_address)
    print_result(scan_results)
