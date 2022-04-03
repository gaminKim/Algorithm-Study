/*
 3개의 벽
 0은 빈 칸, 1은 벽, 2는 바이러스가
 */
#include <iostream>
#include <vector>
#include <queue>


#define MAX 8

using namespace std;

struct pos{
    int x,y;
};

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

vector<pos> empty_pos;

int N,M;
int map[MAX][MAX]={0,};
int res =0;

void BFS()
{
    queue <pos> q;
    int tmp[MAX][MAX]={0,};

    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            tmp[i][j]=map[i][j];
            if ( tmp[i][j]== 2 )    q.push({i,j});
        }
    }
    
    while(!q.empty()){
        int x = q.front().x;
        int y = q.front().y;
        q.pop();
        for(int i=0;i<4;i++){
            int nx = x+dx[i];
            int ny = y+dy[i];
            
            if( nx >= 0 && nx < N && ny >= 0 && ny < M && tmp[nx][ny] == 0){
                tmp[nx][ny] = 2;
                q.push({nx,ny});
            }
        }
    }
    int cnt = 0;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            if ( tmp[i][j]== 0 )    cnt++;
        }
    }
    if ( cnt > res )    res = cnt;
}

void DFS(int idx , int cnt)
{
    if(cnt == 3){
        BFS();
        return ;
    }
    
    for(int i=idx;i<empty_pos.size();i++){
        pos e = empty_pos[i];
        map[e.x][e.y]=1;
        DFS(i+1,cnt+1);
        map[e.x][e.y]=0;
    }
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cin >> map[i][j];
            if ( map[i][j] == 0 )   empty_pos.push_back({i,j});
        }
    }
    
    DFS(0,0);
    cout << res;
    
    return 0;
}

