#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;
using pll = pair < ll, ll>;
using matrix = vector<vector<ll>>;

const int MAXN = 1e6 + 10;
const int mod = 1e9 + 7;

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);

    double a, b;
    cin >> a >> b;

    double s = sqrt(a * a + b * b);

    cout << fixed << setprecision(17) << a / s << " " << b / s << '\n';

    return 0;
}