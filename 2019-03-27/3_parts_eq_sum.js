const canThreePartsEqualSum = nums => {
  const sums = [0, 0, 0];
  const sum = nums.reduce((a, e) => a + e, 0);
  const parts = 3;
  const target = sum / parts;
  
  if (sum % parts) {
    return false;
  }

  for (let i = 0, j = 0; i < parts; i++) {
    for (; sums[i] !== target; j++) {
      if (j >= nums.length) {
        return false;
      }

      sums[i] += nums[j];
    }
  }
  
  return sums.every(e => e === sums[0]);
};

[
  [-6, 6, 0, 4, 3, -3, 6, -2, 6, 3, 1, 3],
  [-5, 6, 0, 4, 3, -3, 6, -2, 6, 3, 1, 3],
  [6, 1, -4, 6, 5, -7, 3, 4, 6, 1]
].forEach(e => console.log(canThreePartsEqualSum(e)));
