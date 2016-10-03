import org.apache.commons.compress.archivers.sevenz.SevenZArchiveEntry;
import org.apache.commons.compress.archivers.sevenz.SevenZFile;

import java.io.*;

public class Main {
    public static void main(String[] args) {
        SevenZFile sevenZFile;
        try {
            // change this file to the 7z file which you have downloaded
            sevenZFile = new SevenZFile(new File("/Users/shouxian/Downloads/stackoverflow.com-PostLinks.7z"));

            // the files inside of the SevenZFile object acts like a list
            // getNexEntry() will get the next item inside of the list
            SevenZArchiveEntry entry = sevenZFile.getNextEntry();
            while(entry!=null){
                // prints out the name of the file and the size of the file in bytes
                System.out.println(entry.getName() + " (Size: " + entry.getSize() + ")");

                // place the file name into an outputstream object
                FileOutputStream out = new FileOutputStream(entry.getName());
                byte[] content = new byte[(int) entry.getSize()];

                // uses the outputstream object to write into the byte array object above
                sevenZFile.read(content, 0, content.length);
                out.write(content);
                out.close();

                // and a BufferedReader on top to comfortably read the file
                BufferedReader reader = new BufferedReader(new InputStreamReader(new ByteArrayInputStream(content)));
                String line;

                // this while loop will read the file line by line until it reaches the EOF line
                while ((line = reader.readLine()) != null)
                {
                    // prints out the line in the file
                    // we can do other stuff to the line string
                    System.out.println(line);
                }

                // gets the next item inside of the zip file
                entry = sevenZFile.getNextEntry();
            }
            // close the zip file
            sevenZFile.close();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}