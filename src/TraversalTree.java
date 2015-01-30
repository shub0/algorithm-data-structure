/**
 * 
 * Tree.java
 * Feb 5, 2013
 */

import java.util.ArrayList;

/**
 * @author huangsp
 *
 */

public class TraversalTree {
	
	@SuppressWarnings("unchecked")
	public static ArrayList<ArrayList<Integer>> levelOrderBottom(TreeNode root) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ArrayList<ArrayList<Integer>> levelTraversalReverse = new ArrayList<ArrayList<Integer>>();
        if (root != null){
            ArrayList<ArrayList<Integer>> levelTraversal = new ArrayList<ArrayList<Integer>>();
            ArrayList<TreeNode> nodesInTree = new ArrayList<TreeNode>();
            nodesInTree.add(root);
            nodesInTree.add(null);
            ArrayList<Integer> currentLevel = new ArrayList<Integer>();;
            while ( nodesInTree.size() > 0){            	
                TreeNode currentNodes = nodesInTree.remove(0);
                if (currentNodes != null){
                    currentLevel.add(currentNodes.val);
                    if (currentNodes.left != null)  nodesInTree.add(currentNodes.left);
                    if (currentNodes.right != null) nodesInTree.add(currentNodes.right);
                }else{
                    levelTraversal.add((ArrayList<Integer>)currentLevel.clone());
                    if (nodesInTree.size() > 0){
                        nodesInTree.add(null);
                    }
                    currentLevel.clear();
                }
            }
            while(levelTraversal.size() > 0){
                levelTraversalReverse.add(levelTraversal.remove(levelTraversal.size() - 1));
            }
        }
        return levelTraversalReverse;
        
    }
	
	@SuppressWarnings("unchecked")
	public ArrayList<ArrayList<Integer>> levelOrder(TreeNode root) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ArrayList<ArrayList<Integer>> levelTraversal = new ArrayList<ArrayList<Integer>>();
        if (root != null){
            ArrayList<TreeNode> nodesInTree = new ArrayList<TreeNode>();
            nodesInTree.add(root);
            nodesInTree.add(null);
            ArrayList<Integer> currentLevel = new ArrayList<Integer>();;
            while ( nodesInTree.size() > 0){                
                TreeNode currentNodes = nodesInTree.remove(0);
                if (currentNodes != null){
                    currentLevel.add(currentNodes.val);
                    if (currentNodes.left != null)  nodesInTree.add(currentNodes.left);
                    if (currentNodes.right != null) nodesInTree.add(currentNodes.right);
                }else{
                    levelTraversal.add((ArrayList<Integer>)currentLevel.clone());
                    if (nodesInTree.size() > 0){
                        nodesInTree.add(null);
                    }
                    currentLevel.clear();
                }
            }
        }
        return levelTraversal;
    }
	@SuppressWarnings("unchecked")
	public ArrayList<ArrayList<Integer>> zigzagLevelOrder(TreeNode root){
		ArrayList<ArrayList<Integer>> zigzagLevelTraversal = new ArrayList<ArrayList<Integer>>();
		if (root == null)	return zigzagLevelTraversal;
		else{
			ArrayList<TreeNode>	nodesInTree = new ArrayList<TreeNode>();
			ArrayList<Integer> currentLevel = new ArrayList<Integer>();
			nodesInTree.add(root);
			nodesInTree.add(null);
			while(nodesInTree.size() > 0){
				TreeNode currentNode = nodesInTree.remove(0);
				
				if (currentNode != null){
					currentLevel.add(currentNode.val);
					if (currentNode.left != null)	nodesInTree.add(currentNode.left);
					if (currentNode.right != null)	nodesInTree.add(currentNode.right);
				}else{
					if (zigzagLevelTraversal.size() % 2 == 0){
						zigzagLevelTraversal.add((ArrayList<Integer>) currentLevel.clone());
					}else{
						ArrayList<Integer> reverseCurrentLevel = new ArrayList<Integer>();
						for (int index = currentLevel.size() - 1; index >= 0; index--){
							reverseCurrentLevel.add(currentLevel.get(index));
						}
						zigzagLevelTraversal.add(reverseCurrentLevel);
					}
					currentLevel.clear();
					if (nodesInTree.size() > 0)	nodesInTree.add(null);
				}
			}
			return zigzagLevelTraversal;
		}
	}
	public int maxPathSum(TreeNode root) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (root == null)   return 0;
        else{
        	int[] maxSum = new int[1];
        	maxSum[0] = Integer.MIN_VALUE;
            findSum(root, maxSum);
            return maxSum[0];
        }
    }
	private int findSum(TreeNode root, int[] maxSum){
		if ( root == null)  return 0;
		else{
			int localSum = root.val;
			int leftSum = findSum(root.left, maxSum);
			int rightSum = findSum(root.right, maxSum);
			if (leftSum > 0)    localSum += leftSum;
			if (rightSum > 0)   localSum += rightSum;
			if (localSum > maxSum[0])  maxSum[0] = localSum;
			if (Math.max(leftSum, rightSum) > 0){
				return root.val + Math.max(leftSum, rightSum);
			}
	        else    return root.val;
		}
	}
}
