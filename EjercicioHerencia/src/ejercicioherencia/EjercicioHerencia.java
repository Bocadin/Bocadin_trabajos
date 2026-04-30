package ejercicioherencia;

public class EjercicioHerencia {
    
    protected int combustibleLitros;
    protected boolean encendido;
    
    public EjercicioHerencia (int combustibleLitros){
        this.combustibleLitros = combustibleLitros; 
        this.encendido= false;
    }
    
    public void arranconGen(){
        System.out.println("El rayo macqueen fiaummmm");
    }
}
