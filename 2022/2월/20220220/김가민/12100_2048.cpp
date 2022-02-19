#include <string>
#include <iostream>
#include <queue>
using namespace std;

int map[21][21];	//보드의 상태
int n, ans = 0;

void shift(int type)
{
	queue<int> q;
	switch (type)
	{
		//좌
	case 0:
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (map[i][j])
					q.push(map[i][j]);

				map[i][j] = 0;
			}
			int idx = 0;
			while (!q.empty())
			{
				int data = q.front();
				q.pop();
				if (map[i][idx] == 0)
				{
					map[i][idx] = data;
				}
				else if (map[i][idx] == data)
				{
					map[i][idx] *= 2;
					idx++;
				}
				else
				{
					idx++;
					map[i][idx] = data;
				}
			}
		}
		break;
		//우
	case 1:
		for (int i = 0; i < n; i++)
		{
			for (int j = n - 1; j >= 0; j--)
			{
				if (map[i][j])
					q.push(map[i][j]);

				map[i][j] = 0;
			}
			int idx = n - 1;
			while (!q.empty())
			{
				int data = q.front();
				q.pop();
				if (map[i][idx] == 0)
				{
					map[i][idx] = data;
				}
				else if (map[i][idx] == data)
				{
					map[i][idx] *= 2;
					idx--;
				}
				else
				{
					idx--;
					map[i][idx] = data;
				}
			}
		}
		break;
		//상
	case 2:
		for (int j = 0; j < n; j++)
		{
			for (int i = 0; i < n; i++)
			{
				if (map[i][j])
					q.push(map[i][j]);

				map[i][j] = 0;
			}
			int idx = 0;
			while (!q.empty())
			{
				int data = q.front();
				q.pop();
				if (map[idx][j] == 0)
				{
					map[idx][j] = data;
				}
				else if (map[idx][j] == data)
				{
					map[idx][j] *= 2;
					idx++;
				}
				else
				{
					idx++;
					map[idx][j] = data;
				}
			}
		}
		break;
		//하
	case 3:
		for (int j = 0; j < n; j++)
		{
			for (int i = n - 1; i >= 0; i--)
			{
				if (map[i][j])
					q.push(map[i][j]);

				map[i][j] = 0;
			}
			int idx = n - 1;
			while (!q.empty())
			{
				int data = q.front();
				q.pop();
				if (map[idx][j] == 0)
				{
					map[idx][j] = data;
				}
				else if (map[idx][j] == data)
				{
					map[idx][j] *= 2;
					idx--;
				}
				else
				{
					idx--;
					map[idx][j] = data;
				}
			}
		}
		break;
	}

}

void DFS(int cnt)
{
	if (cnt == 5)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				ans = max(ans, map[i][j]);
			}
		}
		return;
	}
	int backup[21][21];
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			backup[i][j] = map[i][j];
		}
	}
	for (int i = 0; i < 4; i++)
	{
		shift(i);
		DFS(cnt + 1);

		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				map[i][j] = backup[i][j];
			}
		}
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> map[i][j];
		}

	}

	DFS(0);
	cout << ans << "\n";
	return 0;
}