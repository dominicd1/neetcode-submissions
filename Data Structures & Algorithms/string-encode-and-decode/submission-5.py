class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for ele in strs:
            length = 0
            tempstr = ""
            for char in ele:
                length += 1
                tempstr += char


            # Include length prefix
            output+= str(length)
            # Include delimiter prefix
            output += "#"
            output+= tempstr

       # print(output)
        return output

    def decode(self, s: str) -> List[str]:
        str_list = []
        i = -1;
        prefixCount = 0
        numberActive = True
        numberActiveStr = ""
        for char in s:
            if(char.isdigit() and prefixCount == 0):
                if (not numberActive):
                    numberActive = True
                numberActiveStr += char
                
            elif (numberActive):
                if (char == "#"):
                    prefixCount = int(numberActiveStr)
                    i += 1
                    str_list.append("")
                    numberActive = False
                    numberActiveStr = ""
            else:
                prefixCount -= 1
                 # print(i)
                str_list[i] += char
                # print (str_list[i])
                
        return str_list

        

