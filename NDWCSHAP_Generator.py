# -*- coding: utf-8 -*-
# NDWCSHAP Generator
# Author: Lesserkuma (github.com/lesserkuma)

import argparse, sys, re, base64, hashlib

# From https://code.google.com/archive/p/wmb-asm/wikis/NintendoSpot.wiki
offset_map = [ 0x17, 0x14, 0x11, 0x0D, 0x0B, 0x06, 0x0F, 0x0E, 0x09, 0x15, 0x0C, 0x04, 0x02, 0x01, 0x12, 0x10, 0x05, 0x03, 0x13, 0x0A, 0x07, 0x08, 0x00, 0x16 ]
xor_key1 = b"952uybjnpmu903bia@bk5m[-"
xor_key2 = b"38g6zxjk20gvmv]6^=j&%vY1"

def ssid2cfg(ssid):
	data = bytearray(base64.b64decode(ssid.encode("ascii")))
	for i in range(0, len(data)):
		data[i] ^= xor_key1[i]
	data_new = bytearray([0] * len(data))
	for offset, i in enumerate(offset_map):
		data_new[i] = data[offset]
	for i in range(0, len(data_new)):
		data_new[i] ^= xor_key2[i]
	return data_new

def cfg2ssid(data):
	data = bytearray(data)
	for i in range(0, len(data)):
		data[i] ^= xor_key2[i]
	data_new = bytearray([0] * len(data))
	for offset, i in enumerate(offset_map):
		data_new[offset] = data[i]
	for i in range(0, len(data_new)):
		data_new[i] ^= xor_key1[i]
	return base64.b64encode(data_new).decode("ascii")

####
class ArgParseCustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter): pass

print("NDWCSHAP Generator v1.0\nby Lesserkuma\n")
parser = argparse.ArgumentParser()
parser.add_argument("--apnum", help="generates SSID and WEP key based on apnum provided", type=str, default=False)
parser.add_argument("--ssid", help="generates WEP key and apnum based on SSID provided", type=str, default=False)
args = parser.parse_args()

if args.ssid:
	if len(args.ssid) != 32 or not re.match(r"^[A-Za-z0-9+/]*={0,2}$", args.ssid):
		print(f"Error: The SSID must be a 32 character base64 string.")
		sys.exit(1)
	cfg = ssid2cfg(ssid=args.ssid)
	wep_key = hashlib.md5(cfg).digest()[-0xD:]
	magic = cfg[0:8]
	if magic != b"NDWCSHAP":
		print(f"Error: “{args.ssid:s}” is not a valid NDWCSHAP SSID.")
		sys.exit(1)
	apnum = cfg[8:18]
	try:
		apnum = apnum.decode("ascii")
	except:
		apnum = '0x' + ', 0x'.join(format(x, '02X') for x in apnum)
		print("Error: Invalid apnum bytes:", apnum)
		sys.exit(1)
	
	print(f"SSID:    {args.ssid:s}")
	print(f"WEP Key: {wep_key.hex():s}")
	print(f"Apnum:   {apnum:s}")

elif args.apnum:
	apnum = args.apnum.rjust(10, "0")[:10]
	try:
		cfg = list(b"NDWCSHAP" + apnum.encode("ascii"))
	except:
		print("Error: Invalid apnum.")
		sys.exit(1)
	cfg += [ 0x1C, 0x01, 0x20, 0x9D, 0x68, 0xAF ]
	cfg = bytearray(cfg)
	ssid = cfg2ssid(data=cfg)
	wep_key = hashlib.md5(cfg).digest()[-0xD:]

	print(f"SSID:    {ssid:s}")
	print(f"WEP Key: {wep_key.hex():s}")
	print(f"Apnum:   {apnum:s}")

else:
	parser.print_help()
