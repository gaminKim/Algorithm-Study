#include<bits/stdc++.h>

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair < ll, ll>;
using matrix = vector<vector<ll>>;

const int MAXN = 1e5 + 1;
const int mod = 1e9 + 7;

int n, m, indegree[32010];
priority_queue<int, vector<int>, greater<int>> pq;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n >> m;

    vector<int> v[32010];

    for (int i = 0; i < m; i++) {
        int a, b; cin >> a >> b;
        v[a].push_back(b);
        indegree[b]++;
    }

    //위상정렬 사용
    for (int i = 1; i <= n; i++)
        if (!indegree[i]) pq.push(i);
    
    for (int i = 1; i <= n; i++) {
        int x = pq.top();
        pq.pop();
        
        cout << x << ' ';

        for (auto nx : v[x]) {
            indegree[nx]--;
            if (!indegree[nx]) pq.push(nx);
        }
    }

    return 0;
}