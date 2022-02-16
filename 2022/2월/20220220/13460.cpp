#include<bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;
using pll = pair < ll, ll>;
using matrix = vector<vector<ll>>;

const int MAXN = 1e9;
const int mod = 1e9;

pii blue;
pii red;
pii ex;

int visited[11][11][11][11] = { 0, };
int dx[] = { -1, 1, 0, 0 };
int dy[] = { 0, 0, 1, -1 };

typedef struct tt {
    pii r;
    pii b;
    int cnt;
};

int bfs(vector<string> s) {
    queue<tt> q;

    q.push({ red, blue, 0 });

    visited[red.first][red.second][blue.first][blue.second] = 1;

    while (!q.empty()) {
        int rx = q.front().r.first;
        int ry = q.front().r.second;
        int bx = q.front().b.first;
        int by = q.front().b.second;
        int cnt = q.front().cnt;
        q.pop();

        if (s[rx][ry] == 'O' && (rx != bx || ry != by)) {
            return cnt;
        }

        if (cnt > 10) {
            return -1;
        }


        for (int i = 0; i < 4; i++) {
            int nrx = rx;
            int nry = ry;
            int nbx = bx;
            int nby = by;

            int rd = 0, bd = 0;

            while (s[nrx + dx[i]][nry + dy[i]] != '#' && s[nrx][nry] != 'O') {
                nrx += dx[i];
                nry += dy[i];
                rd++;
            }

            while (s[nbx + dx[i]][nby + dy[i]] != '#' && s[nbx][nby] != 'O') {
                nbx += dx[i];
                nby += dy[i];
                bd++;
            }

            if (nrx == nbx && nry == nby) {
                if (s[nrx][nry] == 'O') continue;
                if (rd > bd) {
                    nrx -= dx[i];
                    nry -= dy[i];
                } else {
                    nbx -= dx[i];
                    nby -= dy[i];
                }
            }

            if (!visited[nrx][nry][nbx][nby]) {
                visited[nrx][nry][nbx][nby] = 1;
                q.push({ { nrx, nry }, { nbx, nby }, cnt + 1 });
            }
        }

    }

    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int n, m;
    cin >> n >> m;
    vector<string> s(n);

    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (s[i][j] == 'B') {
                blue = { i, j };
            }
            else if (s[i][j] == 'R') {
                red = { i, j };
            }
        }
    }

    cout << bfs(s);
    return 0;
}