/**
 * 
 * FlattenTree.java
 * Dec 31, 2012
 */
/**
 * @author huangsp
 *
 */
public class FlattenTree {
	public void flattenTree(TreeNode root){
		if (root == null)	return;
		if (root.left != null)	flattenTree(root.left);
		if (root.right != null)	flattenTree(root.right);
		if (root.left == null)	return;
		TreeNode pointer = root.left;
		while(pointer.right != null){
			pointer = pointer.right;
		}
		pointer.right = root.right;
		root.right = root.left;
		root.left = null;
	}
}
