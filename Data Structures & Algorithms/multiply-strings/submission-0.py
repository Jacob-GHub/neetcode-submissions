class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == "0" or num2[0] == "0": 
            return "0"

        char_to_int = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        int_to_char = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

        int_1, int_2 = 0,0

        for char in num1:
            int_1 *= 10
            int_1 += char_to_int[char]
        
        for char in num2:
            int_2 *= 10
            int_2 += char_to_int[char]
        
        product = int_1 * int_2
        res = ""

        while product > 0:
            res += int_to_char[product % 10]
            product //= 10
        
        return res[::-1]

