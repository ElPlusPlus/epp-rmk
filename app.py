from pymodbus.client import ModbusSerialClient

client = ModbusSerialClient(
    port='/dev/USB0',
    baudrate=9600,
    timeout=3
)

if client.connect():
    print("Connected to device")
    result = client.read_holding_registers(address=252, count=1, slave=1)
    if not result.isError():
        frequency = result.registers[0]
        print(f"Frequency: {frequency}")
    client.close()
else:
    print("Failed to connect")
