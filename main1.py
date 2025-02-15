class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
    
sol1 = Solution()
print(sol1.isAnagram("anagram", "nagarama"))


# ეს კოდი ამოწმებს არის თუ არა s სტრიქონი t-ის ანაგრამა.  return sorted(s) == sorted(t)  -- ეს ხაზი ორივე სტრიქონს აწყობს თანმიმდევრობით და შემდეგ ადარებს არიან თუ აარა ერთნაირები.