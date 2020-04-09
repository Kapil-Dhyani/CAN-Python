
import can

interface = 'vector'
channel = 0
baud = 1000 * 125

bus = can.Bus(interface=interface, channel=channel, bitrate=baud)

message = can.Message(arbitration_id=0x79e, is_extended_id=False,dlc=8,
                      data=[0x02, 0x10, 0x01])

bus.send(message, timeout=.2)
