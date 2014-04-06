import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
public class Anagrams {
	public ArrayList<String> anagrams(String[] strs) {
		if (strs.length < 2) {
			return new ArrayList<String>();
		} else {
			HashMap<String, ArrayList<String>> anagramMap = new HashMap<String, ArrayList<String>>();
			ArrayList<String> output = new ArrayList<String>();
			for (int index = 0; index < strs.length; index ++) {
				char[] word = strs[index].toCharArray();
				Arrays.sort(word);
				String currentWord = new String(word);
				if (!anagramMap.containsKey(currentWord)) {
					anagramMap.put(currentWord, new ArrayList<String>());					
				}
				anagramMap.get(currentWord).add(strs[index]);
			}
			for (String key: anagramMap.keySet()) {
				if (anagramMap.get(key).size() > 1)
					output.addAll(anagramMap.get(key));
			}
			return output;
		}
	}
	public static void main(String[] args){
        String[] strs = {"hos","jew","nub","cod","old","way","fur","fla","cot","baa","leo","uzi",
                        "tho","pry","tun","hex","fog","tad","eat","sow","cop","eke",
                        "jam","arc","guy","tow","aid","ann","bus","ten","ate","ewe","roy","leg","gas","bug","jay","sup","phd"};
        String[] str = {"hos","soh","phd","sho","dhp","gub","bug"};
        System.out.println(new Anagrams().anagrams(strs));
    }

}
