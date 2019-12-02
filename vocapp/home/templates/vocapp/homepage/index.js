function onRegisterClick(){
  window.location.href = "/register";
}

function onBackClick(){
  window.location.href = "/";
}

function onContactClick(){
  window.location.href = "/contact";
}

function onLoginClick(){
  window.location.href = "/login";
}

function onDashboardClick(){
  window.location.href = "/dashboard";
}

// function onVersionClick(){
//   var xhttp = new XMLHttpRequest();
//   xhttp.onreadystatechange = function() {
//     if (this.readyState == 4 && this.status == 200) {
//       document.getElementById('version').innerHTML = this.responseText;
//     }
//   };
//   xhttp.open('GET', 'http://127.0.0.1:8000/api/version', true);
//   xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//   xhttp.send();
// }
