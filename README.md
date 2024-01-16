# NDWCSHAP Generator (by Lesserkuma)

This tool helps you creating your own NDWCSHAP access point, given you can and want to run a hotspot with the ancient WEP128 encryption. Any Nintendo DS, DSi and 3DS will auto-connect to these kinds of hotspots without the need of going through Nintendo Wi-Fi Connection settings. This feature was officially used at “DS Station” kiosks, likely from 2006 until 2020.

To create your own access point, you need to specify a value called “apnum” which was used to distinguish between individual store chains and locations. This allowed developers to distribute location-based WFC content to their games, similar to Nintendo Zone locations.

## Command Line Arguments

```
--apnum APNUM              generates SSID and WEP key based on apnum provided
--ssid SSID                generates WEP key and apnum based on SSID provided
```

## Thanks
Some technical information was found at [wmb-asm - NintendoSpot.wiki](https://code.google.com/archive/p/wmb-asm/wikis/NintendoSpot.wiki).
