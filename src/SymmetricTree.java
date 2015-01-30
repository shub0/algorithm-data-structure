

/**
 * 
 * SymmetricTree.java
 * Dec 6, 2012
 */

/**
 * @author huangsp
 *
 */
public class SymmetricTree {
	// recursive algorithm, O(N) time
	public boolean isSymmetric(TreeNode root) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (root == null)	return true;
        else{
        	return isSymmetric(root.left, root.right);
        }
	}
	private boolean isSymmetric(TreeNode root1, TreeNode root2){
		if (root1 == null && root2 == null)		return true;
		else if (root1 == null || root2 == null)		return false;
		else{
			if (root1.val != root2.val)		return false;
			else
				return isSymmetric(root1.right, root2.left) && isSymmetric(root1.left, root2.right);
		}
	}
	// Tips: get a symmetric tree
	@SuppressWarnings("unused")
	private void symmetricTree(TreeNode root){
		TreeNode tmp = root.left;
		root.left = root.right;
		root.right = tmp;
		if (root.left != null)	symmetricTree(root.left);
		if (root.right != null)	symmetricTree(root.right);
	}
}
