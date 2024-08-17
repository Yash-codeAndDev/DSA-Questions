import java.util.*;
public class Solution1
{
    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);
        int testCases = 0;
        int valX = 0;
        testCases = sc.nextInt();
        sc.nextLine();
        String[] arr = new String[testCases];
        for(int i=0;i<testCases;i++)
        {
            arr[i] = sc.nextLine();
        }
        
        for(int i=0;i<testCases;i++){
            
            if( arr[i].charAt(0) == '+'){
                valX++;
            }else if(arr[i].charAt(1) == '+'){
                valX++;
            }
            else if(arr[i].charAt(0) == '-'){
                valX--;
            }else{
                valX--;
            }
        }
        System.out.println(valX);
        sc.close();
	}
}