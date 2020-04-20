#!/usr/bin/python
# File: legacy_router.py
#Cesar Aldrete
#Luis Alva

from mininet.net import Mininet
from mininet.node import Host, Node, Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def myNetwork():
	net = Mininet(topo=None, build=False, ipBase='10.0.0.0/8', controller=Controller)
	info('*** Adding controller\n' )
	net.addController('c0') #initiated reference controller c0

	info('*** Add switches\n')
	s1 = net.addSwitch('s1') #adding switch s1	
	s1.cmd('sysctl -w net.ipv4.ip_forward=1') #send data between host
	#This is required if you want your system to act as a router

	info('*** Add hosts\n')
	#data will be passed between 2 host h1 & h2
	h2 = net.addHost('h2', cls=Host, ip='10.0.0.2')
	h1 = net.addHost('h1', cls=Host, ip='10.0.0.1')
	
	info('*** Add links\n')
	#connecting ports on the switch
	net.addLink(h1, s1)
	net.addLink(h2, s1)
	
	info('*** Starting network\n')
	net.start() #begin network
	net.pingAll() #testing network with pingAll()
	
	info('*** Starting CLI\n') 
	CLI(net) #command-line interface to talk to nodes

	info('*** Stopping Network\n')
	net.stop() #terminates network

if __name__ == '__main__':
	setLogLevel( 'info' )
	myNetwork()

