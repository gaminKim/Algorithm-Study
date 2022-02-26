#include <iostream>
#define MAX 10

using namespace std;

struct pos{
    int x,y;
};
int N,M;
int ans=11;
int map[MAX][MAX] = {0,};
int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};
pos red, blue;


pos move(int idx, pos npos)
{
    pos tmp = npos;
    while(1)
    {
        tmp.x += dx[idx];
        tmp.y += dy[idx];
        if(tmp.x < 0 || tmp.y < 0 || tmp.x >= N || tmp.y >= M || map[tmp.x][tmp.y] == -1)
        {
            tmp.x -= dx[idx];
            tmp.y -= dy[idx];
            break;
        }
        if( map[tmp.x][tmp.y] == 1) break;
    }
    return tmp;
}
int solve(int dir)
{
    pos nr = red;
    pos nb = blue;
    
    nr = move(dir, red);
    nb = move(dir, blue);

    
    if(map[nb.x][nb.y]==1)  return -1;
    else if(map[nr.x][nr.y]==1)  return 1;

    if(nr.x == nb.x && nr.y == nb.y)
    {
        switch(dir){
            case 0:
                red.x > blue.x ? nr.x++ : nb.x++;
                break;
            case 1:
                red.y < blue.y ? nr.y-- : nb.y--;
                break;
            case 2:
                red.x < blue.x ? nr.x-- : nb.x--;
                break;
            case 3:
                red.y > blue.y ? nr.y++ : nb.y++;
                break;
        }
    }
    red = nr;
    blue = nb;
    return 0;
    
}

void DFS(int cnt){
    if(cnt == 10)   return;
    for(int i=0;i<4;i++){
        pos red_tmp = red;
        pos blue_tmp = blue;
        
        int res = solve(i);
        if(res == -1)   continue;
        else if(res == 1){
            if( ans > cnt)   ans = cnt+1;
            return;
        }
        DFS(cnt+1);
        
        red  = red_tmp;
        blue = blue_tmp;
        
    }
}
int main(void)
{
    cin >> N >> M;
    
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            char ch;
            cin >> ch;
            if(ch == '#' )  map[i][j] = -1; // 장애물
            else if(ch == 'O')  map[i][j] = 1; // 골
            else if(ch == 'R')  red = {i,j};
            else if(ch == 'B')  blue = {i,j};
        }
    }
    DFS(0);
    if(ans == 11 )  cout << -1;
    else cout << ans;
    
    return 0;
}

