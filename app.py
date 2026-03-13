from pymodbus.client import ModbusSerialClient
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

client = ModbusSerialClient(
    port='/dev/ttyUSB0',
    baudrate=9600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=3
)

if client.connect():
    print("Connected to device")
    result = client.read_holding_registers(address=252, count=1, slave=4)
    if not result.isError():
        frequency = result.registers[0]
        print(f"Frequency: {frequency}")
    else:
        print(f"Error: {result}")
    client.close()
else:
    print("Failed to connect")
