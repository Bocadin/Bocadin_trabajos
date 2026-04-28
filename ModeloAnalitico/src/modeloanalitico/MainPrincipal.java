package modeloanalitico;

public class MainPrincipal {
    public static void main(String[] args) {
        
        // Vamos a instanciar (fabricar) nuestro primer objeto.
        // TIPO_DE_DATO nombreVariable = new CONSTRUCTOR(valores...);
        ModeloAnalitico modelo1 = new ModeloAnalitico("Regresion Logistica", 0.50);
        ModeloAnalitico modelo2 = new ModeloAnalitico("Arbol de Decisiones", 0.65);
        
        // Cada objeto vive en su propio de espacio de memoria de forma independiente
        // Si entreno al modelo1, el modelo2 no se ve afectado.
        
        System.out.println("--- Estado INICIAL ---");
        modelo1.mostrarDesempenio();
        modelo2.mostrarDesempenio();
        
        System.out.println("\n--- Ejecutando Comportamientos ---");
        // Utilizamos el punto (.) para acceder a los métodos del objeto
        modelo1.entrenarModelo(); 
        
        System.out.println("\n--- Estado FINAL ---");
        modelo1.mostrarDesempenio();
        modelo2.mostrarDesempenio(); // Este sigue en 0.65 y false, porque nunca lo entrenamos
    }
}
