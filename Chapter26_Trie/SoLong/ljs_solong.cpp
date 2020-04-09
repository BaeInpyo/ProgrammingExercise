#include <string.h>
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

#define ALPHABETS 26

unordered_map<string, int> inserted;
vector<string> dictionary;
vector<int> frequencies;

struct TrieNode {
    TrieNode* children[ALPHABETS];
    int topId;

    TrieNode() : topId(-1) {
        memset(children, 0, sizeof(children));
    }
    ~TrieNode() {
        for (int i=0; i<ALPHABETS; i++)
            if (children[i]) delete children[i];
    }

    void insert(const char* key, int id) {
        if (key[0] == '\0')
            return;
        TrieNode* next = children[toNumber(key[0])];
        if (!next)
            next = new TrieNode();
        if (next->topId == -1 || frequencies[next->topId] < frequencies[id]
                              || frequencies[next->topId] == frequencies[id]
                              && dictionary[next->topId] > dictionary[id])
            next->topId = id;
        next->insert(key+1, id);
    }

    int type(const char* key, int id) {
        if (key[0] == '\0')
            return 0;
        if (topId == id)
            return 1;
        return 1 + children[toNumber(key[0])]->type(key+1, id);
    }

    int toNumber(char c) { c - 'A'; }
};

void solution() {
    int n, m, prio, res = 0;
    string s;
    cin >> n >> m;

    inserted.clear();
    dictionary.clear();
    frequencies.clear();

    TrieNode* root = new TrieNode();
    for (int i=0; i<n; i++) {
        cin >> s >> prio;
        dictionary.push_back(s);
        frequencies.push_back(prio);
        inserted.insert({"s", i});
        root->insert(s.c_str(), i);
    }
    while (m--) {
        cin >> s;
        auto itr = inserted.find(s);
        if (itr != inserted.end())
            res += root->type(s.c_str(), itr->second);
        else
            res += s.size();
        res++;
    }
    cout << res-1 << endl;
}

int main() {
    int c;
    cin >> c;
    while (c--) solution();
    return 0;
}
