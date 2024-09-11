import win32con

# 定义特殊按键与虚拟键码的映射
key_map = {
    'ENTER': win32con.VK_RETURN,
    'SHIFT': win32con.VK_SHIFT,
    'CTRL': win32con.VK_CONTROL,
    'ALT': win32con.VK_MENU,
    'ESC': win32con.VK_ESCAPE,
    'TAB': win32con.VK_TAB,
    'BACKSPACE': win32con.VK_BACK,
    'DELETE': win32con.VK_DELETE,
    'UP': win32con.VK_UP,
    'DOWN': win32con.VK_DOWN,
    'LEFT': win32con.VK_LEFT,
    'RIGHT': win32con.VK_RIGHT,
    'F1': win32con.VK_F1,
    'F2': win32con.VK_F2,
    'F3': win32con.VK_F3,
    'F4': win32con.VK_F4,
    'F5': win32con.VK_F5,
    'F6': win32con.VK_F6,
    'F7': win32con.VK_F7,
    'F8': win32con.VK_F8,
    'F9': win32con.VK_F9,
    'F10': win32con.VK_F10,
    'F11': win32con.VK_F11,
    'F12': win32con.VK_F12,
    'A': 0x41,
    'B': 0x42,
    'C': 0x43,
    'D': 0x44,
    'E': 0x45,
    'F': 0x46,
    'G': 0x47,
    'H': 0x48,
    'I': 0x49,
    'J': 0x4A,
    'K': 0x4B,
    'L': 0x4C,
    'M': 0x4D,
    'N': 0x4E,
    'O': 0x4F,
    'P': 0x50,
    'Q': 0x51,
    'R': 0x52,
    'S': 0x53,
    'T': 0x54,
    'U': 0x55,
    'V': 0x56,
    'W': 0x57,
    'X': 0x58,
    'Y': 0x59,
    'Z': 0x5A,
    'a': 0x41,  # lower case 'a'
    'b': 0x42,  # lower case 'b'
    'c': 0x43,  # lower case 'c'
    'd': 0x44,  # lower case 'd'
    'e': 0x45,  # lower case 'e'
    'f': 0x46,  # lower case 'f'
    'g': 0x47,  # lower case 'g'
    'h': 0x48,  # lower case 'h'
    'i': 0x49,  # lower case 'i'
    'j': 0x4A,  # lower case 'j'
    'k': 0x4B,  # lower case 'k'
    'l': 0x4C,  # lower case 'l'
    'm': 0x4D,  # lower case 'm'
    'n': 0x4E,  # lower case 'n'
    'o': 0x4F,  # lower case 'o'
    'p': 0x50,  # lower case 'p'
    'q': 0x51,  # lower case 'q'
    'r': 0x52,  # lower case 'r'
    's': 0x53,  # lower case 's'
    't': 0x54,  # lower case 't'
    'u': 0x55,  # lower case 'u'
    'v': 0x56,  # lower case 'v'
    'w': 0x57,  # lower case 'w'
    'x': 0x58,  # lower case 'x'
    'y': 0x59,  # lower case 'y'
    'z': 0x5A,  # lower case 'z'
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'SPACE': 0x20,
    '-': 0xBD,
    '=': 0xBB,
    '[': 0xDB,
    ']': 0xDD,
    '\\': 0xDC,
    ';': 0xBA,
    '\'': 0xDE,
    ',': 0xBC,
    '.': 0xBE,
    '/': 0xBF,
    '`': 0xC0
}


def get_virtual_key_code(key_name):
    """将特殊按键的字符串转换为虚拟键码"""
    return key_map.get(key_name.upper(), None)


