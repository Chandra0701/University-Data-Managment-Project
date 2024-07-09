// Sample data for demonstration purposes
const grades = [
    {  course: 'Math',credit:'4' ,grade:' ' },
    {  course: 'History',credit:'3' ,grade: ' ' },
    {  course: 'Physics',credit:'4', grade: ' ' },
    {  course: 'DSA',credit:'4' ,grade:' ' },
    {  course: 'Discrete math',credit:'3' ,grade: ' ' },
    {  course: 'DBMS',credit:'4', grade: ' ' },
    // Add more data here
];

// Function to populate the grade list
function populateGradeList() {
    const gradeList = document.getElementById('grade-list');
    gradeList.innerHTML = ''; // Clear previous content

    const table = document.createElement('table');
    const thead = document.createElement('thead');
    const tbody = document.createElement('tbody');

    // Create table header
    const headerRow = document.createElement('tr');
    const headers = ['course','credit', 'Grade'];

    headers.forEach(headerText => {
        const th = document.createElement('th');
        th.textContent = headerText;
        headerRow.appendChild(th);
    });

    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Populate table rows with grades data
    grades.forEach(grade => {
        const row = document.createElement('tr');
        const values = [ grade.course,grade.credit, grade.grade];

        values.forEach(value => {
            const td = document.createElement('td');
            td.textContent = value;
            row.appendChild(td);
        });

        tbody.appendChild(row);
    });

    table.appendChild(tbody);
    gradeList.appendChild(table);
}

// Call the function to populate the grade list on page load
window.onload = populateGradeList;
