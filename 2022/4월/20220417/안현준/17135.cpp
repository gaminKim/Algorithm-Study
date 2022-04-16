#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>
#include <set>
using namespace std;

int N, M, D;
int arr[16][16];
int archer[3];
int temp[16][16];
int dx[3] = {0, -1, 0};
int dy[3] = {-1, 0, 1};
int visit[16][16];
int answer;
int kill;

set<pair<int, int>> v;

void shot(int x, int y) {
    memset(visit, 0, sizeof(visit));
    queue<pair<int, int>> q;
    q.push({x, y});
    visit[x][y] = 1;

    while (!q.empty()) {
        int fx = q.front().first;
        int fy = q.front().second;
        int dist = visit[fx][fy];
        q.pop();

        if (dist > D) {
            break;
        }
        if (temp[fx][fy] == 1) {
            v.insert({fx, fy});
            break;
        }

        for (int i = 0; i < 3; i++) {
            int nx = fx + dx[i];
            int ny = fy + dy[i];

            if (nx > 0 && nx <= N && ny > 0 && ny <= M && visit[nx][ny] == 0) {
                q.push({nx, ny});
                visit[nx][ny] = dist + 1;
            }
        }
    }
}

int simulation() {
    //복사
    kill = 0;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            temp[i][j] = arr[i][j];
        }
    }

    for (int k = 0; k < N; k++) {
        //화살쏘기
        v.clear();
        for (int i = 0; i < 3; i++) {
            shot(N, archer[i]);
        }

        for (pair<int, int> p : v) {
            kill++;
            temp[p.first][p.second] = 0;
        }

        //한칸씩 내리기
        for (int i = N - 1; i >= 0; i--) {
            for (int j = 1; j <= M; j++) {
                temp[i + 1][j] = temp[i][j];
            }
        }
    }
    return kill;
}
void setArcher(int idx, int cnt) {
    if (cnt == 3) {
        answer = max(answer, simulation());
        return;
    }
    if (idx > M) {
        return;
    }

    archer[cnt] = idx;
    setArcher(idx + 1, cnt + 1);
    archer[cnt] = 0;
    setArcher(idx + 1, cnt);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M >> D;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            cin >> arr[i][j];
        }
    }
    setArcher(1, 0);
    cout << answer << '\n';
}