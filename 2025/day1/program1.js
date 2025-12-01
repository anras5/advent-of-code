const fs = require("node:fs");

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

  currentValue = 50; // we start at 50
  countOfZeros = 0;

  for (const step of steps) {
    if (step.direction === "L") {
      currentValue = currentValue - parseInt(step.value);
      currentValue = currentValue % 100;
    } else {
      currentValue = currentValue + parseInt(step.value);
      currentValue = currentValue % 100;
    }
    if (currentValue === 0) {
      countOfZeros++;
    }
  }

  console.log(countOfZeros);
});
