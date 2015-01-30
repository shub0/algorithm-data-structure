/**
 * 
 * AddInt.java
 * Nov 22, 2012
 */

/**
 * @author huangsp
 *
 */
class ListNode {
   int val;
   ListNode next;
   ListNode(int x) {
	   val = x;
	   next = null;
   }
   public String toString(){
	   return val+"";
   }
}
public class AddInt {
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Start typing your Java solution below
        // DO NOT write main() function
		if (l1 == null) return l2;
		else if (l2 == null) return l1;
		else{
			int sum = l1.val + l2.val;
			ListNode head = new ListNode(sum % 10);
			ListNode pointer = head;
			int carry = sum / 10;
			while (l1.next != null || l2.next != null){
				sum = carry;
				if (l1.next != null){
					l1 = l1.next;
					sum += l1.val;
				}
				if (l2.next != null){
					l2 = l2.next;
					sum += l2.val;
				}
				pointer.next = new ListNode(sum % 10);
				carry = sum / 10;
				pointer = pointer.next;
			}
			if (carry != 0){
				pointer.next = new ListNode(carry);
			}
			return head;
		}
    }
	public static void print(ListNode head){
		ListNode current = head;
		while (current.next != null){
			System.out.printf("%d", current.val);
			current = current.next;
		}
		System.out.printf("%d", current.val);
	}
	public static void main(String[] args){
		ListNode l1 = new ListNode(5);
		l1.next = new ListNode(1);
		ListNode l2 = new ListNode(9);
		print(new AddInt().addTwoNumbers(l1, l2));
	}
}
