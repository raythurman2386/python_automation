var __spreadArray =
  (this && this.__spreadArray) ||
  function (to, from, pack) {
    if (pack || arguments.length === 2)
      for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
          if (!ar) ar = Array.prototype.slice.call(from, 0, i);
          ar[i] = from[i];
        }
      }
    return to.concat(ar || Array.prototype.slice.call(from));
  };
var PasswordGenerator = /** @class */ (function () {
  function PasswordGenerator(
    length,
    includeUppercase,
    includeLowercase,
    includeNumbers,
    includeSpecialCharacters
  ) {
    if (includeUppercase === void 0) {
      includeUppercase = true;
    }
    if (includeLowercase === void 0) {
      includeLowercase = true;
    }
    if (includeNumbers === void 0) {
      includeNumbers = true;
    }
    if (includeSpecialCharacters === void 0) {
      includeSpecialCharacters = true;
    }
    this.length = length;
    this.includeUppercase = includeUppercase;
    this.includeLowercase = includeLowercase;
    this.includeNumbers = includeNumbers;
    this.includeSpecialCharacters = includeSpecialCharacters;
  }
  PasswordGenerator.prototype.getRandomCharacterFromArray = function (arr) {
    return arr[Math.floor(Math.random() * arr.length)];
  };
  PasswordGenerator.prototype.generateCharacterPool = function () {
    var characterPool = [];
    if (this.includeUppercase)
      characterPool = characterPool.concat(
        __spreadArray([], Array(26), true).map(function (_, i) {
          return String.fromCharCode(65 + i);
        })
      );
    if (this.includeLowercase)
      characterPool = characterPool.concat(
        __spreadArray([], Array(26), true).map(function (_, i) {
          return String.fromCharCode(97 + i);
        })
      );
    if (this.includeNumbers)
      characterPool = characterPool.concat(
        __spreadArray([], Array(10), true).map(function (_, i) {
          return String.fromCharCode(48 + i);
        })
      );
    if (this.includeSpecialCharacters)
      characterPool = characterPool.concat(
        "!@#$%^&*()_-+=[]{}|;:'\",.<>?/".split("")
      );
    return characterPool;
  };
  PasswordGenerator.prototype.generatePassword = function () {
    var characterPool = this.generateCharacterPool();
    var password = "";
    for (var i = 0; i < this.length; i++) {
      password += this.getRandomCharacterFromArray(characterPool);
    }
    return password;
  };
  return PasswordGenerator;
})();
// Example usage:
var passwordGenerator = new PasswordGenerator(15, true, true, true, true);
var password = passwordGenerator.generatePassword();
console.log(password); // Example output: "7xKgPz!cBn2D"
