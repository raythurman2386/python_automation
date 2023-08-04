class PasswordGenerator {
  private length: number;
  private includeUppercase: boolean;
  private includeLowercase: boolean;
  private includeNumbers: boolean;
  private includeSpecialCharacters: boolean;

  constructor(
    length: number,
    includeUppercase: boolean = true,
    includeLowercase: boolean = true,
    includeNumbers: boolean = true,
    includeSpecialCharacters: boolean = true
  ) {
    this.length = length;
    this.includeUppercase = includeUppercase;
    this.includeLowercase = includeLowercase;
    this.includeNumbers = includeNumbers;
    this.includeSpecialCharacters = includeSpecialCharacters;
  }

  private getRandomCharacterFromArray(arr: string[]): string {
    return arr[Math.floor(Math.random() * arr.length)];
  }

  private generateCharacterPool(): string[] {
    let characterPool: string[] = [];
    if (this.includeUppercase) characterPool = characterPool.concat([...Array(26)].map((_, i) => String.fromCharCode(65 + i)));
    if (this.includeLowercase) characterPool = characterPool.concat([...Array(26)].map((_, i) => String.fromCharCode(97 + i)));
    if (this.includeNumbers) characterPool = characterPool.concat([...Array(10)].map((_, i) => String.fromCharCode(48 + i)));
    if (this.includeSpecialCharacters) characterPool = characterPool.concat("!@#$%^&*()_-+=[]{}|;:'\",.<>?/".split(''));
    return characterPool;
  }

  public generatePassword(): string {
    const characterPool = this.generateCharacterPool();
    let password = '';
    for (let i = 0; i < this.length; i++) {
      password += this.getRandomCharacterFromArray(characterPool);
    }
    return password;
  }
}

// Example usage:
const passwordGenerator = new PasswordGenerator(12, true, true, true, true);
const password = passwordGenerator.generatePassword();
console.log(password); // Example output: "7xKgPz!cBn2D"

