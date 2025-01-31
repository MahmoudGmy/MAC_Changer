#!/usr/bin/env python

import subprocess  #to help in run system command
import optparse #to use command line arguments
import re # to use  regular expression

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="The Interface Name U want to Change its MAC")
    parser.add_option("-m", "--mac", dest="new_mac", help="The New MAC")
    (options, arguments) = parser.parse_args()
    if not options.interface :
        parser.error("[-] Please Specify an interface, use --help for more info.")
    elif not options.new_mac :
        parser.error("[-] Please Specify an new MAC, use --help for more info.")
    return options

def return_current_mac(interface) :
    ifconfig_result = subprocess.check_output(["ifconfig", interface],text=True)
    mac_address = re.search(r"\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}", ifconfig_result)
    if mac_address :
        return mac_address[0]
    else :
        return 0

def change_mac(interface,new_mac):
    print(f"[+] Changing MAC Address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def check_changed_of_mac(interface,new_mac) :
    current_mac = return_current_mac(interface)
    if current_mac !=0 :
        if current_mac ==new_mac :
            print(f"[+] MAC changed successfully to {new_mac}")
        else :
            print(f"[-] Error in changing MAC, it still  {current_mac}")
    else :
        print("[-] not found current MAC")




Options= get_arguments()
change_mac(Options.interface,Options.new_mac)
check_changed_of_mac(Options.interface,Options.new_mac)



