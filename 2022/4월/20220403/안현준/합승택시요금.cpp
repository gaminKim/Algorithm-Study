#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

int dist1[201];
int dist2[201][201];

priority_queue<pair<int,int>> pq1;
vector<pair<int,int>> v[201];
int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    for(int i =0;i<fares.size();i++){
        v[fares[i][0]].push_back({fares[i][1],fares[i][2]});
        v[fares[i][1]].push_back({fares[i][0],fares[i][2]});
    }
    memset(dist1,0x0f,sizeof(dist1));
    memset(dist2,0x0f,sizeof(dist2));
    pq1.push({0,s});
    while(!pq1.empty()){
        int d = pq1.top().first*-1;
        int node=pq1.top().second;
        pq1.pop();
        if(dist1[node] < d)
            continue;
        for(pair<int,int> next:v[node]){
            if(dist1[next.first] > d+next.second){
                dist1[next.first] = d+next.second;
                pq1.push({dist1[next.first]*-1, next.first});
            }
        }
    }
    dist1[s]=0;
    int answer=2000000000;
    for(int i=1;i<=n;i++){
        if(i==s){
            if(answer> dist1[a]+dist1[b])
                answer=dist1[a]+dist1[b];
            continue;
        }
        
        priority_queue<pair<int,int>> pq2;
        pq2.push({0,i});
        while(!pq2.empty()){
            int d = pq2.top().first*-1;
            int node=pq2.top().second;
            pq2.pop();
            if(dist2[i][node] < d)
                continue;
            for(pair<int,int> next:v[node]){
                if(dist2[i][next.first] > d+next.second){
                    dist2[i][next.first] = d+next.second;
                    pq2.push({dist2[i][next.first]*-1, next.first});
                }
            }
        }
        dist2[i][i]=0;
        if(answer> dist1[i]+dist2[i][a]+dist2[i][b])
            answer=dist1[i]+dist2[i][a]+dist2[i][b];
    } 
    return answer;
}