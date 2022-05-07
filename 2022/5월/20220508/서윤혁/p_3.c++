#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;
using pll = pair < ll, ll>;
using matrix = vector<vector<ll>>;

const int MAXN = 1e5 + 1;
const int mod = 1e9;

struct T {
    int x, y, cnt;
};

int n, m, g[101][101], visited[101][101];
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, -1, 1};

int solve() {
    deque<T> deq;
    deq.push_back({0, 0, 0});
    visited[0][0] = 1;

    
    while (!deq.empty()) {
        T k = deq.front();
        deq.pop_front();
        
        if (k.x == n - 1 && k.y == m - 1) return k.cnt;
        
        for (int i = 0; i < 4; i++) {
            int nx = k.x + dx[i];
            int ny = k.y + dy[i];
            
            if (nx < 0 || nx >= n || ny < 0 || ny >= m || visited[nx][ny]) continue;
            visited[nx][ny] = 1;

            if (g[nx][ny] == 1) {
                deq.push_back({nx, ny, k.cnt + 1});
            } else {
                deq.push_front({nx, ny, k.cnt});
            }
        }
    }
    return 0;
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    cin >> m >> n;
    
    for (int i = 0; i < n; i++) {
        string s; cin >> s;
        for (int j = 0; j < s.length(); j++) g[i][j] = s[j] - '0';
    }

    cout << solve();
    return 0;
}