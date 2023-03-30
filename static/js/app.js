const menu = document.querySelector("#mobile-menu");
const menuLinks = document.querySelector(".navbar__menu");

const textarea = document.querySelector("textarea");
const lineNumbers = document.querySelector(".line-numbers");

menu.addEventListener("click", function () {
  menu.classList.toggle("is-active");
  menuLinks.classList.toggle("active");
});

textarea.addEventListener("keyup", (event) => {
  const numberOfLines = event.target.value.split("\n").length;

  lineNumbers.innerHTML = Array(numberOfLines).fill("<span></span>").join("");
});

textarea.addEventListener("keydown", (event) => {
  if (event.key === "Tab") {
    const start = textarea.selectionStart;
    const end = textarea.selectionEnd;

    textarea.value =
      textarea.value.substring(0, start) + "\t" + textarea.value.substring(end);

    event.preventDefault();
  }
});

//input.addEventListener("change", () => {
//  let files = input.files;
//  console.log(files);
//
//  if (files.length == 0) return;
//
//  const file = files[0];
//
//  let reader = new FileReader();
//
//  reader.onload = (e) => {
//    const file = e.target.result;
//
//    const lines = file.split(/\r\n|\n/);
//    textarea.value = lines.join = "\n";
//  };
//
//  reader.onerror = (e) => alert(e.target.error.name);
//
//  reader.readAsText(file);
//});

//var clicks = 0;
//if (submitButton) {
//  submitButton.addEventListener("click", function () {
//    clicks += 1;
//    const output = JSON.stringify({ clicks });
//    console.log(output);
//    $.ajax({
//      url: "/quizzer",
//      type: "POST",
//      contentType: "application/json",
//      data: output,
//    });
//  });
//}
//
//var clicks = 0;
//function onClick() {
//  clicks += 1;
//  document.getElementById("submit__code__button__clicks").innerHTML = clicks;
//  output = JSON.stringify({ clicks });
//  $.ajax({
//    url: "/quizzer",
//    type: "POST",
//    contentType: "application/json",
//    data: output,
//  });
//}
//
// function grabCode() {
// let get = document.getElementById("code");
//   let code = JSON.stringify({ code: get.value });
//   alert("Insert Correct / incorrect thing");
// }
