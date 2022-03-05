#include <iostream>
#define MAX 500

using namespace std;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

int map[MAX][MAX] = {0,};
bool visited[MAX][MAX] = {0,};

int N,M;
int res = 0;

void solve(int x, int y)
{
    //ㅗ
    if(x-1 >= 0 && y-1 >= 0 && y+1 < M )    res = max(res, map[x][y-1]+ map[x][y] + map[x][y+1] + map[x-1][y] );
    //ㅏ
    if( x-1 >= 0 && x+1 < N && y+1 < M )    res = max(res, map[x-1][y] + map[x][y] + map[x+1][y] + map[x][y+1]);
    //ㅜ
    if( y-1 >= 0 && y+1 < M && x+1 < N)     res = max(res, map[x][y] + map[x][y-1] + map[x][y+1] + map[x+1][y]);
    //ㅓ
    if(y-1 >= 0 && x-1 >= 0 && x+1 < N)     res = max(res, map[x][y] + map[x][y-1] + map[x-1][y] + map[x+1][y]);
}

void DFS(int cnt , int sum ,int x, int y)
{
    if(cnt == 4){
        if( sum > res ) res= sum;
        return ;
    }
    for(int i=0;i<4;i++){
        int nx = x +dx[i];
        int ny = y + dy[i];
        if( nx <0 || ny <0 || nx >= N || ny >= M || visited[nx][ny])   continue;
        visited[nx][ny]=1;
        DFS(cnt+1,sum+map[nx][ny],nx,ny);
        visited[nx][ny]=0;
    }
}

int main(void)
{
    cin >> N >> M;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++)    cin >> map[i][j];
    }
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            visited[i][j]=1;
            DFS(1,map[i][j],i,j);
            solve(i,j);
            visited[i][j]=0;
        }
    }
    cout << res;
    return 0;
}

