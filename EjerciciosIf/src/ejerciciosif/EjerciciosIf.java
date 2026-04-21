package ejerciciosif;

import java.util.Scanner;
public class EjerciciosIf {
    
    public static void main(String[] args) {
      
        int edad= 18;
        
        if (edad >= 18){
            System.out.println("El algortimo determina que eres MAYOR de edad");
        }else{
            System.out.println("El agortimo determina que eres MENOR de edad");
        }
        
        
        double probabilidadCarga= 0.85;
            if (probabilidadCarga >= 0.90) {
                System.out.println("Altamente probable.");
}           else if (probabilidadCarga >= 0.50) {
                System.out.println("Probabilidad media.");
}           else {
                System.out.println("Baja probabilidad.");
}
        int opcion_menu = 2;

        switch (opcion_menu) {
            case 1:
                System.out.println("Iniciando ETL...");
                    break; // IMPORTANTE: EL break le dice a Java que se salga del switch, sino ejecutará todo lo de abajo
            case 2:
                System.out.println("Filtrando base de datos...");
                    break;
            case 3:
                System.out.println("Exportando a CSV...");
                    break;
            default:
        // default es el equivalente a "else", es el caso de seguridad.
                System.out.println("Error 404: Opción no válida en el sistema.");
            }
       
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("--- SENSOR DE ALERTA AMBIENTAL ---");
        System.out.print("Ingrese la temperatura del sistema (double): ");
        double nivelTemp = scanner.nextDouble();
        
        System.out.print("Ingrese presión del cilindro (int): ");
        int presion = scanner.nextInt();
        
        // Evaluamos doble factor de riesgo
        if (nivelTemp > 80.0 && presion > 100) {
            System.out.println("¡ALERTA ROJA! Riesgo inminente de explosión térmica.");
        } else if (nivelTemp > 80.0 || presion > 100) {
            System.out.println("Aviso: Un valor excedió el límite de control. Por favor, revise de inmediato.");
        } else {
            System.out.println("Sistema en condiciones operativas óptimas. Riesgo calculado bajo.");
        }
        
        scanner.close();
        
        int contador = 0; // Inicializamos un iterador

        while (contador <= 5) {
            System.out.println("Iteración número: " + contador);
            contador++; // contador++ es equivalente a decir: contador = contador + 1;
}
        for (int i = 0; i < 10; i++) {
            System.out.println("Procesando epoch n.º " + i);
    // 'i' será primero 0 y se ejecutará. 0 < 10, i aumenta a 1. Y así sucesivamente.
}
        // Forma 1: Cuando YA sabemos cuáles son los datos. Directo a memoria.
        int[] puntuaciones_sat = {1200, 1500, 1050, 1340, 950};
// Forma 2: Cuando sabemos el TAMAÑO pero los datos vendrán vacíos y se insertarán por algoritmo
        double[] probabilidadVentas = new double[4]; // Arreglo de longitud 4 lleno de ceros (0.0).

// Acceso a posiciones y mutación
// Importante en CS: ¡Los arreglos comienzan su índice iterativo desde cero a N-1 elementos!
        probabilidadVentas[0] = 0.52; 
        probabilidadVentas[1] = 0.70; 
        
        System.out.println("El valor en la posiscion 2 de la lista puntuaciones_sat es:"+ puntuaciones_sat[1]);
// probabilidadVentas[4] = 0.11; // 💥 ¡ERROR FATAL! ArrayIndexOutOfBoundsException (Solo llega de 0 a 3)
    }
    
}
