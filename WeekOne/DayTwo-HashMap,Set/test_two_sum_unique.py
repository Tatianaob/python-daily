from two_sum_unique import twoSum

def test_two_sum():
    assert sorted(twoSum([2, 4, 3, 5, 7, 8, 1, 9], 10)) == sorted([(2, 8), (3, 7), (1, 9)])
    assert sorted(twoSum([1, 2, 3, 4], 5)) == sorted([(1, 4), (2, 3)])
    assert twoSum([], 10) == []
    assert twoSum([5,5,5], 10) == [(5,5)]

test_two_sum()
print("All tests passed!")