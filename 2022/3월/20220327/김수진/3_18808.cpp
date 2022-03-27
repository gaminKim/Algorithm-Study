#include <iostream>
#define MAX 40

using namespace std;

int N,M,K;
int R,C;
int res=0;
int paper[MAX][MAX]={0,};
int sticker[10][10]={0,};

void rotate()
{
    int tmp[10][10]={0,};
    
    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            tmp[j][R-1-i] = sticker[i][j];
        }
    }
    swap(R,C);

    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            sticker[i][j] = tmp[i][j];
        }
    }
}

bool attach(int x, int y)
{
    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            if(x+i >= N || y+j >=M) return false;
            if(paper[x+i][y+j] && sticker[i][j])    return false;
        }
    }
    
    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            if(sticker[i][j])    paper[x+i][y+j]=1;
        }
    }
    return true;
}

bool solve(){
    for(int r =0;r<4;r++)
    {
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                /*
                 종이 1, 스티커 1  불가능
                 종이 0,  스티커 1 가능
                 종이 1, 스티커 0 가능
                 종이 0, 스티커 0 가능
                 */
                if( paper[i][j] && sticker[0][0])   continue;
                if(attach(i,j)) return true;
            }
        }
        rotate();
    }
    return false;
}

int main(void)
{
    cin >> N >> M >> K;
    for(int l=0;l<K;l++){
        cin >> R >> C;
        int size = 0;
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                cin >> sticker[i][j];
                if(sticker[i][j])   size++;
            }
        }
        if(solve()) res+=size;
    }
    
    cout << res;
    
    return 0;
}


