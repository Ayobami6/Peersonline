// First Like button try
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

// Second Like button try
$(document).ready(function () {
  var csrftoken = getCookie("csrftoken");
  var likeButton = $("#like-button");
  likeButton.click(function () {
    var pk = likeButton.attr("data-pk");
    $.ajax({
      url: `posts/like/${pk}`,
      type: "POST",
      headers: { "X-CSRFToken": csrftoken },
      success: function (response) {
        likeButton.text("Liked");
      },
    });
  });
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
// third try
$(document).ready(function () {
  var csrftoken = getCookie("csrftoken");
  var likeButton = $("#like-button");
  var postId = likeButton.attr("data-pk");
  var like = localStorage.getItem("like");

  likeButton.click(function () {
    fetch(`/posts/like/${postId}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    })
      .then(function (response) {
        if (response.ok) {
          likeButton.text("Liked");
          localStorage.setItem("like", "Liked");
        }
      })
      .catch(function (error) {
        console.error("An error occurred while liking the post:", error);
      });
  });

  if (like === "Liked") {
    likeButton.text("Liked");
  } else {
    likeButton.text("Like");
  }
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// 4th try
$(document).ready(function () {
  var csrftoken = getCookie("csrftoken");
  var postId = $("#like-button").attr("data-pk");
  var like_count_id = `${postId}-like-count`;
  $(document).on("click", "#like-button", function () {
    $.ajax({
      url: $(this).attr("data-href"),
      type: "POST",
      headers: { "X-CSRFToken": csrftoken },
      data: {
        post_id: $(this).attr("data-pk"),
      },
      success: function (response) {
        setTotalLikes(response.total_likes);
        // $("#like_count").empty();
        // $("span#like_count").text(response.total_likes);
        // $(`span#${like_count_id}`).text(response.total_likes);
        // document.getElementById(like_count_id).innerHTML = response.total_likes;
        // console.log(response.total_likes);
        // document.getElementById("like_count").innerHTML = response.total_likes;
      },
    });
  });
});

function setTotalLikes(total_likes) {
  $("#like-count").empty();
  $("span#like-count").text(total_likes);
}