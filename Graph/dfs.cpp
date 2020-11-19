//question link
// https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/

#include<stdio.h>
#include<vector>
#include<iostream>
using namespace std;
int ans=0;
void dfs(vector<vector<int>> &matrix,int x, vector<int> &visited){
	if(visited[x]==0){
		visited[x]=1;
		int l=matrix[x].size();
		if(l==0)
			return; 
		for(int i=0;i<l;i++){
			if(visited[matrix[x][i]]==0){
				ans+=1;
				dfs(matrix,matrix[x][i],visited);
			}		
	    }
	}
	else
		return;
}
int main(){
	int n,m,i,a,b,x;
	cin>>n>>m;
	vector<vector<int>> matrix(n);
	vector<int> visited(n,0);
	for(i=0;i<n;i++){
		cin>>a>>b;
		matrix[a-1].push_back(b-1);
		matrix[b-1].push_back(a-1);
	}
	cin>>x;
	dfs(matrix,x-1,visited);
	cout<<n-ans-1;
	return 0;
}