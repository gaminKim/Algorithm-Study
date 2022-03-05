#include <iostream>
#define MAX 20

using namespace std;

int dx[4] = {0,0,-1,1};
int dy[4] = {1,-1,0,0};

int dice[6] = {0,};
int N,M;
int map[MAX][MAX]={0,};
int x,y; //현재 주사위 위치

void solve(int dir)
{
    dir--;
    int nx = x+dx[dir];
    int ny = y+dy[dir];
    if(nx <0 || ny < 0|| nx>= N || ny >= M) return ;
    x=nx;y=ny;
    int tmp = dice[0];
    switch(dir){
        case 0: //0,2,3,5
            dice[0] = dice[3];
            dice[3]=dice[5];
            dice[5]=dice[2];
            dice[2] = tmp;
            break;
        case 1: // 0,2,3,5
            dice[0] = dice[2];
            dice[2]=dice[5];
            dice[5]=dice[3];
            dice[3] = tmp;
            break;
        case 2: // 0,1,4,5
            dice[0] = dice[4];
            dice[4]=dice[5];
            dice[5]=dice[1];
            dice[1] = tmp;
            break;
        case 3: //0,1,4,5
            dice[0] = dice[1];
            dice[1]=dice[5];
            dice[5]=dice[4];
            dice[4] = tmp;
            break;
    }
    if(map[x][y]==0){
        map[x][y]=dice[5];
    }
    else{
        dice[5]=map[x][y];
        map[x][y]=0;
    }
    
    cout << dice[0]<<"\n";
            

}

int main(void)
{
    int K;
    cin >> N >> M;
    cin >> x >> y;
    cin >> K;
    
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++)    cin >> map[i][j];
    }
    
    for(int i=0;i<K;i++){
        int dir;
        cin >> dir;
        solve(dir);
    }
    return 0;
}

