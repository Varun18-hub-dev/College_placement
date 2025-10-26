document.querySelector("button [type= 'reset']").addEventListener("click", function() {
        const result = document.querySelector(".result");
        if (result) result.innerHTML = "";
    });