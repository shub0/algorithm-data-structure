import java.util.ArrayList;

/**
 * 
 * Triangle.java
 * Dec 6, 2012
 */

/**
 * @author huangsp
 *
 */
public class Triangle {
	public int minimumTotal(ArrayList<ArrayList<Integer>> triangle) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (triangle.size() == 0)   return 0;
        else if (triangle.size() == 1)   return triangle.get(0).get(0);
        else{
            int row = triangle.size();
            ArrayList<Integer> prevSum = triangle.get(0);
            for (int index = 1; index < row; index++){
                ArrayList<Integer> currentSum = new ArrayList<Integer>();
                ArrayList<Integer> currentData = triangle.get(index);
                currentSum.add(prevSum.get(0) + currentData.get(0));
                for (int index2 = 1; index2 < triangle.get(index).size() - 1; index2++){
                    int min = Math.min(prevSum.get(index2 - 1), prevSum.get(index2));
                    currentSum.add(currentData.get(index2) + min);
                }
                currentSum.add(prevSum.get(prevSum.size() - 1) + currentData.get(currentData.size() - 1));
                prevSum = currentSum;
            }
            int min = prevSum.get(0);
            for (int index = 0; index < prevSum.size(); index++){
                if (min > prevSum.get(index))    min = prevSum.get(index);
            }
            return min;
        }
    }
	public static void main(String[] arrays){
		ArrayList<Integer> list1 = new ArrayList<Integer>();
		list1.add(-1);
		ArrayList<Integer> list2 = new ArrayList<Integer>();
		list2.add(2);
		list2.add(3);
		ArrayList<Integer> list3 = new ArrayList<Integer>();
		list3.add(1);
		list3.add(-1);
		list3.add(-1);
		ArrayList<ArrayList<Integer>> triangle = new ArrayList<ArrayList<Integer>>();
		triangle.add(list1);
		triangle.add(list2);
		triangle.add(list3);
		System.out.println(new Triangle().minimumTotal(triangle));
	}
}
