// Last updated: 5/8/2026, 3:05:15 PM
1class BrowserHistory {
2private:
3    struct Node {
4        string url;
5        Node* prev;
6        Node* next;
7        Node(string url) : url(url), prev(nullptr), next(nullptr) {}
8    };
9    Node* curr;
10
11public:
12    BrowserHistory(string homepage) { curr = new Node(homepage); }
13
14    void visit(string url) {
15        if(curr->next){
16            curr->next->prev = nullptr;
17        }
18        Node* node = new Node(url);
19        node->prev = curr;
20        curr->next = node;
21        curr = curr->next;
22    }
23
24    string back(int steps) {
25        int step = 0;
26        while (step < steps && curr->prev != nullptr) {
27            step++;
28            curr = curr->prev;
29        }
30        return curr->url;
31    }
32
33    string forward(int steps) {
34        int step = 0;
35        while (step < steps && curr->next != nullptr) {
36            step++;
37            curr = curr->next;
38        }
39        return curr->url;
40    }
41};
42
43/**
44 * Your BrowserHistory object will be instantiated and called as such:
45 * BrowserHistory* obj = new BrowserHistory(homepage);
46 * obj->visit(url);
47 * string param_2 = obj->back(steps);
48 * string param_3 = obj->forward(steps);
49 */