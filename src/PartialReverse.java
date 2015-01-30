

/**
 * 
 * PartialReverse.java
 * Feb 6, 2013
 */

/**
 * @author huangsp
 *
 */
public class PartialReverse {
	public void partialReverse(ListNode head, int startPos, int endPos){
		if (startPos >= endPos) return;
		else{
			int index = 0;
			ListNode previous = null;
			ListNode current = head;
			ListNode next = head.next;
			while (index < startPos){
				previous = current;
				current = next;
				next = current.next;
				index++;
			}
			// record split position
			ListNode pos1 = previous;
			ListNode pos2 = current;
			while (index <= endPos){
				next = current.next;
				current.next = previous;
				previous = current;
				current = next;
				index++;
			}
			if (startPos == 0){
				head = previous;
			}else
				pos1.next = previous;
			pos2.next = next;
		}
	}
}
