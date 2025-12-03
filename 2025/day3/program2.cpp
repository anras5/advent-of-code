#include <iostream>
#include <fstream>

using namespace std;


int main() {

    ifstream infile("input.txt");

    string line;
    long long total = 0;
    while (getline(infile, line)) {

        string builder = "";
        int startRange = 0;
        for(int number = 1; number <= 12; number++) {
            int endRange = line.length() - (12 - number);

            string snippet = "";
            for (int i = startRange; i < endRange; i++) {
                snippet += line[i];
            }

            int max = snippet[0] - '0';
            int iMax = 0;
            for (int i = 1; i < snippet.length(); i++) {
                if (snippet[i] - '0' > max) {
                    max = snippet[i] - '0';
                    iMax = i;
                }
            }

            iMax = iMax + startRange;
            startRange = iMax + 1;

            builder += to_string(max);

        }

        cout << builder << endl;
        total += stoll(builder);
    }

    cout << "Total Joltage: " << total << endl;
    return 0;
}
