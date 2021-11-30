//Todavía no hay nada subido
package ConcursoAoC2021;
import java.util.Scanner;
import java.io.File;

public class FileReader{
    public static void main (String[] args){
        try{
            Scanner scanner = new Scanner (new File("C:\\Users\\diego\\OneDrive\\Escritorio\\VSCODE\\ConcursoAoC2021\\Día 1\\input.txt"));
            while(scanner.hasNext()){
                System.out.println(scanner.next());
            }
        } catch (Exception E){
            System.out.println("Nope");
        }
    }
}