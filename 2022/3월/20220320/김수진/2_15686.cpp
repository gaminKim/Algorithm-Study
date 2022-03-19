/*
 0은 빈 칸, 1은 집, 2는 치킨집이다.
 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오
 */
#include <iostream>
#include <vector>
#define MAX 50

using namespace std;

struct pos {
    int x,y;
};

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

bool visited[MAX] = {0,};
int map[MAX][MAX]={0,};
int N,M;
int ans=1e9;

vector<pos> chicken;
vector<pos> house;

int calcDistance()
{
    int res =0;
    
    for(int i=0;i<house.size();i++){
        int hx = house[i].x;
        int hy = house[i].y;
        int dis =1e9;
        
        for(int j=0;j<chicken.size();j++){
            if(!visited[j]) continue;
            int cx = chicken[j].x;
            int cy = chicken[j].y;
            
            int dx = hx > cx ? hx-cx : cx-hx;
            int dy = hy > cy ? hy-cy : cy-hy;
            
            if( dis > dx+dy)    dis = dx+dy;
        }
        res+=dis;
    }
    return res;
}

void DFS(int idx, int cnt){
    if(cnt == M){
        int res =calcDistance();
        ans = res < ans ? res : ans;
    }
    
    for(int i=idx;i<chicken.size();i++){
        visited[i] = 1;
        DFS(i+1,cnt+1);
        visited[i] = 0;
    }
}
int main(void){
    cin >> N >> M;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin >> map[i][j];
            if(map[i][j] == 1)  house.push_back({i,j});
            else if(map[i][j] == 2) {
                chicken.push_back({i,j});
                map[i][j]=0;
            }
        }
    }
    
    DFS(0,0);
    cout << ans;
    return 0;
}


