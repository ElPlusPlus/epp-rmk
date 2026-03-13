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
    
    for slave_id in [247]:
        result = client.read_holding_registers(address=0, count=1, slave=slave_id)
        if not result.isError():
            print(f"Success! Slave ID: {slave_id}, Register 0: {result.registers[0]}")
            break
        result = client.read_holding_registers(address=252, count=1, slave=slave_id)
        if not result.isError():
            print(f"Register 252: {result.registers[0]}")
            break
        if slave_id % 10 == 0:
            print(f"Tested up to slave ID {slave_id}...")
    else:
        print("No valid slave ID found")
    
    client.close()
else:
    print("Failed to connect")
