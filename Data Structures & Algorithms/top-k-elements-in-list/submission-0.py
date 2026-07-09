class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}

        for i in nums:
            if i in mapp:
                mapp[i] += 1
            else:
                mapp[i] = 1
        
        mapp = sorted(mapp, key=lambda x: mapp[x], reverse=True)
        return mapp[:k]