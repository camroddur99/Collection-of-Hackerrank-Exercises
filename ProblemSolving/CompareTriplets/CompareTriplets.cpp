#include<cmath>
#include<cstdio>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
int main(){
	int suma=0,sumb=0;
	vector <int> a(3);
	vector <int> b(3);
	for(int i=0;i<3;i++){
		cin>>a[i];
	}
	for(int i=0;i<3;i++){
		cin>>b[i];
	}
	for(int i=0;i<3;i++){
		if (a[i]>b[i]){
			suma += 1;
		}
		else if(b[i]>a[i]){
			sumb += 1;
		}
	}
	cout << suma<<" "<<sumb;
	return 0;
}
