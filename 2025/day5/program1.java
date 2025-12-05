import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays.*;
import java.util.List;

class Range {

    public long start;
    public long end;

    public Range(long start, long end) {
        this.start = start;
        this.end = end;
    }
}

class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(args[0]));

        List<Range> lines = new ArrayList<>();

        try {
            StringBuilder sb = new StringBuilder();
            String line = br.readLine();

            // reading ranges
            while (!line.isEmpty()) {
                lines.add(
                    new Range(
                        Long.parseLong(line.split("-")[0]),
                        Long.parseLong(line.split("-")[1])
                    )
                );
                line = br.readLine();
            }
            line = br.readLine();

            int counter = 0;
            // reading values
            while (line != null) {
                long value = Long.parseLong(line);
                for (Range range : lines) {
                    if (value >= range.start && value <= range.end) {
                        counter++;
                        break;
                    }
                }
                line = br.readLine();
            }
            System.out.println(counter);
        } finally {
            br.close();
        }
    }
}
