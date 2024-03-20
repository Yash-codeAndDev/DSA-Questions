#include<bits/stdc++.h>
#include<iostream>

using namespace std;


class SegmentTree{

    vector<int> seg;
    public:
    SegmentTree(int n){
        seg.resize(4*n+1);
        for(int i=0; i<(4*n+1); i++)
        {
            seg[i] = -1;
        }
    }        

    void build(int index , int low,int high,int arr[]){

        if(low==high){
            seg[index] = arr[low];
            return;
        }

        int mid = (low+high)/2;
        build(2*index+1,low,mid,arr);
        build(2*index+2,mid+1,high,arr);
        
        seg[index] = min(seg[2*index+1],seg[2*index+2]);

    }

    int query(int index,int low,int high,int l,int r){
        // no overlap 
        if(r<low || high<l ){
            return 100000;
        }
        //complete overlap
        if(low >= l && high <=r){
            return seg[index];
        }

        int mid = (low+high) >>1;

        int left = query(2*index+1,low,mid,l,r);
        int right = query(2*index+2,mid+1,high,l,r);
        return min(left,right);
    }
    
    void update(int index, int low, int high, int i, int val){
        if(low == high){
            seg[index] = val;
            return;
        }
        int mid = (low+high)/2;
        if (i <= mid){
            update(2*index+1, low, mid, i, val);
        }
        else{
            update(2*index+2, mid+1, high, i, val);
        }
        seg[index] = min(seg[2*index+1],seg[2*index+2]);
    }

    void printSeg()
    {
        for(int i=0;i<seg.size(); i++){
            if(seg[i] != -1){
                cout<<seg[i]<<" ";
            }
        }
        cout<<endl;
    }
};

/*
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
*/
void solve2(){
    cout<<"Array1 size : ";
    int n1;
    cin>>n1;
    int arr1[n1];
    cout<<"Array1 input : ";
    for(int i=0; i<n1; i++){
        cin>>arr1[i];
    }
    
    SegmentTree sg1(n1);
    sg1.build(0,0,n1-1,arr1);
    sg1.printSeg();
    
    cout<<"Array2 size : "; 
    int n2;
    cin>>n2;
    int arr2[n2];
    cout<<"Array1 input : ";
    for(int i=0; i<n2; i++){
        cin>>arr2[i];
    }
    SegmentTree sg2(n2);
    sg2.build(0,0,n2-1,arr2);
    sg2.printSeg();

    int q;
    cout<<"Number of Querry : ";
    cin >>q;

    while(q--){
        int type;

        cout<<"Type : ";
        cin>>type;
        if(type == 1){
            int l1,r1,l2,r2;
            cin>>l1>>r1>>l2>>r2;

            int min1 = sg1.query(0,0,n1-1,l1,r1);
            int min2 = sg2.query(0,0,n2-1,l2,r2);
            cout<<min(min1,min2)<<endl;
        }
        else{
            int arrNo, i, val;
            cin>>arrNo>>i>>val;

            if(arrNo == 1){
                sg1.update(0,0,n1-1,i,val);
                arr1[i] = val;
                sg1.printSeg();
            }else{
                sg2.update(0,0,n2-1,i,val);
                arr2[i] = val;
                sg2.printSeg();
            }

        }
    }

}


int main()
{
    // solve();
    solve2();
}