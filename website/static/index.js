function deleteProduct(productId) {
  fetch('/delete-product', {
    method: "POST",
    body: JSON.stringify({ productId: productId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}




// Get the modal
const modal = document.getElementById("Modal");


const btn = document.getElementById("modalbtn");

// When the user clicks on the button, open the modal
btn.onclick = function () {
  modal.style.display = "block";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


// Get the modal
const modal_edit = document.getElementById("Modal");


const btn = document.getElementById("modalbtn");

// When the user clicks on the button, open the modal
btn.onclick = function () {
  modal_edit.style.display = "block";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    modal_edit.style.display = "none";
  }
}