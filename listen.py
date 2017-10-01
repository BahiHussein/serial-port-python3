import sys
import glob
import serial
import time


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


    


print('Enter your commands below.\r\nInsert "exit" to leave the application.')

allports = serial_ports()

print(serial_ports())




    

kinput = input(">> Enter port name ")

for p in allports:
    if kinput in p or kinput in p.lower():
        kinput = p
        

ser = serial.Serial(
    port= kinput,
    baudrate=9600
)

if ser.isOpen():
    print('port was open')
    ser.close()
    print('x - port closed')

try: 
    ser.open()
    print('port '+kinput+' is opened and listening')
except Exception as e:
    print("error open serial port: " + str(e))
    exit()

if ser.isOpen():

    try:
        ser.flushInput() #flush input buffer, discarding all its contents
        ser.flushOutput()#flush output buffer, aborting current output 
                 #and discard all that is in buffer

        time.sleep(0.5)  #give the serial port sometime to receive the data

        print('listening....')

        while True:
           response = ser.readline()
           print("read data: " + response)


    except Exception as e1:
           print("error communicating...: " + str(e1))

else:
    print("cannot open serial port ")


