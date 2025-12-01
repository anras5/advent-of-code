const fs = require("node:fs");

function mod(n, m) {
  return ((n % m) + m) % m;
}

fs.readFile("./input.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  const lines = data.split("\n").filter((line) => line.trim().length > 0);
  const steps = lines.map((line) => {
    const direction = line[0];
    const value = parseInt(line.slice(1).trim());
    return { direction, value };
  });

  currentValue = 50;
  countOfZeros = 0;

  for (const step of steps) {
    if (step.direction === "L") {
      const high = currentValue - 1;
      const low = currentValue - step.value - 1;
      countOfZeros += Math.floor(high / 100) - Math.floor(low / 100);
      currentValue = currentValue - step.value;
    } else {
      const high = currentValue + step.value;
      countOfZeros += Math.floor(high / 100) - Math.floor(currentValue / 100);
      currentValue = currentValue + step.value;
    }
    currentValue = mod(currentValue, 100);
    console.log(currentValue, countOfZeros);
  }

  console.log(countOfZeros);
});
