﻿# NDWCSHAP Generator (by Lesserkuma)

This tool helps you creating your own NDWCSHAP access point. Any Nintendo DS, DSi and 3DS will auto-connect to these kinds of hotspots without the need of going through Nintendo Wi-Fi Connection settings. This feature was officially used at “DS Station” kiosks, likely from 2006 until 2020. Note that these access points use the ancient 128-bit WEP encryption that is no longer considered secure.

To create your own access point combination of SSID and WEP key, you need to specify a value called “apnum”. This value was used to distinguish between individual store chains and locations which allowed developers to distribute location-based WFC content to their games, similar to Nintendo Zone locations.

If you use hostapd, add these lines to hostapd.conf:
```
channel=11
interface=wlan0
ssid=<SSID>
auth_algs=3
wep_default_key=0
wep_key0=<WEP KEY>
wep_rekey_period=300
```

## Command Line Arguments

```
--apnum APNUM              generates SSID and WEP key based on apnum provided
--ssid SSID                generates WEP key and apnum based on SSID provided
```

## Thanks
Some technical information was found at [wmb-asm - NintendoSpot.wiki](https://code.google.com/archive/p/wmb-asm/wikis/NintendoSpot.wiki) by yellows8.
