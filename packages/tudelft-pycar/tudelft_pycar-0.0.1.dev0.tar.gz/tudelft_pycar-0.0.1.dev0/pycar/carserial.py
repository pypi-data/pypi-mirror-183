import serial
import serial.tools.list_ports

def get_ports():
    """
    Return a list of available ports.

    `ListPortInfo` contains:
    - `device`: full path to device
    - `name`: display name
    """
    return serial.tools.list_ports.comports()

def connect(port):
    """
    Connect to a port.

    `port` should be a file path, e.g. COM6 or /dev/ttyUSB0.
    Returns an object that implements `read()` and `write()`.
    You should `close()` a port before dropping it!
    """

    # These parameters are copied from `EPOCommunications.c`
    ser = serial.Serial(port, 115200, rtscts=True)
    ser.open()
    return ser

def main():
    """Example: list serial ports."""
    ports = get_ports()
    if ports == []:
        print("No serial ports found.")
        return

    for port in ports:
        print(port.device)

if __name__ == "__main__":
    main()
