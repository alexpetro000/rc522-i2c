var rc522i2c = require('./build/Release/rc522-i2c');

rc522i2c(function(rfidTagSerialNumber) {
	console.log(rfidTagSerialNumber);
});