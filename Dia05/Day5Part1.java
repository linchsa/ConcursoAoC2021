//SIN ACABAR
import java.util.Arrays;

public class Day5Part1 {
    static void imprimir(char matriz[][]){
        for(int i=0;i<matriz.length;i++){
            for(int j=0;j<matriz.length;j++){
            System.out.print(matriz[i][j]);
            }
            System.out.print("\n");
        }
    }
    public static void main(String[] args){
        char matriz[][]= new char [9][9];
        for(int i=0;i<matriz.length;i++){
            for(int j=0;j<matriz.length;j++){
            matriz[i][j]='.';
            }
        }
        imprimir(matriz);
        
    }
    
}
