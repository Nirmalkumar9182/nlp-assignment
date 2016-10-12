import org.apache.commons.compress.archivers.sevenz.SevenZArchiveEntry;
import org.apache.commons.compress.archivers.sevenz.SevenZFile;
import org.apache.commons.io.output.ByteArrayOutputStream;

import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Main {

    public static void main(String[] args) {
        SevenZFile sevenZFile;
        try {
            // change this file to the 7z file which you have downloaded
            File zipFile = new File("/Users/shouxian/Downloads/stackoverflow.com-Posts.7z");

            Path f = Paths.get("/Users/shouxian/Downloads/stackoverflow.com-Posts.7z");
            sevenZFile = new SevenZFile(zipFile);

            // the files inside of the SevenZFile object acts like a list
            // getNexEntry() will get the next item inside of the list
            SevenZArchiveEntry entry = sevenZFile.getNextEntry();
            while(entry!=null){
                String name = entry.getName();

                if(entry.isDirectory()) {
                    System.out.println(String.format("Found directory entry %s", name));
                } else {
                    // If this is a file, we read the file content into a
                    // ByteArrayOutputStream ...
                    System.out.println(String.format("Unpacking %s ...", name));
                    ByteArrayOutputStream contentBytes = new ByteArrayOutputStream();

                    // ... using a small buffer byte array.
                    byte[] buffer = new byte[2048];

                    int bytesRead;

                    // initialize file class with output.xml as our output file
                    FileWriter fw = new FileWriter("output.xml", true);
                    BufferedWriter bw = new BufferedWriter(fw);
                    PrintWriter out = new PrintWriter(bw);
                    String content = "";

                    // we set the current time and the end time for running our code
                    long t= System.currentTimeMillis();
                    long end = t+1000;

                    // run the code for 1 millisecond
                    while(System.currentTimeMillis() < end) {
                        bytesRead = sevenZFile.read(buffer);

                        // read contents of the file and write it into our byte array buffer
                        contentBytes.write(buffer, 0, bytesRead);
                    }

                    // Assuming the content is a UTF-8 text file we can interpret the
                    // bytes as a string.
                    content = contentBytes.toString("UTF-8");

                    // write the contents of the file into output.xml
                    out.println(content);

                    out.close();
                }

                System.out.println("Done");

                // gets the next item inside of the zip file
                entry = sevenZFile.getNextEntry();
            }
            // close the zip file
            sevenZFile.close();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } finally {

        }
    }
}