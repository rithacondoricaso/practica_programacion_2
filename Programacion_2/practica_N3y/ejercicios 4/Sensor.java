public class Sensor {
    public static String tipo = "Generico";
    protected String id;
    protected boolean encendido;

    public Sensor(String id) {
        this.id = id;
        this.encendido = false;
    }

    public void activar() {
        encendido = true;
        System.out.println(id + " activado");
    }

    public void desactivar() {
        encendido = false;
        System.out.println(id + " desactivado");
    }

    @Override
    public String toString() {
        return tipo + " [id=" + id + ", encendido=" + encendido + "]";
    }
}
