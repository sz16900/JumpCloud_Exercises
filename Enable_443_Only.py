# Observations:
	# Because the assignment specifically states "https/443 incoming only" I decided to 
	# drop all connections except the https/443 incoming.
	# This, however, does not allow for a two-way communication and hence cannot open a 
	# simple https page like www.google.com
	# Yet, in order to have a two way communication to open an https website, one can try  
	# to run the following script:
		# https://github.com/sz16900/Network/blob/master/firewall_443_only_two-way.py

import sys, os, subprocess as sp

def allow_443_incoming(DEBUG=False):
    options = {'iptables': '/sbin/iptables', 'protocol': 'tcp', 'port': 443}
    ipcommands = '{iptables} -A INPUT -p {protocol} --dport {port} -m conntrack --ctstate \
    NEW,ESTABLISHED -j ACCEPT'.format(**options)

    if DEBUG:
        print ipcommands
    else:
    	# Flush policies in case there's any
        sp.call('/sbin/iptables -F', shell=True)
        # Lets drop everything since the assignment explicitly states: 
        # "allow incoming https/443 connections only."
	sp.call('/sbin/iptables -A INPUT -j DROP', shell=True)
	sp.call('/sbin/iptables -A OUTPUT -j DROP', shell=True)
	sp.call('/sbin/iptables -A FORWARD -j DROP', shell=True)
	# Lets create our policy
        iptables = sp.call(ipcommands, shell=True)

if __name__ == '__main__':
    # Check if you are running as root
    if os.getuid() != 0:
        print "You must be root to create policies with iptables."
        sys.exit(2)
    else:
        allow_443_incoming()
