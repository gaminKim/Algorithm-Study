#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int N, M;
int map[8][8];
int visit[8][8];
int temp[8][8];
queue<pair<int,int>> q;
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int answer;

bool isRange(int x, int y)
{
	return x >= 0 && y >= 0 && x < N&&y < M;
}

int bfs(int i, int j)
{
	q.push({ i,j });
	visit[i][j] = 1;
	int cnt = 0;
	while (!q.empty())
	{
		int x = q.front().first;
		int y = q.front().second;
		for (int k = 0; k < 4; k++)
		{
			int nx = x + dx[k];
			int ny = y + dy[k];
			if (isRange(nx, ny) && temp[nx][ny] == 0)
			{
				temp[nx][ny] = 2;
				visit[nx][ny] = 1;
				q.push({ nx,ny });
			}
		}
		cnt++;
		q.pop();
	}
	return cnt;
}


int spread()
{	
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			temp[i][j] = map[i][j];
		}
	}
	int ret = 0;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (temp[i][j] == 2 && visit[i][j]==0)
			{
				ret += bfs(i, j);
			}
			if (temp[i][j] == 1)
			{
				ret++;
			}
		}
	}
	return ret;
}

void wall(int cnt)
{
	if (cnt == 3)
	{
		memset(visit, 0, sizeof(visit));
		answer = max(answer, N*M - spread());
		return;
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (map[i][j] == 0)
			{
				map[i][j] = 1;
				wall(cnt + 1);
				map[i][j] = 0;
			}
		}
	}
}




int main()
{
	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> map[i][j];
		}
	}
	wall(0);
	cout << answer;
}