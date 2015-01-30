/**
 * 
 * LinkedSibling.java
 * Dec 2, 2012
 */

/**
 * @author huangsp
 *
 */
class TreeLinkNode{
	int val;
	TreeLinkNode left;
	TreeLinkNode right;
	TreeLinkNode next;
	TreeLinkNode(int val){
		this.val = val;
		left = null;
		right = null;
		next = null;
	}
	public String toString(){
		return val + "";
	}
}
public class LinkedSibling {
	// for full & balanced tree
	public void connect(TreeLinkNode root){
		if (root == null) return;
		else{
			if(root.left != null)
				root.left.next =  root.right;
			if (root.right != null){
				if (root.next != null){
					root.right.next = root.next.left;
				}else
					root.right.next = null;
			}
			connect(root.left);
			connect(root.right);
		}
	}
	// for partial unbalanced tree
	// iterative algorithm and level-wise traversal
	public void connect2(TreeLinkNode root){
		// firstNode is the first node of each level
		TreeLinkNode firstNode = root;
		while (firstNode != null){
			root = firstNode;
			// arrive at the end of current level
			while(root != null){
				if (root.left != null && root.right != null){
					root.left.next = root.right;
					root.right.next = nextNode(root.next);
				}else if (root.left != null ){
					root.left.next = nextNode(root.next);
				}else if (root.right != null){
					root.right.next = nextNode(root.next);
				}
				root = root.next;
			}
			// visit next level
			firstNode = nextNode(firstNode);
		}
	}
	
	private TreeLinkNode nextNode(TreeLinkNode root){
		if (root == null) 	return null;
		else if (root.left != null) 	return root.left;
		else if (root.right != null)	return root.right;
		else return nextNode(root.next);
	}
	public static void main(String[] args){
		TreeLinkNode node1 = new TreeLinkNode(2);
		TreeLinkNode node2 = new TreeLinkNode(1);
		TreeLinkNode node3 = new TreeLinkNode(3);
		TreeLinkNode node4 = new TreeLinkNode(0);
		TreeLinkNode node5 = new TreeLinkNode(7);
		TreeLinkNode node6 = new TreeLinkNode(9);
		TreeLinkNode node7 = new TreeLinkNode(1);
		TreeLinkNode node8 = new TreeLinkNode(2);
		TreeLinkNode node9 = new TreeLinkNode(1);
		TreeLinkNode node10 = new TreeLinkNode(0);
		TreeLinkNode node11 = new TreeLinkNode(8);
		TreeLinkNode node12 = new TreeLinkNode(8);
		TreeLinkNode node13 = new TreeLinkNode(7);
		
		node1.left = node2;
		node1.right = node3;
		node2.left = node4;
		node2.right = node5;
		//node2.right = node6;
		node3.left = node6;
		node3.right = node7;
		
		node4.left = node8;
		node5.left = node9;
		node5.right = node10;
		node7.left = node11;
		node7.right = node12;
		node10.right = node13;
		//node6.right = node10;
		LinkedSibling myProblem = new LinkedSibling();
		myProblem.connect2(node1);
		System.out.println(node1);
	}
}
