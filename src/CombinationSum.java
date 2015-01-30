/**
 * 
 * CombinationSum.java
 * Nov 25, 2012
 */
import java.util.*;
/**
 * @author Shubo Liu
 *
 */
public class CombinationSum {
	HashSet<ArrayList<Integer>> solutionSet;
	public ArrayList<ArrayList<Integer>> combinationSum(int[] candidates, int target) {
        // Start typing your Java solution below
        // DO NOT write main() function
       	solutionSet = new HashSet<ArrayList<Integer>>();
       	ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
        if (candidates.length == 0) return list;
        else{
        	Arrays.sort(candidates);
            ArrayList<Integer> solution = new ArrayList<Integer>();
            /*
            for (int index = 0; index < candidates.length; index++){
                solution.add(candidates[index]);
                if (findCombinationSum(candidates, solution, index, target - candidates[index])){
                	ArrayList<Integer> aSolution = new ArrayList<Integer>();
                	aSolution.addAll(solution);
                    solutionSet.add(aSolution);
                }
                solution.remove(solution.size() - 1);
            }*/
            findCombinationSum(candidates, solution, 0, target);
            //findCombinationSum(candidates, solution, 0, target);
            for (ArrayList<Integer> example : solutionSet)
            	list.add(example);
            return list;
        }
    }
    @SuppressWarnings("unchecked")
	private boolean findCombinationSum(int[] candidates, ArrayList<Integer> solution, 
                int startIndex, int target){
        if (target == 0) return true;
        else if (target < candidates[startIndex]) return false;
        else{
        	//if (startIndex == candidates.length - 1) return false;
            for (int index = startIndex; index < candidates.length; index++){
                solution.add(candidates[index]);
                if (findCombinationSum(candidates, solution, index, target - candidates[index])){
                	
                    solutionSet.add((ArrayList<Integer>) solution.clone());
                }
                solution.remove(solution.size() - 1);
            }
            return false;
        }
    }
    public ArrayList<ArrayList<Integer>> combinationSum2(int[] candidates, int target){
    	ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
    	if (candidates.length < 1) return list;
    	else{
    		Arrays.sort(candidates);
    		solutionSet = new HashSet<ArrayList<Integer>>();
    		ArrayList<Integer> aSolution = new ArrayList<Integer>();
    		findCombination(candidates, 0, target, aSolution);
    		for (ArrayList<Integer> ex: solutionSet)
    			list.add(ex);
    		return list;
    	}
    }
    @SuppressWarnings("unchecked")
	private boolean findCombination(int[] candidates, int startPos, int target, ArrayList<Integer> aSolution){
    	if (target == 0) return true;
    	else if (target < candidates[startPos]) return false;
    	else if(startPos == candidates.length - 1) return false;
    	else{
    		for (int index = startPos; index < candidates.length; index++){
    			aSolution.add(candidates[index]);
    			if (findCombination(candidates, index + 1, target - candidates[index], aSolution)){
    				solutionSet.add((ArrayList<Integer>) aSolution.clone());
    			}
    			aSolution.remove(aSolution.size() - 1);
    		}
    		return false;
    	}
    }
    public void doCombination(int[] data, int T){
    	doCombination(data, new ArrayList<Integer>(), 0, 3);
    }
    private void doCombination(int[] data, ArrayList<Integer> solution, int start, int T){
    	if(solution.size() == T)	System.out.println(solution);
    	else if(start == data.length)	return;
    	else{
    		solution.add(data[start]);
    		doCombination(data, solution, start + 1, T);
    		solution.remove(solution.size() - 1);
    		doCombination(data, solution, start + 1, T);
    	}
    }
    public void doPermutation(int[] data, int T){
    	doPermutation(data, new ArrayList<Integer>(), new boolean[data.length], 3);   	
    }
    private void doPermutation(int[] data, ArrayList<Integer> solution, boolean[] visited, int T){
    	if (solution.size() == T)	System.out.println(solution);
    	else{
    		for (int index = 0; index < data.length; index ++){
    			if(!visited[index]){
    				solution.add(data[index]);
    				visited[index] = true;
    				doPermutation(data, solution, visited, T);
    				solution.remove(solution.size() - 1);
    				visited[index] = false;
    			}
    		}
    	}
    }
    public static void main(String[] args){
    	int[] data = {10,2,7,6};
    	new CombinationSum().doPermutation(data,3);
    }
}
