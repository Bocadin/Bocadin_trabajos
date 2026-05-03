package encapsulamiento;

public class UsuarioBaseDatos {
    
    // 1. ATRIBUTOS PRIVADOS (Nadie externo a esta clase puede verlos ni modificarlos)
    private String username;
    private String password;
    private int nivelAcceso;

    // 2. CONSTRUCTOR (Es público para que podamos instanciar el objeto)
    public UsuarioBaseDatos(String username, String password, int nivelAcceso) {
        this.username = username;
        this.password = password;
        
        // Ya desde la construcción aplicamos filtros de seguridad
        if (nivelAcceso < 1) {
            this.nivelAcceso = 1; // Asignamos nivel mínimo preventivo
        } else {
            this.nivelAcceso = nivelAcceso;
        }
    }

    // 3. GETTERS (Métodos de sólo lectura)
    // El usuario es de acceso libre para lectura.
    public String getUsername() {
        return this.username;
    }

    public int getNivelAcceso() {
        return this.nivelAcceso;
    }
    
    // Fíjate que a propósito NO creamos un getPassword(). 
    // Por seguridad en este sistema dictaminamos que la contraseña nunca puede ser leída, solo validada o cambiada.

    // 4. SETTERS (Métodos de escritura controlada)
    // Supongamos que queremos cambiar el nivel de acceso por una promoción.
    public void setNivelAcceso(int nuevoNivel) {
        // En vez de modificación directa, el Setter evalúa si en efecto la petición es lógica
        if (nuevoNivel >= 1 && nuevoNivel <= 5) {
            this.nivelAcceso = nuevoNivel;
            System.out.println("Nivel de acceso actualizado correctamente a: " + this.nivelAcceso);
        } else {
            System.err.println("ERROR: Nivel de acceso denegado. Se mantienen los privilegios previos.");
        }
    }

    // Setter para la contraseña, con validaciones de longitud
    public void setPassword(String passwordActual, String nuevaPassword) {
        if(this.password.equals(passwordActual)) {      // .equals sirve para comparar Textos (Strings) en Java!
            if(nuevaPassword.length() >= 8) {
                this.password = nuevaPassword;
                System.out.println("Contraseña cambiada con éxito.");
            } else {
                System.err.println("ERROR: La nueva contraseña debe tener 8 o más caracteres.");
            }
        } else {
            System.err.println("CREDENCIALES INVÁLIDAS: Contraseña actual incorrecta.");
        }
    }
}
