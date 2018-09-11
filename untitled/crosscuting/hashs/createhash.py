import hashlib

def generatademd5(encryptlabel):
    key = str(encryptlabel)
    return hashlib.md5(key .encode()).hexdigest()

def decryptMD5(testHash):
        s = []
        while True:
                m = hashlib.md5()
                for c in s:
                        m.update(chr(c))
                hash = m.hexdigest()
                if hash == testHash:
                        return ''.join([chr(c) for c in s])
                wrapped = True
                for i in range(0, len(s)):
                        s[i] = (s[i] + 1) % 256
                        if s[i] != 0:
                                wrapped = False
                                break
                if wrapped:
                        s.append(0)