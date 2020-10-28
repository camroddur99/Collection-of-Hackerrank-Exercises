import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class CompareTriplets{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int a = 0;
        int b = 0;
        int[] arr1 = new int[3];
        int[] arr2 = new int[3];
        for (int i=0;i<3;i++){
            arr1[i] = input.nextInt();
        }
        for (int i=0;i<3;i++) {
            arr2[i] = input.nextInt();
        }
        for (int i=0;i<3;i++) {
            if (arr1[i] > arr2[i]){
                a += 1;
            }
            else if (arr2[i] > arr1[i]){
                b += 1;
            } 
        }
        System.out.println(a+" "+b);       
    }
}