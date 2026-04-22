package ejercicios1jav;

import java.util.Scanner;
public class Ejercicios1Jav {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        System.out.println("Ingrese su salario anual :D");
        double salarioAnual= leer.nextDouble();
        
        if (salarioAnual < 10000){
            System.out.printf("La cantidad de %.2f no paga impuestos \n", salarioAnual);
        }else if (salarioAnual>= 10000 || salarioAnual <= 30000){
            double impuesto = salarioAnual*0.15;
                   System.out.printf("Debe de pagar %.2f pesos \n", impuesto);  
        }else{
            double impuesto1= salarioAnual*0.30;
            System.out.printf("Debe pagar %.2f pesos \n", impuesto1);
            
        }
        
        
    }
    
}
