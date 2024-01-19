var CounterModule = (function() {
    // Private variable
    var count = 0;

    // Private function to log the current count
    function logCount() {
        console.log("Current count: " + count);
    }

    // Public API
    function increment() {
        count++;
        logCount();
    }

    function decrement() {
        count--;
        logCount();
    }

    function getCount() {
        return count;
    }

    // Expose public methods
    return {
        increment: increment,
        decrement: decrement,
        getCount: getCount
    };
})();

// Example usage
CounterModule.increment(); // Output: Current count: 1
CounterModule.increment(); // Output: Current count: 2
CounterModule.decrement(); // Output: Current count: 1

// Accessing private variable (avoid doing this in practice, use public methods)
console.log("Current count (direct access): " + CounterModule.count); // Output: undefined

// Accessing count through public method
console.log("Current count (via public method): " + CounterModule.getCount()); // Output: Current count: 1
