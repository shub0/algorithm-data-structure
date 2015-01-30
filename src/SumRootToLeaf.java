/**
 * 
 * SumRootToLeaf.java
 * Mar 23, 2013
 */

/**
 * @author huangsp
 *
 */
public class SumRootToLeaf {
	//int sum = 0;
	public int findSum(TreeNode root){
		return findSum(root,"",0);
	}
	private int findSum(TreeNode root, String number, int sum){
		if (root == null)	return sum;
		else if (isLeaf(root)){
			number += (root.val +"");
			sum += Integer.valueOf(number);
			return sum;
		}else{
			number += (root.val +"");
			int size = number.length();
			if (root.left != null)
				sum = findSum(root.left, number, sum);
			number = number.substring(0, size);
			if (root.right != null)
				sum = findSum(root.right, number, sum);
			return sum;
		}
	}
	private boolean isLeaf(TreeNode root){
		if (root.left == null && root.right == null)	return true;
		else return false;
	}
	public static void main(String[] args){
		TreeNode root = new TreeNode(1);
		root.left = new TreeNode(2);
		root.right = new TreeNode(3);
		SumRootToLeaf myTest = new SumRootToLeaf();
		System.out.println(myTest.findSum(root));
	}
}
