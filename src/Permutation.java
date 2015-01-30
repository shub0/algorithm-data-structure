import java.util.ArrayList;
import java.util.HashSet;

/**
 * 
 * Permutation.java
 * Dec 1, 2012
 */

/**
 * @author huangsp
 *
 */
public class Permutation {
	ArrayList<ArrayList<Integer>> solution = new ArrayList<ArrayList<Integer>>();
	HashSet<ArrayList<Integer>> solutionSet = new HashSet<ArrayList<Integer>>();
	public ArrayList<ArrayList<Integer>> permutation(int[] num){
		if (num.length == 0) return solution;
		else{
			boolean[] isUsed = new boolean[num.length];
			doPermutation(num, new ArrayList<Integer>(), isUsed);
			for (ArrayList<Integer> ex : solutionSet)
				solution.add(ex);
			return solution;
		}
	}
	@SuppressWarnings("unchecked")
	private void doPermutation(int[] num, ArrayList<Integer> aSolution, boolean[] isUsed){
		if (num.length == aSolution.size()){
			solutionSet.add((ArrayList<Integer>) aSolution.clone());
		}else{
			for (int index = 0; index < num.length; index++){
				if (!isUsed[index]){
					isUsed[index] = true;
					aSolution.add(num[index]);
					doPermutation(num, aSolution, isUsed);
					aSolution.remove(aSolution.size() - 1);
					isUsed[index] = false;
				}
			}
		}
	}
	public static void main(String[] args){
		int[] num = {1,2,2};
		System.out.println(new Permutation().permutation(num));
	}
}
