import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

listWlan = wlan.scan()

print(listWlan[0])