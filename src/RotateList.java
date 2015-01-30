/**
 * 
 * RotateList.java
 * Dec 4, 2012
 */

/**
 * @author Shubo Liu
 *
 */
public class RotateList {
	public ListNode reverse(ListNode head){
		if (head == null || head.next == null) return head;
		else{
			ListNode previous = null;
			ListNode current = head;
			ListNode next = head.next;
			while (current.next != null){
				next = current.next;
				current.next = previous;
				previous = current;
				current = next;
			}
			current.next = previous;
			return current;
		}
	}
	public ListNode rotate(ListNode head, int n){
		 if (head == null || n == 0) return head;
	        else{
	            ListNode pointer1 = head;
	            ListNode pointer2 = head;
	            while(n > 0){
	            	if (pointer1.next != null)		pointer1 = pointer1.next;
	            	else pointer1 = head;
	                n--;
	            }
	            if (pointer1 == null)  return head;
	            else{
	                while(pointer1.next != null){
	                    pointer1 = pointer1.next;
	                    pointer2 = pointer2.next;
	                }
	                pointer1.next = head;
	                ListNode newHead = pointer2.next;
	                pointer2.next = null;
	                return newHead;
	            }
	        }
		
	}
	// rotate list from index m to index n (not 0 base index)
	public ListNode rotateList(ListNode head, int m, int n){
		if (head == null || m >= n)		return head;
		else{
			int index = 1;
			ListNode previous = null;
			ListNode current  = head;
			ListNode next = head.next;
			while(index < m){
				previous = current;
				current = next;
				next = current.next;
				index ++;
			}
			ListNode pos1 = previous;
			ListNode pos2 = current;
			while(index <= n){
				next = current.next;
				current.next = previous;
				previous = current;
				current = next;
				index ++;
			}
			if (m == 1)	head = previous;
			else	{pos1.next = previous;}
			pos2.next = next;
			return head;
		}
		
	}
	public static ListNode insert(ListNode head, int val){
		ListNode current = head;
		while (current.next != null){
			current = current.next;
		}
		current.next = new ListNode(val);
		return head;
	}
	private static void print(ListNode head){
		while(head != null){
			System.out.printf("%d   ", head.val);
			head = head.next;
		}
	}
	public static void main(String[] args){
		ListNode head = new ListNode(1);
		for (int index = 2; index < 12; index++)
			head = insert(head, index);
		ListNode newHead = new RotateList().rotateList(head, 1,11);
		print(newHead);
	}
}
