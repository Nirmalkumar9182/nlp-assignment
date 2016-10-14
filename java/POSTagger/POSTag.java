/**
 * Created by Vincent on 12/10/2016.
 */
import opennlp.tools.postag.POSTaggerME;
import opennlp.tools.postag.POSModel;
import opennlp.tools.sentdetect.SentenceDetectorME;
import opennlp.tools.sentdetect.SentenceModel;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Random;

public class POSTag {
    public static void main(String[] args) {
        File modelFile = new File("en-pos-maxent.bin");
        File sentFile = new File("en-sent.bin");

        try {
            POSModel posModel = new POSModel(modelFile);
            POSTaggerME tagger = new POSTaggerME(posModel);
            SentenceModel sentModel = new SentenceModel(sentFile);
            SentenceDetectorME sentenceDetector = new SentenceDetectorME(sentModel);

            BufferedReader br = new BufferedReader(new FileReader("answer_without_angle.txt"));

            String line = null;
            int count = 0;

            while ((line = br.readLine()) != null) {
                Random rand = new Random();

                int  n = rand.nextInt(30) + 1;
                for (int i = 0; i < n; i++) {
                    br.readLine();
                }

                while (line.length() == 1 || line.length() == 0) {
                    line = br.readLine();
                }

                String sentences[] = sentenceDetector.sentDetect(line);

                for (int j = 0; j < sentences.length; j++) {
                    String result = tagger.tag(sentences[j]);
                    System.out.println(String.format("Result: %s", result));

                    count++;
                }

                if (count == 10) {
                    break;
                }
            }

            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
