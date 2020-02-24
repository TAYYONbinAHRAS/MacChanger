import subprocess
import optparse
from optparse import OptionParser

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--iface",dest="interface",help="Please Enter Write your ip address... (-i wlan0) or (--iface wlan0)")
    parse_object.add_option("-m","--mac",dest="mac_address",help="Pleasse Enter Write your mac_addres... (-m 11:22:33:44:55:66)")
    (user_inputs,arguments) = parse_object.parse_args()
    print("\n")
    print(user_inputs.interface)
    print("\n")
    print(user_inputs.mac_address)
    print("\n")
    mac_changed(user_inputs.interface,user_inputs.mac_address)
    print("\n")
    new_mac(user_inputs.interface)
    print("\n")
    print("MacChanger Susccesful...")
    return parse_object.parse_args()

def mac_changed(interface,mac_address):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
    subprocess.call(["ifconfig",interface,"up"])

def new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    print(ifconfig)

try:    
    get_user_input()
except TypeError:
    print("""

            	 ..TAYYON..

            		 //////\\\\\/	
            		///O    O\\\/
            	       ///        \\\/
            	             ||	  
            	         \  (--)  /
            		  \______/
            	


        hi please use it like this

        [+] python MacChanger.py -i interface -m six character mac_address

        sample:

        [+] python MacChanger.py -i wlan0 -m 11:22:33:44:55:66

            				""")
