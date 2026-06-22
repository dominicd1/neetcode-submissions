class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        
        counter_dict = {}
        for string in strs:
            #sort the string (anagrams match to a sorted string)
            sortedString = "".join(sorted(string))

            #if anagram found, add to anagram group list
            if sortedString in counter_dict:
                counter_dict[sortedString].append(string)

            #if anagram not found, create a new anagram group list
            else:
                counter_dict[sortedString] = [string]

            #convert dictionary into final list and return
        return list(counter_dict.values())