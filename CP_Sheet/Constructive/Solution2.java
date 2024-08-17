import java.util.Scanner;

public class Solution2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        StringBuilder result = new StringBuilder(str);

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            // Check if it's the first digit and should be inverted
            if (i == 0 && c >= '5' && c < '9') {
                result.setCharAt(i, (char) ('9' - c + '0'));
            }
            
            // Check for other digits
            else if (i > 0 && c >= '5') {
                result.setCharAt(i, (char) ('9' - c + '0'));
            }
        }
        
        System.out.println(result.toString());
        sc.close();
    }
}
