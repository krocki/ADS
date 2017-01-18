/*Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

*/

class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {

		std::map<int, int> pairs;
		std::vector<int> answer;

		for (int i = 0; i < nums.size(); i++) {

			std::map<int, int>::iterator it = pairs.find(target - nums[i]);
			if (it != pairs.end()) {
				answer.push_back(it->second);
				answer.push_back(i);
				return answer;
			} else
				pairs[nums[i]] = i;

		}
	}
};
