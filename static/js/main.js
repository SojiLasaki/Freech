// //GET SEARCH FORM AND PAGE LINKS
// let searchForm = document.getElementById('searchForm')
// let pageLinks = document.getElementsByClassName('page-link')

// //ENSURE SEARCHFORM EXISTS
// if (searchForm) {
//     for (let i = 0; pageLinks.length > i; i++) {
//         pageLinks[i].addEventListener('click', function (e) {
//             e.preventDefault()

//             //GET THE DATA ATTRIBUTES
//             let page = this.dataset.page

//             //ADD HIDDEN SEARCH INPUT TO FORM
//             searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

//             //SUBMIT FORM
//             searchForm.submit()
//         })
//     }
// }

// let tags = document.getElementsByClassName('project-tag')
    
// for (let i =0; tags.length > i; i++){
//     tags[i].addEventListener('click', (e) => {
//         let tagId = e.target.dataset.tag
//         let projectId = e.target.dataset.project

//          //console.log('Tag id:', tagId)
//          //console.log('project id:', projectId)
//         fetch('http://127.0.0.1:8000/api/remove-tag/', {
//             method:'DELETE',
//             headers:{
//                 'Content-Type':'application/json'
//             },
//             body:JSON.stringify({'project': projectId, 'tag': tagId })
//         })
//             .then(response => response.json())
//             .then(data => {
//                 e.target.remove()
//             })
//     })
// }



// Tell JS which HTML elements you are wanting it to look at and store them in a new variable:
const menuBtn = document.getElementById("menu-btn");
const closeBtn = document.getElementById("close-btn");
const listsContainer = document.getElementById("lists-container");

// Add an event listener to the menu & close buttons:
menuBtn.addEventListener("click", toggleMenu);
closeBtn.addEventListener("click", toggleMenu);

// Define the toggleMenu() function
function toggleMenu() {
    listsContainer.classList.toggle("open");
    menuBtn.classList.toggle("hidden");
    closeBtn.classList.toggle("visible");
}

// Remember: Don't call the function here. You only want the function to run when the button and/or links are clicked!

// Check out the nav-links in index.html: onclick="toggleMenu()" was added to each link so the mobile menu will also close when a link is clicked.



    // Define flashcards data
    
    // Initialize current flashcard index
    let currentIndex = 0;

    // Function to toggle between displaying term and definition
    function toggleText() {
        const termElement = document.querySelector(".term");
        const definitionElement = document.querySelector(".definition");

        termElement.classList.toggle("hidden");
        definitionElement.classList.toggle("hidden");
    }

// Function to display the current flashcard
function displayFlashcard() {
    const currentFlashcard = flashcards[currentIndex];
    const termElement = document.querySelector(".term");
    const definitionElement = document.querySelector(".definition");
    
    termElement.textContent = currentFlashcard.question;
    definitionElement.textContent = currentFlashcard.answer;
    document.getElementById("currentNum").textContent = currentIndex + 1;
    document.getElementById("totalNum").textContent = flashcards.length;
    
    // Always show question first, then toggle display of definition
    termElement.classList.remove("hidden");
    definitionElement.classList.add("hidden");
}

// Function to display the next flashcard
function handleNext() {
    currentIndex = (currentIndex + 1) % flashcards.length;
    displayFlashcard();
    // Reset "View Answer" button text
    const viewAnswerBtn = document.getElementById("viewAnswerBtn");
    viewAnswerBtn.textContent = "View Answer";
}

    // Function to display the previous flashcard
    function handlePrevious() {
        currentIndex = (currentIndex - 1 + flashcards.length) % flashcards.length;
        displayFlashcard();
    }

    // Function to handle "View Answer" button click
    function handleViewAnswer() {
        toggleText(); // Toggle between question and answer
        const viewAnswerBtn = document.getElementById("viewAnswerBtn");
        if (viewAnswerBtn.textContent === "View Answer") {
            viewAnswerBtn.textContent = "Hide Answer";
        } else {
            viewAnswerBtn.textContent = "View Answer";
        }
    }

    // Function to display a random flashcard
    function handleNew() {
        currentIndex = Math.floor(Math.random() * flashcards.length);
        displayFlashcard();
    }

// Initial display of flashcard
window.onload = function() {
    displayFlashcard();
    // Hide the answer initially
    toggleText();
    // Correct initial display by toggling again
    toggleText();
};
