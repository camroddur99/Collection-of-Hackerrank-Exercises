import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class aVeryBigSum {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        long sum = 0;
        for (int i=0;i<x;i++){
            sum += input.nextInt();
        }
        System.out.println(sum);
    }
}