#include<bits/stdc++.h>

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair < ll, ll>;
using matrix = vector<vector<ll>>;

#define INF 1e18
const int MAXN = 1e5 + 1;
const int mod = 1e9 + 7;

int n, e;
vector<pii> v[2001];

void bf(int s) {
    vector<ll> dist(501, INF);
    dist[s] = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (auto k : v[j]) {
                int cost = k.second;
                int nx = k.first;
                if (dist[nx] > cost + dist[j] && dist[j] != INF) {
                    dist[nx] = dist[j] + cost;
                    if (i == n - 1) {
                        cout << -1 << "\n";
                        return;
                    }
                }
            }
        }
    }
    for (int i = 1; i < n; i++)
        printf("%lld\n", dist[i] != INF ? dist[i] : -1);
    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n >> e;
    for (int i = 0; i < e; i++) {
        int a, b, c;
        cin >> a >> b >> c; a--; b--;
        v[a].push_back(make_pair(b, c));
    }
    bf(0);
    return 0;
}