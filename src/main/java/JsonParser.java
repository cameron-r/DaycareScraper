import org.json.JSONObject;


public class JsonParser {

    public String parseJson(String jsonString) {
        JSONObject jsonObject = new JSONObject(jsonString);

        return jsonObject.get("testKey").toString();
    }
}
