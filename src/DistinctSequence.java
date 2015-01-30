/**
 * 
 * DistinctSequence.java
 * Nov 26, 2012
 */

/**
 * @author Shubo Liu
 * Time complexity is O(m*n) and space complexity is O(m*n)
 */
public class DistinctSequence {
	public int numDistinct(String S, String T) {
        // Start typing your Java solution below
        // DO NOT write main() function
		if (S.length() == 0 || T.length() == 0 || S.length() < T.length()) 	return 0;
		else{
			// dynamic programming
			int[][] dynamicMatrix = new int[S.length()][T.length()];
			if (S.charAt(0) == T.charAt(0)) dynamicMatrix[0][0] = 1;
			else dynamicMatrix[0][0] = 0;
			for (int index = 1; index < S.length(); index++){
				dynamicMatrix[index][0] = dynamicMatrix[index - 1][0] + ((S.charAt(index) == T.charAt(0)) ? 1 : 0);
			}
			for (int index = 1; index < T.length(); index++){
				dynamicMatrix[0][index] = 0;
			}
			// S[x] = T[Y] f(x,y) = f(x - 1, y - 1) + f(x - 1, y);
			// S[x] != T[Y] f(x, y) = f(x - 1, y)
			for (int indexT = 1; indexT < T.length(); indexT ++){
				for (int indexS = 1; indexS < S.length(); indexS++){
					if (S.charAt(indexS) == T.charAt(indexT)){
						dynamicMatrix[indexS][indexT] = dynamicMatrix[indexS - 1][indexT - 1] + dynamicMatrix[indexS - 1][indexT];
					}else{
						dynamicMatrix[indexS][indexT] = dynamicMatrix[indexS - 1][indexT];
					}
				}
			}
			return dynamicMatrix[S.length() - 1][T.length() - 1];
		}  
    }
	public static void main(String[] args){
		System.out.println(new DistinctSequence().numDistinct("Rabbbittt", "Rabbit"));
	}
}
