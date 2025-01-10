
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;

public class DataProcessor {
    private static final Random random = new Random();

    public static List<Integer> generateRandomData() {
        List<Integer> data = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            data.add(random.nextInt(100) + 1);
        }
        return data;
    }

    public static List<Integer> processData(List<Integer> data) {
        return data.stream()
                  .filter(x -> x > 50)
                  .map(x -> x * 2)
                  .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        List<Integer> data = generateRandomData();
        List<Integer> processed = processData(data);
        
        System.out.println("Original data: " + data);
        System.out.println("Processed data: " + processed);
    }
}

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;

public class DataProcessor {
    private static final Random random = new Random();

    public static List<Integer> generateRandomData() {
        List<Integer> data = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            data.add(random.nextInt(100) + 1);
        }
        return data;
    }

    public static List<Integer> processData(List<Integer> data) {
        return data.stream()
                  .filter(x -> x > 50)
                  .map(x -> x * 2)
                  .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        List<Integer> data = generateRandomData();
        List<Integer> processed = processData(data);
        
        System.out.println("Original data: " + data);
        System.out.println("Processed data: " + processed);
    }
}
