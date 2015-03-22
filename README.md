# qualys_ip_extract
Very basic python script to take IPs from qualys asset group and reduce dotted quad ranges to single IPs. (e.g. 192.168.1.1-192.168.1.5 turns into 192.168.1.1, 192.168.1.2, 192.168.1.3, 192.168.1.4, 192.168.1.5)

Takes existing CSV file as input and can accept both single IPs and ranges but does not currently work with CIDR

Usage: python ip_extract.py $iplist.csv 
