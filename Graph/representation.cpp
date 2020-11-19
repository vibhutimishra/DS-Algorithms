
// question link 
// https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/tutorial/

#include<iostream>
#include<vector>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n,m;
    vector<vector<int>> matrix;
	vector<int> temp;
    cin>>n>>m;
	for(int j=0;j<n;j++){
		temp.push_back(0);
	}
    for(int i=0; i<n; i++){        
        matrix.push_back(temp);
    }
    for(int i=0;i<m;i++){
        int a,b;
        cin>>a>>b;
        matrix[a-1][b-1]=1;
        matrix[b-1][a-1]=1;
    }
    int q;
    cin>>q;
    for(int i=0;i<q;i++){
        int a,b;
        cin>>a>>b;
        if(matrix[a-1][b-1]==1)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
    return 0;
}