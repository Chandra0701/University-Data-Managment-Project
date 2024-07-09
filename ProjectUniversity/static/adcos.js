document.addEventListener("DOMContentLoaded", function() {
    const courseForm = document.getElementById("course-form");
    const message = document.getElementById("message");

    courseForm.addEventListener("submit", function(e) {
        e.preventDefault();
    });

    const addCourseButton = document.getElementById("add-course");
    addCourseButton.addEventListener("click", function() {
        const courseCode = document.getElementById("course_code").value;
        const courseName = document.getElementById("course_name").value;
        const creditHours = document.getElementById("credit_hours").value;

        // You can perform client-side validation here before sending data to the server.

        // Send the course data to the server using fetch or XMLHttpRequest.
        // Example:
        fetch("add_course.php", {
            method: "POST",
            body: JSON.stringify({
                courseCode: courseCode,
                courseName: courseName,
                creditHours: creditHours
            }),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            // Display the server response to the user.
            message.textContent = data.message;
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
