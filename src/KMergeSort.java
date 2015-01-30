/**
 * 
 * KMergeSort.java
 * Nov 28, 2012
 */
import java.util.*;
/**
 * @author Shubo Liu
 * K external merge sort
 * Algorithm complexity is O(NlogK) for time and O(k) for space
 */
public class KMergeSort {
	public ListNode mergeKLists(ArrayList<ListNode> lists) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (lists.size() == 1) return lists.get(0);
        else{
        	ListNode sentinel = new ListNode(0);
        	ListNode pointer = sentinel;
        	int size = lists.size();
        	ListNode[] heap = new ListNode[size];
        	int i = 0;
        	for (int index = 0; index < lists.size(); index++){
        		if (lists.get(index) == null) size --;
        		else{
        			heap[i] = lists.get(index);
        			i++;
        		}
        	}
        	buildHeap(heap, size);
        	while(size > 0){
        		ListNode minNode = heap[0];
        		pointer.next = minNode;
        		if (minNode.next != null){
        			heap[0] = minNode.next;
        			heapIFY(heap, 0, size);
        		}else{
        			heap[0] = heap[size - 1];
        			size --;
        			heapIFY(heap, 0 , size);
        		}
        		pointer = pointer.next;
        	}
        	return sentinel.next;
        }
    }
	private void heapIFY(ListNode[] heap, int index, int size){
		int leftChild = 2 * (index + 1) - 1;
		int rightChild = 2 * (index + 1);
		int next = index;
		if ((leftChild < size) && (heap[leftChild].val < heap[index].val))
			next = leftChild;
		if ((rightChild < size) && (heap[rightChild].val < heap[next].val))
			next = rightChild;
		if (next == index) return;
		ListNode tmp = heap[next];
		heap[next] = heap[index];
		heap[index] = tmp;
		heapIFY(heap, next, size);
	}
	private void buildHeap(ListNode[] heap, int size){
		for (int index = size / 2; index >= 0; index--){
			heapIFY(heap, index, size);
		}
	}
	// build a test case
	public static void main(String[] args){
		ListNode head1 = new ListNode(-1);
		head1.next = new ListNode(1);
		//head1.next.next = new ListNode(7);
		ListNode head2 = new ListNode(-3);
		head2.next = new ListNode(1);
		head2.next.next = new ListNode(4);
		ListNode head3 = new ListNode(-2);
		head3.next = new ListNode(-1);
		head3.next.next = new ListNode(0);
		ArrayList<ListNode> lists = new ArrayList<ListNode>();
		lists.add(head1);
		lists.add(head2);
		lists.add(head3);
		ListNode mergeList = new KMergeSort().mergeKLists(lists);
		System.out.println(mergeList.val);
	}
}
