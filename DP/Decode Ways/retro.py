def numDecodings(s):
    if len(s) == 0 or s[0] == '0':
        return 0

    num_decoding = [0]* (len(s))
    num_decoding[0] = 1

    for i in range(1,len(s)):
        if s[i]!='0':
            num_decoding[i] += num_decoding[i-1]

        if 10<=int(s[i:i+1])<=26:
            if i == 1:
                num_decoding[i] += + 1
                continue
            num_decoding[i] += num_decoding[i-2]

    return num_decoding[-1]
