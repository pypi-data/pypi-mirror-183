import binascii
import ctypes

MB_ABORTRETRYIGNORE = 2
MB_CANCELTRYCONTINUE = 6
MB_HELP = 0x4000
MB_OK = 0
MB_OKCANCEL = 1
MB_RETRYCANCEL = 5
MB_YESNO = 4
MB_YESNOCANCEL = 3

MB_ICONEXCLAMATION = MB_ICONWARNING = 0x30
MB_ICONINFORMATION = MB_ICONASTERISK = 0x40
MB_ICONQUESTION = 0x20
MB_ICONSTOP = MB_ICONERROR = MB_ICONHAND = 0x10

MB_DEFBUTTON1 = 0
MB_DEFBUTTON2 = 0x100
MB_DEFBUTTON3 = 0x200
MB_DEFBUTTON4 = 0x300

MB_APPLMODAL = 0
MB_SYSTEMMODAL = 0x1000
MB_TASKMODAL = 0x2000

MB_DEFAULT_DESKTOP_ONLY = 0x20000
MB_RIGHT = 0x80000
MB_RTLREADING = 0x100000

MB_SETFOREGROUND = 0x10000
MB_TOPMOST = 0x40000
MB_SERVICE_NOTIFICATION = 0x200000

IDABORT = 3
IDCANCEL = 2
IDCONTINUE = 11
IDIGNORE = 5
IDNO = 7
IDOK = 1
IDRETRY = 4
IDTRYAGAIN = 10
IDYES = 6

def int2bin(int):
    return bin(int)[2:]

def bin2int(bin):
    return int(bin)

def str2bin(str):
    return ''.join(format(i, '08b') for i in bytearray(str, encoding ='utf-8'))

def bin2str(binr):
    n = int('0b'+binr, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

def box(text, style, title):
    return ctypes.windll.user32.MessageBoxW(None, text, title, style)

def file(file):
    deffilefile = open(file)
    deffilefile.close()