package ejercicioherencia;

public class AutoTesla extends EjercicioHerencia {
    private double bateriaElectronica;
    
    public AutoTesla(int combustibleLitros, double bateria){
        super (combustibleLitros);
        this.bateriaElectronica = bateria;
         }
    
        @Override
        public void arranconGen(){
        System.out.println("El rayo macqueen fiaummmm");
        
        
        
    }
    
    
}
