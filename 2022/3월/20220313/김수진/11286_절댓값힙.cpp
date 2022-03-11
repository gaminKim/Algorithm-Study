#include <iostream>
#include <queue>

using namespace std;

priority_queue <pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> q;

int main(void)
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int N;
    cin >> N;
    for(int i=0;i<N;i++){
        int cmd;
        cin >> cmd;
        
        if(cmd == 0){
            int num = 0;
            if(q.size()>0){
                num = q.top().second;
                q.pop();
            }
            cout << num << "\n";
        }
        else    q.push({abs(cmd),cmd});
    }
    
    return 0;
}
