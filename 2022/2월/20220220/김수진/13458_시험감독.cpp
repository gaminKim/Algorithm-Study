//총감독 오직 1명
#include <iostream>
#include <cmath>
#define MAX 1000000
using namespace std;

int main(void)
{
    int A,B,C;
    int student[MAX]={0,};
    
    cin >> A;
    for(int i=0;i<A;i++)    cin>> student[i];
    cin >> B >> C;
    
    //감독관의 총 수는 최대 백만 * 백만 = 1조
    long long cnt =0;
    for(int i=0;i<A;i++){
        cnt++;
        student[i] -= B;
        if(student[i] > 0 ){
            double res = (double)student[i]/(double)C; //연산 결과를 double으로 하기 위해
            cnt+=ceil(res); // 올림
        }
    }
    cout << cnt;
    return 0;
}
