import java.util.ArrayList;
import java.util.Arrays;

/**
 * 
 * Anagram2.java
 * Nov 22, 2012
 */

/**
 * @author Shubo Liu
 *
 */
public class Anagram2 {
	private class Duplex implements Comparable<Duplex>{
		String str;
		String sortedStr;
		public Duplex(String str){
			this.str = str;
			char[] charArray = str.toCharArray();
			Arrays.sort(charArray);
			sortedStr = Arrays.toString(charArray);
		}

		@Override
		public int compareTo(Duplex that) {
			// TODO Auto-generated method stub
			return this.sortedStr.compareTo(that.sortedStr);
		}
		public boolean equals(Duplex that){
			return this.sortedStr.equals(that.sortedStr);
		}
		@Override
		public String toString(){
			return str + "(" + sortedStr + ")";
		}
	}
    // Start typing your Java solution below
    // DO NOT write main() function
	// O(NlogN) + O(N * MlogM) time complexity
	 public ArrayList<String> anagrams(String[] strs) {
		 int size = strs.length;
		 ArrayList<String> list = new ArrayList<String>();
		 if (size < 2) return list;
		 else{
			 Duplex[] strArray = new Duplex[size];
			 for (int index = 0; index < size; index++){
				 strArray[index] = new Duplex(strs[index]);
			 }
			 Arrays.sort(strArray);
			 boolean flag = false;
			 for (int index = 0; index < size - 1; index++){
				 if (strArray[index].equals(strArray[index+1])){
					 if (!flag){
						 list.add(strArray[index].str);
						 flag = true;
					 }
					 list.add(strArray[index + 1].str); 
				 }
				 else{
					 flag = false;
				 }
			 }
			 return list;
		 }

	    
	}
     public static void main(String[] args){
    	 String[] strs = {"hos","jew","nub","cod","old","way","fur","fla","cot","baa","leo","uzi",
    			 "tho","pry","tun","hex","fog","tad","eat","sow","cop","eke",
    			 "jam","arc","guy","tow","aid","ann","bus","ten","ate","ewe","roy","leg","gas","bug","jay","sup","phd","cra"};
    	 ArrayList<String> output = new Anagram2().anagrams(strs);
    	System.out.println(output);
     }
}
