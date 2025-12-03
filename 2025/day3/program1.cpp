#include <iostream>
#include <fstream>

using namespace std;


int main() {

    ifstream infile("input.txt");

    string line;
    long long total = 0;
    while (getline(infile, line)) {
        int i=0;
        int firstMax = line[i] - '0';
        int iMax = 0;
        for (; i<line.length()-1; i++) {
            int value = line[i] - '0';
            if (value > firstMax) {
                firstMax = value;
                iMax = i;
            }
        }
        int secondMax = line[iMax+1] - '0';
        for (int j = iMax+2; j<line.length(); j++) {
            int value = line[j] - '0';
            if (value > secondMax) {
                secondMax = value;
            }
        }
        int joltage = firstMax * 10 + secondMax;

        total += joltage;

    }

    cout << "Total Joltage: " << total << endl;
    return 0;
}
