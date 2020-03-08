#include <iostream>
#include <list>

using namespace std;

class Nerd {
    public:
        int probs;
        int noodles;
        int isNerdierThan(const Nerd& newNerd) {
            return probs > newNerd.probs && noodles > newNerd.noodles;
        }
        bool operator==(const Nerd& newNerd) const {
            return probs == newNerd.probs && noodles == newNerd.noodles;
        }
};

void solution() {
    int n;
    cin >> n;
    Nerd firstNerd;
    cin >> firstNerd.probs >> firstNerd.noodles;
    list<Nerd> nerds;
    nerds.push_back(firstNerd);
    int ret = 1;
    for (int i=0; i < n - 1; i++) {
        Nerd newNerd;
        cin >> newNerd.probs >> newNerd.noodles;
        auto notNerds = list<Nerd>();
        for (Nerd& nerd : nerds) {
            if (newNerd.isNerdierThan(nerd))
                notNerds.push_back(nerd);
            else if (nerd.isNerdierThan(newNerd))
                break;
        }
        for (Nerd& noNerd : notNerds)
            nerds.remove(noNerd);
            //nerds.remove_if([](Nerd n){ return noNerd == n; });
        nerds.push_back(newNerd);
        ret = ret + nerds.size();
    }
    cout << ret << endl;
}


int main() {
    int c;
    cin >> c;
    while (c--) {
        solution();
    }
    return 0;
}
