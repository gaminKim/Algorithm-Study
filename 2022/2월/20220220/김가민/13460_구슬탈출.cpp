#include<iostream>
#include<algorithm>
#include<math.h>
#include<cstring>
#include<fstream>
#include<queue>

using namespace std;
char map[10][11];	//문자열의 끝 종료지점을 받기 위해 11로 선언 함
int dy[4] = { -1, 1, 0, 0 };
int dx[4] = { 0, 0, -1, 1 };

struct INFO
{
	int rY, rX;
	int bY, bX;
	int cnt;
};
INFO start;
int BFS()
{
	queue<INFO> q;
	int checked[10][10][10][10] = { 0, };
	int res = -1;
	q.push(start);
	checked[start.rY][start.rX][start.bY][start.bX] = 1;
	while (!q.empty())
	{
		INFO curr = q.front();
		q.pop();

		if (curr.cnt > 10)
			break;
		if (map[curr.rY][curr.rX] == 'O' && map[curr.bY][curr.bX] != 'O')
		{
			res = curr.cnt;
			break;
		}
		for (int i = 0; i < 4; i++)
		{
			int next_ry = curr.rY;
			int next_rx = curr.rX;
			int next_by = curr.bY;
			int next_bx = curr.bX;
			while (1)
			{
				if (map[next_ry][next_rx] != '#'
					&& map[next_ry][next_rx] != 'O')
				{
					next_ry += dy[i];
					next_rx += dx[i];
				}
				else
				{
					if (map[next_ry][next_rx] == '#')
					{
						next_ry -= dy[i];
						next_rx -= dx[i];
					}
					break;
				}
			}
			while (1)
			{
				if (map[next_by][next_bx] != '#'
					&& map[next_by][next_bx] != 'O')
				{
					next_by += dy[i];
					next_bx += dx[i];
				}
				else
				{
					if (map[next_by][next_bx] == '#')
					{
						next_by -= dy[i];
						next_bx -= dx[i];
					}
					break;
				}
			}
			if (next_by == next_ry && next_rx == next_bx)
			{
				if (map[next_ry][next_rx] != 'O')
				{
					int red_dis = abs(next_ry - curr.rY)
						+ abs(next_rx - curr.rX);
					int blue_dis = abs(next_by - curr.bY)
						+ abs(next_bx - curr.bX);
					if (red_dis > blue_dis)
					{
						next_ry -= dy[i];
						next_rx -= dx[i];
					}
					else
					{
						next_by -= dy[i];
						next_bx -= dx[i];
					}
				}
			}

			if (checked[next_ry][next_rx][next_by][next_bx] == 0)
			{
				checked[next_ry][next_rx][next_by][next_bx] = 1;
				INFO next;
				next.rY = next_ry;
				next.rX = next_rx;
				next.bY = next_by;
				next.bX = next_bx;
				next.cnt = curr.cnt + 1;
				q.push(next);
			}
		}
	}
	return res;
}
void INPUT()
{
	int N, M;
	scanf("%d %d", &N, &M);

	for (int i = 0; i < N; ++i)
	{
		scanf("%s", map[i]);
	}
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			if (map[i][j] == 'R')
			{
				start.rY = i;
				start.rX = j;
			}
			if (map[i][j] == 'B')
			{
				start.bY = i;
				start.bX = j;
			}
		}
	}
	start.cnt = 0;
}
int main()
{
	int ans = 0;
	INPUT();
	ans = BFS();
	printf("%d\n", ans);
	return 0;
}