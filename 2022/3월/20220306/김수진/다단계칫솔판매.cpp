//이익금의 총 합
// union-find 쓰면 되지않을까.. 
#include <string>
#include <vector>
#include <map>
#define MAX 10000

using namespace std;

map <string, int> m;
int parent[MAX]={0,};
int profit[MAX]={0,};

void solve(int idx ,int amount)
{
    if( idx == -1 ) return;
    int divide = amount/10;
    profit[idx] += amount - divide;
    if(divide == 0 )    return ;
    solve(parent[idx], divide);
}

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    vector<int> answer;
    
    for(int i=0;i<enroll.size();i++)    m[enroll[i]] =i;
    for(int i=0;i<referral.size();i++){
        if(referral[i].compare("-")==0)    parent[i] = -1;
        else    parent[i] = m[referral[i]];        
    }
    for(int i=0;i<seller.size();i++){
        solve(m[seller[i]], amount[i] * 100);
    }
    for(int i=0;i<enroll.size();i++)    answer.push_back(profit[i]);
    return answer;
}
