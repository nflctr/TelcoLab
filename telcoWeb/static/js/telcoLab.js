const form = document.querySelector('form');
const paramInput = document.querySelector('textarea[name="param-generator"]');

let isFormValid = false;

const validateInputs = () => {
  paramInput.classList.remove('invalid');
  paramInput.nextElementSibling.classList.add("hidden");
  isFormValid = true;
  
  var len = paramInput.value.split(/[\s]+/);

  if(len.length !== 9){
    paramInput.classList.add("invalid");
    paramInput.nextElementSibling.classList.remove("hidden");
    isFormValid = false;}
  // if (!paramInput.value) {
  //  paramInput.classList.add("invalid");
  //  paramInput.nextElementSibling.classList.remove("hidden");}
  // if (!paramInput.value) {
  //  paramInput.classList.add("invalid");
  //  paramInput.nextElementSibling.classList.remove("hidden");}
};

form.addEventListener('submit', (e) => {
  e.preventDefault();
  validateInputs();
  if(isFormValid) {
    paramInput
  }
});

paramInput.addEventListener('input', () => {
  validateInputs();
});

// var wordLen = 9; // Maximum word length
//   function checkWordLen(obj){
//   var len = obj.value.split(/[\s]+/);
//     if(len.length != wordLen){
//         alert("You cannot put moreor less than "+wordLen+" words in this text area.");
//         obj.oldValue = obj.value!=obj.oldValue?obj.value:obj.oldValue;
//         obj.value = obj.oldValue?obj.oldValue:"";
//         paramInput.classList.add("invalid");
//         paramInput.nextElementSibling.classList.remove("hidden");
//         return false;
//     }
//   return true;
// }