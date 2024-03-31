document.addEventListener('DOMContentLoaded', function () {
    const increaseButton = document.getElementById('increaseFuValue');
    const decreaseButton = document.getElementById('decreaseFuValue');
    const valueInput = document.getElementById('fuValue');

    // Define your custom sequence of values
    const values = [20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 110];
    let currentIndex = 2; // Start at the third value (index 2)

    increaseButton.addEventListener('click', function () {
        var input = document.getElementById('fuValue');
        if (currentIndex < values.length - 1) {
            currentIndex++; // Increase the index within bounds
            valueInput.value = values[currentIndex]; // Update the input value
            triggerHTMX(input); // Manually trigger HTMX
        }
    });

    decreaseButton.addEventListener('click', function () {
        var input = document.getElementById('fuValue');
        if (currentIndex > 0) {
            currentIndex--; // Decrease the index within bounds
            valueInput.value = values[currentIndex]; // Update the input value
            triggerHTMX(input); // Manually trigger HTMX
        }
    });

    function triggerHTMX(input) {
        if ("createEvent" in document) {
            var evt = document.createEvent("HTMLEvents");
            evt.initEvent("change", false, true);
            input.dispatchEvent(evt);
        } else {
            input.fireEvent("onchange");
        }
    }
});


document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('increaseHanValue').addEventListener('click', function() {
        var input = document.getElementById('hanValue');
        input.value = parseInt(input.value) + 1; // Increment the value
        triggerHTMX(input); // Manually trigger HTMX
    });

    document.getElementById('decreaseHanValue').addEventListener('click', function() {
        var input = document.getElementById('hanValue');
        input.value = Math.max(1, parseInt(input.value) - 1); // Decrement the value, with a minimum of 1
        triggerHTMX(input); // Manually trigger HTMX
    });

    function triggerHTMX(input) {
        if ("createEvent" in document) {
            var evt = document.createEvent("HTMLEvents");
            evt.initEvent("change", false, true);
            input.dispatchEvent(evt);
        } else {
            input.fireEvent("onchange");
        }
    }
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('increaseHonbaValue').addEventListener('click', function() {
        var input = document.getElementById('honbaValue');
        input.value = parseInt(input.value) + 1; // Increment the value
        triggerHTMX(input); // Manually trigger HTMX
    });

    document.getElementById('decreaseHonbaValue').addEventListener('click', function() {
        var input = document.getElementById('honbaValue');
        input.value = Math.max(0, parseInt(input.value) - 1); // Decrement the value, with a minimum of 1
        triggerHTMX(input); // Manually trigger HTMX
    });

    function triggerHTMX(input) {
        if ("createEvent" in document) {
            var evt = document.createEvent("HTMLEvents");
            evt.initEvent("change", false, true);
            input.dispatchEvent(evt);
        } else {
            input.fireEvent("onchange");
        }
    }
});



document.body.addEventListener('htmx:configRequest', function (event) {
    var csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    event.detail.headers['X-CSRFToken'] = csrfToken;
});
