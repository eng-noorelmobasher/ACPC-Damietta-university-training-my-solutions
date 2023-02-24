#include <bits/stdc++.h>
#define ll long long
using namespace std;
 
int main()
{
	int n,v,m; cin >> n;
	int res=1;
	cin>>v;
	m = v;
	for(int i=1; i<n ; i++)
	{
	    cin >> v;
		if(v>m)
			res++;
		else break;
		m = v;
	}
	cout << res << "\n";
}