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

    public String toString() {
        return "[" + start + ", " + end + "]";
    }
}

class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(args[0]));

        List<Range> ranges = new ArrayList<>();

        try {
            StringBuilder sb = new StringBuilder();
            String line = br.readLine();

            // reading ranges
            while (!line.isEmpty()) {
                ranges.add(
                    new Range(
                        Long.parseLong(line.split("-")[0]),
                        Long.parseLong(line.split("-")[1])
                    )
                );
                line = br.readLine();
            }

            // sort ranges
            ranges.sort((a, b) -> Long.compare(a.start, b.start));

            Range currentRange = ranges.get(0);
            long counter = 0;

            for (int i = 1; i < ranges.size(); i++) {
                Range nextRange = ranges.get(i);
                if (nextRange.start <= currentRange.end) {
                    System.out.println(
                        "Current range: " + currentRange.toString()
                    );
                    currentRange.end = Math.max(
                        currentRange.end,
                        nextRange.end
                    );
                    System.out.println("Next range: " + nextRange.toString());
                    System.out.println(
                        "Merged range: " + currentRange.toString()
                    );
                } else {
                    counter += currentRange.end - currentRange.start + 1;
                    currentRange = nextRange;
                }
            }
            counter += currentRange.end - currentRange.start + 1;
            System.out.println(counter);
        } finally {
            br.close();
        }
    }
}
