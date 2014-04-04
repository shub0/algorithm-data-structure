
public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null) {
        	return l2;
        } else if (l2 == null) {
        	return l1;
        } else {
        	int sum = l1.val + l2.val;
        	ListNode head = new ListNode(sum % 10);
        	ListNode pointer = head;
        	int carry = sum / 10;
        	while (l1.next != null | l2.next != null) {
        		sum = carry;
        		if (l1.next != null) {
        			sum += l1.next.val;
        			l1 = l1.next;
        		}
        		if (l2.next != null) {
        			sum += l2.next.val;
        			l2 = l2.next;
        		}
        		pointer.next = new ListNode(sum % 10);
        		carry = sum / 10;
        		pointer = pointer.next;
        	}
        	if (carry != 0) {
        		pointer.next = new ListNode(carry);
        	}
        	return head;
        }
    }
    public static void main(String[] args){
        ListNode l1 = new ListNode(5);
        l1.next = new ListNode(1);
        ListNode l2 = new ListNode(0);
        ListNode.print(new AddTwoNumbers().addTwoNumbers(l1, l2));
    }
}