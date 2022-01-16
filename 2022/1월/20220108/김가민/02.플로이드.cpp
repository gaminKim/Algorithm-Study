#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
int INF = 100000000;
int floyd[101][101];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n;
    cin >> m;
    //무한대로 초기화
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= n; ++j)
        {
            floyd[i][j] = INF;
        }
    }
    //값 입력 받으면서 최솟값만 넣어주기
    for (int i = 0; i < m; ++i)
    {
        int a, b, c;
        cin >> a >> b >> c;
        floyd[a][b] = min(floyd[a][b], c);
    }
    //플로이드 와샬 구현
    for (int k = 1; k <= n; ++k)
    {
        for (int i = 1; i <= n; ++i)
        {
            for (int j = 1; j <= n; ++j)
            {

                if (floyd[i][k] + floyd[k][j] < floyd[i][j])
                    floyd[i][j] = floyd[i][k] + floyd[k][j];
            }
        }
    }

    //출력
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= n; ++j)
        {
            if (floyd[i][j] == INF || i == j)
                cout << 0 << " ";
            else
                cout << floyd[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}