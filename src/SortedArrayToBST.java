/**
 * 
 * SortedArrayToBST.java
 * Nov 25, 2012
 */

/**
 * @author huangsp
 *
 */
public class SortedArrayToBST {
	public TreeNode sortedArrayToBST(int[] num) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (num.length == 0) return null;
        else if (num.length == 1) return new TreeNode(num[0]);
        else{
            return buildTree(num, 0, num.length - 1);
        }
    }
    private TreeNode buildTree(int[] num, int startIndex, int endIndex){
        if (startIndex == endIndex) return new TreeNode(num[startIndex]);
        else{
            int middleIndex = (startIndex + endIndex) / 2;
            TreeNode root = new TreeNode(num[middleIndex]);
            if (middleIndex > startIndex)
                root.left = buildTree(num, startIndex, middleIndex - 1);
            if (middleIndex < endIndex)
                root.right = buildTree(num, middleIndex + 1, endIndex);
            return root;
        }
    }
    public static void main(String[] args){
		int[] inOrder = {1,2,3,4,5,6,7};
		TreeNode root2 = new SortedArrayToBST().sortedArrayToBST(inOrder);
		System.out.println(root2);
    }
}
