import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {
        String jsonString = FileReader.readFile("data/test.json");

        String data = new JsonParser().parseJson(jsonString);
        System.out.println(data);
    }
}
