export function millis(amount) {
  return new Promise((resolve) => {
    setTimeout(resolve, amount);
  });
}

export function frame() {
  return new Promise((resolve) => {
    requestAnimationFrame(resolve);
  });
}
