# 함수 선언식 vs 함수 표현식

## 🔎함수 선언식

```javascript
console.log(helloA());

function helloA() {
    return "Hello, world A!";
};
```

[output]

```mark
Hello, world A!
```

**✅함수를 실행하는 코드 다음에 함수를 선언하는 코드가 있는데 정상적으로 실행되는 이유:**

**호이스팅** 때문! 함수 선언식으로 만들어진 함수들은 프로그램 실행 전 코드 최상단에 끌어올려진다. 



## 🔎함수 표현식

***그렇다면 함수 표현식도 선언식처럼 선언 전 실행 코드를 작성해도 작동이 될까?***

```javascript
console.log(helloB());

let helloB = function() {
    return "Hello, world B!";
};
```

[output]

```MARK
TypeError: helloB is not a function
```

결과는 NO🙅‍♀️ 위처럼 타입에러가 발생한다.

**✅함수 표현식은 호이스팅이 이루어지지 않는다.**

제대로 함수가 호출되려면 코드가 아래와 같이 작성되어야 한다.

```javascript
let helloB = function() {
    return "Hello, world B!";
};

console.log(helloB());
```

---



#### ✅함수 표현식을 더 간단하게 쓰는 방법

1. **화살표 함수**

   ```javascript
   let helloB = () => {
       return "Hello, world B!";
   };
   ```

   

2. **return 하는 값이 하나밖에 없을 때**

   ```javascript
   let helloB = () => "Hello, world B!";
   ```

**⚠️화살표 함수도 함수 표현식처럼 호이스팅이 되지 않는다⚠️**

---

