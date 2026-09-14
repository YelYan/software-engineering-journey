console.log("Process is running!");
console.log("Process ID:", process.pid);

setTimeout(() => {
  console.log("Process is still running...");
}, 10000);
