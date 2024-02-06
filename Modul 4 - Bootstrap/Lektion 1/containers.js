// Function to update the size display
function updateSize() {
    var width = window.innerWidth;
    var height = window.innerHeight;
    document.getElementById('size').innerText = 'Browser size: ' + width + ' x ' + height;
  }

  // Call the function initially
  updateSize();

  // Add event listener for window resize
  window.addEventListener('resize', updateSize);