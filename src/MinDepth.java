

/**
 * 
 * MinDepth.java
 * Mar 24, 2013
 */

/**
 * @author huangsp
 *
 */
public class MinDepth {
	public static int minDepth(TreeNode root){
		if (root.left == null && root.right == null)	return 1;
		else{
			int left = Integer.MAX_VALUE;
			int right = Integer.MAX_VALUE;
			if (root.left != null)	left = minDepth(root.left);
			if (root.right != null)	right = minDepth(root.right);
			return 1 + Math.min(right, left);
		}
	}
}
