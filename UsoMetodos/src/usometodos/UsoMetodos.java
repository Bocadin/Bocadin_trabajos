package usometodos;

public class UsoMetodos {

    public static void limpiarDatos() {
        System.out.println("Ya te limpié los datos");
    }
    public static double calcularDistancia (double a, double b){
        double dist= Math.abs ( a - b );
        return dist;
    }
    public static void main(String[]args){
        limpiarDatos();
        limpiarDatos();
        double metricaDistancia = calcularDistancia (170.3, 102.1);
        System.out.println("Distancia capturada por el sensor: " + metricaDistancia);
    }
}
