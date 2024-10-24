class Solution:
    def romanToInt(self, s: str) -> int:
        char_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        lists=list(s)
        # lists.reverse()
        print(lists)
        cnt=0
        i=0
        while i < len(lists):
            print(i)
            if i +1 > len(lists)-1:
                cnt+=char_dict[lists[i]]
                i+=1
            elif lists[i] == "I" and lists[i+1]=="V":
                cnt+=4
                i+=2
            elif lists[i] == "I" and lists[i+1]=="X":
                cnt+=9
                i+=2
            elif lists[i] == "X" and lists[i+1]=="L":
                cnt+=40
                i+=2
            elif lists[i] == "X" and lists[i+1]=="C":
                cnt+=90
                i+=2
            elif lists[i] == "C" and lists[i+1]=="D":
                cnt+=400
                i+=2
            elif lists[i] == "C" and lists[i+1]=="M":
                cnt+=900
                i+=2
            else:
                cnt+=char_dict[lists[i]]
                i+=1

        
        return cnt

