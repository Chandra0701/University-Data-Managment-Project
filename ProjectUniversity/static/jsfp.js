document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("payment-form");
    form.addEventListener("submit", function (e) {
        e.preventDefault();
        
        // Here, you would normally send the payment data to a server for processing.
        // This is just a front-end example, and you need a secure back-end for real payments.
        // You can use AJAX or fetch to send the data to your server.
        
        alert("Payment Successful!");
        form.reset();
    });
});
