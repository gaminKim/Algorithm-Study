#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#define MAX_CARD 7
#define MAX 4

using namespace std;
/*1. 카드 순서 선택 2. 가까운 카드부터 */

struct info{
    int x,y,cnt;
};

vector<vector<int>> tmp_board;
vector<int> card;
int cx,cy;
int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

int BFS(int dest)
{
    bool visited[MAX][MAX]={0,};
    queue<info> q;
    q.push({cx,cy,0});
    visited[cx][cy]=1;
    
    while(!q.empty()){
        int x = q.front().x;
        int y = q.front().y;
        int cnt = q.front().cnt;
        q.pop();
        
        if(tmp_board[x][y] == dest){
            tmp_board[x][y] =0;
            cx=x;
            cy=y;
            return cnt+1;
        }
        
        for(int i=0;i<4;i++){
            int nx = x+dx[i];
            int ny = y+dy[i];
            if(nx<0 || ny <0 || nx >= MAX || ny >= MAX || visited[nx][ny])  continue;
            q.push({nx,ny,cnt+1});
            visited[nx][ny]=1;
        }
        for(int i=0;i<4;i++){
            int nx = x;
            int ny = y;
            while( nx+dx[i]>=0 && ny+dy[i]>=0 && nx+dx[i] < MAX && ny+dy[i] < MAX){
                nx+=dx[i];
                ny+=dy[i];
                if(tmp_board[nx][ny] != 0)  break;
            }
            if(visited[nx][ny] )    continue;
            visited[nx][ny]=1;
            q.push({nx,ny,cnt+1});
        }
    }
}
int solution(vector<vector<int>> board, int r, int c) {
    int answer = 1e9;
    bool card_check[7] = {0,};
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++)    if(board[i][j]!=0)  card_check[board[i][j]] = 1;
    }
    for(int i=0;i<7;i++)    if(card_check[i])   card.push_back(i);
    
    do{
        int res =0;
        cx=r; 
        cy=c;
        tmp_board = board;
        for(int i=0;i<card.size();i++){
            res += BFS(card[i]);
            res += BFS(card[i]);
        }
        answer = min(answer, res);
    }while(next_permutation(card.begin(),card.end()));
    
    return answer;
}
