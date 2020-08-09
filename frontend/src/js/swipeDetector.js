export default class SwipeDetector {
  constructor({
    el, maxTime = 300, minDistance = 100, callback = () => {},
  }) {
    this.el = el;
    this.maxTime = maxTime;
    this.minDistance = minDistance;
    this.callback = callback;

    this.handlers = [];
    this.handlers.push(['touchstart', this.handleTouchStart.bind(this)]);
    this.handlers.push(['touchmove', this.handleTouchMove.bind(this)]);
    this.handlers.push(['touchend', this.handleTouchEnd.bind(this)]);

    this.start();
  }

  start() {
    this.handlers.forEach((handler) => {
      const [eventName, method] = handler;
      this.el.addEventListener(eventName, method);
    });
  }

  stop() {
    this.handlers.forEach((handler) => {
      const [eventName, method] = handler;
      this.el.removeEventListener(eventName, method);
    });
  }

  handleTouchStart(e) {
    // cancel swipe if there are more than one touches
    if (e.touches.length !== 1) {
      this.touchStart = null;
      return;
    }
    this.touchStart = {
      x: e.touches[0].clientX,
      y: e.touches[0].clientY,
      time: new Date(),
    };
  }

  handleTouchMove(e) {
    if (!this.touchStart) return;
    const touch = e.touches[0];
    this.lastTouchPos = { x: touch.clientX, y: touch.clientY };
  }

  handleTouchEnd() {
    if (!this.touchStart || !this.lastTouchPos) return;
    const deltaT = new Date() - this.touchStart.time;
    if (deltaT > this.maxTime) return;
    const dx = this.lastTouchPos.x - this.touchStart.x;
    const dy = this.lastTouchPos.y - this.touchStart.y;
    const distance = Math.sqrt(dx * dx + dy * dy);

    if (distance > this.minDistance) {
      if (Math.abs(dx) > Math.abs(dy)) this.callback(dx > 0 ? 'right' : 'left');
      else this.callback(dy > 0 ? 'down' : 'up');
    }
  }
}
