function changeBorderColor(element) {
    // Remove the border-red-500 class from all steps
    document.querySelectorAll('.step').forEach(step => {
        step.classList.remove('border-red-500');
    });

    // Add the border-red-500 class to the clicked step
    element.classList.add('border-red-500');
    console.log("border-red-500");
}