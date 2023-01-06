"""
2180. 统计各位数字之和为偶数的整数个数
简单
21
相关企业
给你一个正整数 num ，请你统计并返回 小于或等于 num 且各位数字之和为 偶数 的正整数的数目。

正整数的 各位数字之和 是其所有位上的对应数字相加的结果。

 

示例 1：

输入：num = 4
输出：2
解释：
只有 2 和 4 满足小于等于 4 且各位数字之和为偶数。    
示例 2：

输入：num = 30
输出：14
解释：
只有 14 个整数满足小于等于 30 且各位数字之和为偶数，分别是： 
2、4、6、8、11、13、15、17、19、20、22、24、26 和 28 。
"""
from tqdm import trange


class Solution:
    @staticmethod
    def count_even_lc(num: int) -> int:
        """
        作者：力扣官方题解
        链接：https://leetcode.cn/problems/count-integers-with-even-digit-sum/solutions/2045888/tong-ji-ge-wei-shu-zi-zhi-he-wei-ou-shu-rvqol/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        ans = 0
        for x in range(1, num + 1):
            s = 0
            while x:
                s += x % 10
                x //= 10
            ans += s % 2 == 0
        return ans

    @staticmethod
    def count_even(num: int) -> int:
        is_odd = int(num % 2 == 1)
        is_sum_odd = sum(map(int, str(num))) % 2 == 1
        bias = int(not bool(is_odd) and is_sum_odd)
        return (num - is_odd) // 2 - bias


if __name__ == '__main__':
    s = Solution()
    for i in trange(1, 1000):
        lc = s.count_even_lc(i)
        self = s.count_even(i)
        if lc != self:
            print(i, lc, self)
            break
