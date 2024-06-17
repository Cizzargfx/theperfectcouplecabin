document.getElementById('emailForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting

    // Here, you would typically handle the email sending process
    // For demonstration purposes, we'll simulate a successful send
    // Replace this with your actual email sending logic

    // Simulate email sending (success scenario)
    setTimeout(function() {
        document.getElementById('statusMessage').textContent = 'Good'; // Update status message
        document.getElementById('statusMessage').style.color = 'green'; // Change text color to green for success
    }, 2000); // Simulating a 2-second delay, adjust as needed
});
