export function computeOverlayPosition(targetEl, overlay) {
  const overlayWidth = overlay.getBoundingClientRect().width;
  let left;
  let top;

  // try correctly positionning the overlay using getClientRects()
  // If it fails (getClientRects may not be available), fallback to a more basic positionning
  // based on offsetTop
  try {
    const boundsList = targetEl.getClientRects();
    let highestBounds = boundsList[0];
    let highestBoundsTop = Number.POSITIVE_INFINITY;
    boundsList.forEach((bounds) => {
      // sometimes there is some extra 'bounds' that has invalid values, including a 0 width.
      // we use this to discard those invalid bounds
      if (bounds.width === 0) return;

      top = bounds.y - bounds.height;
      if (top < highestBoundsTop) {
        highestBoundsTop = top;
        highestBounds = bounds;
      }
    });
    top = (targetEl.offsetTop - boundsList[0].y) + highestBounds.y - 5;
    left = Math.min(highestBounds.x, window.innerWidth - overlayWidth - 25);
  } catch (e) {
    top = targetEl.offsetTop;
    if (window.innerWidth > overlayWidth + 25) {
      left = Math.min(targetEl.offsetLeft, window.innerWidth - overlayWidth - 25);
    } else {
      left = (window.innerWidth - overlayWidth) / 2;
    }
  }

  return { left, top };
}
