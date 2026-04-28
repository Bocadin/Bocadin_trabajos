package reinoanimal;

public class Perro {
    String Nombre; 
    String Color; 
    int patas;   
    
    public Perro(String name, String color, int legs){
        this.Nombre = name;
        this.Color = color; 
        this.patas = legs;
    }
    
    public void SonidoPerro(){
        System.out.println("El perro hace guau guau");
    }
    
}
