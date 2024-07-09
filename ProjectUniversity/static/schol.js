// JavaScript code to load and display scholarship information

// Sample scholarship data (you can replace this with your actual data)
const scholarships = [
    {
        name: "Merit Scholarship",
        amount: "5,0000",
        eligibility: "For high-achieving students",
    },
    {
        name: "Need-Based Scholarship",
        amount: "3,0000",
        eligibility: "For students with demonstrated financial need",
    },
    // Add more scholarship objects as needed
];

// Function to display scholarships on the webpage
function displayScholarships() {
    const scholarshipList = document.getElementById("scholarship-list");

    scholarships.forEach((scholarship) => {
        const scholarshipItem = document.createElement("div");
        scholarshipItem.classList.add("scholarship-item");

        const name = document.createElement("h3");
        name.textContent = scholarship.name;

        const amount = document.createElement("p");
        amount.textContent = "Amount: " + scholarship.amount;

        const eligibility = document.createElement("p");
        eligibility.textContent = "Eligibility: " + scholarship.eligibility;

        scholarshipItem.appendChild(name);
        scholarshipItem.appendChild(amount);
        scholarshipItem.appendChild(eligibility);

        scholarshipList.appendChild(scholarshipItem);
    });
}

// Call the function to display scholarships when the page loads
window.addEventListener("DOMContentLoaded", displayScholarships);
