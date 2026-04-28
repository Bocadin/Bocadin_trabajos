package modeloanalitico;

public class ModeloAnalitico {
    
        // 1. ATRIBUTOS (El estado del objeto)
        // Se definen directamente dentro de la clase, afuera de cualquier método.
        String nombreAlgoritmo;
        double precision;
        boolean estaEntrenado;
 
    // 2. CONSTRUCTOR
    // Es un método especial que "construye" o inicializa el objeto en la memoria (RAM)
    // Obligatoriamente DEBE llamarse EXACTAMENTE igual que la clase y no tiene la palabra "void".
    public ModeloAnalitico(String npNombre, double npPrecisionInicial) {
        // Asignamos los valores que nos pasan por paréntesis a nuestros atributos
        nombreAlgoritmo = npNombre;
        precision = npPrecisionInicial;
        estaEntrenado = false; // Por defecto nace sin estar entrenado
    }

    // 3. MÉTODOS (El comportamiento)
    // Acciones que el objeto sabe hacer consigo mismo.
    public void entrenarModelo() {
        System.out.println("Iniciando fase de entrenamiento para " + nombreAlgoritmo + "...");
        // Simulamos un proceso...
        precision = precision + 0.15; // Su precisión sube al entrenar
        estaEntrenado = true;
        System.out.println("Entrenamiento completado exitosamente.");
    }

    public void mostrarDesempenio() {
        System.out.println("--- Reporte del Modelo ---");
        System.out.println("Algoritmo: " + nombreAlgoritmo);
        System.out.println("Precisión actual: " + precision);
        System.out.println("Estado de entrenamiento: " + estaEntrenado);

    }
    
}
