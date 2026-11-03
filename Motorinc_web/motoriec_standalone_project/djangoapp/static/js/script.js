document.addEventListener("DOMContentLoaded", function () {
    // Sample maintenance status button on the home page.
    const statusButton = document.getElementById("statusButton");
    const statusText = document.getElementById("statusText");

    if (statusButton && statusText) {
        statusButton.addEventListener("click", function () {
            statusText.textContent = "Sample status: Your bike is marked as ready for its next routine check.";
        });
    }

    // Search the visible inventory table rows.
    const searchBox = document.getElementById("searchBox");
    const inventoryTable = document.getElementById("inventoryTable");

    if (searchBox && inventoryTable) {
        searchBox.addEventListener("input", function () {
            const searchTerm = searchBox.value.toLowerCase().trim();
            const rows = inventoryTable.querySelectorAll("tr");

            rows.forEach(function (row) {
                const rowText = row.textContent.toLowerCase();
                row.style.display = rowText.includes(searchTerm) ? "" : "none";
            });
        });
    }

    // Front-end demonstration for the service request form.
    const serviceForm = document.getElementById("serviceForm");
    const errorMessage = document.getElementById("errorMessage");
    const costText = document.getElementById("costText");
    const confirmation = document.getElementById("confirmation");
    const bookingCounter = document.getElementById("bookingCounter");

    if (serviceForm) {
        const savedCount = Number(sessionStorage.getItem("motoriecBookingCount") || "0");
        if (bookingCounter) {
            bookingCounter.textContent = "Successful requests in this session: " + savedCount;
        }

        serviceForm.addEventListener("submit", function (event) {
            event.preventDefault();

            const fullName = document.getElementById("fname").value.trim();
            const email = document.getElementById("email").value.trim();

            if (!fullName || !email) {
                if (errorMessage) {
                    errorMessage.textContent = "Please enter your name and email address.";
                }
                return;
            }

            if (errorMessage) {
                errorMessage.textContent = "";
            }
            if (costText) {
                costText.textContent = "Your request details are ready for review.";
            }
            if (confirmation) {
                confirmation.classList.add("show");
            }

            const newCount = Number(sessionStorage.getItem("motoriecBookingCount") || "0") + 1;
            sessionStorage.setItem("motoriecBookingCount", String(newCount));
            if (bookingCounter) {
                bookingCounter.textContent = "Successful requests in this session: " + newCount;
            }

            serviceForm.reset();
        });
    }
});
