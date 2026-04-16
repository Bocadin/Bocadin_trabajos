package primerprogramabocadin;


public class PrimerProgramaBocadin {

    public static void main(String[] args) {
        // 1. Declaración de variables
        int edad = 20;
        double estatura = 1.75;
        double peso = 68.5;
        boolean esEstudiante = true;
        String carrera = "Ciencia de Datos";

        // 2. Operación simple
        // Ojo, en Java las variables pueden sumarse si son números o concatenarse si son cadenas
        double indiceMasaCorporal = peso / (estatura * estatura);

        // 3. Imprimir resultados usando el operador de concatenación (+)
        System.out.println("--- Perfil del Estudiante ---");
        System.out.println("Carrera: " + carrera);
        System.out.println("Edad: " + edad + " años");
        System.out.println("Estudiante Activo: " + esEstudiante);
        System.out.println("IMC calculado: " + indiceMasaCorporal);
    }
    
}
