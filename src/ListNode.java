/**
 * Definition for singly-linked list.
 */
public class ListNode {
	int val;
	ListNode next;

	ListNode(int x) {
		val = x;
		next = null;
	}
	public static void print(ListNode head){
        ListNode current = head;
        while (current.next != null){
            System.out.printf("%d", current.val);
            current = current.next;
        }
        System.out.printf("%d", current.val);
	}
}