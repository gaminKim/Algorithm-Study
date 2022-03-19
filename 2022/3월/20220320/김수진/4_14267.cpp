#include <iostream>
#include <vector>

#define MAX 100001

using namespace std;

vector<int> adj[MAX];
int ans[MAX]={0,};
int praise[MAX]={0,};

void DFS(int idx, int w)
{
    ans[idx] += w;
    for(int i=0;i<adj[idx].size();i++)  DFS(adj[idx][i] , w);
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int N,M;
    cin >> N >> M;
    
    for(int i=1;i<=N;i++){
        int p;
        cin >> p;
        if(p != -1) adj[p].push_back(i);
    }
    
    for(int i=0;i<M;i++)
    {
        int idx,w;
        cin >> idx >> w;
        praise[idx] +=w;
    }
    for(int i=2;i<=N;i++){
        if(praise[i] > 0 )  DFS(i,praise[i]);
    }
    for(int i=1;i<=N;i++)   cout << ans[i] << " ";
    
    return 0;
}

