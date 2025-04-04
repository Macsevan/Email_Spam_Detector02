document.addEventListener("DOMContentLoaded", () => {
    const textarea = document.querySelector("textarea");
    const button = document.querySelector("button");
    const form = document.querySelector("form");

    // Word count feedback
    const wordCountDisplay = document.createElement("div");
    wordCountDisplay.style.fontSize = "14px";
    wordCountDisplay.style.color = "#666";
    wordCountDisplay.style.marginTop = "5px";
    textarea.parentNode.insertBefore(wordCountDisplay, textarea.nextSibling);

    textarea.addEventListener("input", () => {
        const words = textarea.value.trim().split(/\s+/).filter(Boolean);
        wordCountDisplay.textContent = `Word count: ${words.length}`;
        button.disabled = textarea.value.trim() === "";
    });

    // Fade effect for result div
    form.addEventListener("submit", () => {
        const resultDiv = document.querySelector(".result");
        if (resultDiv) {
            resultDiv.style.transition = "opacity 0.5s";
            resultDiv.style.opacity = 0;
            setTimeout(() => {
                resultDiv.style.opacity = 1;
            }, 500);
        }
    });
});
