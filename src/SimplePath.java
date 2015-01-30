import java.util.ArrayList;


/**
 * 
 * SimplePath.java
 * Dec 5, 2012
 */

/**
 * @author huangsp
 *
 */
public class SimplePath {
	public String simplifyPath(String path){
		String[] files = path.split("/");
		int len = files.length;
		ArrayList<String> list = new ArrayList<String>();
		for (int index = 0; index < len; index++){
			if (files[index].equals("")) continue;
			if (files[index].equals("..")){
				if(!list.isEmpty())
					list.remove(list.size() - 1);
				continue;
			}else if (files[index].equals(".")){
				continue;
			}else{
				list.add("/" + files[index]);
			}
		}
		
		StringBuffer simplePath= new StringBuffer();
		for (String ex : list){
			if (ex.equals("/"))	continue;
			else simplePath.append(ex);
		}
		if (simplePath.toString().equals(""))	return "/";
		return simplePath.toString();
	}
	public static void main(String[] args){
		SimplePath myPath = new SimplePath();
		System.out.println(myPath.simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"));
	}
}
