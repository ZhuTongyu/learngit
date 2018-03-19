#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
};

 bool traverse(struct TreeNode *left, struct TreeNode *right)
{
	if (left == NULL && right == NULL) {
		return true;
	}

	if (left == NULL || right == NULL) {
		return false;
	}// 和上一个if 是递进关系，能到达这个if判定，必然左右子树不全为空

	if (left->val != right->val) {
		return false;
	}

	return traverse(left->left, right->right) && traverse(left->right, right->left);
}

 bool isSymmetricTree(struct TreeNode* root)
 {
	 if (root == NULL) {
		 return true;
	 }

	 return traverse(root->left, root->right);
 }
int main()
{
	//int tree[] = { 1,2,2,3,4,4,3 };
	struct TreeNode root, n10, n11, n20, n21, n22, n23;
	root.val = 1;
	n10.val = 2;
	n11.val = 2;
	n20.val = 3;
	n21.val = 4;
	n22.val = 4;
	n23.val = 3;
	root.left = &n10;
	root.right = &n11;
	n10.left = &n20;
	n10.right = &n21;
	n11.left = &n22;
	n11.right = &n23;
	n20.left = NULL;
	n20.right = NULL;
	n21.left = NULL;
	n21.right = NULL;
	n22.left = NULL;
	n22.right = NULL;
	n23.left = NULL;
	n23.right = NULL;
	printf("%s\n", isSymmetricTree(&root) ? "true" : "false");
	return 0;
}