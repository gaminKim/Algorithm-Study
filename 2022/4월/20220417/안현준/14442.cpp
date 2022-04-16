#include <algorithm>
#include <iostream>
#include <queue>
using namespace std;

int N, M, K;
char arr[1001][1001];
int visit[1001][1001][11];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

struct Pos {
    int x;
    int y;
    int breakCnt;
};

bool isRange(int x, int y) { return x > 0 && y > 0 && x <= N && y <= M; }

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M >> K;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            cin >> arr[i][j];
        }
    }

    queue<Pos> q;
    q.push({1, 1, 0});
    visit[1][1][0] = 1;

    while (!q.empty()) {
        int fx = q.front().x;
        int fy = q.front().y;
        int bc = q.front().breakCnt;

        if (fx == N && fy == M) break;

        int dist = visit[fx][fy][bc];
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = fx + dx[i];
            int ny = fy + dy[i];

            if (isRange(nx, ny)) {
                if (arr[nx][ny] == '1' && bc < K &&
                    (visit[nx][ny][bc + 1] == 0 ||
                     visit[nx][ny][bc + 1] > dist + 1)) {
                    q.push({nx, ny, bc + 1});
                    visit[nx][ny][bc + 1] = dist + 1;
                } else if (arr[nx][ny] == '0' &&
                           (visit[nx][ny][bc] == 0 ||
                            visit[nx][ny][bc] > dist + 1)) {
                    q.push({nx, ny, bc});
                    visit[nx][ny][bc] = dist + 1;
                }
            }
        }
    }
    int answer = 1000 * 1000 + 1;
    for (int i = 0; i <= K; i++) {
        if (visit[N][M][i] > 0) answer = min(answer, visit[N][M][i]);
    }

    if (answer == 1000 * 1000 + 1)
        cout << -1;
    else
        cout << answer;
}