package algoritmoia;

public class AlgoritmoIA {
    
    // El modificador 'protected' es el primo hermano de 'private'.
    // protected significa: "Secreto para el exterior, pero mi familia(clases Hijas) SÍ pueden tener acceso a esto".
    protected String nombreAlgoritmo;
    protected int tiempoProcesamientoSegundos;

    // Constructor del padre
    public AlgoritmoIA(String nombreAlgoritmo, int tiempoSegundos) {
        this.nombreAlgoritmo = nombreAlgoritmo;
        this.tiempoProcesamientoSegundos = tiempoSegundos;
    }

    // Método general que todo algoritmo de IA tendrá
    public void ejecutarPrediccion() {
        System.out.println("El algoritmo Genérico está evaluando los umbrales de predicción.");
    }
}
