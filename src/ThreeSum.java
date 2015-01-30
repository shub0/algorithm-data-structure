/**
 * 
 * ThreeSum.java
 * Nov 22, 2012
 */
import java.util.*;
/**
 * @author huangsp
 *
 */
public class ThreeSum {
	/*public ArrayList<ArrayList<Integer>> threeSum(int[] num) {
        // Start typing your Java solution below
        // DO NOT write main() function
        Arrays.sort(num);
       
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        int len = num.length;
        if (len < 3) return new ArrayList<ArrayList<Integer>>();
        for (int index1 = 0; index1 < len; index1++){
        	int index3 = len - 1;
        	int index2 = index1 + 1;
            while(index2 < index3){
                int sum = num[index1] + num[index2] + num[index3];
                if (sum > 0) index3 --;
                else if (sum < 0) index2 ++;
                else{
                	ArrayList<Integer> list = new ArrayList<Integer>();
                	list.add(num[index1]);
            		list.add(num[index2]);
            		list.add(num[index3]);
            		// remove duplicate
                	if (result.size() == 0){
                		result.add(list);
                	}else{
                		  boolean flag = false;
                          for (int index = 0; index < result.size(); index++){
                              ArrayList<Integer> previousList = result.get(index);
                              if (num[index1] == previousList.get(0) && 
                  				num[index2] == previousList.get(1)  && num[index3] == previousList.get(2))
                      			{
                                  flag = true; 
                                  break; 
                      			}
                          }
                  		if (!flag)
                  			result.add(list);
                	}
                	index2++;
                }
            }
        }
        return result;
    }*/
    
	@SuppressWarnings("unchecked")
	public ArrayList<ArrayList<Integer>> threeSum(int[] num) {
        // Start typing your Java solution below
        // DO NOT write main() function
        Arrays.sort(num);
       
        Set<ArrayList<Integer>> resultSet = new HashSet<ArrayList<Integer>>();
        int len = num.length;
        if (len < 3) return new ArrayList<ArrayList<Integer>>();
        for (int index1 = 0; index1 < len; index1++){
            int index3 = len - 1;
        	int index2 = index1 + 1;
            while(index2 < index3){
                int sum = num[index1] + num[index2] + num[index3];
                if (sum > 0) index3 --;
                else if (sum < 0) index2 ++;
                else{
                	ArrayList<Integer> list = new ArrayList<Integer>();
                	list.add(num[index1]);
            		list.add(num[index2]);
            		list.add(num[index3]);
            		// remove duplicate
                	resultSet.add((ArrayList<Integer>)list.clone());
                	index2++;
                }        
            }
        }
        
    	ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
    	for (ArrayList<Integer> ex: resultSet){
            result.add(ex);
    	}
        return result;
    }
	public int[] twoSum(int[] numbers, int target) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int len = numbers.length;
        int[] copy = new int[len];
        for (int index = 0; index < len; index++){
            copy[index] = numbers[index];
        }
        Arrays.sort(copy);
        int left = 0;
        int right = len - 1;
        while (left < right){
            int sum = copy[left] + copy[right];
            if (sum == target)  break;
            else if (sum > target)  right --;
            else left ++;
        }
        int[] indices = new int[2];
        for (int index = 0; index < len; index ++){
            if (copy[left] == numbers[index] && indices[0] == 0){
                indices[0] = index + 1;
            }
            else if (copy[right] == numbers[index] && indices[1] == 0)  indices[1] = index + 1;
        }
        Arrays.sort(indices);
        return indices;
    }
	
	public ArrayList<ArrayList<Integer>> fourSum(int[] num, int target){
		ArrayList<ArrayList<Integer>> solutionList = new ArrayList<ArrayList<Integer>>();
        int len = num.length;
        if (len < 4)    return solutionList;
        else{
            HashSet<ArrayList<Integer>> solutionSet = new HashSet<ArrayList<Integer>>();
            int outerLeft = 0;
            int outerRight = len - 1;
            Arrays.sort(num);
            while(outerLeft < outerRight - 2){
                int innerLeft = outerLeft + 1;
                int innerRight = outerRight - 1;
                int bestSum = num[outerLeft] + num[innerLeft] 
                        + num[innerRight] + num[outerRight];
                while (innerLeft < innerRight){
                    int sum = num[outerLeft] + num[innerLeft] 
                        + num[innerRight] + num[outerRight];
                    if (Math.abs(sum - target) < Math.abs(bestSum - target)){
                        bestSum = sum;
                    }
                    if (sum == target){
                        ArrayList<Integer> solution = new ArrayList<Integer>();
                        solution.add(num[outerLeft]);
                        solution.add(num[innerLeft]);
                        solution.add(num[innerRight]);
                        solution.add(num[outerRight]);
                        innerLeft ++;
                        solutionSet.add(solution);
                    }else if(sum < target){
                        innerLeft ++;
                    }else{
                        innerRight --;
                    }
                }
                if (bestSum <= target){
                    outerLeft ++;
                }else{
                    outerRight --;
                }
            }
            for (ArrayList<Integer> ex: solutionSet){
                solutionList.add(ex);
            }
            return solutionList;
        }
	}
	public static void main(String[] args){
    	int[] data = {-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6};
    	//ArrayList<ArrayList<Integer>> result = new ThreeSum().fourSum(data, 0);
    	ArrayList<ArrayList<Integer>> result = new ThreeSum().threeSum(data);
    	System.out.println(result);
    }
}
