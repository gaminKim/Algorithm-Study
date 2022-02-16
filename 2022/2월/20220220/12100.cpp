#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;
using pll = pair < ll, ll>;
using matrix = vector<vector<ll>>;

const int MAXN = 1e9;
const int mod = 1e9;

int n, ans;

int dx[] = { 1, -1 , 0, 0 };
int dy[] = { 0, 0 , -1, 1 };

matrix up(matrix ar) {
	int v[20][20];
	memset(v, 0, sizeof(v));

	for (int i = 1; i < n; i++) {
		for (int j = 0; j < n; j++) {
			int t = i;
			while (t > 0 && ar[t-1][j] == 0) {
				ar[t - 1][j] = ar[t][j];
				ar[t][j] = 0;
				t--;
			}

			if (t > 0 && !v[t - 1][j] && ar[t - 1][j] == ar[t][j]) {
				v[t - 1][j] = 1;
				ar[t - 1][j] *= 2;
				ar[t][j] = 0;
			}
		}
	}
	return ar;
}


matrix down(matrix ar) {
	int v[20][20];
	memset(v, 0, sizeof(v));

	for (int i = n - 2; i >= 0; i--) {
		for (int j = 0; j < n; j++) {
			int t = i;
			while (t < n - 1 && ar[t+1][j] == 0) {
				ar[t + 1][j] = ar[t][j];
				ar[t][j] = 0;
				t++;
			}

			if (t < n - 1 && !v[t + 1][j] && ar[t + 1][j] == ar[t][j]) {
				v[t + 1][j] = 1;
				ar[t + 1][j] *= 2;
				ar[t][j] = 0;
			}
		}
	}
	return ar;
}


matrix left(matrix ar) {
	int v[20][20];
	memset(v, 0, sizeof(v));

	for (int i = 0; i < n; i++) {
		for (int j = 1; j < n; j++) {
			int t = j;
			while (t > 0 && ar[i][t - 1] == 0) {
				ar[i][t - 1] = ar[i][t];
				ar[i][t] = 0;
				t--;
			}

			if (t > 0 && !v[i][t-1] && ar[i][t-1] == ar[i][t]) {
				v[i][t-1] = 1;
				ar[i][t-1] *= 2;
				ar[i][t] = 0;
			}
		}
	}
	return ar;
}


matrix right(matrix ar) {

	int v[20][20];
	memset(v, 0, sizeof(v));

	for (int i = 0; i < n; i++) {
		for (int j = n - 2; j >= 0; j--) {
			int t = j;
			while (t < n-1 && ar[i][t + 1] == 0) {
				ar[i][t + 1] = ar[i][t];
				ar[i][t] = 0;
				t++;
			}

			if (t < n - 1 && !v[i][t + 1] && ar[i][t + 1] == ar[i][t]) {
				v[i][t + 1] = 1;
				ar[i][t + 1] *= 2;
				ar[i][t] = 0;
			}
		}
	}
	return ar;
}


void dfs(matrix ar, int depth) {

	if (depth == 5) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (ans < ar[i][j]) {
					ans = ar[i][j];
				}
			}
		}
		return;
	}

	dfs(up(ar), depth + 1);
	dfs(down(ar), depth + 1);
	dfs(left(ar), depth + 1);
	dfs(right(ar), depth + 1);
}


int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> n;

	matrix ar(n, vector<ll>(n));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> ar[i][j];
		}
	}

	dfs(ar, 0);
	cout << ans << '\n';
}