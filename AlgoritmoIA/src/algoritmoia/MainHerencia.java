package algoritmoia;

public class MainHerencia {
    public static void main(String[] args) {
        
        System.out.println("--- PRUEBA 1 : SUPERCLASE O PADRE ---");
        AlgoritmoIA simplePadre = new AlgoritmoIA("Regresion Lineal OLS", 2);
        simplePadre.ejecutarPrediccion();
        // simplePadre.calibrarPesos(); // ESTO FALLA. El padre es ignorante del método que se inventó su hijo, no sabe hacerlo.
        
        System.out.println("\n--- PRUEBA 2 : SUBCLASE O HIJO ---");
        RedNeuronal complexHijo = new RedNeuronal("Perceptron Multicapa", 4500, 15);
        
        // ¡Magia! Puede ejecutar su método super calibrado porque lo sobrescribimos con @Override
        complexHijo.ejecutarPrediccion(); 
        
        // Además, puede ejecutar libremente sus métodos y código de nicho exclusivos.
        complexHijo.calibrarPesos();
    }
}