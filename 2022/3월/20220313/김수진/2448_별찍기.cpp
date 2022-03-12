#include <iostream>
#define MAX 10000

using namespace std;

char star[MAX][MAX];

void draw(int row, int col)
{
    star[row][col]='*';
    
    star[row+1][col-1]='*';
    star[row+1][col+1]='*';
    
    star[row+2][col-2]='*';
    star[row+2][col-1]='*';
    star[row+2][col]='*';
    star[row+2][col+1]='*';
    star[row+2][col+2]='*';
}

void solve(int len, int row, int col)
{
    if (len == 3)
    {
        draw(row, col);
        return;
    }
        
    solve(len / 2, row, col);  // 첫 번째 삼각형의 꼭짓점
    solve(len / 2, row + len / 2, col - len / 2);  // 두 번째 삼각형의 꼭짓점
    solve(len / 2, row + len / 2, col + len / 2);  // 세 번째 삼각형의 꼭짓점
}

int main(void)
{
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);

    int N;
    cin >> N;
    for(int i=0;i<N;i++){
        for(int j=0;j<2*N-1;j++)    star[i][j]=' ';
    }
    
    solve(N,0,N-1);
    
    for(int i=0;i<N;i++){
        for(int j=0;j<2*N-1;j++){
            cout << star[i][j];
        }
        cout << "\n";
    }
    return 0;
}

