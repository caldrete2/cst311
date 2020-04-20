import time
import random
from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

message = raw_input('Input lowercase sentence: ')
address = (serverName, serverPort)

rrtData = []

for i in range(10):
    init_time = time.time()
    rttTime = str(time.strftime(" %H:%M:%S"))
    print 'Ping: ' + str(i) + rttTime

    clientSocket.sendto(message, address)

    try:
        responseMessage, serverAddress = clientSocket.recvfrom(2048)
        print responseMessage

        end_time = time.time()
        rtt = end_time - init_time
        print 'Round Trip Time: ' +str(rtt) + ' s\n\n'

        rrtData.append(rtt)
    except timeout:
        print 'Request Timed out\n\n'


estimatedRTT = 0.0
devRTT = 0.0

for i in range(len(rrtData)):
    randomSample = random.choice(rrtData)
    estimatedRTT = (1 - 0.125) * estimatedRTT + 0.125 * randomSample
    devRTT = (1 - 0.25) * devRTT + 0.25 * abs(randomSample - estimatedRTT)

timeout = estimatedRTT + 4 * devRTT

print 'Max RTT: ' + str(max(rrtData)) + ' s'
print 'Min RTT: ' + str(min(rrtData)) + ' s'
print 'Avgerage RTT: ' + str(sum(rrtData) / len(rrtData)) + ' s'
print 'Packet loss percentage: ' + str((10 - len(rrtData)) * 10) + '%'
print 'EstimatedRTT: ' + str(estimatedRTT) + ' s'
print 'Timeout Interval: ' + str(timeout) + ' s\n\n'
~

