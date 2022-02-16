#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;
using pll = pair < ll, ll>;
using matrix = vector<vector<ll>>;

const int MAXN = 1e9;
const int mod = 1e9;

int ar[101][101];
char d[10001];
vector<pair<pii, pii>> snake;
int n;

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);

	cin >> n;
	int k; cin >> k;

	while (k--) {
		int x, y; cin >> x >> y;
		ar[x][y] = 1;
	}
	int L; cin >> L;

	while (L--) {
		int k; char c;
		cin >> k >> c;
		d[k] = c;
	}

	int i = 0;
	snake.push_back({ {1, 1}, {0, 1} });
	int checked[101][101];
	while (1) {
		i++;
		for (int u = 0; u < snake.size(); u++) {
			int sx = snake[u].first.first;
			int sy = snake[u].first.second;
			int dx = snake[u].second.first;
			int dy = snake[u].second.second;
			
			if (d[i - u]) {
				int tmp;
				if (d[i - u] == 'L') {
					if ((dx == 1 && dy == 0) || (dx == -1 && dy == 0)) {
						tmp = snake[u].second.first;
						snake[u].second.first = snake[u].second.second;
						snake[u].second.second = tmp;
					}
					else {
						tmp = snake[u].second.first;
						snake[u].second.first = snake[u].second.second * -1;
						snake[u].second.second = tmp * -1;
					}
				}
				else if (d[i - u] == 'D') {
					if ((dx == 0 && dy == 1) || (dx == 0 && dy == -1)) {
						tmp = snake[u].second.first;
						snake[u].second.first = snake[u].second.second;
						snake[u].second.second = tmp;
					}
					else {
						tmp = snake[u].second.first;
						snake[u].second.first = snake[u].second.second * -1;
						snake[u].second.second = tmp * -1;
					}
				}
			}
			snake[u].first.first += dx;
			snake[u].first.second += dy;

			if (ar[snake[u].first.first][snake[u].first.second] == 1) {
				ar[snake[u].first.first][snake[u].first.second] = 0;
				snake.insert(snake.begin() + 1, { {sx, sy}, {dx, dy} });
				break;
			}

			if (snake[u].first.first < 1 || snake[u].first.first > n || snake[u].first.second < 1 || snake[u].first.second > n) {
				cout << i;
				exit(0);
			}

			checked[snake[u].first.first][snake[u].first.second]++;

			if (checked[snake[u].first.first][snake[u].first.second] > 1) {
				cout << i;
				exit(0);
			}
			if (u == 0) {
				memset(checked, 0, sizeof(checked));
			}
		}
	}
	return 0;
}