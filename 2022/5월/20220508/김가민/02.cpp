#include<bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int x, y;
    cin >> x >> y;

    double deno = sqrt(pow(x, 2) + pow(y, 2));
    double a = x / deno;
    double b = y / deno;

    cout << a << " " << b;
}