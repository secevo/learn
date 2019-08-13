class Solution:
    hex_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    def toHex(self, num: int) -> str:
        hex_char_list = []
        if num < 0:
            num = (1<<32)+num
        while True:
            hex_char = self.hex_chars[num & 0xf]
            hex_char_list.insert(0, hex_char)
            num >>= 4
            if num == 0:
                break
        return ''.join(hex_char_list)