#include <iostream>
#include <algorithm>
using namespace std;

int N;
int t[16];
int p[16];
int dp[17];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> t[i] >> p[i];
	}

	for (int i = N; i > 0; i--) {
		if (i + t[i] - 1 > N)
			dp[i] = dp[i + 1];
		else
			dp[i] = max(dp[i + 1], dp[i + t[i]] + p[i]);
	}
	cout << dp[1];
}