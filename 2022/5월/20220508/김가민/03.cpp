#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;
int N, M;
int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };
string map[101];
bool checked[101][101];
int BFS()
{
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, 
        greater<pair<int, pair<int, int>>>> pq;
    pq.push({ 0, {0, 0} });
    checked[0][0] = true;
    
    while (!pq.empty())
    {
        int currR = pq.top().second.first;
        int currC = pq.top().second.second;
        int cnt = pq.top().first;
        pq.pop();

        if (currR == N - 1 && currC == M - 1)
            return cnt;

        for (int i = 0; i < 4; ++i)
        {
            int nextR = currR + dr[i];
            int nextC = currC + dc[i];
            if (nextR >= 0 && nextR <N && nextC >= 0 && nextC < M
                &&!checked[nextR][nextC])
            {
                if (map[nextR][nextC] == '1')
                    pq.push({ cnt + 1, {nextR, nextC} });

                else
                    pq.push({ cnt, {nextR, nextC} });

                checked[nextR][nextC] = true;
            }
        }
    }
}

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> M >> N;

    for (int i = 0; i < N; ++i)
    {
            cin >> map[i];
    }
    cout << BFS() << "\n";
    return 0;
}