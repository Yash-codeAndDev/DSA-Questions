import java.util.Scanner;

public class Solution3 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int[][] mat = new int[5][5];
        int row = 0;
        int col = 0;
        for(int i =0 ; i<5; i++)
        {
            for(int j=0 ; j<5; j++)
            {
                mat[i][j] = sc.nextInt();

                if(mat[i][j] == 1){
                    row = i;
                    col = j;
                }
            }
        }
        
        int numMoves = Math.abs(row-2) +Math.abs(col-2);
        System.out.println(numMoves); 
    }
}
