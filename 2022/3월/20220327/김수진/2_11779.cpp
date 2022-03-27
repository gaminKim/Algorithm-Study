#include <iostream>
#include <vector>
#include <queue>
#define INF 1e9
#define MAX 1001

using namespace std;

struct info{
    int distance , node;
};

int dis[MAX]={0,};
int route[MAX]={0,};
vector <info> adj[MAX];
int N,M;
int s,e;

void dijkstra(int start)
{
    for(int i=1;i<=N;i++)   dis[i] = INF;
    priority_queue<pair<int, int>> pq;

    dis[start] = 0;
    pq.push({0,start});
    
    while(!pq.empty())
    {
        int cost = pq.top().first * -1;
        int node = pq.top().second;
        
        pq.pop();
        
        for(int i=0;i<adj[node].size();i++){
            
            int next = adj[node][i].node;
            int next_dis = adj[node][i].distance + cost;
            
            if(next_dis < dis[next]) {
                route[next] = node;
                dis[next] = next_dis;
                pq.push({-1 * next_dis , next});
            }
        }
    }
}

int main(void)
{
    cin >> N >> M;
    for(int i=0;i<M;i++){
        int start,end,dis;
        cin >> start >> end >> dis;
        adj[start].push_back({dis, end });
    }
    cin >> s >> e;
    dijkstra(s);
    
    vector <int> ans;
    int idx= e;
    while(idx != s){
        ans.push_back(idx);
        idx = route[idx];
    }
    ans.push_back(s);
    
    cout <<dis[e] <<"\n";
    int size = ans.size();
    cout << size << "\n";
    for(int i = size-1;i>=0;i--)    cout << ans[i] << " ";
    return 0;
}

