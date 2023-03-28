const menu = document.querySelector("#mobile-menu");
const menuLinks = document.querySelector(".navbar__menu");
const submitButton = document.getElementById("submit__code__button");

menu.addEventListener("click", function () {
  menu.classList.toggle("is-active");
  menuLinks.classList.toggle("active");
});

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
