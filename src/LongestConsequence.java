/**
 * 
 * LongestConsequence.java
 * Mar 23, 2013
 */
import java.util.HashMap;
/**
 * @author huangsp
 *
 */
public class LongestConsequence {
	public int findLongestConsequence(int[] data){
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();	// HashMap<digit, length>
		int max = 0;
		for (int ex : data){
			if (map.containsKey(ex))	continue;
			map.put(ex, 1);
			if (map.containsKey(ex - 1)) max = Math.max(max, merge(map, ex - 1, ex));
			if (map.containsKey(ex + 1)) max = Math.max(max, merge(map, ex, ex + 1));
		}
		return max;
	}
	private int merge(HashMap<Integer, Integer> map, int left, int right){
		int upper = right + map.get(right) - 1;
		int lower = left - map.get(left) + 1;
		int len = upper - lower + 1;
		map.put(upper, len);
		map.put(lower, len);
		return len;
	}
	public static void main(String[] args){
		LongestConsequence myTest = new LongestConsequence();
		int[] data = {200,1,201,2,202,3,100,4};
		System.out.println(myTest.findLongestConsequence(data));
	}
}
