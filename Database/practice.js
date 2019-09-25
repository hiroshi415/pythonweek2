function main(lines) { // lines: Array<string>
    let ans = 0
    let len = (String(lines[0]).split(' '))[0]
    // lines.forEach((v, i) => console.log(`lines[${i}]: ${v}`));
    for (let i = 1; i<(lines.length); i++ ) {
        for(let j = 0; j<String(lines[i]).split(' ').length; j++) {
            if((String(lines[i]).split(' '))[i] == (String(lines[i+1]).split(' '))[j]) {
                ans += Number((String(lines[i]).split(' '))[len-1])
                ans += Number(String(lines[i+1]).split(' ')[len-1])
            }
        }
    }
    if(ans > 100) {
        return -1
    } else {
        return ans
    }
}


let a = [
    ['3 2'],

    ['1 2 100'],

    ['2 3 100']
]

let b = [
    ['3 2'],
    ['1 2 10'],
    ['2 3 27']
]

// console.log(String(b[1]).split(' ')[2])
// console.log(Number((String(b[1]).split(' '))[2])+Number((String(b[1]).split(' '))[2]))

console.log(main(a))
console.log(main(b))