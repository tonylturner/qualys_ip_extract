#!/usr/bin/python

import csv
import sys
from netaddr import *
import pprint

with open(sys.argv[1], 'rU') as f:
	file_read = csv.reader(f)
	for row in file_read:
		ip_network_cidr = []
		for ip in row:
			if '-' in ip:
				dash = ip.find('-')
				ip_start = ip[:dash]
				ip_end = ip[dash + 1:]
				ip_range = list(iter_iprange(ip_start, ip_end))
				ip_range = cidr_merge(ip_range)
				for ip in ip_range:
					ip_network_cidr.append(str(ip))
					ipcidr=ip
					#print ipcidr
					'''to only include usable addresses, but this was a little buggy as it incorrectly applied CIDR mask'''
					#for ipaddr in ipcidr.iter_hosts():
					for ipaddr in ipcidr:
						print ipaddr
			elif '-' not in ip:
				print ip
	
