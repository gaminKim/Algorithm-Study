#include <iostream>
#include <queue>

using namespace std;

priority_queue <int,vector<int>,greater<int>> q;

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
                num = q.top();
                q.pop();
            }
            cout << num << "\n";
        }
        else    q.push(cmd);
    }
    
    return 0;
}
