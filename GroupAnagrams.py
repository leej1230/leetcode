class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort_strs = []
        # for s in strs:
        #     sort_strs.append("".join(sorted(s)))
        # #print(sort_strs)
        # taken = set()
        # ans = []
        # for i in range(len(strs)):
        #     if i in taken:
        #         continue
        #     tmp = []
        #     taken.add(i)
        #     tmp.append(strs[i])
        #     for j in range(i+1,len(strs)):
        #         if sort_strs[i] == sort_strs[j]:
        #             taken.add(j)
        #             tmp.append(strs[j])
        #     ans.append(tmp)
        # return ans
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()