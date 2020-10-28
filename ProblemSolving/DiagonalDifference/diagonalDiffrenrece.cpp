#include<stdio.h>
#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
	int x, sum1 = 0, sum2 = 0,i = 0, j = 0,total;
	cin >> x;
	for(i=0;i<x;i++){
		for(j=0;j<x;j++){
			int arr;
			cin>>arr;
			if(i==j){
				sum1 += arr;
			}
			if(i+j == x-1){
				sum2 += arr;
			}
		}
	}
	total = sum1 - sum2;
	if(total<0){
		total = total *(-1);
	}
	cout<<total;
	return 0;
}

