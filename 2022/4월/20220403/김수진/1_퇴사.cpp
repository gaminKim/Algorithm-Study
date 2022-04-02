#include <iostream>
#define MAX 17

using namespace std;

int T[MAX];
int P[MAX];
int DP[MAX]={0,};

int main(void)
{
    int N;
    scanf("%d",&N);
    
    for(int i=1;i<=N;i++)    scanf("%d %d",&T[i], &P[i]);
        
    for(int i=N ;i>=1; i--)   {
        if(i + T[i] -1 > N){
            DP[i] = DP[i+1];
            continue;
        }
        DP[i]= max(DP[i+1], P[i]+DP[i + T[i]]);
    }
    cout << DP[1];
    return 0;
    
}

