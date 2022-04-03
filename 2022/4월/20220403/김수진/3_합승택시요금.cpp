#include <string>
#include <algorithm>
#include <vector>
#define MAX 201
#define INF 99999999

using namespace std;

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    int answer = INF;
    int dp[MAX][MAX]={0,};
    
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(i==j)    dp[i][j]=0;
            else    dp[i][j]=INF;
        }
    }
    for(int i=0;i<fares.size();i++){
        dp[fares[i][0]][fares[i][1]] = fares[i][2];
        dp[fares[i][1]][fares[i][0]] = fares[i][2];
    }
    for(int k=1;k<=n;k++){
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                dp[i][j]= min(dp[i][j],dp[i][k]+dp[k][j]);
            }
        }
    }
    for(int i=1;i<=n;i++){
        answer = min(answer,dp[s][i]+dp[i][a]+dp[i][b]);
    }
    return answer;
}
