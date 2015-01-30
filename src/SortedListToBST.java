/**
 * 
 * sortedListToBST.java
 * Dec 19, 2012
 */

/**
 * @author huangsp
 *
 */
public class SortedListToBST {
	private TreeNode sortedListToBST(ListNode head, int len) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (len == 0)   return null;
        else if (len == 1)	return new TreeNode(head.val);
        else{
            int leftLength = len / 2;
            ListNode leftHead = head;
            ListNode leftTail = getNode(head, leftLength - 1);         
            ListNode center = leftTail.next;
            leftTail.next = null;
            ListNode rightHead = center.next;
            center.next = null;
            TreeNode root = new TreeNode(center.val);
            root.left = sortedListToBST(leftHead, leftLength);
            root.right = sortedListToBST(rightHead, len - 1 - leftLength);
            return root;
        }
    }
	public TreeNode sortedListToBST(ListNode head){
		int len = listLength(head);
		return sortedListToBST(head, len);
	}
    private ListNode getNode(ListNode head, int index){
        if (index == 0) return head;
        else{
            int countIndex = 0;
            ListNode current = head;
            while(countIndex < index){
                current = current.next;
                countIndex++;
            }
            return current;
        }
    }
    private int listLength(ListNode head){
        if (head == null)   return 0;
        else{
            int len = 1;
            ListNode current = head;
            while(current.next != null){
                len++;
                current = current.next;
            }
            return len;
        }
    }
    public static void main(String[] args){
    	ListNode head = new ListNode(1);
    	ListNode current = head;
    	for (int index = 2; index < 9; index++){
    		current.next = new ListNode(index);
    		current = current.next;
    	}
    	TreeNode root = new SortedListToBST().sortedListToBST(head);
    	//System.out.println(root);
    	UniqueBST printer = new UniqueBST();
    	printer.treePrintLevel(root);
    }
}
