class Solution:
    def toHex(self, num: int) -> str:
        num = num & (2**32-1)
        if num<10 and num>=0:
            return str(num)

        hash_dict ={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',
                    8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',
                    14:'e',15:'f'}
        stack = []
        while num > 0:
            remainder = num%16
            stack.insert(0,hash_dict[remainder])
            num = num//16
        return ''.join(stack)

# I don't understand what is num = num & (2**32-1)
