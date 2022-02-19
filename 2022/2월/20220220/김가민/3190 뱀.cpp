#include <string>
#include <iostream>

using namespace std;

int map[101][101];	//보드의 상태
int n, k, l;
int head_x, head_y;	//뱀의 머리 위치
int snack_x[10001], snack_y[10001];	//초당 뱀의 위치
char dir[10001];	//뱀의 방향변환 정보를 담을 배열
//뱀의 방향 우상좌하
int dr[4] = { 0, -1, 0, 1 };
int dc[4] = { 1, 0, -1, 0 };

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> n >> k;
	for (int i = 0; i < k; i++)
	{
		int a, b;
		cin >> a >> b;
		map[a][b] = 1;
	}
	cin >> l;
	for (int i = 0; i < l; i++)
	{
		int sec;
		char d;
		cin >> sec >> d;
		dir[sec] = d;
	}
	int time = 0, dir_index = 0, tail_x, tail_y, tail_idx = 0;
	//초기 뱀의 위치
	head_x = 1, head_y = 1;
	tail_x = 1, tail_y = 1;
	snack_x[time] = 1, snack_y[time] = 1;
	map[head_y][head_x] = -1;
	while (true)
	{
		time++;
		int next_y = head_y + dr[dir_index];
		int next_x = head_x + dc[dir_index];
		if (next_x <= 0 || next_x > n || next_y <= 0 || next_y > n || map[next_y][next_x] == -1)
			break;
		snack_y[time] = next_y;
		snack_x[time] = next_x;
		tail_x = snack_x[tail_idx];
		tail_y = snack_y[tail_idx];

		if (map[next_y][next_x] == 0)
		{
			//snack_y[time] = next_y;
			//snack_x[time] = next_x;
			map[tail_y][tail_x] = 0;
			tail_idx++;
		}
		head_x = next_x;
		head_y = next_y;
		map[next_y][next_x] = -1;	//뱀을 위치 시킴
		if (dir[time] == 'L')
		{
			dir_index = (dir_index + 1) % 4;
		}
		else if (dir[time] == 'D')
		{
			dir_index = (dir_index + 3) % 4;
		}
	}
	cout << time << "\n";
	return 0;
}