const startTime = Date.now();

console.log("Application started!");

console.log("Process ID:", process.pid);

setInterval(() => {
  const runningFor = Date.now() - startTime;

  console.log(`Process running for ${runningFor} ms`);
}, 2000);
