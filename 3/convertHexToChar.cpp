#include<iostream>
using namespace std;
int main()
{
	int x;
	cin>>x;
	while(x)
	{
		int u=(x/10)*16 + x%10;
		cout<<(char)u;
		cin>>x;
	}
	return 0;
}
