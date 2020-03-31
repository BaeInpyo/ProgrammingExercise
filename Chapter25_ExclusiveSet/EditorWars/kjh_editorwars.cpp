#include <iostream>

using namespace std;

struct NODE {
    int val;
    int size;
    NODE* parent;
    NODE* counter;
};

NODE* root(NODE* _node) {
    if (!_node) return 0;
    auto node = _node;
    while (node->parent) {
        node = node->parent;
    }
    while (_node->parent && _node->parent != node) {
        auto temp = _node->parent;
        _node->parent = node;
        _node = temp;
    }
    return node;
}

NODE* merge(NODE* a, NODE* b) {
    auto ra = root(a);
    auto rb = root(b);
    if (ra == rb) return ra;
    rb->parent = ra;
    return ra;
}

NODE users[10000];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    #ifdef DEBUG
    freopen("input.txt", "r", stdin);
    #endif
    int C;
    cin >> C;
    while (C--) {
        int n, m;
        cin >> n >> m;
        for (int i = 0; i < n; i++) {
            users[i].parent = 0;
            users[i].counter = 0;
            users[i].val = i;
            users[i].size = 0;
        }
        string s;
        int a, b;
        bool cont = false;
        for (int i = 0; i < m; i++) {
            cin >> s >> a >> b;
            if (cont) continue;
            if (s[0] == 'A') {
                NODE* anode = &users[a];
                NODE* bnode = &users[b];
                auto aroot = root(anode);
                auto broot = root(bnode);
                if (aroot == root(broot->counter) || broot == root(aroot->counter)) {
                    cont = true;
                    cout << "CONTRADICTION AT " << i+1 << '\n';
                    continue;
                }
                auto _node = merge(anode, bnode);
                if (aroot->counter && broot->counter) {
                    auto _counter = merge(aroot->counter, broot->counter);
                    _node->counter = _counter;
                    _counter->counter = _node;
                }
                else if (aroot->counter) {
                    _node->counter = root(aroot->counter);
                }
                else if (broot->counter) {
                    _node->counter = root(broot->counter);
                }
            }
            else if (s[0] == 'D') {
                NODE* anode = &users[a];
                NODE* bnode = &users[b];
                auto aroot = root(anode);
                auto broot = root(bnode);
                if (aroot == broot) {
                    cont = true;
                    cout << "CONTRADICTION AT " << i+1 << '\n';
                    continue;
                }

                if (!aroot->counter && !broot->counter) {
                    aroot->counter = broot;
                    broot->counter = aroot;
                }
                else if (!aroot->counter) {
                    aroot->counter = broot;
                    broot->counter = merge(broot->counter, anode);
                }
                else if (!broot->counter) {
                    broot->counter = aroot;
                    aroot->counter = merge(aroot->counter, bnode);
                }
                else {
                    aroot->counter = merge(aroot->counter, bnode);
                    broot->counter = merge(broot->counter, anode);
                }
            }
            else return -123;
        }
        if (cont) 
            continue;

        for (int i = 0; i < n; i++) {
            root(&users[i])->size++;
        }
        int ret = 0;
        for (int i = 0; i < n; i++) {
            auto _root = root(&users[i]);
            if (i == _root->val) {
                auto _counter = _root->counter;
                if (_counter) {
                    if (_counter->val < i) // not visited yet
                        ret += max(_counter->size, _root->size);
                }
                else {
                    ret += _root->size;
                }
            }
        }
        cout << "MAX PARTY SIZE IS " << ret << '\n';
    }
    return 0;
}
