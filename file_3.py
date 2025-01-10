
import random
from typing import List

def generate_random_data() -> List[int]:
    data = [random.randint(1, 100) for _ in range(10)]
    return data

def process_data(data: List[int]) -> List[int]:
    return [x * 2 for x in data if x > 50]

def main() -> None:
    data = generate_random_data()
    processed = process_data(data)
    print(f"Original data: {data}")
    print(f"Processed data: {processed}")

if __name__ == "__main__":
    main()

function generateRandomData() {
    return Array.from({ length: 10 }, () => 
        Math.floor(Math.random() * 100) + 1
    );
}

function processData(data) {
    return data
        .filter(x => x > 50)
        .map(x => x * 2);
}

function main() {
    const data = generateRandomData();
    const processed = processData(data);
    
    console.log("Original data:", data);
    console.log("Processed data:", processed);
}

main();

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

function generateRandomData() {
    return Array.from({ length: 10 }, () => 
        Math.floor(Math.random() * 100) + 1
    );
}

function processData(data) {
    return data
        .filter(x => x > 50)
        .map(x => x * 2);
}

function main() {
    const data = generateRandomData();
    const processed = processData(data);
    
    console.log("Original data:", data);
    console.log("Processed data:", processed);
}

main();

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
