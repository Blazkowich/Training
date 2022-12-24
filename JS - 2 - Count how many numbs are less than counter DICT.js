var number,numbers,dict,count;
number = [3,5,1,4];
numbers = [];
dict = {};
for (var numb, i = 0, b = number.length; (i<b); i += 1) {
    numb = number[i];
    if (!(numb in dict)) {
        dict[numb] = 0;
    }
    dict[numb] += 1;
}
for (var numbTwo, c = 0, d = number.length; (c<d); c += 1) {
    numbTwo = number[c];
    count = 0;
    for (const [key, value] of Object.entries(dict)) {
        if (key < numbTwo) {
            count += value;
        }
    }
    numbers.push(count);
}
console.log(numbers);