import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

/**
 * 
 * Subset.java
 * Dec 11, 2012
 */

/*
 * @author huangsp
 *
 */

public class Subset {
	HashSet<ArrayList<Integer>> solutionSet;
    // straight forward algorithm
    public ArrayList<ArrayList<Integer>> subsetsWithDup(int[] num) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int len = num.length;
        ArrayList<ArrayList<Integer>> solutionList = new ArrayList<ArrayList<Integer>>();
        if (len == 0)   return solutionList;
        if (len == 1){
            ArrayList<Integer> solution = new ArrayList<Integer>();
            solution.add(num[0]);
            solutionList.add(solution);
            return solutionList;
        }
        else{
        	Arrays.sort(num);
        	solutionSet = new HashSet<ArrayList<Integer>>();
            for (int numOfElement = 1; numOfElement <= len; numOfElement ++){
            	ArrayList<Integer> solution = new ArrayList<Integer>();
                subsetWithDup(num, 0, numOfElement, solution);
            }
            for (ArrayList<Integer> ex: solutionSet){
                solutionList.add(ex);
            }
            return solutionList;
        }
    }
    
    private void subsetWithDup(int[] num, int startPos, int size, ArrayList<Integer> solution){
        if (solution.size() == size){
        	ArrayList<Integer> newSolution = new ArrayList<Integer>();
        	newSolution.addAll(solution);
            solutionSet.add(newSolution);
            return;
        }else if (startPos == num.length){
            return;
        }
        else{
            for (int index = startPos; index < num.length; index++){
                solution.add(num[index]);
                subsetWithDup(num, index + 1, size, solution);
                solution.remove(solution.size() - 1);
            }
        }
    }
    
    // elegant algorithm
    public ArrayList<ArrayList<Integer>> subsetsWithDup2(int[] num){
    	int len = num.length;
    	ArrayList<ArrayList<Integer>> solutionList = new ArrayList<ArrayList<Integer>>();
    	// an empty arrayList is default
    	solutionList.add(new ArrayList<Integer>());
        if (len == 0)   return solutionList;
        else if (len == 1){
            ArrayList<Integer> solution = new ArrayList<Integer>();
            solution.add(num[0]);
            solutionList.add(solution);
            return solutionList;
        }else{
        	Arrays.sort(num);
        	solutionSet = new HashSet<ArrayList<Integer>>();
        	subsetWithDup2(num, 0, new ArrayList<Integer>());
        	for (ArrayList<Integer> ex: solutionSet){
        		if (ex.size() > 0)
        			solutionList.add(ex);
            }
            return solutionList;
        }
    }
    @SuppressWarnings("unchecked")
	private void subsetWithDup2(int[] number, int startPos, ArrayList<Integer> aSubset){
    	// reach the end of the number array, terminate
    	if (startPos == number.length){
    		solutionSet.add((ArrayList<Integer>) aSubset.clone());
    	}else{
    		// add current element and continue searching
    		aSubset.add(number[startPos]);
    		subsetWithDup2(number, startPos + 1, aSubset);
    		// did not add current element and continue searching
    		aSubset.remove(aSubset.size() - 1);
    		subsetWithDup2(number, startPos + 1, aSubset);
    	}
    }
    
	public ArrayList<ArrayList<Integer>> subset(int[] num){
		int len = num.length;
		ArrayList<ArrayList<Integer>> solutionList = new ArrayList<ArrayList<Integer>>();		
		if (len == 0){
			solutionList.add(new ArrayList<Integer>());
		}
		else if (len == 1){
			solutionList.add(new ArrayList<Integer>());
			ArrayList<Integer> solution = new ArrayList<Integer>();
			solution.add(num[0]);
			solutionList.add(solution);
		}else{
			Arrays.sort(num);
			ArrayList<Integer> solution = new ArrayList<Integer>();
			solutionSet = new HashSet<ArrayList<Integer>>();
			subset(num, 0, solution);
			for(ArrayList<Integer> ex: solutionSet){
				solutionList.add(ex);
			}
		}
		return solutionList;
	}
	@SuppressWarnings("unchecked")
	private void subset(int[] num, int startPos, ArrayList<Integer> solution){
		if (startPos == num.length){
			solutionSet.add((ArrayList<Integer>) solution.clone());
		}else{
			solution.add(num[startPos]);
			subset(num, startPos + 1, solution);
			solution.remove(solution.size() - 1);
			subset(num, startPos + 1, solution);
		}		
	}
    public static void main(String[] args){
    	int[] num = {1,2,2};
    	System.out.println(new Subset().subset(num));
    }
    
}
