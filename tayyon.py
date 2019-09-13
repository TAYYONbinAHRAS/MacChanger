import subprocess
import optparse
from optparse import OptionParser

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--iface",dest="interface",help="Please Enter Write your ip address... (-i wlan0) or (--iface eth0)")
    parse_object.add_option("-m","--mac",dest="mac_address",help="Pleasse Enter Write your mac_addres... (-m 11:22:33:44:55:66)")
    return parse_object.parse_args()
def mac_changed(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

def new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    print(ifconfig)
    
print("""

	 ..TAYYON..

		 //////\\\\\/	
		///O    O\\\/
	       ///        \\\/
	             ||	  
	         \  (--)  /
		  \______/
	
				""")
print(""" 
     Succesful
    	|| 

    	""")
(user_input,arguments) = get_user_input()
mac_changed(user_input.interface,user_input.mac_address)
new_mac(user_input.interface)

