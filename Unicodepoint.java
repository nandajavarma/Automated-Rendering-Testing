import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Unicodepoint {

public static void main(String[] args) {

InputStreamReader inputStreamReader = new InputStreamReader(System.in);
BufferedReader bufferedReader = new BufferedReader(inputStreamReader);

try {
  String line = null;
  while ((line = bufferedReader.readLine()).length() > 0) {
    for (int index = 0; index < line.length(); index++) {
      String hexCode = Integer.toHexString(line.codePointAt(index)).toUpperCase();

      String hexCodeWithAllLeadingZeros = "0000" + hexCode;
      String hexCodeWithLeadingZeros = hexCodeWithAllLeadingZeros.substring(hexCodeWithAllLeadingZeros.length()-4);

      System.out.println("\\u" + hexCodeWithLeadingZeros);
    }

  }
} catch (IOException ioException) {
       ioException.printStackTrace();
  }
 }
}
