
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import opennlp.tools.stemmer.PorterStemmer;

import java.util.Set;
 
public class Top20WordsAfterStemming {
 
	public static void main(String[] args) throws FileNotFoundException, IOException {
		File file = new File("C:/Users/MehaDP/Desktop/for NLP/answer_without_angle.txt");
		BufferedReader bufferedReader = null;
		bufferedReader = new BufferedReader(new FileReader(file));
		String inputLine = null;
		Map<String, Integer> crunchifyMap = new HashMap<>();
 
		try {
			while ((inputLine = bufferedReader.readLine()) != null) {
				String[] words = inputLine.split("[~%â€™ï+?><., @\\\\1234567890_\n\t\r.,;:-=`\"$/\\]\\[&|\'\'!?(){}-]");
				
				for (int counter = 0; counter < words.length; counter++) {
					
					String key = words[counter].toLowerCase(); 
					PorterStemmer stemmer = new PorterStemmer();
					String keyCHANGE = stemmer.stem(key.toString());
					
					if (keyCHANGE.length() > 0) {
						if (crunchifyMap.get(keyCHANGE) == null) {
							crunchifyMap.put(keyCHANGE, 1);
						} else {
							int value = crunchifyMap.get(keyCHANGE).intValue();
							value++;
							crunchifyMap.put(keyCHANGE, value);
						}
					}
				}
			}
			Set<Map.Entry<String, Integer>> entrySet = crunchifyMap.entrySet();

			List<String> myTopOccurrence = crunchifyFindMaxOccurance(crunchifyMap, 20);
			System.out.println("\nTop 20 Words after Stemming: ");
			for (String result : myTopOccurrence) {
				System.out.println("> " + result);
			}
 
		}
 
		catch (IOException error) {
			System.out.println("Invalid File");
		} finally {
			bufferedReader.close();
		}
	}
 	public static List<String> crunchifyFindMaxOccurance(Map<String, Integer> map, int n) {
		List<CrunchifyComparable> l = new ArrayList<>();
		List<String> stopWords = Arrays.asList("the", "to", "a", "you", "and", "is", "of", "it", "in", "i", "that", "this", "has",
				"for", "if", "be", "your", "on", "can", "with", "are", "as","but","have","not","use","or","an", "at", "so","do",
				"but", "by", "into", "no", "not", "such", "their", "then", "there", "these", "they", "was", "will", "which",
				"gt","t","lt","s");
		
		for (Map.Entry<String, Integer> entry : map.entrySet()) {
			String x = entry.getKey();
			if(stopWords.contains(x)) {
				continue;
			}
			
			l.add(new CrunchifyComparable(entry.getKey(), entry.getValue()));
		}
			
		
		Collections.sort(l);
		List<String> list = new ArrayList<>();
		for (CrunchifyComparable w : l.subList(0, n)) {
			
			
			list.add(w.wordFromFile + ":" + w.numberOfOccurrence);
		}
			
		
		return list;
	}
}
 
class CrunchifyComparable implements Comparable<CrunchifyComparable> {
	public String wordFromFile;
	public int numberOfOccurrence;
 
	public CrunchifyComparable(String wordFromFile, int numberOfOccurrence) {
		super();
		this.wordFromFile = wordFromFile;
		this.numberOfOccurrence = numberOfOccurrence;
	}
 
	@Override
	public int compareTo(CrunchifyComparable arg0) {
		int crunchifyCompare = Integer.compare(arg0.numberOfOccurrence, this.numberOfOccurrence);
		return crunchifyCompare != 0 ? crunchifyCompare : wordFromFile.compareTo(arg0.wordFromFile);
	}
 
	@Override
	public int hashCode() {
		final int uniqueNumber = 19;
		int crunchifyResult = 9;
		crunchifyResult = uniqueNumber * crunchifyResult + numberOfOccurrence;
		crunchifyResult = uniqueNumber * crunchifyResult + ((wordFromFile == null) ? 0 : wordFromFile.hashCode());
		return crunchifyResult;
	}
 
	@Override
	public boolean equals(Object crunchifyObj) {
		if (this == crunchifyObj)
			return true;
		if (crunchifyObj == null)
			return false;
		if (getClass() != crunchifyObj.getClass())
			return false;
		CrunchifyComparable other = (CrunchifyComparable) crunchifyObj;
		if (numberOfOccurrence != other.numberOfOccurrence)
			return false;
		if (wordFromFile == null) {
			if (other.wordFromFile != null)
				return false;
		} else if (!wordFromFile.equals(other.wordFromFile))
			return false;
		return true;
	}
}