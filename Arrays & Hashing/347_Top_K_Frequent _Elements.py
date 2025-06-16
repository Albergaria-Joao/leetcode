class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # My solution O(N + LogU + K) 
        
        # dic = defaultdict(list)

        # for n in nums:
        #     dic[n].append(n)

        # lista = sorted(list(dic.values()), key=len, reverse=True)
        
        # res = []
        # for i in range(k):
        #     res.append(lista[i][0])

        # return(res)

        # Suggested solution

        # Step 1: Count frequencies
        freq = Counter(nums)  # O(n)
        # Counts the frequency of each entry in nums
        
        # Step 2: Use a min-heap of size k with (frequency, number) pairs
        # lambda means I'm creating an anonymous function to compare each item (x) to the next (x[1])
        heap = heapq.nlargest(k, freq.items(), key=lambda x: x[1])  # O(n log k)

        # Step 3: Extract just the elements
        return [item[0] for item in heap]  # O(k)
        # item[1] would extract the frequency
