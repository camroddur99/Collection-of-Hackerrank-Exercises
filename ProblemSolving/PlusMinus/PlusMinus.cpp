#include<cmath>
#include<cstdio>
#include<vector>
#include<iostream>
#include<algorithm>
#include<iomanip>
using namespace std;
int main(){
	int n,pos=0,neg=0,zer=0;
	float posd,negd,zerd;
	cin>>n;
	vector<int> arr(n);
	for(int i=0;i<n;i++){
		cin>>arr[i];
		if (arr[i] < 0){
			neg += 1;
		}
		else if (arr[i] > 0){
			pos += 1;
		}
		else{
			zer += 1;
		}
	}
	posd = (float)pos/(float)n;
	negd = (float)neg/(float)n;
	zerd = (float)zer/(float)n;
	std::cout<<std::fixed;
	std::cout<<std::setprecision(6);
	std::cout<<posd<<"\n"<<negd<<"\n"<<zerd;
	return 0;
}
