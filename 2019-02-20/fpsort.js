const decimal = n => ("" + n).split`.`[1];
const fpSort = nums => nums.sort((a, b) => decimal(a).localeCompare(decimal(b)) || a - b);

console.log(fpSort([4.5234, 3.434, 434.0004, 23.89, 23.009182, 9.023185, 0.0023801284, 6.007123, 15.67, 7.67]));
