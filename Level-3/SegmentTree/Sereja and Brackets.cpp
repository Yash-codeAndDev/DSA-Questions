#include <bits/stdc++.h>
using namespace std;

struct info {
    int open, close, full;
    info(int _open, int _close, int _full) {
        open = _open;
        close = _close;
        full = _full;
    }
};

info mergeSeg(info left, info right) {
    info ans = info(0, 0, 0);
    ans.full = left.full + right.full + min(left.open, right.close);
    ans.open = left.open + right.open - min(left.open, right.close);
    ans.close = left.close + right.close - min(left.open, right.close);
    return ans;
}

void buildSeg(int ind, int low, int high, string s, info seg[]) {
    if (low == high) {
        seg[ind] = info(s[low] == '(', s[low] == ')', 0);
        return;
    }
    int mid = (low + high) / 2; 
    buildSeg(2 * ind + 1, low, mid, s, seg);
    buildSeg(2 * ind + 2, mid + 1, high, s, seg);
    seg[ind] = mergeSeg(seg[2 * ind + 1], seg[2 * ind + 2]);
}

int main() {
    string s;
    cin >> s;
    int q;
    cin >> q;
    int n = s.size();
    info seg[4 * n];
    buildSeg(0, 0, n - 1, s, seg);
    while (q--) {
        int l, r;
        cin >> l >> r;
        l--;
        r--;
        cout << "Query result for range [" << l << ", " << r << "]: " << seg[0].full << endl;
    }

    return 0;
}
