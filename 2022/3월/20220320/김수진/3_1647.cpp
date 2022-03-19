#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 100001

using namespace std;

struct info{
    int from,to,cost;
};
int N,M;
int res;
int parent[MAX]={0,};

bool comp(info a, info b)
{
    if(a.cost<b.cost)   return true;
    return false;
}

int find(int idx)
{
    if(idx == parent[idx])  return idx;
    else{
        parent[idx] = find(parent[idx]);
        return parent[idx];
    }
}

void Union(int idx1, int idx2)
{
    idx1 = find(idx1);
    idx2 = find(idx2);
    
    if(idx1 != idx2 ) // 서로 부모가 다르다면
    {
        parent[idx2] = idx1;
    }
}



int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    
    vector<info> edge;
    
    for(int i=0;i<M;i++){
        int from,to,cost;
        cin >> from >> to >>cost;
        edge.push_back({from,to,cost});
    }
    for(int i=1;i<=N;i++)   parent[i]=i;
    
    sort(edge.begin(),edge.end(),comp);
    
    int max_cost=0;
    int ans=0;
    
    for(int i=0;i<M;i++){
        
        int from = edge[i].from;
        int to = edge[i].to;
        int cost = edge[i].cost;
        
        int from_p = find(from);
        int to_p = find(to);
        
        if(from_p != to_p){
            Union(from,to);
            ans += cost;
            max_cost = max_cost > cost ? max_cost : cost;
        }
    }
    cout << ans - max_cost;
    return 0;
}

