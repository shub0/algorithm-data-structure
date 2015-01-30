/**
 * 
 * RecoveryBST.java
 * Dec 1, 2012
 */

/**
 * @author Shubo Liu
 *
 */
public class RecoveryBST {
	public void recoverTree(TreeNode root){
		TreeNode node1 = null;
		TreeNode node2 = null;
		int[] count = new int[2];
		count[0] = Integer.MAX_VALUE;
		node1 = getFirst(root, count, node1);
		count[1] = Integer.MIN_VALUE;
		node2 = getSecond(root, count, node2);
		int tmp = node1.val;
		node1.val = node2.val;
		node2.val = tmp;
	}
	private TreeNode getFirst(TreeNode root, int[] count, TreeNode node1){
		if (root == null) 	return node1;
		node1 = getFirst(root.left, count, node1);
		if (root.val < count[0])	node1 = root;
		count[0] = root.val;
		node1 = getFirst(root.right, count, node1);
		return node1;
	}
	private TreeNode getSecond(TreeNode root, int[] count, TreeNode node2){
		if (root == null) 	return node2;
		node2 = getSecond(root.right, count, node2);
		if (root.val > count[1])	node2 = root;
		count[1] = root.val;
		node2 = getSecond(root.left, count, node2);
		return node2;
	}
	
}
