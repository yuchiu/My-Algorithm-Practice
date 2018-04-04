import java.util.*;

public class ArrayStructure{

    private int[] myArray = new int[50];
    private int arraySize = 10;
    public void generateRandomArray(){
        for(int i = 0; i<arraySize;i++){
            myArray[i]=(int)(Math.random()*10);
        }
    }
    public void printArr(){
        System.out.println("--------------");
        for(int i = 0; i<arraySize;i++){
            System.out.print("| "+ i +" |");
            System.out.println("| "+myArray[i]+" |");
            System.out.println("--------------");
        }
    }
    public int getValueAtIndex(int index){
        if(index< arraySize){
            return myArray[index];
        }
        return 0;
    }
    public boolean findByValue(int searchValue){
        boolean didValueFound = false;
        for(int i =0; i<arraySize; i++){
            if(myArray[i] == searchValue){
                didValueFound = true;
            }
        }
        return didValueFound;
    }
    public static void main(String[] args){
        ArrayStructure newArray = new ArrayStructure();

        newArray.generateRandomArray();
        newArray.printArr();
        System.out.println(newArray.getValueAtIndex(2));
        System.out.println(newArray.findByValue(8));
    }
}