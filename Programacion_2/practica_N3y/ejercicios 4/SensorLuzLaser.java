public class SensorLuzLaser extends Sensor {
    public static String tipo = "Luz Laser";
    private int alcance;

    public SensorLuzLaser(String id, int alcance) {
        super(id);
        this.alcance = alcance;
    }

    @Override
    public String toString() {
        return tipo + " [id=" + id + ", alcance=" + alcance
                + ", encendido=" + encendido + "]";
    }
}
