class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return 'Zero'
        words = ['','One','Two','Three','Four','Five',
                 'Six','Seven','Eight','Nine','Ten',
                 'Eleven','Twelve','Thirteen','Fourteen','Fifteen',
                 "Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["","Ten","Twenty","Thirty","Forty","Fifty",
                "Sixty","Seventy","Eighty","Ninety"]
        quantity = ['Trillion','Billion','Million','Thousand','']
        num = str(num)
        n = len(num)
        num = '0'*(3-n%3) + num
        print(num)
        res = ''
        r = len(num)//3
        for i in range(r):
            added = ''
            three = num[3*i:3*(i+1)]
            hundred = three[0]
            ten = three[1:]
            if hundred!='0':
                added = words[int(hundred)] + ' ' + 'Hundred' + ' '
            if ten[0] == '0' or ten[0] == '1':
                if ten!='00':
                    added += words[int(ten)] + ' '
            else:
                added += tens[int(ten[0])] + ' '
                if ten[1] != '0':
                    added += words[int(ten[1])] + ' '
            
            if added == ' ' or added == '  ' or added == '':
                res += ''
            else:
                added += quantity[-(r-i)] + ' '
                res += added

        return res.strip()

# 面向用例编程hhh
# 困难题，实际也就中等吧