// buy and rent page javascript
function showControls(event) {
    // Get the specific carousel related to the card
    const carousel = event.currentTarget.closest('.card').querySelector('.carousel');
    
    // Get the previous and next controls for that specific carousel
    const prevControl = carousel.querySelector('.carousel-control-prev');
    const nextControl = carousel.querySelector('.carousel-control-next');
    
    // Show the controls by changing opacity to 1
    prevControl.style.opacity = '1';
    nextControl.style.opacity = '1';
}

function hideControls(event) {
    // Get the specific carousel related to the card
    const carousel = event.currentTarget.closest('.card').querySelector('.carousel');
    
    // Get the previous and next controls for that specific carousel
    const prevControl = carousel.querySelector('.carousel-control-prev');
    const nextControl = carousel.querySelector('.carousel-control-next');
    
    // Hide the controls by changing opacity to 0
    prevControl.style.opacity = '0';
    nextControl.style.opacity = '0';
}

// // add home page javascript

// Function to handle displaying the correct price field    this old code
// function togglePriceField() {
//     const saleRentValue = document.getElementById("sale-rent").value;
//     if (saleRentValue === "sell") {
//         document.getElementById("sell-price").style.display = "block";
//         document.getElementById("rent-price").style.display = "none";
//     } else {
//         document.getElementById("sell-price").style.display = "none";
//         document.getElementById("rent-price").style.display = "block";
//     }
// }

// this is new code
function togglePriceField() {
    const saleRentValue = document.getElementById("sale-rent").value;
    
    // Show/hide price fields based on the selected option
    if (saleRentValue === "sell") {
        document.getElementById("sell-price").style.display = "block";
        document.getElementById("rent-price").style.display = "none";
        // Remove the required attribute from rent price input when it's hidden
        document.getElementById("rent-price").removeAttribute("required");
        // Keep the required attribute on selling price input
        document.getElementById("selling-price").setAttribute("required", "true");
    } else {
        document.getElementById("sell-price").style.display = "none";
        document.getElementById("rent-price").style.display = "block";
        // Add the required attribute to rent price input when it's visible
        document.getElementById("rent-price").setAttribute("required", "true");
        // Remove the required attribute from selling price input when it's hidden
        document.getElementById("selling-price").removeAttribute("required");
    }
}


// Function to preview selected images and allow removing them
function previewImages(event) {
    const imagePreviewDiv = document.getElementById('image-preview');
    imagePreviewDiv.innerHTML = ''; // Clear any previously previewed images

    const files = event.target.files;
    Array.from(files).forEach((file, index) => {
        const imgElement = document.createElement('img');
        imgElement.src = URL.createObjectURL(file);
        imgElement.classList.add('preview-image', 'col-md-4', 'image-preview'); // Add Bootstrap classes for grid layout
        imgElement.setAttribute('data-index', index);
        imgElement.style.objectFit = 'cover';
        imgElement.style.height = '150px'; // Set a height for the images

        // Add a remove button to the image
        const removeButton = document.createElement('button');
        removeButton.textContent = 'X';
        removeButton.classList.add('remove-image-btn');
        removeButton.setAttribute('data-index', index);
        removeButton.onclick = function() {
            removeImage(index);
        };

        const imageWrapper = document.createElement('div');
        imageWrapper.classList.add('col-md-4', 'image-preview-wrapper'); // Add grid column for Bootstrap

        imageWrapper.appendChild(imgElement);
        imageWrapper.appendChild(removeButton);

        imagePreviewDiv.appendChild(imageWrapper);
    });
}

// Function to remove an image
function removeImage(index) {
    const images = document.getElementById("images").files;
    const dataTransfer = new DataTransfer();

    Array.from(images).forEach((file, i) => {
        if (i !== index) {
            dataTransfer.items.add(file);
        }
    });

    document.getElementById("images").files = dataTransfer.files;
    previewImages({target: {files: dataTransfer.files}}); // Re-render the preview
}


// -------------------------------------------




// ---------------------------------------
// home page dropdown showing select list javascript

/// Update location button text
const locationItems = document.querySelectorAll('.dropdown-item[data-location]');
const locationButton = document.getElementById('locationButton');
const locationText = document.getElementById('locationText'); // Target the span with id "locationText"

locationItems.forEach(item => {
    item.addEventListener('click', function(event) {
        const selectedLocation = event.target.dataset.location;
        locationText.textContent = selectedLocation; // Update the span with the selected location
    });
});

// Update bedroom button text
const bedroomItems = document.querySelectorAll('.dropdown-item[data-bedroom]');
const bedroomButton = document.getElementById('bedroomButton');
const bedroomText = document.getElementById('bedroomText'); // Target the span with id "bedroomText"

bedroomItems.forEach(item => {
    item.addEventListener('click', function(event) {
        const selectedBedroom = event.target.dataset.bedroom;
        // Update the span text with the selected bedroom, adding "Bedroom" or "Bedrooms" appropriately
        bedroomText.textContent = selectedBedroom + (selectedBedroom === "1" ? " Bedroom" : " Bedrooms");
    });
});


// Update price button text
const priceDropdownButton = document.getElementById('priceButton');
const priceLabelText = document.getElementById('priceText');
const priceItems = document.querySelectorAll('.dropdown-item[data-price]');

// Event listener for dropdown items
priceItems.forEach(item => {
    item.addEventListener('click', function(event) {
        const selectedPrice = event.target.textContent;
        priceLabelText.textContent = selectedPrice;
    });
});



// -------------------------------


// home page price dropdown list javascript and home page buy rent button selection javascript

// Get references to the buttons and dropdowns
const buyButton = document.querySelector('.search-links .button1:nth-child(1)');
const rentButton = document.querySelector('.search-links .button1:nth-child(2)');
const priceButton = document.getElementById('priceButton');
const buyPriceDropdown = document.getElementById('buyPriceDropdown');
const rentPriceDropdown = document.getElementById('rentPriceDropdown');
const priceText = document.getElementById('priceText');

// Function to update the dropdown based on the selected button
function updatePriceDropdown(isBuy) {
    // If "Buy" is selected, show the Buy price options and hide the Rent options
    if (isBuy) {
        buyPriceDropdown.style.display = 'block';
        rentPriceDropdown.style.display = 'none';
    } 
    // If "Rent" is selected, show the Rent price options and hide the Buy options
    else {
        buyPriceDropdown.style.display = 'none';
        rentPriceDropdown.style.display = 'block';
    }
}

// Add click event listener to the price button to toggle dropdown visibility
priceButton.addEventListener('click', function (event) {
    // Prevent the event from propagating to the document and closing the dropdown
    event.stopPropagation();

    // If the dropdown is already open, close it
    if (buyPriceDropdown.style.display === 'block' || rentPriceDropdown.style.display === 'block') {
        buyPriceDropdown.style.display = 'none';
        rentPriceDropdown.style.display = 'none';
    } else {
        // Otherwise, show the appropriate dropdown based on the active button
        if (buyButton.classList.contains('active-btn')) {
            buyPriceDropdown.style.display = 'block';
            rentPriceDropdown.style.display = 'none';

            
        } else if (rentButton.classList.contains('active-btn')) {
            rentPriceDropdown.style.display = 'block';
            buyPriceDropdown.style.display = 'none';
        }
    }
});

// Close dropdown when clicking outside
document.addEventListener('click', function (event) {
    // Check if the click is outside the price dropdown and price button
    if (!priceButton.contains(event.target) && !buyPriceDropdown.contains(event.target) && !rentPriceDropdown.contains(event.target)) {
        buyPriceDropdown.style.display = 'none';
        rentPriceDropdown.style.display = 'none';
    }
});

// Add click event listeners to the Buy and Rent buttons
buyButton.addEventListener('click', function () {
    // Set the Buy button as active
    buyButton.classList.add('active-btn');
    buyButton.classList.remove('btns-hover');
    
    // Set the Rent button as inactive
    rentButton.classList.remove('active-btn');
    rentButton.classList.add('btns-hover');
    
    updatePriceDropdown(true); // Show Buy price options
});

rentButton.addEventListener('click', function () {
    // Set the Rent button as active
    rentButton.classList.add('active-btn');
    rentButton.classList.remove('btns-hover');
    
    // Set the Buy button as inactive
    buyButton.classList.remove('active-btn');
    buyButton.classList.add('btns-hover');
    
    updatePriceDropdown(false); // Show Rent price options
});

// Initialize with Buy price options (by default)
updatePriceDropdown(true); // Default to "Buy" price options

