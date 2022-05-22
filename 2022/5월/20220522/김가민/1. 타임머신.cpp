#include <string>
#include <vector>
#include <iostream>
#define MAX 501
#define INF 987654321
using namespace std;
int n, m;
vector<pair<pair<int, int>, int>> adj;
long long graph[MAX];

void Bellman_Ford()
{
	graph[1] = 0;
	//������ n-1��
	for (int i = 1; i <= n - 1; ++i)
	{
		for (int j = 0; j < adj.size(); ++j)
		{
			int from = adj[j].first.first;
			int to = adj[j].first.second;
			int cost = adj[j].second;

			if (graph[from] == INF)
				continue;
			if (graph[to] > graph[from] + cost)
				graph[to] = graph[from] + cost;
		}
	}
	//���� ����Ŭ�� �߻��ϴ� �� Ȯ��
	for (int j = 0; j < adj.size(); ++j)
	{
		int from = adj[j].first.first;
		int to = adj[j].first.second;
		int cost = adj[j].second;

		if (graph[from] == INF)
			continue;
		if (graph[to] > graph[from] + cost)
		{
			cout << -1 << "\n";
			return;
		}
	}
	//1�� ������ ����� 2�� �������� Ž���ϸ鼭 ���
	for (int i = 2; i <= n; ++i)
	{
		if (graph[i] == INF)
			cout << -1 << "\n";
		else
			cout << graph[i] << "\n";
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> m;
	for (int i = 0; i < m; ++i)
	{
		int a, b, c;
		cin >> a >> b >> c;
		adj.push_back(make_pair(make_pair(a, b), c));
	}
	//�ʱ�ȭ
	for (int i = 1; i <= n; ++i)
	{
		graph[i] = INF;
	}
	Bellman_Ford();
	return 0;
}