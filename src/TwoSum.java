import java.util.Arrays;


public class TwoSum {
	public static int[] twoSum(int[] numbers, int target) {
		int[] indices = {0,0};
        if (numbers == null || numbers.length < 2) {
        	return indices;
        } else {
        	int left = 0;
        	int right = numbers.length - 1;
        	Arrays.sort(numbers);
        	while (left < right) {
        		if ((numbers[left] + numbers[right]) > target) {
        			right --;
        		} else if ((numbers[left] + numbers[right]) < target) {
        			left ++;
        		} else {
        			indices[0] = left + 1;
        			indices[1] = right + 1;
        			break;
        		}
        	}
        	return indices;
        }
    }
	
	public static void main(String[] args){
		int[] numbers = {2,7,11,13};
		System.out.println(Arrays.toString(twoSum(numbers,15)));
	}

}
