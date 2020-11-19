//question link
// https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/

#include<stdio.h>
#include<vector>
#include<map>
#include<queue>
#include<iostream>
using namespace std;

int main(){
	int n,a,b,x,i,ans;
	cin >> n ;
	vector<vector<int>> d(n);
	queue<vector<int>> q;
	vector<int> visited(n,0),temp;
	for(i=0;i<n-1;i++){
		cin>> a >> b;
		d[a-1].push_back(b);
		d[b-1].push_back(a);
	}
	cin>>x;
	temp.clear();
	temp.push_back(1);
	temp.push_back(1);
	visited[0]=1;
	q.push(temp);
	while(!q.empty()){
		int l = q.front()[0];
		int s = d[l-1].size();
		if(q.front()[1]==x-1)
			{
				ans = s-1;
				break;
			}
		else{
			for(i=0; i<s; i++){
				temp.clear();
				if(visited[d[l-1][i]-1]==0)
				{
					temp.push_back(d[l-1][i]);
					temp.push_back(q.front()[1]+1);
					q.push(temp);
					visited[d[l-1][i]-1]=1;
				}
			}
		}
		q.pop();
	}
	cout<<ans;
}
