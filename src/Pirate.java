/**
 * 
 * Pirate.java
 * Dec 18, 2012
 */

/**
 * @author huangsp
 *
 */
class Node{
	int val;
	Node next;
	public Node(int val){
		this.val = val;
	}
}
public class Pirate {
	public Pirate(int n){
		Node head = new Node(1);
		Node current = head;
		for (int index = 2; index <= n; index++){
			current.next = new Node(index);
			current = current.next;
		}
		current.next = head;
		current = head;
		while ( current.next != current){
			current.next = current.next.next;
			current = current.next;
		}
		System.out.println(current.val);
	}
	public static void main(String[] args){
		new Pirate(100);
	}
}
