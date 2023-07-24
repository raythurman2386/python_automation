fn collatz(n: u64) -> Vec<u64> {
    if n <= 0 {
        panic!("Please input a value greater than 0! You input {}", n);
    }

    let mut sequence = vec![n];
    let mut num = n;

    while num != 1 {
        if num % 2 == 0 {
            num /= 2;
        } else {
            num = 3 * num + 1;
        }
        sequence.push(num);
    }

    sequence
}

fn main() {
    let n = 391;
    let result = collatz(n);
    println!("Collatz sequence for {}: {:?}", n, result);
}
