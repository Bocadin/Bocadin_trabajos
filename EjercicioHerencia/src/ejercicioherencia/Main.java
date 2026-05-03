package ejercicioherencia;

public class Main {
    public static void  main(String[] args){
        EjercicioHerencia carro1= new EjercicioHerencia(15);
        carro1.arranconGen();
        
        AutoTesla carro2 = new AutoTesla(15, 89.23);
        carro2.arranconGen();
        
    }
    
}
