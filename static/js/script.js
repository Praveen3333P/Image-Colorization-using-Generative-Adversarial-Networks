const fileInput = document.getElementById("custom-file-input");
const uploadedImage = document.getElementById("uploaded-image");

fileInput.addEventListener("change", function () {
    const selectedFile = this.files[0];

    if (selectedFile) {
        if (selectedFile.type.startsWith("image/")) {
            const imageURL = URL.createObjectURL(selectedFile);
            uploadedImage.src = imageURL;
            uploadedImage.style.display = "block";
        } else {
            alert("Please select an image file (e.g., JPG, PNG).");
            this.value = ""; // Clear the file input field
        }
    }
});

const isDarkMode = localStorage.getItem('darkMode') === 'enabled';

function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle('dark-mode');

    const isEnabled = body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isEnabled ? 'enabled' : 'disabled');

    const darkModeToggleBtn = document.getElementById('dark-mode-toggle');
    if (isEnabled) {
        darkModeToggleBtn.innerHTML = '<i class="bx bxs-sun"></i>';
    } else {
        darkModeToggleBtn.innerHTML = '<i class="bx bxs-moon"></i>';
    }

    const elementsToToggle = ['.navbar', '.left', '.right', '#about', '#contact', '.nav-item'];
    elementsToToggle.forEach((element) => {
        document.querySelector(element).classList.toggle('dark-mode');
    });
}

// Apply dark mode on page load if the user prefers dark mode
if (isDarkMode) {
    document.body.classList.add('dark-mode');
    const darkModeToggleBtn = document.getElementById('dark-mode-toggle');
    darkModeToggleBtn.innerHTML = '<i class="bx bxs-sun"></i>';
    const elementsToToggle = ['.navbar', '.left', '.right', '#about', '#contact', '.nav-item'];
    elementsToToggle.forEach((element) => {
        document.querySelector(element).classList.add('dark-mode');
    });
} else {
    const darkModeToggleBtn = document.getElementById('dark-mode-toggle');
    darkModeToggleBtn.innerHTML = '<i class="bx bxs-moon"></i>';
}
