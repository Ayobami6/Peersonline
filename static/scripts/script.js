$(document).ready(function () {
  var csrftoken = getCookie("csrftoken");
  $("#like-button").click(function () {
    var pk = $(this).attr("data-pk");
    $.ajax({
      url: `posts/like/${pk}`,
      type: "POST",
      headers: { "X-CSRFToken": csrftoken },
      success: function (response) {
        $("#like-button").text("Liked");
        $("#like-count").text(response["total_likes"]);
      },
    });
  });
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Search for the csrf token cookie
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}