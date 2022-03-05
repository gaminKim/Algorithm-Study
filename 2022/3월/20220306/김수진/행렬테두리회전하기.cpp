#include <string>
#include <vector>
#define MAX 101

using namespace std;

struct pos{
    int x,y;
};

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    vector<vector<int>> map(rows + 1, vector<int>(columns + 1));

    int idx = 1;
    for(int i=1;i<=rows;i++)
    {
        for(int j=1;j<=columns;j++){
            map[i][j] = idx;
            idx++;
        } 
    }
    
    for(int i=0;i<queries.size();i++){
        
        vector<vector<int>> tmp(map);
        int min = 1e9;
        pos s= {queries[i][0],queries[i][1]};
        pos e= {queries[i][2],queries[i][3]};
        
        for(int x = s.x; x < e.x; x++){
            tmp[x][s.y] = map[x+1][s.y];
            if(tmp[x][s.y] < min)   min = tmp[x][s.y];   
        }
        for(int y = s.y; y < e.y; y++){
            tmp[e.x][y] = map[e.x][y+1];
            if(tmp[e.x][y] < min)   min = tmp[e.x][y];
        }
        for(int x = e.x; x > s.x; x--){
            tmp[x][e.y] = map[x-1][e.y];
            if(tmp[x][e.y] < min)   min =tmp[x][e.y];
        }
        for(int y = e.y; y > s.y; y--){
            tmp[s.x][y] = map[s.x][y-1];
            if(tmp[s.x][y] < min)   min = tmp[s.x][y];
        }
        answer.push_back(min);
        map = tmp;
    }
    return answer;
}
