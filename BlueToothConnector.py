import os
import subprocess
import pexpect
import sys

class BluetoothCTLerror(Exception):
    pass

class BluetoothCTL:
    def __init__(self):
        self.child = pexpect.spawn("bluetoothctl", echo= False)

    def sendCommandAndGenerateOutput(self,command):
        pause = 0
        self.send(command + "\n")
        time.sleep(pause)
        start_failed = self.child.expect(["bluetooth", pexpect.EOF])

        if start_failed:
            raise BluetoothCTLerror("BluetoothCTL  Exceprtion after Command"+ command)
        
        return self.child.before.split("\r\n")
    
    def agendPreperations(self):
        self.sendCommandAndGenerateOutput("agent on")
        self.sendCommandAndGenerateOutput("default-agent")

    def powerOn(self):
        self.sendCommandAndGenerateOutput("power on")
    
    def scanOnOff(self, scanState):
        if(scanState):
            self.sendCommandAndGenerateOutput("scan on")
        else:
            self.sendCommandAndGenerateOutput("scan off")

    def getAvailableDevices(self):
        outDevices = self.sendCommandAndGenerateOutput("devices")
        devices = {}
        for item in outDevices:
            split = item.split(" ")
            devices[split[1]]= split[2]
        return devices

if name == "__main__":
    bl = BluetoothCTL
    bl.powerOn
    bl.agendPreperations
    bl.scanOnOff(true)
    print(bl.getAvailableDevices)
