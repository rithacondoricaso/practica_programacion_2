public class Camara extends Sensor {
    public static String tipo = "Camara";
    private String resolucion;

    public Camara(String id, String resolucion) {
        super(id);
        this.resolucion = resolucion;
    }

    @Override
    public String toString() {
        return tipo + " [id=" + id + ", resolucion=" + resolucion
                + ", encendido=" + encendido + "]";
    }
}
