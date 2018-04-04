import java.util.*;

public class SortingAlgorithms{
    private final int maxDimension = 50;
    private int[] myArr = new int[maxDimension];
    private int arrLength = 10;


    public void generateArr(){
        Random myRan = new Random();
        for(int i =0; i<arrLength; i++){
            myArr[i]= myRan.nextInt(10);
        }
    }

    public void printArr(){
        System.out.println("----------------");
        for(int i =0; i<arrLength; i ++){
            System.out.println("| "+i+" | "+"| "+myArr[i]+" |");
            System.out.println("--------------------");
        }
    }

    public void linearSearch(int val){
        boolean valueFound = false;
        System.out.println("val "+val+" is found at the following index: ");
        for(int i = 0; i<arrLength; i++){
            if(myArr[i]==val){
                valueFound = true;
                System.out.println(i);
            }
        }
        if(!valueFound){
            System.out.println("not found");
        }
    }

    public void bubbleSort(){
        for(int i = arrLength-1; i>1; i--){
            for(int j = 0; j< i; j ++){
                if(myArr[j]>myArr[j+1]){
                    swapVal(j, j+1);
                }
            }
        }
    }

    public void swapVal(int num1, int num2){
        int temp = myArr[num1];
        myArr[num1]=myArr[num2];
        myArr[num2] = temp;
    }

    public void binarySearch(int val){
        int lowIndex = 0;
        int highIndex = arrLength-1;
        
        while( lowIndex <= highIndex){
            int middle = (highIndex+lowIndex)/2;
            if(val> myArr[middle]){
                lowIndex = middle+1;
            }
            else if(val<myArr[middle]){
                highIndex = middle-1;
            }
            else if(val == myArr[middle]){
                System.out.println(val +" is found at index: "+middle);
                break;
            }
        }
    }

    public void selectionSort(){
        for(int i =0; i <arrLength-1; i++){
            int temp =i;
            for(int j =i; j<arrLength-1;j++){
                if(myArr[temp]>myArr[j+1]){
                    temp = j+1;
                }
                // System.out.println("inside second loop, smallest num is: "+myArr[temp]);
            }
            // int loopnum = i+1;
            // System.out.println("inside selection sort, loop num is: "+loopnum);
            // System.out.println("swapping value of: "+myArr[temp]+" at position: "+temp+" to value of: "+myArr[i]+" at position: "+i);
            swapVal(i, temp);
        }
    }
    
    public static void main(String[] args){
        SortingAlgorithms newArr = new SortingAlgorithms();
        newArr.generateArr();
        newArr.printArr();        
        // newArr.linearSearch(5);
        // newArr.binarySearch(5);
        // newArr.bubbleSort();
        newArr.selectionSort();
        newArr.printArr();
        newArr.binarySearch(5);



    }
}