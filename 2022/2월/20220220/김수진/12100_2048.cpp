#include <iostream>
#define MAX 20

using namespace std;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

int map[MAX][MAX] = {0,};
int N;
int res = 0;

int findMaxVal()
{
    int max =0;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            max = map[i][j] > max ? map[i][j] : max;
        }
    }
    return max;
}

void copy(int arr1[MAX][MAX], int arr2[MAX][MAX])
{
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            arr2[i][j] = arr1[i][j];
        }
    }
}

void move(int dir)
{
    int tmp[MAX][MAX]={0,};
    for(int i=0;i<N;i++){
        if(dir == 0)
        {
            int idx =0;
            for(int j=0;j<N;j++)
            {
                if(map[j][i] != 0 ){
                    tmp[idx][i]=map[j][i];
                    idx++;
                }
            }
        }
        else if(dir == 1)
        {
            int idx =N-1;
            for(int j=N-1;j>=0;j--)
            {
                if(map[i][j] != 0 ){
                    tmp[i][idx]=map[i][j];
                    idx--;
                }
            }
        }
        else if(dir == 2)
        {
            int idx =N-1;
            for(int j=N-1;j>=0;j--)
            {
                if(map[j][i] != 0 ){
                    tmp[idx][i]=map[j][i];
                    idx--;
                }
            }
        }
        else if(dir == 3)
        {
            int idx =0;
            for(int j=0;j<N;j++)
            {
                if(map[i][j] != 0 ){
                    tmp[i][idx]=map[i][j];
                    idx++;
                }
            }
        }
    }
    copy(tmp,map);
}

void add(int dir)
{
        for(int i=0;i<N;i++){
            if(dir ==0 )
            {
                int idx =0;
                while(idx<N-1){
                    if(map[idx][i] == map[idx+1][i]){
                        map[idx][i] *= 2;
                        map[idx+1][i]=0;
                        idx+=2;
                    }
                    else    idx++;
                }
            }
            else if(dir ==1 )
            {
                int idx =N-1;
                while(idx>0){
                    if(map[i][idx] == map[i][idx-1]){
                        map[i][idx] *= 2;
                        map[i][idx-1]=0;
                        idx-=2;
                    }
                    else    idx--;
                }
            }
            else if(dir ==2 )
            {
                int idx =N-1;
                while(idx>0){
                    if(map[idx][i] == map[idx-1][i]){
                        map[idx][i] *= 2;
                        map[idx-1][i]=0;
                        idx-=2;
                    }
                    else    idx--;
                }
            }
            else if(dir ==3 )
            {
                int idx =0;
                while(idx<N-1){
                    if(map[i][idx] == map[i][idx+1]){
                        map[i][idx] *= 2;
                        map[i][idx+1]=0;
                        idx+=2;
                    }
                    else    idx++;
                }
            }
        }
}

void DFS(int cnt)
{
    if(cnt == 5){
        int maxVal = findMaxVal();
        res = res > maxVal ? res : maxVal;
        return;
    }
    for(int i=0;i<4;i++){
        int copymap[MAX][MAX]={0,};
        copy(map,copymap);
        move(i);
        add(i);
        move(i);
        DFS(cnt+1);
        copy(copymap,map);
    }
}

int main(void)
{
    cin >> N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin >> map[i][j];
        }
    }
    DFS(0);
    cout << res ;
    return 0;
}

