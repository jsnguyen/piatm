import time
import Adafruit_MCP9808.MCP9808 as MCP9808
import Adafruit_BMP.BMP085 as BMP085
import HTU21DF


def c_to_f(c):
	return c * 9.0 / 5.0 + 32.0

def MCP9008_get_data():
	sensor = MCP9808.MCP9808()
	sensor.begin()
	temp = c_to_f(sensor.readTempC())
	return {'time':time.time(),'temp':temp}

def BMP085_get_data():
	sensor = BMP085.BMP085()
	temp = c_to_f(sensor.read_temperature())
	pressure = sensor.read_pressure()
	sealevel_pressure = sensor.read_sealevel_pressure()
	altitude = sensor.read_altitude()
	return {'time':time.time(),'temp':temp, 'pressure':pressure, 'sealevel_pressure':sealevel_pressure, 'altitude': altitude}

def HTU21DF_get_data():
	HTU21DF.htu_reset
	temp = c_to_f(HTU21DF.read_temperature())
	humidity = HTU21DF.read_humidity()
	return {'time':time.time(),'temp':temp, 'humidity':humidity}

def get_all_data():
	MCP=MCP9008_get_data()
	BMP=BMP085_get_data()
	HTU=HTU21DF_get_data()
	temp=[MCP['temp'],BMP['temp'],HTU['temp']]
	all={'time':time.time(),'temp':temp,'pressure':BMP['pressure'], 'sealevel_pressure':BMP['sealevel_pressure'], 'altitude':BMP['altitude'], 'humidity':HTU['humidity']}

	return all


if __name__ == '__main__':
	print(get_all_data())
