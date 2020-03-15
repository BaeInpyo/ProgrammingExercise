#include <iostream>
#include <queue>

using namespace std;

static int input = 0;

void genInput(int a, int b) {
    if (input == 0) input = 1983;
    else input = ((long)input * a + b) % 20090711;
}

void solution() {
    int n, a, b;
    cin >> n >> a >> b;
    input = 0;
    priority_queue< int, vector<int>, less<int> > maxHeap;
    priority_queue< int, vector<int>, greater<int> > minHeap;
    int result = 0;
    while (n--) {
        genInput(a, b);
        if (maxHeap.size() == minHeap.size()) maxHeap.push(input);
        else minHeap.push(input);

        if (!minHeap.empty() && (maxHeap.top() > minHeap.top())) {
            maxHeap.push(minHeap.top());
            minHeap.push(maxHeap.top());
            maxHeap.pop();
            minHeap.pop();
        }

        result = (result + maxHeap.top()) % 20090711;
    }
    cout << result << endl;
}

int main() {
    int c;
    cin >> c;
    while (c--) solution();
    return 0;
}
