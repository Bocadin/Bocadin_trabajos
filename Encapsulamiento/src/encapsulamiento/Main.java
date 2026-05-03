package encapsulamiento;

public class Main {
    
    public static void main(String[] args) {
         UsuarioBaseDatos dbaAdmin = new UsuarioBaseDatos("root_admin", "admin123", 5);
        
        // Esto lanzaría un SUPER ERROR ROJO DE COMPILACIÓN:
        // dbaAdmin.password = "hakearCuenta1";  <--- Está privada. Java lo evita protegiendo nuestro sistema
        
        // Uso legítimo del Getter
         System.out.println("Usuario activo: " + dbaAdmin.getUsername());
        
        // Intento fallido de Setter por violar lógica de negocio
        dbaAdmin.setNivelAcceso(-10); 
        
        // Intento exitoso de Setter
        dbaAdmin.setPassword("admin123", "RootSeguro4455"); 
    }
}
    

