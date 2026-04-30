package algoritmoia;

public class RedNeuronal extends AlgoritmoIA {

    // Atributos exclusivos (nicho) de la hija
    private int cantidadCapasOcultas;

    // CONSTRUCTOR DE LA HIJA
    public RedNeuronal(String nombreAlgoritmo, int tiempoSegundos, int capasOcultas) {
        
        // IMPORTANTE: Al heredar, estás OBLIGADO a llamar al Constructor del Padre primero.
        // Se hace usando obligatoriamente en la primera linea la directiva especial 'super()'
        super(nombreAlgoritmo, tiempoSegundos); 
        
        // Una vez que el padre se inicializó a sí mismo, inicializo las variables propias de la hija
        this.cantidadCapasOcultas = capasOcultas;
    }

    // Método exclusivo de la hija
    public void calibrarPesos() {
        System.out.println("Afinando backpropagation para " + this.cantidadCapasOcultas + " capas...");
        // Fíjate que pudimos imprimir cantidadCapasOcultas... pero también podemos usar 'nombreAlgoritmo'.
        // Y jamás declaramos a nombreAlgoritmo en esta clase.  ¡Viene heredado gratuitamente del padre como protected!
        System.out.println("Modelo " + nombreAlgoritmo + " está siendo calibrado internamente.");
    }
    
    // SOBRESCRITURA (Override)
    // El método 'ejecutarPrediccion' ya existía en el Padre. Pero la red neuronal no predice de forma genérica.
    // Nosotros "Pisamos" o Sobrescribimos el diseño de nuestro papá, para que actúe de forma personalizada aquí.
    @Override
    public void ejecutarPrediccion() {
        // Le indicamos al compilador con @Override (una anotación pura) nuestra intención técnica. 
        System.out.println("PREDICCIÓN RED NEURONAL: Multiplicando las matrices por la entropía cruzada para arrojar decimales de probabilidad final.");
    }
}