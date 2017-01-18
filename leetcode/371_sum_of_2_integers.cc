/*371. Sum of Two Integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
*/

class Solution {
public:
	int getSum(int a, int b) {

		return add_carry(a, b);
	}

	int add_carry(int a, int b) {

		if (b == 0) return a;

		int without_carry = a ^ b;
		int carry = (a & b) << 1;

		return add_carry(without_carry, carry);


	}
};
