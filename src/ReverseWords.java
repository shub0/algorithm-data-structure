
public class ReverseWords {
	public static String reverseWords(String input) {
        if (input == null || input.length() == 0) {
			return "";
		}
		String[] words = input.split(" ");
		StringBuilder output = new StringBuilder();
		for (int index = words.length - 1; index >= 0; index --) {
			if (words[index].length() == 0)
				continue;
			output.append(words[index]);
			output.append(" ");
		}
		return output.toString().trim();
    }
	
	public static void main(String[] args) {
		System.out.println(reverseWords(" 1"));
	}
}
