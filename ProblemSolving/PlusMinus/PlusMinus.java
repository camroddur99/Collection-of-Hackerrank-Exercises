import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class PlusMinus{
    private static DecimalFormat df6 = new DecimalFormat("#.######");
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        double pos = 0;
        double neg = 0;
        double zer = 0;

        for(int i=0;i<x;i++){
            int value = input.nextInt();
            if (value > 0){
                pos += 1;
            }
            else if(value < 0){
                neg += 1;
            }
            else{
                zer += 1;
            }
        }
        System.out.println(df6.format(pos/x));
        System.out.println(df6.format(neg/x));
        System.out.println(df6.format(zer/x));
    }
}
