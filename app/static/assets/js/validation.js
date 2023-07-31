function checkname() {
  console.log("inside checkname");
  var nameValue = document.frm.name.value;
  var regex = /^[a-zA-Z \s\.]+$/;

  if (nameValue.trim() == "") {
    document.getElementById("error").innerHTML = "Please Enter Name";
  } else if (!regex.test(nameValue)) {
    document.getElementById("error").innerHTML = "Please Enter Only Alphabets";
    return false;
  } else {
    document.getElementById("error").innerHTML = "";
    return true;
  }
}
/*----------------- email validation function------------------------------------*/
function checkEmail() {
  var emailValue = document.frm.email.value;
  var regexEmail2 =
    /^([A-Za-z0-9]+[/./-_/+\*])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})$/;
  var regexEmail =
    /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
  if (emailValue.trim() == "") {
    document.getElementById("errorMessageShowData").innerHTML =
      "This field can not be empty";
  } else if (regexEmail.test(emailValue) || regexEmail2.test(emailValue)) {
    document.getElementById("errorMessageShowData").innerHTML = "";
    return false;
  } else {
    document.getElementById("errorMessageShowData").innerHTML =
      "Please enter a valid emial";
    return true;
  }
}
/*---------email validation functiona ends here----------------------------------*/
function checkreview() {
  var nameValue = document.frm.review.value;
  var regex = /^[A-Za-z0-9 ]+$/;

  if (nameValue.trim() == "") {
    document.getElementById("errorData").innerHTML = "Please Enter review";
  } else if (!regex.test(nameValue)) {
    document.getElementById("errorData").innerHTML = "Please Enter valid data";
    return false;
  } else {
    document.getElementById("errorData").innerHTML = "";
    return true;
  }
}

function checkphone() {
  var nameValue = document.frm.phone.value;
  var regex = /^[0-9]+$/;

  if (nameValue.trim() == "") {
    document.getElementById("errorPhone").innerHTML = "Please Enter Phone No.";
  } else if (!regex.test(nameValue)) {
    document.getElementById("errorPhone").innerHTML =
      "Please Enter Only number";
    return false;
  } else if (nameValue.length != 10) {
    document.getElementById("errorPhone").innerHTML =
      "Please Enter 10 digits number";
    return false;
  } else {
    document.getElementById("errorPhone").innerHTML = "";
    return true;
  }
}

/* ------------ Password validations_________*/
function checkPassword() {
  var passwordValue = document.frm.password1.value;
  var regex = /^[a-zA-Z0-9!@#$%^&*]{8,16}$/;

  if (passwordValue.trim() == "") {
    document.getElementById("errorPassword").innerHTML = "Password is requied";
  } else if (!regex.test(passwordValue)) {
    document.getElementById("errorPassword").innerHTML =
      "password too short";
    return false;
  } else {
    document.getElementById("errorPassword").innerHTML = "";
    return true;
  }
}
/*----------------check person -------------------*/
function checkPerson() {
  var nameValue = document.frm.number_of_person.value;
  var regex = /^[0-9]+$/;

  if (nameValue.trim() == "") {
    document.getElementById("errorData").innerHTML = "Please Enter number.";
  } else if (!regex.test(nameValue)) {
    document.getElementById("errorData").innerHTML = "Please Enter Only number";
    return false;
  } else if (nameValue <= 0) {
    document.getElementById("errorData").innerHTML =
      "Please Enter positive number";
    return false;
  } else {
    document.getElementById("errorData").innerHTML = "";
    return true;
  }
}

/*------------check person ends here------------------------*/
/*----------------image size validation function------------------*/
Filevalidation = () => {
  console.log("file validation funciton invoked");
  const fi = document.getElementById("feedback_image");
  const typ = document.getElementById("feedback_image").value;
  let result1 = typ.match(".jpeg");
  let result2 = typ.match(".png");
  let result3 = typ.match(".jpg");
  let result4 = typ.match(".raw");
  // Check if any file is selected.
  if (fi.files.length > 0) {
    for (const i = 0; i <= fi.files.length - 1; i++) {
      const fsize = fi.files.item(i).size;
      const file = Math.round(fsize / 1024);
      // The size of the file.
      if (file >= 2048) {
        alert("File too Big, please select a file less than  2 mb");
        document.querySelector(".feedback_image");
        feedback_image.value = "";
      } else {
        if (result1 || result2 || result3 || result4) {
          document.getElementById("size").innerHTML = "<b>" + file + "</b> KB";
        } else {
          alert("selected file is not an image, try again");
          document.querySelector(".feedback_image");
          feedback_image.value = "";
        }
      }
    }
  }

  /*--------image size validation function ends here---*/

  function check_username() {
    var f = document.frm.username.value;
    //console.log(f)
    var reg = /^[A-Za-z]+$/;

    if (f.trim() == "") {
      document.getElementById("error").innerHTML = "Please Enter Your UserName";
    } else if (!reg.test(f)) {
      document.getElementById("error").innerHTML =
        "Please Enter only Alphabets";
      return false;
    } else {
      document.getElementById("error").innerHTML = "";
      return true;
    }
  }

  function checkPassword() {
    var passwordValue = document.frm.password1.value;
    var regexPassword = /^[a-zA-Z0-9!@#$%^&*]{8,16}$/;
    if (passwordValue.trim() == "") {
      document.getElementById("errorPassword").innerHTML =
        "Please Enter Password";
    } else if (!regexPassword.test(passwordValue)) {
      document.getElementById("errorPassword").innerHTML =
        "Please Enter Valid Password";
      return false;
    } else {
      document.getElementById("errorPassword").innerHTML = "";
      return true;
    }
  }

  function checkConfirmPassword() {
    var confirmPasswordValue = document.frm.pass2.value;
    var passwordValue = document.frm.password1.value;
    if (confirmPasswordValue.trim() == "") {
      document.getElementById("errorPassword2").innerHTML =
        "Please Enter Confirm Password";
    } else if (!regexConfirmPassword.test(confirmPasswordValue)) {
      //else if(passwordValue!=confirmPasswordValue)
      document.getElementById("errorPassword2").innerHTML =
        "Please Enter Valid Password";
      return false;
    } else {
      document.getElementById("errorPassword2").innerHTML = "";
      return true;
    }
  }
}
