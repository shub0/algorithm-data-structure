import java.util.Arrays;



/**
 * 
 * SearchNum.java
 * Dec 4, 2012
 */

/**
 * @author huangsp
 *
 */
public class SearchNum {
	// search in a 2D sorted matrix
	public boolean search(int[][]matrix, int val){
		int ROW = matrix.length;
		int COL = matrix[0].length;
		int start = 0;
		int end = ROW * COL - 1;
		if (val < matrix[0][0]) return false;
		if (val > matrix[ROW - 1][COL - 1])	return false;
		while (start <= end){
			int middle = (start + end) / 2;
			int middleRow = (middle) / COL;
			int middleCol = (middle) % COL;
			if (val == matrix[middleRow][middleCol]) 	return true;
			else if(val < matrix[middleRow][middleCol])		end = middle - 1;
			else start = middle + 1;
		}
		return false;
	}
	
	// search range in a sorted array
	public int[] searchRange(int[] num, int val){
		int[] pos = new int[2];
		pos[0] = searchPos(num, val) ;
		pos[1] = searchPos(num, val + 1) - 1;
		// no appearance
		if (pos[0] >= num.length || num[pos[1]] != val){
			pos[0] = -1;
			pos[1] = -1;
		}
		System.out.println(Arrays.toString(pos));
		return pos;
	}
	
	// search in a rotate sorted vector
	public int searchInRotateVector(int[] num, int val){
		int start = 0;
		int end = num.length - 1;
		int middle = (start + end) / 2;
		while ( start <= end){
			middle = (end + start) / 2;
			if (num[middle] == val)		return middle;
			// data from start to middle are in order
			else if (num[start] < num[middle]){
				if (num[start] <= val && val < num[middle])
					end = middle - 1;
				else
					start = middle + 1;
			// data from middle to end are in order
			}else if (num[start] > num[middle]){
				if (num[middle] < val && val <= num[end])
					start = middle + 1;
				else
					end = middle - 1;
			}else{
				/*
				if (num[start] != num[end]){
					start = middle + 1;
				// A[start] == A[middle] == A[end]
				}else{
					end = middle - 1;
				}*/
				start ++;
			}
		}
		// no "val" in vector
		return -1;
	}
	
	// search pivot in a rotated sorted array
	public int searchPivot(int[] num){
		int start = 0;
		int end = num.length - 1;
		int middle = (start + end) / 2;
		while (num[start] > num[end]){
			middle = (start + end) / 2;
			if (num[end] < num[middle])		start = middle + 1;
			else end = middle;
		}
		return start;
	}
	
	// search a insert position in a sorted vector
	// if appeared in the array, find the first position
	public int searchPos(int[] num, int val){
		int start = 0;
		int end = num.length - 1;
		int pos = num.length;
		int middle = 0;
		while (start <= end){
			middle = (start + end) / 2;
			if (val > num[middle])	start = middle + 1;
			else{
				// record current position which is with data not bigger than "val"
				pos = middle;
				end = middle - 1;
			}
		}
		return pos;
	}
	
	public static void main(String[] args){
		SearchNum myTest = new SearchNum();
		int[] num = {1,2,3,3,3,3,4,5,9};
		//myTest.searchRange(num, 2);
		System.out.println(myTest.searchRange(num,3));
		//int[] num2 = {2,3,4,5,6,7,8,9,9,1,2};
		//System.out.println(myTest.searchInRotateVector(num2, 1));
		//System.out.println(myTest.searchPivot(num2));

	}
}
