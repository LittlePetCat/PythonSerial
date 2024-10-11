import struct
def int2bytes(int_num:int):
    '''
    输入0x52或82
    输出b"\x52"
    '''
    return int_num.to_bytes()
def bytes2bytesStr(bytes_data:bytes):
    """
    输入b"\x52\x53"
    输出b"5253"
    """
    return bytes2str(bytes_data=bytes_data).encode("ascii")
def bytes2str(bytes_data:bytes):
    """
    输入b"\x52\x53"
    输出"5253"
    """
    retlst=[]
    for i in range(len(bytes_data)):
        item = hex(bytes_data[i]).replace("0x","")
        if(len(item)==1):
            item = "0"+item
        item = item.upper()
        retlst.append(item)
    return "".join(retlst)
def strbytes2intlist(bytes_data)->list[int]:
    """
    输入:b"\x23\x24"
    输出:[0x23,0x24]
    """
    retlst=[]
    for i in range(len(bytes_data)):
        retlst.append(bytes_data[i])
    return retlst
def intStrList2IntList(intStrList:list[int])->list[int]:
    """
    输入:[50,50,48,49]
    输出:[0x22,0x01]
    """
    i=0
    ret_lst=[]
    while i<(len(intStrList)-1):
        if ((intStrList[i]>=48 and intStrList[i]<=57) or (intStrList[i]>=65 and intStrList[i]<=70)) and ((intStrList[i+1]>=48 and intStrList[i+1]<=57) or (intStrList[i+1]>=65 and intStrList[i+1]<=70)):
            if intStrList[i]>=48 and intStrList[i]<=57:
                intStrList[i]-=48
            else:
                intStrList[i]-=55
            if intStrList[i+1]>=48 and intStrList[i+1]<=57:
                intStrList[i+1]-=48
            else:
                intStrList[i+1]-=55
            ret_lst.append((intStrList[i])*16+intStrList[i+1])
        elif intStrList[i] == 32 and intStrList[i+1]==32:
            ret_lst.append(0)
        else:
            print("Error",intStrList[i],intStrList[i+1])
        i+=2
    return ret_lst
def hexString2int(string:str):
    '''
    输入:"A55D"
    输出:0xA55D
    '''
    return int(string,16)

def bytesToFloat(h1,h2,h3,h4):
    ba = bytearray()
    ba.append(h1)
    ba.append(h2)
    ba.append(h3)
    ba.append(h4)
    return struct.unpack("!f",ba)[0] #將 MSB的 bytes 转成 float，用“！f”参数
    # return struct.unpack("f",ba)[0] #將LSB bytes转成 float，用“f”参数