document.addEventListener("DOMContentLoaded", function() {
    function openTab(tabName) {
        var i, tabcontent, tablinks;

        // Hide all tab contents
        tabcontent = document.getElementsByClassName("tabcontent");
        for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
        }

        // Remove active class from all tab links
        tablinks = document.getElementsByClassName("tablink");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }

        // Show the current tab content and add an active class to the button that opened the tab
        document.getElementById(tabName).style.display = "block";
        document.querySelector(`.tablink[data-tab='${tabName}']`).className += " active";
    }

    // Add click event listener to all tab links
    var tablinks = document.getElementsByClassName("tablink");
    for (var i = 0; i < tablinks.length; i++) {
        tablinks[i].addEventListener("click", function() {
            var tabName = this.getAttribute("data-tab");
            openTab(tabName);
        });
    }

    // Open the default tab
    document.querySelector(".tablink").click();
});
