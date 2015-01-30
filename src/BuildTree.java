
class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;
	TreeNode(int x) { val = x; }
	public String toString(){
		return val + "";
	}
}

public class BuildTree {
	// use postorder sequence and inorder sequence
	public TreeNode buildTree(int[] inOrder, int[] postOrder){
		if (inOrder.length != postOrder.length || inOrder.length == 0)
			return null;
		else{
			return buildTree(inOrder, postOrder, 0, inOrder.length - 1, 0, postOrder.length - 1);
		}
	}
	public TreeNode buildTree(int[] inOrder, int[] postOrder, int inStartIndex, int inEndIndex, int postStartIndex, int postEndIndex){
		if (postStartIndex == postEndIndex){
			return new TreeNode(postOrder[postEndIndex]);
		}else{
			int index;
			TreeNode root = new TreeNode(postOrder[postEndIndex]);
			for (index = inStartIndex; index < inEndIndex; index++){
				if (inOrder[index] == postOrder[postEndIndex]){
					break;
				}
			}
			int nodesInLeftSubTree = index - inStartIndex;
			if (nodesInLeftSubTree > 0)
				root.left = buildTree(inOrder, postOrder, inStartIndex, index, postStartIndex, postStartIndex + nodesInLeftSubTree - 1);
			int nodesInRightSubTree = postEndIndex - postStartIndex - nodesInLeftSubTree;
			if (nodesInRightSubTree > 0)
				root.right = buildTree(inOrder, postOrder, index + 1, inEndIndex, postEndIndex - nodesInRightSubTree , postEndIndex - 1);
			return root;
		}
	}
	// using preorder sequence and inorder sequence
	public TreeNode buildTree2(int[] preOrder, int[] inOrder){
		if (inOrder.length != preOrder.length || inOrder.length == 0)
			return null;
		else{
			return buildTree2(preOrder, inOrder, 0, preOrder.length - 1, 0, inOrder.length - 1);
		}
	}
	private TreeNode buildTree2(int[] preOrder, int[] inOrder, int preStartIndex, int preEndIndex, int inStartIndex, int inEndIndex){
		if (preStartIndex == preEndIndex){
			return new TreeNode(preOrder[preStartIndex]);
		}
		else{
			int index = inStartIndex;
			TreeNode root = new TreeNode(preOrder[preStartIndex]);
			for (index = inStartIndex; index < inEndIndex; index++){
				if (inOrder[index] == preOrder[preStartIndex])
					break;
			}
			int nodesInLeftSubTree = index - inStartIndex;
			if (nodesInLeftSubTree > 0)
				root.left = buildTree2(preOrder, inOrder, preStartIndex + 1, preStartIndex + nodesInLeftSubTree, inStartIndex, index);
			int nodesInRightSubTree = preEndIndex - preStartIndex - nodesInLeftSubTree;
			if (nodesInRightSubTree > 0)
				root.right = buildTree2(preOrder, inOrder, preEndIndex - nodesInRightSubTree + 1, preEndIndex , index + 1, inEndIndex);
			return root;
		}
	}
	// a test case
	public static void main(String[] args){
		int[] inOrder = {1,2,3,4,5,6,7};
		int[] postOrder = {1,3,2,5,7,6,4};
		int[] preOrder = {4,2,1,3,6,5,7};
		//int[] preOrder = {1,2};
		//int[] inOrder = {2,1};
		TreeNode root = new BuildTree().buildTree(inOrder, postOrder);
		TreeNode root2 = new BuildTree().buildTree2(preOrder, inOrder);
		System.out.println(root);
		System.out.println(root2);
	}
}