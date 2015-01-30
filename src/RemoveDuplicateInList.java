/**
 * 
 * RemoveDuplicateInList.java
 * Jan 30, 2013
 */

/**
 * @author huangsp
 *
 */
public class RemoveDuplicateInList {
	public ListNode deleteDuplicates(ListNode head) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (head == null || head.next == null)  return head;
        else{
            ListNode newHead = new ListNode(Integer.MIN_VALUE);
            newHead.next = head;
            ListNode pointer = newHead;
            while (pointer.next != null){
                int currentVal = pointer.next.val;
                if (pointer.next.next != null && currentVal == pointer.next.next.val){
                    ListNode pointer2 = pointer;
                    while (pointer2.next != null && pointer2.next.val == currentVal){
                        pointer2 = pointer2.next;
                    }
                    pointer.next = pointer2.next;
                }else{
                    pointer = pointer.next;
                }     
            }
            return newHead.next;
        }
    }
	
	public ListNode deleteDuplicates2(ListNode head) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (head == null || head.next == null)  return head;
        else{
            ListNode newHead = new ListNode(Integer.MIN_VALUE);
            newHead.next = head;
            ListNode pointer = newHead;
            while (pointer.next != null){
                if (pointer.next != null && pointer.val == pointer.next.val){
                    pointer.next = pointer.next.next;
                }else{
                	pointer = pointer.next;
                }
            }
            return newHead.next;
        }
    }
	
	private ListNode list(int[] data){
		ListNode head = new ListNode(data[0]);
		ListNode pointer = head;
		for (int index = 1; index < data.length; index++){
			pointer.next = new ListNode(data[index]);
			pointer = pointer.next;
		}
		return head;
	}
	private void print(ListNode head){
		ListNode pointer = head;
		while (pointer != null){
			System.out.printf("%d  ", pointer.val);
			pointer = pointer.next;
		}
	}
	public static void main(String[] args){
		int[] data = {1,1,1,1};
		RemoveDuplicateInList myObject = new RemoveDuplicateInList();
		ListNode head = myObject.list(data);
		myObject.print(head);
		System.out.println();
		head = myObject.deleteDuplicates2(head);
		myObject.print(head);
	}
}
