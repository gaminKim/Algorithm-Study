//X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을
#include <iostream>
#include <queue>

#define MAX 100

using namespace std;

struct pos {
    int x,y;
};

queue<pos> snake;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,-1,0,1};

int map[MAX][MAX] = {0,};

int N,K,L;

int main(void)
{
    cin >> N >> K;
    for(int i=0;i<K;i++){
        int x,y;
        cin >> x >> y;
        map[x-1][y-1] = 1;
    }
    
    int L;
    cin >> L;
    queue <pair<int , char>> d;
    for(int i=0;i<L;i++){
        int s;
        char dir;
        cin >> s >> dir;
        d.push({s,dir});
    }
    
    int dir = 3;
    int time = 0;
    pos head = {0,0};
    map[0][0] = -1;
    snake.push({0,0});
    
    while(1){
        
        time++;
        
        int nx = head.x + dx[dir];
        int ny = head.y + dy[dir];
        
        if(nx < 0 || ny < 0 || nx >= N || ny >= N ) break;  //벽
        if( map[nx][ny] == -1)  break;  //자기 몸과 부딪힘
        
        head = {nx,ny};
        snake.push({nx,ny});
        
        if(map[nx][ny] == 0){
            pos tail = snake.front();
            map[tail.x][tail.y] = 0;
            snake.pop();
        }
        map[nx][ny] = -1;
        
        if(d.size() >0 && d.front().first == time){
            char rotate = d.front().second;
            if( rotate == 'L')  dir = dir == 3 ? 0 : dir+1;
            else dir = dir == 0 ? 3 :  dir -1;
            d.pop();
        }
    }
    cout << time;
    return 0;
}

