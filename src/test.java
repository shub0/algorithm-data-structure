import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Stack;
/**
 * 
 * test.java
 * Nov 27, 2012
 */
	
/**
 * @author huangsp
 *
 */
public class test {
	public ListNode swapNode(ListNode head, int n){
		ListNode newHead = new ListNode(Integer.MIN_VALUE);
		newHead.next = head;
		ListNode pointer = newHead;
		int count = n;
		while(pointer.next != null){
			count = n;
			ListNode pointer1 = pointer;
			while(pointer1 != null && count > 0){
				pointer1 = pointer1.next;
				count --;
			}
			if (pointer1 == null)	break;
			ListNode split2 = pointer1.next;
			pointer1.next = null;
			pointer.next = reverse(pointer.next);
			while(pointer.next != null){
				pointer = pointer.next;
			}
			pointer.next = split2;		
		}
		return newHead.next;
	}
	private ListNode reverse(ListNode head){
		ListNode previous = null;
		ListNode current = head;
		ListNode next = head.next;
		while(current.next != null){
			next = current.next;
			current.next = previous;
			previous = current;
			current = next;
		}
		current.next = previous;
		return current;
	}
	private void print(ListNode head){
		while(head != null){
			System.out.printf("%d  ", head.val);
			head = head.next;
		}
	}
	public ArrayList<String> generateParenthesis(int n) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int size = 2 * n;
        ArrayList<String> list = new ArrayList<String>();
        StringBuffer aSolution = new StringBuffer();
        generateParenthesis(list, aSolution, size, 0);
        return list;
    }
    private void generateParenthesis(ArrayList<String> list, StringBuffer aSolution, int size, int count){
        if (aSolution.length() == size && count == 0){
            list.add(aSolution.toString());
        }else if (aSolution.length() == size)   return;
        else{
            if (count > 0){
            	int len = aSolution.length();
                aSolution.append(")");
                generateParenthesis(list, aSolution, size, count - 1);
                aSolution.setLength(len);
            }
            aSolution.append("(");
            generateParenthesis(list, aSolution, size, count + 1);
        }
    }
    public static void main(String[] args){
    	test myTest = new test();
    	/*ListNode head = new ListNode(1);
    	ListNode pointer = head;
    	for (int index = 2; index < 10; index ++){
    		pointer.next = new ListNode(index);
    		pointer = pointer.next;
    	}
    	myTest.print(myTest.swapNode(head, 4));*/
    	System.out.println(myTest.generateParenthesis(3));
    }
}
