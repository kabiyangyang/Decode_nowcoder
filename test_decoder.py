import sys
 
 
def decode(s):
    i = 0
    x, y, z = -1, -1, -1
    while i < len(s):
        if s[i] == '[':
            x = i
        elif s[i] == '|':
            y = i
        elif s[i] == ']':
            z = i
            break
        i += 1
    if x != -1 and y != -1 and z != -1:
        times = int(s[x + 1:y])  # 次数
        sub = s[y + 1:z]  # 子串
        decode_str = s[:x] + times * sub + s[z + 1:]  # 解码
        return decode(decode_str)  # 递归解码
    return s  # 如果一个中括号都没有，说明没有需要解码的部分
 
 
for s in sys.stdin:
    print(decode(s), end='')
