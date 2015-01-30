/**
 * 
 * PartitionList.java
 * Nov 29, 2012
 */

/**
 * @author huangsp
 *
 */
public class PartitionList {
	 public ListNode partition(ListNode head, int x) {
		 if (head == null) return null;
		 if (head.next == null) return head;
		 ListNode myHead = new ListNode(0);
		 myHead.next = head;
		 ListNode current = myHead;
	
		 while (current.next != null && current.next.val < x){
			current = current.next;
		 }
		 if (current.next == null) return head;
		 ListNode current2 = current.next;
		 while ( current.next != null){
			// find a "smaller" node 
			while(current2.next != null && current2.next.val >= x)
				current2 = current2.next;
			if (current2.next == null) break;
			//insert it after "current" node
			ListNode tmp = current.next;
			current.next = current2.next;
			current2.next = current2.next.next;
			current.next.next = tmp;
			// move to next position
			current = current.next;
		}
		head = myHead.next;
		return head;
	 }
	 public ListNode test(ListNode head, int x) {
	        // Start typing your Java solution below
	        // DO NOT write main() function
	        if (head == null)   return head;
	        else if (head.next == null) return head;
	        else{
	            ListNode newHead = new ListNode(Integer.MIN_VALUE);
	            newHead.next = head;
	            ListNode pointer = newHead;
	            while(pointer.next != null && pointer.next.val < x){
	                pointer = pointer.next;
	            }
	            if (pointer.next == null)   return newHead.next;
	            else{
	                while(pointer.next != null){
	                    ListNode pointer2 = pointer;
	                    while (pointer2.next != null && pointer2.next.val >= x){
	                        pointer2 = pointer2.next;
	                    }
	                    if (pointer2.next == null)  break;
	                    else{
	                        ListNode tmp = pointer.next;
	                        pointer.next = pointer2.next;
	                        pointer2.next = pointer2.next.next;
	                        pointer.next.next = tmp;
	                        pointer = pointer.next;
	                    }
	                }
	                return newHead.next;
	            }
	        }
	    }
	 public static void main(String[] args){
		 ListNode node1 = new ListNode(2);
		 node1.next = new ListNode(1);
		 ListNode head = new PartitionList().test(node1, 2);
		 System.out.println(head);
	 }
}
