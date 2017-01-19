/**

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	int maxDepth(TreeNode* root) {

		if (root != NULL) {

			int depthleft = maxDepth(root->left);
			int depthright = maxDepth(root->right);
			int max_d = depthleft > depthright ? depthleft : depthright;

			return 1 + max_d;
		} else return 0;
	}
};


// python

/*# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0
        */
