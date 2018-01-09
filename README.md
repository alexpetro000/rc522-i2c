## RFID RC522 on Raspberry PI with NodeJS (I2C version)

node.js module to access a rfid reader with rc522 chipset which is connected a raspberry pi

## Fork of
https://github.com/ocsacesar/rc522 
modified for accessing i2c version such as RC522 I2C V1.1
and reworked to async addon based on https://github.com/paulhauner/example-async-node-addon

Update: you can now configure which pin is connected to RST Pin and which i2c address is used.  


## Purpose
This node module is to access RFID reader with a rc522 chipset (e.g. [link to ebay](https://www.ebay.co.uk/itm/Hot-RC522-RFID-Read-Write-Card-Module-I2C-IC-RFCard-Inductive-Module-13-56MHz/272575100254?_trksid=p2047675.c100011.m1850&_trkparms=aid%3D222007%26algo%3DSIC.MBE%26ao%3D1%26asc%3D20140107083358%26meid%3D8b37c7ce2e92478780dd684b44b7334b%26pid%3D100011%26rk%3D1%26rkt%3D7%26sd%3D181874320808)) via GPIO interface of the raspberry pi.

## Functionality
The module is currently only able to read the serial number of the tag which is hold onto the reader.


## Example


```
var rc522i2c = require("rc522-i2c");

console.log('Ready!!!');
// pin RPI_V2_GPIO_P1_37 see bcm2835.h, i2c-address,callback 
rc522i2c(26,0x28,function(rfidSerialNumber){
	console.log(rfidSerialNumber);
});
```

Save and run: (Is necessary "sudo")

```
sudo node rfid.js
```


NOTE: Running as root
