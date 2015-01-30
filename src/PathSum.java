/**
 * 
 * PathSum.java
 * Dec 1, 2012
 */
import java.util.ArrayList;
/**
 * @author Shubo Liu
 *
 */
public class PathSum {
	ArrayList<ArrayList<Integer>> solution = new ArrayList<ArrayList<Integer>>();
	public boolean hasPathSum(TreeNode root, int sum){
		if (root == null) return false;
		//else if (sum < 0) return false;
		else if (sum == root.val && isLeaf(root))	return true;
		else{
			return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
		}
	}
		
	public ArrayList<ArrayList<Integer>> findPathSum(TreeNode root, int sum){
		if (root == null) 	return solution;
		else{
			ArrayList<Integer> aSolution = new ArrayList<Integer>();
			findAPathSum(root, sum, aSolution);
			return solution;
		}
	}
	@SuppressWarnings("unchecked")
	private void findAPathSum(TreeNode root, int sum, ArrayList<Integer> aSolution){
		if (root == null) return;
		else if (sum == root.val && isLeaf(root)){
			aSolution.add(root.val);
			solution.add((ArrayList<Integer>) aSolution.clone());
		}else{
			aSolution.add(root.val);
			int currentSize = aSolution.size();
			// check left subtree
			findAPathSum(root.left, sum - root.val, aSolution);
			while(aSolution.size() > currentSize){
				aSolution.remove(aSolution.size() - 1);
			}
			// check right subtree
			findAPathSum(root.right, sum - root.val, aSolution);
			while(aSolution.size() > currentSize){
				aSolution.remove(aSolution.size() - 1);
			}
		}
	}
	
	private boolean isLeaf(TreeNode node){
		if (node == null) return false;
		else if (node.left == null && node.right == null) return true;
		else return false;
	}
	
	public static void main(String[] args){
		/*
		TreeNode node1 = new TreeNode(5);
		TreeNode node2 = new TreeNode(4);
		TreeNode node3 = new TreeNode(8);
		TreeNode node4 = new TreeNode(11);
		TreeNode node5 = new TreeNode(13);
		TreeNode node6 = new TreeNode(4);
		TreeNode node7 = new TreeNode(7);
		TreeNode node8 = new TreeNode(2);
		TreeNode node9 = new TreeNode(5);
		TreeNode node10 = new TreeNode(1);
		
		node1.left = node2;
		node1.right = node3;
		node2.left = node4;
		node3.left = node5;
		node3.right = node6;
		node4.left = node7;
		node4.right = node8;
		node6.left = node9;
		node6.right = node10;
		*/
		TreeNode node1 = new TreeNode(1);
		node1.right = new TreeNode(2);
		node1.right.left = new TreeNode(3);
		//System.out.println(new PathSum().findPathSum(node3, 21));
		PathSum myPath = new PathSum();
		System.out.println(myPath.findPathSum(node1, 6));
	}
	
	
}
