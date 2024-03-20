#include<bits/stdc++.h>
#include<iostream>

using namespace std;



void build(int index , int low,int high,int arr[],int seg[]){

    if(low==high){
        seg[index] = arr[low];
        return;
    }

    int mid = (low+high)/2;
    build(2*index+1,low,mid,arr,seg);
    build(2*index+2,mid+1,high,arr,seg);
    
    seg[index] = min(seg[2*index+1],seg[2*index+2]);

}

int query(int index,int low,int high,int l,int r,int seg[]){
    // no overlap 
    if(r<low || high<l ){
        return 100000;
    }
    //complete overlap
    if(low >= l && high <=r){
        return seg[index];
    }

    int mid = (low+high) >>1;

    int left = query(2*index+1,low,mid,l,r,seg);
    int right = query(2*index+2,mid+1,high,l,r,seg);
    return min(left,right);
}
void update(int index, int low, int high, int i, int val, int seg[]){
    if(low == high){
        seg[index] = val;
    }
    int mid = (low+high)/2;
    if (i <= mid){
        update(2*index+1, low, mid, i, val, seg);
    }
    else{
        update(2*index+2, mid+1, high, i, val, seg);
    }
    seg[index] = min(seg[2*index+1],seg[2*index+2]);
}
void solve(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int segmentTree[4*n];
    build(0,0,n-1,arr,segmentTree);
    // for(int i=0; i< (sizeof(segmentTree)/sizeof(segmentTree[0])); i++)
    // {
    //     cout<<segmentTree[i]<<" ";
    // }
    // cout<<endl;
    int q;
    cin>>q;
    while(q--)
    {

        int type;
        cin>>type;
        if(type == 1){
            int l,r;
            cin>>l>>r;
            cout<<query(0,0,n-1,l,r,segmentTree)<<endl;
        }
        else{
            int i, val;
            cin>>i>>val;
            update(0,0,n-1,i,val,segmentTree);
            arr[i] = val;
        }

    }
}

void solve2(){
    int n1;
    cin>>n1;
    int arr1[n1];
    for(int i=0; i<n1; i++){
        cin>>arr1[i];
    }
    
    int n2;
    cin>>n2;
    int arr2[n2];
    for(int i=0; i<n2; i++){
        cin>>arr2[i];
    }

}


int main()
{
    solve();
}