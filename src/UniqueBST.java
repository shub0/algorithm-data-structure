import java.util.ArrayList;

/**
 * 
 * UniqueBST.java
 * Jan 2, 2013
 */
/**
 * @author huangsp
 *
 */
public class UniqueBST {
	public int numTrees(int n){
		int[] numOfBST = new int[n+1];
		numOfBST[0] = 1;
		numOfBST[1] = 1;
		for (int index = 2; index <= n; index++){
			for (int root = 1; root <= index; root++){
				int leftTree = root - 1;
				int rightTree = index - root;
				numOfBST[index] += numOfBST[leftTree] * numOfBST[rightTree];
			}
		}
		return numOfBST[n];
	}
	
	public ArrayList<TreeNode> generateTree(int n){
		ArrayList<TreeNode> treeList = new ArrayList<TreeNode>();
		if (n == 0)		return treeList;
		else{
			treeList = generateTree(1, n);
			return treeList;
		}
	}
	private ArrayList<TreeNode>	generateTree(int startNumber, int endNumber){
		ArrayList<TreeNode>	rootList = new ArrayList<TreeNode>();
		for (int root = startNumber ; root <= endNumber; root++){
			
			ArrayList<TreeNode> leftChildList = generateTree(startNumber, root - 1);
			ArrayList<TreeNode> rightChildList = generateTree(root + 1, endNumber);
			int leftTree = leftChildList.size();
			int rightTree = rightChildList.size();
			if (leftTree == 0 && rightTree == 0){
				TreeNode rootNode = new TreeNode(root);
				rootList.add(rootNode);
			}
			else if (leftTree == 0){
				for (int j = 0; j < rightTree; j++){
					TreeNode rootNode = new TreeNode(root);
					//TreeNode leftChild = leftChildList.get(i);
					TreeNode rightChild = rightChildList.get(j);
					//rootNode.left = leftChild;
					rootNode.right = rightChild;
					rootList.add(rootNode);
				}
			}else if (rightTree == 0){
				for (int j = 0; j < leftTree; j++){
					TreeNode rootNode = new TreeNode(root);
					TreeNode leftChild = leftChildList.get(j);
					//TreeNode rightChild = rightChildList.get(j);
					rootNode.left = leftChild;
					//rootNode.right = rightChild;
					rootList.add(rootNode);
				}
			}else{
				for (int i = 0; i < leftTree; i++){
					for (int j = 0; j < rightTree; j++){
						TreeNode rootNode = new TreeNode(root);
						TreeNode leftChild = leftChildList.get(i);
						TreeNode rightChild = rightChildList.get(j);
						rootNode.left = leftChild;
						rootNode.right = rightChild;
						rootList.add(rootNode);
					}
				}
			}
		}
		return rootList;
	}
	
	
	void treePrintLevel(TreeNode root){
		ArrayList<TreeNode> nodesInTree = new ArrayList<TreeNode>();
		int index = 0;
		TreeNode current = root;
		nodesInTree.add(current);
		nodesInTree.add(null);
		while ( index < nodesInTree.size() - 1){
			current  = nodesInTree.get(index);			
			if (current != null){
                if (current.left != null) nodesInTree.add(current.left);
                if (current.right != null) nodesInTree.add(current.right);
            }else{
            	if (index != nodesInTree.size() - 1)	nodesInTree.add(null);
            }
			index++;
		}
		System.out.println(nodesInTree);
		System.out.println("Done");
    }
	
	private void print(ArrayList<TreeNode> rootList){
		int numOfBST = rootList.size();
		for (int index = 0; index < numOfBST; index++){
			TreeNode root = rootList.get(index);
			treePrintLevel(root);
			System.out.println();
		}
	}
	public static void main(String[] args){
		//System.out.println(new test().lengthOfLastWords("Hello World"));
		//String[] A = {"c","c","c"};
		UniqueBST myTest = new UniqueBST();
		myTest.print(myTest.generateTree(3));
		
	}
}
