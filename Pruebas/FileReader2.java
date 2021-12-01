//Mierda
import java.util.Scanner;
import java.io.File;

public class FileReader2 {
    public static void main(String[] args){
        String palabra="JUAN";
        try{
        Scanner string = new Scanner (new File ("C:\\Users\\diego\\OneDrive\\Escritorio\\VSCODE\\ConcursoAoC2021\\Pruebas\\input.txt"));
        while(string.hasNext()){
            palabra= string.next();
        }
    } catch (Exception E){
        System.out.println("Nope"); 
    }
    System.out.println(palabra);

    }
    }
    


