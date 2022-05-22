#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
int DP[1001][1001];
string a, b;
string result;
int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    string str1, str2;

	cin >> str1;
	cin >> str2;

	a = ' ' + str1;
	b = ' ' + str2;


	for (int i = 1; i < b.size(); i++) 
	{
		for (int j = 1; j < a.size(); j++) 
		{
			if (a[j] == b[i]) DP[i][j] = DP[i - 1][j - 1] + 1;
			else
				DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]);
		}
	}



	int col = a.size() - 1;
	int row = b.size() - 1;

	while (DP[row][col]) 
	{

		if (DP[row][col] == DP[row - 1][col]) 
		{
			row--;
		}
		else if (DP[row][col] == DP[row][col - 1]) 
		{
			col--;
		}
		else 
		{
			result += a[col];
			row--, col--;
		}

	}

	cout << DP[b.size() - 1][a.size() - 1] << "\n";
	if (result.size() > 0) 
	{
		reverse(result.begin(), result.end());
		cout << result << "\n";
	}
    return 0;
}
