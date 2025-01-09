/*
  You are given an array of size 𝑁, denoted as 𝐴[0 … 𝑁−1], and a list of 𝑄 queries. Each query is one of two types:
    Type 1: Find the maximum number in the array within a specific range [L,R] (inclusive).
    Type 2: Update the value at a specific index idx in the array with a new value val.
*/
package SegmentTree;

import java.util.Arrays;
import java.util.Scanner;

public class MaxInArray {

    static int[] segmentTree;

    public static void build(int indx, int start, int end,int[] arr){
        if(start == end){
            segmentTree[indx] = arr[start];
            return;
        }
        int mid = (start+end)/2;
        build(2*indx+1,start,mid,arr);
        build(2*indx+2,mid+1,end,arr);
        segmentTree[indx] = Math.max(segmentTree[2*indx+1],segmentTree[2*indx+2]);
    }

    public static  int queriesSol(int indx, int start,int end,int ql, int qr){
        if(qr < start || ql > end){
            return Integer.MIN_VALUE;
        }

        if(ql <= start && qr >= end){
            return  segmentTree[indx];
        }
        int mid = (start+end)/2;
        int left = queriesSol(2*indx+1,start,mid,ql,qr);
        int right = queriesSol(2*indx+2,mid+1,end,ql,qr);

        return Math.max(left,right);
    }

    public static  void update(int indx,int start, int end,int uIndx, int cValue){

        if(start == end){
            segmentTree[indx]  = cValue;
        }
        else{

            int mid = (start+end)/2;

            if( start<=uIndx &&  uIndx<= mid){
                update(2*indx+1, start,mid,uIndx,cValue);
            }
            else if( (mid+1)<= uIndx && uIndx <= end ){
                update(2*indx+2, mid+1,end,uIndx,cValue);
            }
            segmentTree[indx] = Math.max(segmentTree[2*indx+1], segmentTree[2*indx+2] );
        }

    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);


        int N;
        System.out.println("Enter Array Size : ");
        N = sc.nextInt();
        int[] arr = new int[N];
        System.out.println("Enter Array Elements");
        for(int i=0;i<N;i++){
            arr[i] = sc.nextInt();
        }
        segmentTree = new  int[N*4];

        build(0,0,N-1,arr);
        System.out.println(Arrays.toString(segmentTree));

        int Q;
        System.out.println("Enter Number of Querries : ");
        Q = sc.nextInt();
        System.out.println("Querries : ");
        System.out.println("type 1 : from - to");
        System.out.println("type 2 : indexToChange - newValue");

        String[][] queries = new String[Q][3];
        for(int i=0; i<Q; i++){
            queries[i][0] = sc.next();
            queries[i][1] = sc.next();
            queries[i][2] = sc.next();

            if(queries[i][0].equals("1"))
            {
                int from = Integer.parseInt(queries[i][1]);
                int to = Integer.parseInt(queries[i][2]);

                int sol = queriesSol(0,0,N-1,from,to);
                System.out.println("Answer : " + sol);
            }
            else{
                int uIndex = Integer.parseInt(queries[i][1]);
                int cVal = Integer.parseInt(queries[i][2]);
                arr[uIndex] = cVal;
                update(0,0,N-1,uIndex,cVal);
                System.out.println("Updated");
            }
        }
    }
}
