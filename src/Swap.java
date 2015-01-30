

/**
 * 
 * Swap.java
 * Feb 4, 2013
 */

/**
 * @author huangsp
 *
 */
public class Swap {
	public ListNode LinkedList(int[] data){
		if (data.length == 1)	return new ListNode(data[0]);
		else{
			ListNode head = new ListNode(data[0]);
			ListNode current = head;
			int len = data.length;
			for (int index = 1; index < len; index++){
				current.next = new ListNode(data[index]);
				current = current.next;
			}
			return head;
		}
	}
	public ListNode swap(ListNode head){
		ListNode newHead = new ListNode(Integer.MIN_VALUE);
		newHead.next = head;
		ListNode pointer = newHead;
		while (pointer.next != null && pointer.next.next != null){
			ListNode tmp1 = pointer.next;
			ListNode tmp2 = tmp1.next;
			ListNode tmp3 = tmp2.next;
			pointer.next = tmp2;
			tmp2.next = tmp1;
			tmp1.next = tmp3;
			pointer = tmp1;
		}
		head = newHead.next;
		return head;
	}
	public ListNode swap(ListNode head, int k){
		if ( k == 1 || head == null || head.next == null)	return head;
		else{
			ListNode newHead = new ListNode(Integer.MIN_VALUE);
			newHead.next = head;
			ListNode pHead = newHead;
			ListNode pNext = newHead.next;
			ListNode pointer = newHead;
			int count = k;
			while(true){
				pHead = pointer;
				pNext = pHead;
				count = k;
				while(count > 0 && pNext.next != null){
					pNext = pNext.next;
					count --;
				}
				if (count > 0){
					break;
				}else{
					ListNode next = pNext.next;
					pNext.next = null;
					pointer.next = reverse(pHead.next);
					while (pointer.next != null){
						pointer = pointer.next;
					}
					pointer.next = next;
				}
			}
			head = newHead.next;
			return head;
		}
	}
	private ListNode reverse(ListNode head){
		if (head == null || head.next == null)	return head;
		else{
			ListNode previous = null;
			ListNode next = head.next;
			ListNode current = head;
			while(current.next != null){
				next = current.next;
				current.next = previous;
				previous = current;
				current = next;
			}
			current.next = previous;
			return current;
		}
	}
	public static void main(String[] args){
		int[] data = {1,2,3,4,5,6,7,8,9};
		Swap myObject = new Swap();
		ListNode head = myObject.LinkedList(data);
		head = myObject.swap(head, 3);
	}
}
