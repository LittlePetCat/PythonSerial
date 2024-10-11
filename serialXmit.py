import serial
import serial.tools.list_ports
class SerialXmit:
    TIME_OUT = 20000
    def __init__(self) -> None:
        self.ser=None

    def __del__(self) -> None:
        if self.ser and self.ser.is_open:
            self.ser.close()

    def ConfigSerial(self,commName=None,baudrate=115200) -> bool:
        try:
            if commName == None:
                port_list = list(serial.tools.list_ports.comports())
                for i in range(len(port_list)):
                    print(f"{i+1}: {port_list[i].device} {port_list[i].description}")
                if(len(port_list)>=1):
                    if len(port_list)==1:
                        x=1
                    else:
                        x=int(input(f"input to select port (1~{len(port_list)}):\n"))
                    if x >= 1 and x <=len(port_list):
                        self.ser=serial.Serial(port=port_list[x-1].name,baudrate=baudrate,timeout=self.TIME_OUT)
                        if self.ser.is_open:
                            self.ser.close()
                        self.ser.open()
                        return True
                else:
                    print("no ports !")
                return False
            else:
                self.ser=serial.Serial(port=commName,baudrate=baudrate,timeout=self.TIME_OUT)
                if self.ser.is_open:
                    self.ser.close()
                self.ser.open()
                return True
        except Exception as e:
            print(e)
            print("Serial config Failed !")
            return False
    
    def Transmit(self, bytesToWrite:bytes)->bool:
        try:
            if self.ser:
                # print(f"tx({len(bytesToWrite)}):{self.StringFy(bytesToWrite)}")
                if self.ser.write(bytesToWrite)!=0:
                    return True
            return False
        except:
            print("write Error !")
            return False
    
    def Recieve(self,n)->bytes:
        try:
            rx=self.ser.read(n)
            # print(f"rx({len(rx)}):{self.StringFy(rx)}")
            return rx
        except Exception as e:
            print(e)
            return b""

    
    def StringFy(self,bts:bytes)->str:
        strret=""
        for i in range(len(bts)):
            strret+=hex(bts[i]).replace("0x","").upper().zfill(2)+" "
        return strret

