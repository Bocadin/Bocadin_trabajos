package reinoanimal;

public class ReinoAnimal {
    String Nombre; 
    String Color; 
    int patas;   
    public ReinoAnimal(String name, String color, int legs){
        this.Nombre = name;
        this.Color = color; 
        this.patas = legs;
    }   
    public void Sonido (){
        System.out.println("El animal hace un sonido genérico");
    }
}
