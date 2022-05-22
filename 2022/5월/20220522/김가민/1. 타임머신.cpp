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
	//간선은 n-1개
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
	//음의 사이클이 발생하는 지 확인
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
	//1번 정점과 연결된 2번 정점부터 탐색하면서 출력
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
	//초기화
	for (int i = 1; i <= n; ++i)
	{
		graph[i] = INF;
	}
	Bellman_Ford();
	return 0;
}