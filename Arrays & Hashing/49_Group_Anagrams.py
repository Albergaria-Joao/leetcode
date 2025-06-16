class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # Creating a dictionary with the default factory of list - if a key does not exist, it creates an empty list for it

        for s in strs:
            key = "".join(sorted(s)) # Here, I join each character of the sorted string with "" separing them (nothing)
            anagrams[key].append(s) # By appending to this key, if no strings exist for it yet, it will automatically be created
        
        return list(anagrams.values()) # Returns the dictionary as a list


        # "BRUTE" SOLUTION
        
        # anagrams = [[]]
        # #chars = [{}]
        # map = {}



        # non_unique = 0
        # groups = 0

        

        # for i in range(len(strs) - 1):
        #     if (strs[i] not in map):
        #         if (i > 0):
        #             groups += 1
        #         map[strs[i]] = groups
        #         print(f"{strs[i]}, {map[strs[i]]}")
                
        #     for j in range(i+1, len(strs)):
        #         if (strs[j] not in map):
        #             if (tuple(sorted(strs[j])) == tuple(sorted(strs[i]))):
        #                 map[strs[j]] = groups       
        #                 print(f" SUB {strs[j]}, {map[strs[j]]}")
        #             elif (i >= len(strs) - 2):
        #                 print(f"SEM PAR {strs[j]}")
        #                 groups += 1
        #                 map[strs[j]] = groups
                    
        # anagrams = [[] for i in range(len(map) - (groups + 1))]
        # print(anagrams)
        # print(map)
        # if (len(strs) == 1):
        #     anagrams.append(strs)
        #     return anagrams

        # for i, n in enumerate(map):
        #     print(map[n])
        #     anagrams[map[n]].append(n)
        # return anagrams
